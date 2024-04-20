import json
from itertools import combinations

import pandas as pd
import pymongo

#
# database_name = "DataSet_36pairs"
# mongo_uri='mongodb://localhost:27017/'
#
# client = pymongo.MongoClient(mongo_uri)
# db = client[database_name]
#
# # List all collections in the database
# collection_names = db.list_collection_names()
# # List to store integrated DataFrames
# integrated_dfs = [pd.DataFrame() for _ in range(36)]  # Assuming 36 DataFrames
#
# # Iterate over each collection
# for collection_name in collection_names:
#     collection = db[collection_name]
#     documents = list(collection.find())
#     for doc in documents:
#         # Load DataFrame from JSON data
#         df_json = doc['df_data']
#         df = pd.read_json(json.dumps(df_json), orient='split')
#
#         # Append the retrieved DataFrame to the list
#         print(df)
#
#         # Retrieve DataFrame from MongoDB document
#         # df_bytes = doc["df_data"]
#         # df = pd.read_pickle(df_bytes)

list_of_combis_pd = list(combinations(list(range(0, 9)), 2))
print(list_of_combis_pd[22])