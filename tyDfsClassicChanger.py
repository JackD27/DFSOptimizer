import pandas as pd 
import numpy as np
import os
import os.path
from pathlib import Path

DKdata = pd.read_csv('DKSalariesClassic.csv')

# DKdata.drop_duplicates(subset='Name', inplace=True)
CFLData = DKdata[['name','pos', 'salary', 'team', 'fpts']]
  
#region Change data mishaps
'''
  DKdata.loc[DKdata['Position'] == "FB", 'Position'] = 'RB'
  DKdata.loc[DKdata['Position'] == "RB", 'IsFlex'] = True
  DKdata.loc[DKdata['Position'] == "WR", 'IsFlex'] = True
  '''
  
  
#endregion


CFLData = CFLData[['name','pos', 'salary', 'team', 'fpts']]
#region File Handling

df_new = pd.DataFrame(np.repeat(CFLData.values, 2, axis=0))

#assign column names of original DataFrame to new DataFrame
df_new.columns = CFLData.columns

path = "data"

try:
    os.mkdir(path)
except OSError:
    print ("Creation of the directory %s failed. Could already be created." % path)
else:
    print ("Successfully created the directory %s " % path)


df_new['fpts'] = df_new['fpts'].fillna(0)

duplicate_values = df_new['name'].duplicated()
print(duplicate_values)
df_new['isDupe'] = duplicate_values

df_new.loc[(df_new['isDupe'] == 1) & (df_new['pos'] != 'QB'), 'pos'] = 'FLEX'
df_new.drop_duplicates(['name', 'pos'], inplace=True)

    
fileName = "SaveThisTo_tyNewDataClassic"
df_new.to_csv(fileName+'.csv', index=False)






if os.path.exists("data/"+fileName+".csv"):
  os.remove("data/"+fileName+".csv")
else:
  print("The file does not exist in Data folder.")
  
Path(fileName+".csv").rename("data/"+fileName+".csv")        


if os.path.exists(fileName+".csv"):
  os.remove(fileName+".csv")
else:
  print("The file does not exist in normal folder. Success!")


#endregion
print("Success")