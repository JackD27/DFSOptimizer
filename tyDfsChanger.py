import pandas as pd 
import os
import os.path
from pathlib import Path

DKdata = pd.read_csv('DKSalariesCaptain.csv')
tyData = pd.read_csv('DKSalariesClassic.csv')

# DKdata.drop_duplicates(subset='Name', inplace=True)
CFLData = tyData[['name','fpts']]

DKdata.rename(columns = {'Name':'name'}, inplace = True)
  
#region Change data mishaps
'''
  DKdata.loc[DKdata['Position'] == "FB", 'Position'] = 'RB'
  DKdata.loc[DKdata['Position'] == "RB", 'IsFlex'] = True
  DKdata.loc[DKdata['Position'] == "WR", 'IsFlex'] = True
  '''
  
  
#endregion

#region File Handling

df_new = DKdata.merge(CFLData)

#assign column names of original DataFrame to new DataFrame

path = "data"

try:
    os.mkdir(path)
except OSError:
    print ("Creation of the directory %s failed. Could already be created." % path)
else:
    print ("Successfully created the directory %s " % path)


df_new.loc[df_new['Roster Position'] == "CPT", 'fpts'] = df_new["fpts"] * 1.5
df_new['fpts'] = df_new['fpts'].fillna(0)

    
fileName = "SaveThisTo_tyNewDataCaptain"
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