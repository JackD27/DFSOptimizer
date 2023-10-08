import pandas as pd 
import os
import os.path
from pathlib import Path

# WATCH OUT FOR AZURA STEVENS!!!
sport = 0
DKdata = pd.read_csv('DKSalariesCaptainWNBA.csv')
playerData = pd.read_csv('WNBAplayerStats.csv')

if sport == 0:
  DKdata.drop_duplicates(subset='Name', inplace=True)
  DKData = DKdata[['Name', 'TeamAbbrev', 'AvgPointsPerGame']]
  playerData = playerData[['PLAYER', 'MIN', 'TEAM', 'GP', 'PTS', 'REB', 'AST', 'STL', 'BLK', 'TOV', '3PA', '3P%']]



  playerData.rename(columns = {'PLAYER': 'Name', 'MIN' : 'MPG', 'TEAM': 'TeamAbbrev', 'PTS' : 'PPG', 'REB' : 'RPG', 'AST' : 'APG', 'STL' : 'SPG', 'BLK' : 'BPG', 'TOV' : 'TPG'}, inplace = True)
  playerData['TeamAbbrev'] = playerData['TeamAbbrev'].str.upper()
  playerData['Name'] = playerData['Name'].str.lower()
  playerData['Name'] = playerData['Name'].str.title()
  
  #region Change data mishaps
  playerData.loc[playerData['Name'] == "Nalyssa Smith", 'Name'] = 'NaLyssa Smith'
  playerData.loc[playerData['Name'] == "Angel Mccoughtry", 'Name'] = 'Angel McCoughtry'
  playerData.loc[playerData['Name'] == "Didi Richards", 'Name'] = 'DiDi Richards'
  playerData.loc[playerData['Name'] == "Dewanna Bonner", 'Name'] = 'DeWanna Bonner'
  playerData.loc[playerData['Name'] == "Dijonai Carrington", 'Name'] = 'DiJonai Carrington'
  playerData.loc[playerData['Name'] == "Aari Mcdonald", 'Name'] = 'Aari McDonald'
  playerData.loc[playerData['Name'] == "Asia (Ad) Durr", 'Name'] = 'Asia Durr'
  playerData.loc[playerData['Name'] == "Diamond Deshields", 'Name'] = 'Diamond DeShields'
  playerData.loc[playerData['Name'] == "Azura Stevens", 'Name'] = 'Azur&#00225; Stevens'
  playerData.loc[playerData['Name'] == "Kayla Mcbride", 'Name'] = 'Kayla McBride'
  playerData.loc[playerData['Name'] == "Teaira Mccowan", 'Name'] = 'Teaira McCowan'
  playerData.loc[playerData['Name'] == "A'Ja Wilson", 'Name'] = "A'ja Wilson"

  playerData.loc[playerData['TeamAbbrev'] == "NYL", 'TeamAbbrev'] = 'NY'
  playerData.loc[playerData['TeamAbbrev'] == "LAS", 'TeamAbbrev'] = 'LA'
  playerData.loc[playerData['TeamAbbrev'] == "LVA", 'TeamAbbrev'] = 'LAV'
  
#endregion

  test1 = pd.DataFrame(playerData['Name'])
  test2 = pd.DataFrame(DKData[['Name', 'AvgPointsPerGame']])   
  noSimilarNames = test2.merge(test1, how = 'outer' ,indicator=True).loc[lambda x : x['_merge']=='left_only']
  try:
    noSimilarNames.loc[noSimilarNames['AvgPointsPerGame'] > 0, 'LeftOut?'] = 'True'
    noSimilarNames.loc[noSimilarNames['AvgPointsPerGame'] <= 0, 'LeftOut?'] = 'False'
  except:
    print('No players in index.')



  PPGpoints = playerData['PPG'] 
  playerData['3P%'] = playerData['3P%'] / 100
  ThreesPGpoints = ((playerData['3PA'] * round(playerData['3P%'], 2)) / playerData['GP']) * .5
  RBGpoints = round(playerData['RPG'], 2) * 1.25
  APGpoints = round(playerData['APG'], 2)* 1.5
  SPGpoints = round(playerData['SPG'], 2) * 2
  BPGpoints = round(playerData['BPG'], 2) * 2
  TPGpoints = round(playerData['TPG'], 2) * -0.5


  jackFPTs = PPGpoints + ThreesPGpoints + RBGpoints + APGpoints + SPGpoints + BPGpoints + TPGpoints
  playerData['jackAPPG'] = round(jackFPTs, 2)

  newData = pd.merge(DKData, playerData)

  newData['DKPPM'] = round(newData['AvgPointsPerGame'] / newData['MPG'], 2)

  newData['jackPPM'] = round(newData['jackAPPG'] / newData['MPG'], 2)

  newData[['ProjMin','jackProjFPTs', 'DKProjFPTs']] = ""
  newData = newData[['Name', 'TeamAbbrev', 'AvgPointsPerGame', 'MPG', 'DKPPM', 'ProjMin', 'DKProjFPTs','jackAPPG', 'jackPPM', 'jackProjFPTs']]
else:
  print('yes')

#region File Handling
path = "data"

try:
    os.mkdir(path)
except OSError:
    print ("Creation of the directory %s failed. Could already be created." % path)
else:
    print ("Successfully created the directory %s " % path)

fileName = "SaveThisTo_myOwnData3"

newData.to_csv(fileName+'.csv', index=False)

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
print(fileName)