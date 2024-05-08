import pandas as pd
import pymongo
from itertools import combinations
import matplotlib.pyplot as plt

cleint_name = "mongodb://localhost:27017/"
db_name = "linux_corrected"
#
# def get_similarity_inPercent(cleint_name, db_name, collection_name):
#     list_of_combis_pd = list(combinations(list(range(0, 9)), 2))
#
#     percentage_df = pd.DataFrame(columns=list_of_combis_pd)
#
#     # Establish a connection to MongoDB
#     client = pymongo.MongoClient(cleint_name)
#
#     # Select the database
#     db = client[db_name]
#
#     # Select the collection
#     collection = db[collection_name]
#
#     # Find all documents in the collection
#     cursor = collection.find({})
#
#     # Create a list to store the documents
#     documents_list = []
#
#     # Iterate over the cursor to access each document
#     for document in cursor:
#         # Remove the '_id' field from the document
#         document.pop('_id', None)
#         documents_list.append(document)
#
#     for committee_size in documents_list:
#         for key_1, value_1 in committee_size.items():
#             for key_2, value_2 in value_1.items():
#
#                 # print(key_2)
#                 List_of_Best_FSI= []
#                 for key_3, value_3 in value_2.items():
#                     # print(key_3)
#                     items = list(value_3.items())
#                     best_FSI_value = items[1][1]
#                     List_of_Best_FSI.append(best_FSI_value)
#     return None