import pandas as pd 
import os
import os.path
from pathlib import Path
from playerStats import *

noSimilarNames = pd.DataFrame

def NBADraftKingsCPTstats(DKFile, playerStats):
    
    
    testing = NBAStats(playerStats)
    DKFile.drop_duplicates(subset='Name', inplace=True)
    DKData = DKFile[['Name', 'TeamAbbrev', 'AvgPointsPerGame']]

    newData = pd.merge(DKData, testing)
    newData['DKPPM'] = round(newData['AvgPointsPerGame'] / newData['MPG'], 2)
    newData['jackPPM'] = round(newData['jackAPPG'] / newData['MPG'], 2)

    newData[['ProjMin','jackProjFPTs', 'DKProjFPTs']] = ""
    newData = newData[['Name', 'TeamAbbrev', 'AvgPointsPerGame', 'MPG', 'DKPPM', 'ProjMin', 'DKProjFPTs','jackAPPG', 'jackPPM', 'jackProjFPTs']]
  
    #region File Handling
    path = "data"
    try:
        os.mkdir(path)
    except OSError:
        print ("Creation of the directory %s failed. Could already be created." % path)
    else:
        print ("Successfully created the directory %s " % path)
    
    fileName = "SaveThisTo_myOwnDataNBAcpt"
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
'''
def NBADraftKingsClassic(DKFile, playerStats):
    
    testing = NBAStats(playerStats)
    DKFile.drop_duplicates(subset='Name', inplace=True)
    DKData = DKFile[['Name', 'TeamAbbrev', 'AvgPointsPerGame', 'Roster Position']]
    

    newData = pd.merge(DKData, testing)
    newData = newData.drop('Roster Position', axis=1).join(newData['Roster Position'].str.split('/', expand=True).stack().reset_index(level=1, drop=True).rename('Roster Position')).reset_index(drop=True)
    newData['DKPPM'] = round(newData['AvgPointsPerGame'] / newData['MPG'], 2)
    newData['jackPPM'] = round(newData['jackAPPG'] / newData['MPG'], 2)

    newData[['ProjMin','jackProjFPTs', 'DKProjFPTs']] = ""
    newData = newData[['Name', 'TeamAbbrev', 'AvgPointsPerGame', 'MPG', 'DKPPM', 'ProjMin', 'DKProjFPTs','jackAPPG', 'jackPPM', 'jackProjFPTs', 'Roster Position']]
  
    #region File Handling
    path = "data"
    try:
        os.mkdir(path)
    except OSError:
        print ("Creation of the directory %s failed. Could already be created." % path)
    else:
        print ("Successfully created the directory %s " % path)
    
    fileName = "SaveThisTo_myOwnDataNBAclassic"
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
'''
def DKgetMissingPeople(DKFile, playerStats, sport, website):
    if website == 'DraftKings':
        DKFile.drop_duplicates(subset='Name', inplace=True)
        DKData = DKFile[['Name', 'TeamAbbrev', 'AvgPointsPerGame']]
        if sport == 'NBA':
            testing = NBAStats(playerStats)
        elif sport == 'NFL':
            testing = NFLStats(playerStats, 'DraftKings')
        test2 = pd.DataFrame(DKData[['Name', 'AvgPointsPerGame']]) 
        test1 = pd.DataFrame(testing['Name'])
        noSimilarNames = test2.merge(test1, how = 'outer' ,indicator=True).loc[lambda x : x['_merge']=='left_only']
        noSimilarNames.loc[noSimilarNames['AvgPointsPerGame'] > 0, 'LeftOut?'] = 'True'
        noSimilarNames.loc[noSimilarNames['AvgPointsPerGame'] <= 0, 'LeftOut?'] = 'False'
    else:
        DKFile.drop_duplicates(subset='Nickname', inplace=True)
        DKData = DKFile[['Nickname', 'Team', 'FPPG']]
        DKData = DKData.rename(columns={'Nickname': 'Name'})
        if sport == 'NBA':
            testing = NBAStats(playerStats)
        elif sport == 'NFL':
            testing = NFLStats(playerStats, 'DraftKings')
        test2 = pd.DataFrame(DKData[['Name', 'FPPG']]) 
        test1 = pd.DataFrame(testing['Name'])
        noSimilarNames = test2.merge(test1, how = 'outer' ,indicator=True).loc[lambda x : x['_merge']=='left_only']
        noSimilarNames.loc[noSimilarNames['FPPG'] > 0, 'LeftOut?'] = 'True'
        noSimilarNames.loc[noSimilarNames['FPPG'] <= 0, 'LeftOut?'] = 'False'
    
    return noSimilarNames

def NFLDraftKingsCPTstats(DKFile, playerStats):
    testing = NFLStats(playerStats, 'DraftKings')
    DKFile.drop_duplicates(subset='Name', inplace=True)
    DKData = DKFile[['Name', 'TeamAbbrev', 'AvgPointsPerGame']]

    newData = pd.merge(DKData, testing)
  
    #region File Handling
    path = "data"
    try:
        os.mkdir(path)
    except OSError:
        print ("Creation of the directory %s failed. Could already be created." % path)
    else:
        print ("Successfully created the directory %s " % path)
    
    fileName = "SaveThisTo_myOwnDataNFLcpt"
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
    
def NFLDraftKingsCLASSICstats(DKFile, playerStats):
    testing = NFLStats(playerStats, 'DraftKings')
    DKFile.drop_duplicates(subset='Name', inplace=True)
    DKData = DKFile[['Name', 'TeamAbbrev', 'AvgPointsPerGame', 'Roster Position', 'Salary']]

    newData = pd.merge(DKData, testing)
  
    newData = newData.drop('Roster Position', axis=1).join(newData['Roster Position'].str.split('/', expand=True).stack().reset_index(level=1, drop=True).rename('Roster Position')).reset_index(drop=True)

    #region File Handling
    path = "data"
    try:
        os.mkdir(path)
    except OSError:
        print ("Creation of the directory %s failed. Could already be created." % path)
    else:
        print ("Successfully created the directory %s " % path)
    
    fileName = "SaveThisTo_myOwnDataNFLClassic"
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
    
def NFLFanDuelCLASSICstats(DKFile, playerStats):
    testing = NFLStats(playerStats, 'FanDuel')
    DKFile.drop_duplicates(subset='Nickname', inplace=True)
    DKData = DKFile[['Nickname', 'Team', 'FPPG', 'Roster Position', 'Salary']]
    DKData = DKData.rename(columns={'Nickname': 'Name'})

    newData = pd.merge(DKData, testing)
  
    newData = newData.drop('Roster Position', axis=1).join(newData['Roster Position'].str.split('/', expand=True).stack().reset_index(level=1, drop=True).rename('Roster Position')).reset_index(drop=True)

    #region File Handling
    path = "data"
    try:
        os.mkdir(path)
    except OSError:
        print ("Creation of the directory %s failed. Could already be created." % path)
    else:
        print ("Successfully created the directory %s " % path)
    
    fileName = "SaveThisTo_myOwnDataNFLClassicFD"
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
    
    


