import pandas as pd 


nbaplayers = pd.read_csv('DKSalariesCaptain.csv')
dupedData2 = pd.read_csv('myOwnDataNBAcpt.csv')

result = pd.merge(nbaplayers, dupedData2)


result.loc[result["Roster Position"] == "CPT", "MyOwnProjFPTs"] = round((result["jackProjFPTs"] * 1.5), 2)
result.loc[result["Roster Position"] != "CPT", "MyOwnProjFPTs"] = round((result["jackProjFPTs"] * 1), 2)

result.drop(['Name + ID'], axis=1, inplace=True)

result['Value'] = round(((result['jackProjFPTs'] * 1000) / result['Salary']), 2)

result = result[['Name', 'ID', 'Game Info', 'TeamAbbrev', 'Roster Position', 'Position','Salary','AvgPointsPerGame', 'MyOwnProjFPTs', 'Value']]
    
gameInfo = result['Game Info'].values[0].split(' ')[0]
print(gameInfo)
result.to_csv('CPT_AvgPoints'+gameInfo+'.csv', index=False)

print("Success")