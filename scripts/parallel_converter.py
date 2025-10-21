import os
import glob
from concurrent.futures import ThreadPoolExecutor

INPUT_FOLDER = 'PoliticalData_ZST' 
OUTPUT_FOLDER = 'PoliticalData_CSV' 
CONVERTER_SCRIPT = 'single_file_converter.py' 
COMMON_FIELDS = "id,subreddit,author,score,created_utc,title,selftext,body,parent_id,link_id" 

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

all_zst_files = glob.glob(os.path.join(INPUT_FOLDER, '*.zst'))
print(f"Found {len(all_zst_files)} files for parallel processing...")
print(f"Chosen fields: {COMMON_FIELDS}")

def run_conversion(input_path):
    """Calls single_file_converter.py"""
    base_filename = os.path.basename(input_path)
    output_filename = base_filename.replace('.zst', '.csv')
    output_path = os.path.join(OUTPUT_FOLDER, output_filename)
    command = (
        f"python3 {CONVERTER_SCRIPT} "
        f'"{input_path}" ' 
        f'"{output_path}" ' 
        f'"{COMMON_FIELDS}"'
    )
    print(f"Start: {base_filename}")
    try:
        result = os.system(command) 
        if result == 0:
            print(f"SUCCESS: {output_filename}")
        else:
            print(f"FAILED: convertation {output_filename} failed: {result}")
        return result
        
    except Exception as e:
        print(f"Critical error in {output_filename}: {e}")
        return -1

if __name__ == "__main__":
    MAX_WORKERS = os.cpu_count() + 2 
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        executor.map(run_conversion, all_zst_files) 
    print("\n--------------------------")
    print("Parallel convertation finished")