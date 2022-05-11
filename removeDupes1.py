import pandas as pd 
import os
import os.path
from pathlib import Path

sport = 0
DKdata = pd.read_csv('DKSalariesCaptain.csv')
playerData = pd.read_csv('playerStats.csv')

if sport == 0:
  DKdata.drop_duplicates(subset='Name', inplace=True)
  DKData = DKdata[['Name', 'TeamAbbrev', 'AvgPointsPerGame']]
  playerData = playerData[['FULL NAME', 'MPG', 'TEAM', 'GP', 'PPGPointsPoints per game.', 'RPGReboundsRebounds per game.', 'APGAssistsAssists per game.', 'SPGStealsSteals per game.'
                         , 'BPGBlocksBlocks per game.', 'TOPGTurnoversTurnovers per game.', '3PA', '3P%']]

#region Change data mishaps
  playerData.loc[playerData['TEAM'] == "Bro", 'TEAM'] = 'Bkn'
  playerData.loc[playerData['TEAM'] == "San", 'TEAM'] = 'Sas'
  playerData.loc[playerData['TEAM'] == "Nor", 'TEAM'] = 'Nop'
  playerData.loc[playerData['TEAM'] == "Pho", 'TEAM'] = 'Phx'
  playerData.loc[playerData['FULL NAME'] == "Nic Claxton", 'FULL NAME'] = 'Nicolas Claxton'
  playerData.loc[playerData['FULL NAME'] == "Robert Williams III", 'FULL NAME'] = 'Robert Williams'
  playerData.loc[playerData['FULL NAME'] == "P.J. Washington", 'FULL NAME'] = 'PJ Washington'
  playerData.loc[playerData['FULL NAME'] == "Trevon Scott", 'FULL NAME'] = 'Tre Scott'
  playerData.loc[playerData['FULL NAME'] == "RJ Nembhard Jr.", 'FULL NAME'] = 'RJ Nembhard'
  playerData.loc[playerData['FULL NAME'] == "Willy Hernangomez", 'FULL NAME'] = 'Guillermo Hernangomez'
  
#endregion

  playerData.rename(columns = {'FULL NAME': 'Name', 'TEAM': 'TeamAbbrev', 'PPGPointsPoints per game.' : 'PPG', 'RPGReboundsRebounds per game.' : 'RPG', 'APGAssistsAssists per game.' : 'APG', 'SPGStealsSteals per game.' : 'SPG'
                             , 'BPGBlocksBlocks per game.' : 'BPG', 'TOPGTurnoversTurnovers per game.' : 'TPG'}, inplace = True)
  playerData['TeamAbbrev'] = playerData['TeamAbbrev'].str.upper()

  test1 = pd.DataFrame(playerData['Name'])
  test2 = pd.DataFrame(DKData[['Name', 'AvgPointsPerGame']])   
  noSimilarNames = test2.merge(test1, how = 'outer' ,indicator=True).loc[lambda x : x['_merge']=='left_only']
  noSimilarNames.loc[noSimilarNames['AvgPointsPerGame'] > 0, 'LeftOut?'] = 'True'
  noSimilarNames.loc[noSimilarNames['AvgPointsPerGame'] <= 0, 'LeftOut?'] = 'False'



  PPGpoints = playerData['PPG'] 
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
    
fileName = "SaveThisTo_myOwnData"
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