import pandas as pd

def NBAStats(NBAplayerStats):
    
  NBAplayerStats = NBAplayerStats[['FULL NAME', 'MPG', 'TEAM', 'GP', 'PPGPointsPoints per game.', 'RPGReboundsRebounds per game.', 'APGAssistsAssists per game.', 'SPGStealsSteals per game.'
                         , 'BPGBlocksBlocks per game.', 'TOPGTurnoversTurnovers per game.', '3PA', '3P%']]

#region Change data mishaps
  NBAplayerStats.loc[NBAplayerStats['TEAM'] == "Bro", 'TEAM'] = 'Bkn'
  NBAplayerStats.loc[NBAplayerStats['TEAM'] == "San", 'TEAM'] = 'Sas'
  NBAplayerStats.loc[NBAplayerStats['TEAM'] == "Nor", 'TEAM'] = 'Nop'
  NBAplayerStats.loc[NBAplayerStats['TEAM'] == "Pho", 'TEAM'] = 'Phx'
  NBAplayerStats.loc[NBAplayerStats['TEAM'] == "Gol", 'TEAM'] = 'Gsw'
  NBAplayerStats.loc[NBAplayerStats['FULL NAME'] == "Nic Claxton", 'FULL NAME'] = 'Nicolas Claxton'
  NBAplayerStats.loc[NBAplayerStats['FULL NAME'] == "Robert Williams III", 'FULL NAME'] = 'Robert Williams'
  NBAplayerStats.loc[NBAplayerStats['FULL NAME'] == "P.J. Washington", 'FULL NAME'] = 'PJ Washington'
  NBAplayerStats.loc[NBAplayerStats['FULL NAME'] == "Trevon Scott", 'FULL NAME'] = 'Tre Scott'
  NBAplayerStats.loc[NBAplayerStats['FULL NAME'] == "RJ Nembhard Jr.", 'FULL NAME'] = 'RJ Nembhard'
  NBAplayerStats.loc[NBAplayerStats['FULL NAME'] == "Willy Hernangomez", 'FULL NAME'] = 'Guillermo Hernangomez'
  NBAplayerStats.loc[NBAplayerStats['FULL NAME'] == "MarJon Beauchamp", 'FULL NAME'] = 'Marjon Beauchamp'
  NBAplayerStats.loc[NBAplayerStats['FULL NAME'] == "A.J. Green", 'FULL NAME'] = 'AJ Green'
  
#endregion

  NBAplayerStats.rename(columns = {'FULL NAME': 'Name', 'TEAM': 'TeamAbbrev', 'PPGPointsPoints per game.' : 'PPG', 'RPGReboundsRebounds per game.' : 'RPG', 'APGAssistsAssists per game.' : 'APG', 'SPGStealsSteals per game.' : 'SPG'
                             , 'BPGBlocksBlocks per game.' : 'BPG', 'TOPGTurnoversTurnovers per game.' : 'TPG'}, inplace = True)
  NBAplayerStats['TeamAbbrev'] = NBAplayerStats['TeamAbbrev'].str.upper()
  PPGpoints = NBAplayerStats['PPG'] 
  ThreesPGpoints = ((NBAplayerStats['3PA'] * round(NBAplayerStats['3P%'], 2)) / NBAplayerStats['GP']) * .5
  RBGpoints = round(NBAplayerStats['RPG'], 2) * 1.25
  APGpoints = round(NBAplayerStats['APG'], 2)* 1.5
  SPGpoints = round(NBAplayerStats['SPG'], 2) * 2
  BPGpoints = round(NBAplayerStats['BPG'], 2) * 2
  TPGpoints = round(NBAplayerStats['TPG'], 2) * -0.5


  jackFPTs = PPGpoints + ThreesPGpoints + RBGpoints + APGpoints + SPGpoints + BPGpoints + TPGpoints
  NBAplayerStats['jackAPPG'] = round(jackFPTs, 2)
  
  return NBAplayerStats

def WNBAStats(WNBAplayerStats):
    print('WNBA')
    
