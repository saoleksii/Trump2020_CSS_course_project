import zstandard
import os
import json
import sys
import csv
from datetime import datetime
import logging.handlers

log = logging.getLogger("bot")
log.setLevel(logging.DEBUG)
log.addHandler(logging.StreamHandler())
def read_and_decode(reader, chunk_size, max_window_size, previous_chunk=None, bytes_read=0):
    chunk = reader.read(chunk_size)
    bytes_read += chunk_size
    if previous_chunk is not None:
        chunk = previous_chunk + chunk
    try:
        return chunk.decode()
    except UnicodeDecodeError:
        if bytes_read > max_window_size:
            raise UnicodeError(f"Unable to decode frame after reading {bytes_read:,} bytes")
        return read_and_decode(reader, chunk_size, max_window_size, chunk, bytes_read)
def read_lines_zst(file_name):
    with open(file_name, 'rb') as file_handle:
        buffer = ''
        reader = zstandard.ZstdDecompressor(max_window_size=2**31).stream_reader(file_handle)
        while True:
            chunk = read_and_decode(reader, 2**27, (2**29) * 2)
            if not chunk:
                break
            lines = (buffer + chunk).split("\n")

            for line in lines[:-1]:
                yield line, file_handle.tell()
            buffer = lines[-1]
        reader.close()
if __name__ == "__main__":
    if len(sys.argv) < 4:
        input_file_path = r"placeholder_input.zst"
        output_file_path = r"placeholder_output.csv"
        fields = ["author","score","created_utc","body"] 
    else:
        input_file_path = sys.argv[1]
        output_file_path = sys.argv[2]
        fields = sys.argv[3].split(",") 
    is_submission = "submission" in input_file_path.lower()
    file_size = os.stat(input_file_path).st_size
    file_lines, bad_lines = 0, 0
    line, created = None, None
    output_file = open(output_file_path, "w", encoding='utf-8', newline="")
    writer = csv.writer(output_file)
    writer.writerow(fields)
    log.info(f"Start processing: {os.path.basename(input_file_path)}...")
    try:
        for line, file_bytes_processed in read_lines_zst(input_file_path):
            try:
                obj = json.loads(line)
                output_obj = []
                for field in fields:
                    value = ""
                    if field == "created": 
                        value = datetime.fromtimestamp(int(obj['created_utc'])).strftime("%Y-%m-%d %H:%M")
                    elif field == "link":
                        if 'permalink' in obj:
                            value = f"https://www.reddit.com{obj['permalink']}"
                        elif 'subreddit' in obj and 'link_id' in obj and 'id' in obj:
                            value = f"https://www.reddit.com/r/{obj['subreddit']}/comments/{obj['link_id'][3:]}/_/{obj['id']}/"
                    elif field == "author":
                        value = f"u/{obj.get('author', '[deleted]')}"
                    elif field == "body":
                        value = obj.get('body', '')
                    elif field == "selftext":
                        value = obj.get('selftext', '')
                    elif field == "title":
                        value = obj.get('title', '')
                    else:
                        value = obj.get(field, "")
                    output_obj.append(str(value).encode("utf-8", errors='replace').decode())
                writer.writerow(output_obj)
                created = datetime.utcfromtimestamp(int(obj['created_utc']))
            except json.JSONDecodeError:
                bad_lines += 1
            except KeyError as err:
                 log.warning(f"KeyError: Object does not have row {err}. Row missed.")
                 bad_lines += 1
            file_lines += 1
            if file_lines % 100000 == 0:
                log.info(f"{created.strftime('%Y-%m-%d %H:%M:%S')} : {file_lines:,} : {bad_lines:,} : {(file_bytes_processed / file_size) * 100:.0f}%")
    except Exception as err:
        log.error(f"Handling error: {os.path.basename(input_file_path)}: {err}")
        log.error(line)
    output_file.close()
    log.info(f"Complete: {os.path.basename(input_file_path)} | Total lines: {file_lines:,} | Total errors: {bad_lines:,}")
