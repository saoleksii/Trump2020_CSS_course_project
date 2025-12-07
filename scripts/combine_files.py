import pandas as pd

df1 = pd.read_csv('political_data.csv', low_memory=False)
df2 = pd.read_csv('political_data_lexa.csv', low_memory=False)
df_combined_rows = pd.concat([df1, df2], ignore_index=True)

print(len(df_combined_rows))
df_combined_rows.to_csv("combined_output.csv", index=False, encoding='utf-8')
print(df_combined_rows.T.head(10))
