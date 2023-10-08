import pandas as pd 

df2 = pd.read_csv('NFLNumberFire.csv', encoding= 'unicode_escape')

df2 = df2.dropna()
df2.rename(columns={"PLAYER": 'Name'}, inplace=True)

df2["Name"] = df2["Name"].str.split().str[0:-1].str.join(sep=" ")
df2.to_csv('NFLNumberFire2.csv', index=False)


print(df2)