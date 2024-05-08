import pandas as pd
import pymongo
from itertools import combinations
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', None)  # Show all rows
pd.set_option('display.max_columns', None)  # Show all columns
pd.set_option('display.width', None)  # Auto-detect width



cleint_name = "mongodb://localhost:27017/"
db_name = "linux_corrected"
collection_name = '00000009'
chunksize = 10


def compare_candidates(dict1, dict2):
    keys_dict1 = [key for key, value in dict1.items() if value == 1.0]
    keys_dict2 = [key for key, value in dict2.items() if value == 1.0]
    # Count the number of keys with value 1.0 that are the same in both dictionaries
    count_same = sum(1 for key in keys_dict1 if key in keys_dict2)
    percentage_same = count_same / len(keys_dict1)
    return percentage_same


# list_of_combis_pd = list(combinations(list(range(0, 9)), 2))
#
# percentage_df = pd.DataFrame(columns=list_of_combis_pd)
#
#     # Establish a connection to MongoDB
# client = pymongo.MongoClient(cleint_name)
#
#     # Select the database
# db = client[db_name]
#
#     # Select the collection
# collection = db[collection_name]
#
#     # Find all documents in the collection
# cursor = collection.find({})
#
#     # Create a list to store the documents
# documents_list = []
#
#     # Iterate over the cursor to access each document
# for document in cursor:
#         # Remove the '_id' field from the document
#     document.pop('_id', None)
#     documents_list.append(document)
#
# for final_committee in documents_list:
#     # print(final_committee)
#     # """{'1': {'0.1': {'avg_avg': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8.000000000000002}, 'max_avg': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8}, 'min_avg': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8}, 'max_max': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8}, 'min_min': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8}, 'max_min': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8}, 'min_max': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8}, 'avg_min': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8.000000000000002}, 'avg_max': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8.000000000000002}}, '0.2': {'avg_avg': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 7.9999999999999964}, 'max_avg': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8}, 'min_avg': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8}, 'max_max': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8}, 'min_min': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8}, 'max_min': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8}, 'min_max': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8}, 'avg_min': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8.000000000000002}, 'avg_max': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8.000000000000002}}, '0.30000000000000004': {'avg_avg': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8.000000000000002}, 'max_avg': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8}, 'min_avg': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8}, 'max_max': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8}, 'min_min': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8}, 'max_min': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8}, 'min_max': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8}, 'avg_min': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8.000000000000002}, 'avg_max': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8.000000000000002}}, '0.4': {'avg_avg': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 7.9999999999999964}, 'max_avg': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8}, 'min_avg': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8}, 'max_max': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8}, 'min_min': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8}, 'max_min': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8}, 'min_max': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8}, 'avg_min': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8}, 'avg_max': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8}}, '0.5': {'avg_avg': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8.000000000000002}, 'max_avg': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8}, 'min_avg': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8}, 'max_max': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8}, 'min_min': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8}, 'max_min': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8}, 'min_max': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8}, 'avg_min': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8}, 'avg_max': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8}}, '0.6': {'avg_avg': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8.000000000000004}, 'max_avg': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8}, 'min_avg': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8}, 'max_max': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8}, 'min_min': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8}, 'max_min': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8}, 'min_max': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8}, 'avg_min': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8}, 'avg_max': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8}}, '0.7000000000000001': {'avg_avg': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 7.9999999999999964}, 'max_avg': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8}, 'min_avg': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8}, 'max_max': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8}, 'min_min': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8}, 'max_min': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8}, 'min_max': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8}, 'avg_min': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8}, 'avg_max': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8}}, '0.8': {'avg_avg': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8.000000000000002}, 'max_avg': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8}, 'min_avg': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8}, 'max_max': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8}, 'min_min': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8}, 'max_min': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8}, 'min_max': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8}, 'avg_min': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8}, 'avg_max': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8}}, '0.9': {'avg_avg': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8}, 'max_avg': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8}, 'min_avg': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8}, 'max_max': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8}, 'min_min': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8}, 'max_min': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8}, 'min_max': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8}, 'avg_min': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8.000000000000002}, 'avg_max': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1}, 'optimized_value': 8.000000000000002}}}}"""
#    for committee_size_from_one_on, full_result in final_committee.items():
#         # print(full_result)
#         # """{'0.1': {'avg_avg': {'final_committee': {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': """
#         for p_value_till_one, value_2 in full_result.items():
#                 # print(p_value_till_one) 0.1,0,2,0,3,...,1.0
#             list_of_chosen_candidate = []
#             for key_3, value_3 in value_2.items():
#                     # print(key_3)
#                 items = list(value_3.items())
#                 best_committee = items[0][1]
#                 #     list_of_chosen_candidate will get a list of ideal committee for each nine methods  made up of dict  {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1} for all nine methods
#                 list_of_chosen_candidate.append(best_committee)
#             # print(list_of_chosen_candidate)
#             # print(len(list_of_chosen_candidate)) --> 9 for all nine methods


