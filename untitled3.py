import pandas as pd 


nbaplayers = pd.read_csv('DKSalariesCaptainWNBA.csv')
dupedData2 = pd.read_csv('myOwnData3out.csv')

result = pd.merge(nbaplayers, dupedData2)


result.loc[result["Roster Position"] == "CPT", "DKFPTs"] = round((result["AvgPointsPerGame"] * 1.5), 2)
result.loc[result["Roster Position"] != "CPT", "DKFPTs"] = round((result["AvgPointsPerGame"] * 1), 2)
result.loc[result["Roster Position"] == "CPT", "MyOwnProjFPTs"] = round((result["DKProjFPTs"] * 1.5), 2)
result.loc[result["Roster Position"] != "CPT", "MyOwnProjFPTs"] = round((result["DKProjFPTs"] * 1), 2)

result.loc[result["Roster Position"] == "CPT", "jackProjFPTs"] = round((result["jackProjFPTs"] * 1.5), 2)
result.loc[result["Roster Position"] != "CPT", "jackProjFPTs"] = round((result["jackProjFPTs"] * 1), 2)

result.loc[result["MyOwnProjFPTs"] == 0, "DKFPTs"] = 0

result.drop(['Name + ID', 'TeamAbbrev', 'Position'], axis=1, inplace=True)

result['Value'] = round(((result['jackProjFPTs'] * 1000) / result['Salary']), 2)

result = result[['Name', 'ID', 'Game Info', 'Roster Position', 'Salary','AvgPointsPerGame', 'MyOwnProjFPTs', 'DKFPTs', 'jackProjFPTs', 'Value']]
    
gameInfo = result['Game Info'].values[0].split(' ')[0]
print(gameInfo)
result.to_csv('WNBA_CPT_AvgPoints'+gameInfo+'.csv', index=False)

print("Success")