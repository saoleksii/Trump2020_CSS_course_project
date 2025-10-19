import pandas as pd
import glob
import os

df = pd.read_csv("Conservative_comments.csv")
print(df.T.head(10))
all_files = glob.glob(os.path.join(".", "*.csv"))
df_list = []
for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    df_list.append(df)
combined_df = pd.concat(df_list, axis=0, ignore_index=True)
combined_df.to_csv("combined_output.csv", index=False, encoding='utf-8')
print("Completed")
df_combined = pd.read_csv("combined_output.csv", low_memory=False)
print(df_combined.T.head(10))
df_cleaned = df_combined.drop(["id", "score", "parent_id", "link_id", "author"], axis=1)
print(df_cleaned.T.head(10))
df_cleaned.to_csv("cleared_data.csv")