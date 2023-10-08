import pandas as pd 
import os
import os.path
from pathlib import Path

DKdata = pd.read_csv('DKSalariesNFL.csv')

DKdata.drop_duplicates(subset='Name', inplace=True)
CFLData = DKdata[['Name','Position', 'Roster Position','Salary', 'TeamAbbrev', 'AvgPointsPerGame', 'ID', 'Game Info']]
  
#region Change data mishaps
'''
  DKdata.loc[DKdata['Position'] == "FB", 'Position'] = 'RB'
  DKdata.loc[DKdata['Position'] == "RB", 'IsFlex'] = True
  DKdata.loc[DKdata['Position'] == "WR", 'IsFlex'] = True
  '''
  
  
#endregion

CFLData = CFLData.drop('Roster Position', axis=1).join(DKdata['Roster Position'].str.split('/', expand=True).stack().reset_index(level=1, drop=True).rename('Roster Position')).reset_index(drop=True)

CFLData = CFLData[['Name','Position', 'Roster Position', 'ID', 'TeamAbbrev','Game Info', 'Salary', 'AvgPointsPerGame']]
#region File Handling
path = "data"

try:
    os.mkdir(path)
except OSError:
    print ("Creation of the directory %s failed. Could already be created." % path)
else:
    print ("Successfully created the directory %s " % path)
    
fileName = "SaveThisTo_myOwnData4"
CFLData.to_csv(fileName+'.csv', index=False)



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