#             list_of_combis = list(combinations(list(range(len(list_of_chosen_candidate))), 2))
#             # print(list_of_combis) get --> [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (4, 5), (4, 6), (4, 7), (4, 8), (5, 6), (5, 7), (5, 8), (6, 7), (6, 8), (7, 8)]

# function to compare each pair of methods get the result like above

# get_similarity_inPercent will bring the followng result
 #  (0, 1)    (0, 2)    (0, 3)    (0, 4)    (0, 5)    (0, 6)    (0, 7)    (0, 8)    (1, 2)    (1, 3)    (1, 4)  (1, 5)    (1, 6)    (1, 7)    (1, 8)    (2, 3)    (2, 4)    (2, 5)    (2, 6)    (2, 7)    (2, 8)    (3, 4)    (3, 5)    (3, 6)    (3, 7)    (3, 8)    (4, 5)    (4, 6)    (4, 7)    (4, 8)    (5, 6)    (5, 7)    (5, 8)    (6, 7)    (6, 8)    (7, 8)
# 0    1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000     1.0  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000
# 1    1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000     1.0  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000
# 2    1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000     1.0  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000
# 3    1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000     1.0  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000
# 4    1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000     1.0  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000
# 5    1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000     1.0  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000
# 6    1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000     1.0  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000
# 7    1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000     1.0  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000
# 8    1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000     1.0  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000
# 9    0.500000  0.500000  0.500000  0.500000  0.500000  0.500000  0.500000  1.000000  0.500000  0.500000  0.500000     1.0  0.500000  0.500000  0.500000  0.500000  1.000000  0.500000  0.500000  1.000000  0.500000  0.500000  0.500000  1.000000  0.500000  0.500000  0.500000  0.500000  1.000000  0.500000  0.500000  0.500000  0.500000  0.500000  0.500000  0.500000
# 10   0.500000  0.500000  0.500000  0.500000  0.500000  0.500000  0.500000  0.500000  0.500000  1.000000  0.500000     1.0  1.000000  0.500000  1.000000  0.500000  1.000000  0.500000  0.500000  1.000000  0.500000  0.500000  1.000000  1.000000  0.500000  1.000000  0.500000  0.500000  1.000000  0.500000  1.000000  0.500000  1.000000  0.500000  1.000000  0.500000


def get_similarity_inPercent(cleint_name, db_name, collection_name):
    list_of_combis_pd = list(combinations(list(range(0, 9)), 2))

    percentage_df = pd.DataFrame(columns=list_of_combis_pd)

    # Establish a connection to MongoDB
    client = pymongo.MongoClient(cleint_name)

    # Select the database
    db = client[db_name]

    # Select the collection
    collection = db[collection_name]

    # Find all documents in the collection
    cursor = collection.find({})

    # Create a list to store the documents
    documents_list = []

    # Iterate over the cursor to access each document
    for document in cursor:
        # Remove the '_id' field from the document
        document.pop('_id', None)
        documents_list.append(document)

    for committee_size in documents_list:
        for key_1, value_1 in committee_size.items():
            for key_2, value_2 in value_1.items():

                # print(key_2)
                list_of_chosen_candidate = []
                for key_3, value_3 in value_2.items():
                    # print(key_3)
                    items = list(value_3.items())
                    best_committee = items[0][1]
                    list_of_chosen_candidate.append(best_committee)
# list_of_chosen_candidate will get a list of ideal committee for each nine methods made up of dict like: {'x[0]': 0, 'x[1]': 0, 'x[2]': 0, 'x[3]': 0, 'x[4]': 0, 'x[5]': 0, 'x[6]': 0, 'x[7]': 0, 'x[8]': 1} for all nine methods
                list_of_combis = list(combinations(list(range(len(list_of_chosen_candidate))), 2))
                row_values = []
                for combi in list_of_combis:
                    percentage_value = compare_candidates(list_of_chosen_candidate[combi[0]],
                                                          list_of_chosen_candidate[combi[1]])
                    row_values.append(percentage_value)
                percentage_df.loc[len(percentage_df)] = row_values
    return percentage_df
l =get_similarity_inPercent(cleint_name, db_name, collection_name)
# print(l)
#
# def percentage_avg(similarity_inPercent):
#     column_averages = similarity_inPercent.mean()
#     print(similarity_inPercent)
#     print(column_averages)
#     return column_averages


