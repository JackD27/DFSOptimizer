import pulp
import pandas as pd
from pandas.api.types import CategoricalDtype
    
data_file = 'myOwnDataNFLClassic.csv'

df = pd.read_csv(data_file, index_col=['Name', 'Roster Position'], skipinitialspace=True)

totalMoney = 0
totalPoints = 0

legal_assignments = df.index   
name_set = df.index.unique(0)  

costs = df['Salary'].to_dict()
values = df['FP'].to_dict()
#ids = df['ID'].to_dict()

# set up LP
draft = pulp.LpVariable.dicts('selected', legal_assignments, cat='Binary')

prob = pulp.LpProblem('Draft_Kings_CFL', pulp.LpMaximize)

# obj
prob += pulp.lpSum([draft[n, p]*values[n,p] for (n, p) in legal_assignments])

# salary cap
prob += pulp.lpSum([draft[n, p]*costs[n,p] for (n, p) in legal_assignments]) <= 50000

# pick 1 QB
prob += pulp.lpSum([draft[n, p] for (n, p) in legal_assignments if p == 'QB']) == 1

# pick 1 RB
prob += pulp.lpSum([draft[n, p] for (n, p) in legal_assignments if p == 'RB']) == 2

# pick 2 WR
prob += pulp.lpSum([draft[n, p] for (n, p) in legal_assignments if p == 'WR']) == 3

# pick 1 DST
prob += pulp.lpSum([draft[n, p] for (n, p) in legal_assignments if p == 'TE']) == 1

# pick 2 FLEX
prob += pulp.lpSum([draft[n, p] for (n, p) in legal_assignments if p == 'FLEX']) == 1

# pick 1 DST
prob += pulp.lpSum([draft[n, p] for (n, p) in legal_assignments if p == 'DST']) == 1


# use each player only once

      

needNames = ['Marcus Mariota', 'Jamaal Williams','Khalil Herbert']         #add names in the brackets, if you want a certain player or not.

for names in needNames:
    prob += pulp.lpSum([draft[n, p] for (n, p) in legal_assignments if n == names]) == 1    #change to 0 if you dont want the player, change to 1 if you want the player.
    
removeNames = ['Cordarrelle Patterson']         #add names in the brackets, if you want a certain player or not.

for names in removeNames:
    prob += pulp.lpSum([draft[n, p] for (n, p) in legal_assignments if n == names]) == 0   #change to 0 if you dont want the player, change to 1 if you want the player.

    
for name in name_set:
    prob += pulp.lpSum([draft[n, p] for (n, p) in legal_assignments if n == name]) <=1
    
    
prob += pulp.lpSum([draft[n, p]*values[n,p] for (n, p) in legal_assignments]) <= 1000

prob.solve()


lineup = []

for idx in draft:
    if draft[idx].varValue:
        lineup.append({
                        'Name': idx[0],
                        'Salary': costs[idx],
                        'Role': idx[1],
                        'PPG': values[idx]
                })
        
lineups = pd.DataFrame(lineup)

positions = ['QB', 'RB', 'WR', 'TE', 'FLEX', 'DST']
cat_size_order = CategoricalDtype(['QB', 'RB', 'WR', 'TE', 'FLEX', 'DST'], ordered=True)

lineups = lineups.reset_index(drop=True)
lineups['Role'] = lineups['Role'].astype(cat_size_order)
lineups['PPG'] = lineups['PPG'].astype(float)
lineups = lineups.sort_values(by=['Role'])
print(lineups)
totalMoney = lineups['Salary'].sum()
print("Total used amount of salary cap:", totalMoney, "Amount remaining: ", 50000 - totalMoney)
print("Projected points for the game: ", round(lineups['PPG'].sum(), 3))
