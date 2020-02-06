import pandas as pd
pd.set_option('display.max_colwidth', 15)

# load expert and council data set
df_eac = pd.read_csv("./expert_and_council_data_set.csv", sep=',', index_col=0, skipinitialspace=True) 
# print dataframe infos
print(df_eac.info())
# print first five rows
print(df_eac.head())