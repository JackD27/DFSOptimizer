import pandas as pd 

position = pd.DataFrame()
nbaplayers = pd.read_csv('DKSalariesClassic.csv')
dupedData2 = pd.read_csv('myOwnDataNFLClassic.csv')

result = pd.merge(nbaplayers, dupedData2)

#result.loc[result["Roster Position"] != "CPT", "MyOwnProjFPTs"] = round((result["DKProjFPTs"] * 1), 2)
result.loc[result["Roster Position"] != "CPT", "jackProjFPTs"] = round((result["FP"] * 1), 2)

position = result["Roster Position"].str.split('/', expand=True)
hmm = pd.merge(result, position, left_index=True, right_index=True, how='outer')
print(hmm.columns.get_loc(0))
print(hmm.columns.get_loc('Name'))

newCol = hmm.iloc[:, 17:]
PGs = newCol[newCol.isin(['SG']).any(axis=1)]
#hmm.iloc[:, 17:-1] != "PG"

result.drop(['TeamAbbrev', 'Position'], axis=1, inplace=True)

result = result[['Name', 'ID', 'Game Info', 'Roster Position', 'Salary','AvgPointsPerGame', 'jackProjFPTs']]
    
result.to_csv('CLASSIC_AvgPointsFOOTBALL.csv', index=False)

print("Success")
    