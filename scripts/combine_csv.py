import pandas as pd
import glob
import os

folder_path = '.'

all_files = glob.glob(os.path.join(folder_path, "*.csv"))

df_list = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    df_list.append(df)

combined_df = pd.concat(df_list, axis=0, ignore_index=True)

combined_df.to_csv("combined_output.csv", index=False, encoding='utf-8')