#=====================================================================================================
#the following function will give a result df like, it apply only for one round of the experiment. we gether for each collection 10 rounds of experiment so we need to chunk the percentage_df into 10 pars before apply this function
#    0.1       0.2       0.3       0.4       0.5       0.6       0.7       0.8       0.9       1.0
# (0, 1)_1   1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000
# (0, 1)_2   1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000
# (0, 1)_3   0.666667  0.666667  0.666667  0.666667  0.666667  0.666667  0.666667  0.666667  0.666667  0.666667
# (0, 1)_4   0.750000  0.750000  0.750000  0.750000  0.750000  0.750000  0.750000  0.750000  0.750000  0.750000
# (0, 1)_5   0.800000  0.800000  0.800000  0.800000  0.800000  0.800000  0.800000  0.800000  0.800000  0.800000
# (0, 1)_6   0.833333  0.833333  0.833333  0.833333  0.833333  0.833333  0.833333  0.833333  0.833333  0.833333
def rising_p_for_similarity(percentage_df):
    """ here the chunksize should be 10, the length from 0.1, 0.2 0.3, to 1.0 that is same as the length of p_values"""
    column_names = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9,1.0]
    groups_df = pd.DataFrame(columns=column_names)

    for pairs in percentage_df.columns:
        j = 1

        for i in range(0, len(percentage_df[pairs]), 10):
            new_row = pd.DataFrame(percentage_df[pairs].values[i:i + 10]).transpose()
            new_row_df = pd.DataFrame(new_row.to_numpy(), columns=groups_df.columns, index=[f"{pairs}_{j}"])

            groups_df = groups_df._append(new_row_df, ignore_index=False)
            j += 1
    return groups_df


# print(rising_p_for_similarity(l))


#
#
#
# print(get_similarity_inPercent(cleint_name, db_name, collection_name))
#

def mergeGroup(cleint_name, db_name, collection_name):
    df = rising_p_for_similarity(get_similarity_inPercent(cleint_name, db_name, collection_name))
    num_rows_len = len(df)
    # print(num_rows_len)
    sub_group_size = int(num_rows_len/36)
    inner_sub_group_size = int(num_rows_len/360)
    averaged_df = pd.DataFrame()

    # Iterate through each set of 72 rows
    for i in range(0, len(df), sub_group_size):
        # Extract the current set of 72 rows
        subset = df.iloc[i:i + sub_group_size]

        # Initialize an empty DataFrame to store the merged results for this subset
        merged_subset = pd.DataFrame()

        # Iterate through each row in the inner sub-group
        for j in range(inner_sub_group_size):
            # Calculate the indices of the rows to merge with
            merge_indices = list(range(j, len(subset), inner_sub_group_size))

            # Extract the rows to merge with
            merge_rows = subset.iloc[merge_indices]

            # Calculate the mean of the merged rows
            merged_mean = merge_rows.mean()

            # Add the index of the first row in the subset to the merged_mean
            merged_mean['Original_Index'] = subset.index[j]

            # Append the merged_mean to the merged_subset DataFrame
            merged_subset = merged_subset._append(merged_mean, ignore_index=True)

        # Append the merged_subset DataFrame to the averaged_df
        averaged_df = averaged_df._append(merged_subset, ignore_index=True)

    # Set the index to Original_Index column
    averaged_df.set_index('Original_Index', inplace=True)

    return averaged_df


def check_percentage_stable_value(df):
    # Align the DataFrame with its first column
    df_aligned = df.eq(df.iloc[:, 0], axis=0)

    # Check if all values in each row are the same
    all_same = df_aligned.all(axis=1)

    # Calculate the percentage of rows where all values are the same
    percent_same = (all_same.sum() / len(df)) * 100
    return percent_same


def add_column_avg(df):
    df['Row_Average'] = df.mean(axis=1)
    return df

df = mergeGroup(cleint_name, db_name, collection_name)
print(df)

def percentage_methods_compare(df_func_merge_group):
    list_of_combis_pd = list(combinations(list(range(0, 9)), 2))
    # Initialize a list to store the percentages for each chunk
    percentage_list = []
    percentage_dict = {}
    chunk_size = int(len(df_func_merge_group)/36)
    # Iterate over the DataFrame in chunks
    for i in range(0, len(df_func_merge_group), chunk_size):
        # Get the chunk of rows
        chunk = df_func_merge_group.iloc[i:i + chunk_size]
        # Count the number of rows where all values are the same
        p = check_percentage_stable_value(chunk)
        # Append the percentage to the list
        percentage_list.append(p)

    for i in range(len(list_of_combis_pd)):
        percentage_dict[str(list_of_combis_pd[i])] = percentage_list[i]

    return percentage_dict


print(percentage_methods_compare(df))


def chunk_dataframe(df):
    chunk_size = len(df)/36
    num_chunks = 36  # Calculate the number of chunks
    chunked_dfs = []  # List to store chunked DataFrames

    for i in range(int(num_chunks)):
        # Slice the DataFrame to get the chunk
        chunk = df.iloc[i * chunk_size: (i + 1) * chunk_size]
        chunked_dfs.append(chunk)  # Append the chunk to the list of chunked DataFrames

    return chunked_dfs





# def insert_into_mongodb(client, db, collection, data):
#     collection.insert_one(data)
#     # Close connection
#     client.close()
