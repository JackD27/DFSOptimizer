import pandas as pd 
from DraftKingsFiles import *
from Variables import Variable

help = Variable()

help.setSport('NFL')
help.setWebsite('DraftKings')
help.setGameMode('CPT')


DKFile = pd.read_csv('DKSalariesNFL.csv')
playerData = pd.read_csv('playerStats.csv', encoding= 'unicode_escape')


def Main(whatSport, whatWebsite, whatGamemode, DKFile, playerStats):
    if whatSport == 'NBA' and whatGamemode == 'CPT' and whatWebsite == 'DraftKings':
        NBADraftKingsCPTstats(DKFile, playerStats)
    elif whatSport == 'NFL' and whatGamemode == 'CPT' and whatWebsite == 'DraftKings':
        NFLDraftKingsCPTstats(DKFile, playerStats)
    elif whatSport == 'NFL' and whatGamemode == 'Classic' and whatWebsite == 'DraftKings':
        NFLDraftKingsCLASSICstats(DKFile, playerStats)
    elif whatSport == 'NFL' and whatGamemode == 'Classic' and whatWebsite == 'FanDuel':
        NFLFanDuelCLASSICstats(DKFile, playerStats)
       
        '''
    if whatSport == 'NBA' and whatGamemode == 'Classic' and whatWebsite == 'DraftKings':
        NBADraftKingsClassic(DKFile, playerStats)
        missingPeople = DKgetMissingPeople(DKFile, playerData)
        print(missingPeople)
        '''

missingPeople = DKgetMissingPeople(DKFile, playerData, help.getSport(), help.getWebsite())
print(missingPeople)
Main(help.getSport(),  help.getWebsite(), help.getGameMode(), DKFile, playerData)  