def NFLStats(NFLplayerStats, website):
  #NFLplayerStats.rename(columns={"PLAYER": 'Name'}, inplace=True)
  NFLplayerStats.rename(columns={"ppg_projection": 'FP'}, inplace=True)
  NFLplayerStats["Name"] = NFLplayerStats['first_name'].astype(str) +" "+ NFLplayerStats["last_name"]
  NFLplayerStats = NFLplayerStats.dropna()
  #NFLplayerStats["Name"] = NFLplayerStats["Name"].str.split().str[0:4].str.join(sep=" ")
  #region Change data mishaps
  if website == 'DraftKings':
    NFLplayerStats.loc[NFLplayerStats['Name'] == "Buffalo", 'Name'] = 'Bills '
    NFLplayerStats.loc[NFLplayerStats['Name'] == "Los Angeles Rams", 'Name'] = 'Rams '
    NFLplayerStats.loc[NFLplayerStats['Name'] == "New Orleans", 'Name'] = 'Saints '
    NFLplayerStats.loc[NFLplayerStats['Name'] == "New England", 'Name'] = 'Patriots '
    NFLplayerStats.loc[NFLplayerStats['Name'] == "Miami", 'Name'] = 'Dolphins '
    NFLplayerStats.loc[NFLplayerStats['Name'] == "San Francisco", 'Name'] = '49ers '
    NFLplayerStats.loc[NFLplayerStats['Name'] == "Tennessee", 'Name'] = 'Titans '
    NFLplayerStats.loc[NFLplayerStats['Name'] == "Cleveland", 'Name'] = 'Browns '
    NFLplayerStats.loc[NFLplayerStats['Name'] == "Cincinnati", 'Name'] = 'Bengals '
    NFLplayerStats.loc[NFLplayerStats['Name'] == "Indianapolis", 'Name'] = 'Colts '
    NFLplayerStats.loc[NFLplayerStats['Name'] == "Philadelphia", 'Name'] = 'Eagles '
    NFLplayerStats.loc[NFLplayerStats['Name'] == "Baltimore", 'Name'] = 'Ravens '
    NFLplayerStats.loc[NFLplayerStats['Name'] == "Carolina", 'Name'] = 'Panthers '
    NFLplayerStats.loc[NFLplayerStats['Name'] == "Washington", 'Name'] = 'Commanders '
    NFLplayerStats.loc[NFLplayerStats['Name'] == "Green Bay", 'Name'] = 'Packers '
    NFLplayerStats.loc[NFLplayerStats['Name'] == "Kansas City", 'Name'] = 'Chiefs '
    NFLplayerStats.loc[NFLplayerStats['Name'] == "Los Angeles Chargers", 'Name'] = 'Chargers '
    NFLplayerStats.loc[NFLplayerStats['Name'] == "New York Jets", 'Name'] = 'Jets '
    NFLplayerStats.loc[NFLplayerStats['Name'] == "Pittsburgh", 'Name'] = 'Steelers '
    NFLplayerStats.loc[NFLplayerStats['Name'] == "Jacksonville", 'Name'] = 'Jaguars '
    NFLplayerStats.loc[NFLplayerStats['Name'] == "New York Giants", 'Name'] = 'Giants '
    NFLplayerStats.loc[NFLplayerStats['Name'] == "Chicago", 'Name'] = 'Bears '
    NFLplayerStats.loc[NFLplayerStats['Name'] == "Atlanta", 'Name'] = 'Falcons '
    NFLplayerStats.loc[NFLplayerStats['Name'] == "Detroit", 'Name'] = 'Lions '
    NFLplayerStats.loc[NFLplayerStats['Name'] == "Minnesota", 'Name'] = 'Vikings '
    NFLplayerStats.loc[NFLplayerStats['Name'] == "Houston", 'Name'] = 'Texans '
    NFLplayerStats.loc[NFLplayerStats['Name'] == "Las Vegas", 'Name'] = 'Raiders '
    NFLplayerStats.loc[NFLplayerStats['Name'] == "Arizona", 'Name'] = 'Cardinals '
    NFLplayerStats.loc[NFLplayerStats['Name'] == "Seattle", 'Name'] = 'Seahawks '
    NFLplayerStats.loc[NFLplayerStats['Name'] == "Denver", 'Name'] = 'Broncos '
    NFLplayerStats.loc[NFLplayerStats['Name'] == "D.K. Metcalf", 'Name'] = 'DK Metcalf'
    NFLplayerStats.loc[NFLplayerStats['Name'] == "Laviska Shenault", 'Name'] = 'Laviska Shenault Jr.'
    NFLplayerStats.loc[NFLplayerStats['Name'] == "Mitchell Trubisky", 'Name'] = 'Mitch Trubisky'
    NFLplayerStats.loc[NFLplayerStats['Name'] == "Josh Palmer", 'Name'] = 'Joshua Palmer'
    NFLplayerStats.loc[NFLplayerStats['Name'] == "Gabriel Davis", 'Name'] = 'Gabe Davis'
    NFLplayerStats.loc[NFLplayerStats['Name'] == "Travis Etienne", 'Name'] = 'Travis Etienne Jr.'
    NFLplayerStats.loc[NFLplayerStats['Name'] == "A.J. Dillon", 'Name'] = 'AJ Dillon'
    NFLplayerStats.loc[NFLplayerStats['Name'] == "Melvin Gordon", 'Name'] = 'Melvin Gordon III'
    NFLplayerStats.loc[NFLplayerStats['Name'] == "K.J. Hamler", 'Name'] = 'KJ Hamler'
    NFLplayerStats.loc[NFLplayerStats['Name'] == "D.J. Chark", 'Name'] = 'DJ Chark Jr.'
    NFLplayerStats.loc[NFLplayerStats['Name'] == "Tampa Bay", 'Name'] = 'Buccaneers '
    NFLplayerStats.loc[NFLplayerStats['Name'] == "Darrell Henderson", 'Name'] = 'Darrell Henderson Jr.'
    NFLplayerStats.loc[NFLplayerStats['Name'] == "Richie James", 'Name'] = 'Richie James Jr.'
    NFLplayerStats.loc[NFLplayerStats['Name'] == "D.J. Moore", 'Name'] = 'DJ Moore'
    NFLplayerStats.loc[NFLplayerStats['Name'] == "Marvin Jones", 'Name'] = 'Marvin Jones Jr.'
    NFLplayerStats.loc[NFLplayerStats['Name'] == "Khadarel Hodge", 'Name'] = 'KhaDarel Hodge'
    NFLplayerStats.loc[NFLplayerStats['Name'] == "Jeff Wilson", 'Name'] = 'Jeff Wilson Jr.'
    NFLplayerStats.loc[NFLplayerStats['Name'] == "Dallas", 'Name'] = 'Cowboys '
    
  else:
    NFLplayerStats.loc[NFLplayerStats['Name'] == "Bills ", 'Name'] = 'Bills '
    NFLplayerStats.loc[NFLplayerStats['Name'] == "Rams ", 'Name'] = 'Rams '
    NFLplayerStats.loc[NFLplayerStats['Name'] == "New Orleans", 'Name'] = 'New Orleans Saints'
    NFLplayerStats.loc[NFLplayerStats['Name'] == "New England", 'Name'] = 'New England Patriots'
    NFLplayerStats.loc[NFLplayerStats['Name'] == "Miami", 'Name'] = 'Miami Dolphins'
    NFLplayerStats.loc[NFLplayerStats['Name'] == "San Francisco", 'Name'] = 'San Francisco 49ers'
    NFLplayerStats.loc[NFLplayerStats['Name'] == "Tennessee", 'Name'] = 'Tennessee Titans'
    NFLplayerStats.loc[NFLplayerStats['Name'] == "Cleveland", 'Name'] = 'Cleveland Browns'
    NFLplayerStats.loc[NFLplayerStats['Name'] == "Cincinnati", 'Name'] = 'Cincinnati Bengals'
    NFLplayerStats.loc[NFLplayerStats['Name'] == "Indianapolis", 'Name'] = 'Indianapolis Colts'
    NFLplayerStats.loc[NFLplayerStats['Name'] == "Philadelphia", 'Name'] = 'Philadelphia Eagles'
    NFLplayerStats.loc[NFLplayerStats['Name'] == "Baltimore", 'Name'] = 'Baltimore Ravens'
    NFLplayerStats.loc[NFLplayerStats['Name'] == "Carolina", 'Name'] = 'Carolina Panthers'
    NFLplayerStats.loc[NFLplayerStats['Name'] == "Washington", 'Name'] = 'Washington Commanders'
    NFLplayerStats.loc[NFLplayerStats['Name'] == "Green Bay", 'Name'] = 'Green Bay Packers'
    NFLplayerStats.loc[NFLplayerStats['Name'] == "Kansas City", 'Name'] = 'Kansas City Chiefs'
    NFLplayerStats.loc[NFLplayerStats['Name'] == "Pittsburgh", 'Name'] = 'Pittsburgh Steelers'
    NFLplayerStats.loc[NFLplayerStats['Name'] == "Jacksonville", 'Name'] = 'Jacksonville Jaguars'
    NFLplayerStats.loc[NFLplayerStats['Name'] == "Chicago", 'Name'] = 'Chicago Bears'
    NFLplayerStats.loc[NFLplayerStats['Name'] == "Atlanta", 'Name'] = 'Atlanta Falcons'
    NFLplayerStats.loc[NFLplayerStats['Name'] == "Detroit", 'Name'] = 'Detroit Lions'
    NFLplayerStats.loc[NFLplayerStats['Name'] == "Minnesota", 'Name'] = 'Minnesota Vikings'
    NFLplayerStats.loc[NFLplayerStats['Name'] == "Houston", 'Name'] = 'Houston Texans'
    NFLplayerStats.loc[NFLplayerStats['Name'] == "Las Vegas", 'Name'] = 'Las Vegas Raiders'
    NFLplayerStats.loc[NFLplayerStats['Name'] == "Arizona", 'Name'] = 'Arizona Cardinals'
  
#endregion
  NFLplayerStats = NFLplayerStats[['Name', 'FP']]

  print(NFLplayerStats['Name'].head(10))

  return NFLplayerStats