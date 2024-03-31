import function_merge_df

cleint_name = "mongodb://localhost:27017/"
db_name = "DataTest_Voting_10"
collection_name = '00000001'
chunksize = 9

df = function_merge_df.mergeGroup(cleint_name, db_name, collection_name, chunksize, 8)
print(df)
