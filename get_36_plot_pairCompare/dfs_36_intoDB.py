import numpy as np
import pandas
from matplotlib import pyplot as plt
import pymongo
from pymongo import MongoClient
import pandas as pd
import function_pair_compare
import plot_code

cleint_name = "mongodb://localhost:27017/"
db_name_f = "linux_temp"
db_name_t = "DataSet_36pairs_2"

# below is with rising committee size_ we normalize the committe size from 1 to 10
# ======================================================================
# dfList = plot_code.get_normalised_result(df) this df as parameter is the result of function_pair_compare.mergeGroup(cleint_name, db_name, collection_name) therefore the following version
# dfList = plot_code.get_normalised_result(function_pair_compare.mergeGroup(cleint_name, db_name, collection_name))
#  plot_code.store_dfs_in_mongodb(dfList) this dfList as parameter is the result of the above function. dfList = plot_code.get_normalised_result(function_pair_compare.mergeGroup(cleint_name, db_name, collection_name))

def integrated_da_pairCompare(cleint_name, db_name_t, db_name_f, collection_name):
    plot_code.store_dfs_in_mongodb(cleint_name, db_name_t, collection_name, plot_code.get_normalised_result(
        function_pair_compare.mergeGroup(cleint_name, db_name_f, collection_name)))
# integrated_da_pairCompare(cleint_name,db_name_t, db_name_f, collection_name)




def iterate_all_cllections(cleint_name, db_name_from, db_name_to):
# MongoDB connection settings
    mongo_client = pymongo.MongoClient(cleint_name)  # Update MongoDB URI as needed

    # Access the database
    db = mongo_client[db_name_from]

    # List all collections in the database
    collection_names = db.list_collection_names()
    used_names = mongo_client[db_name_to].list_collection_names()
# Convert lists to sets to find unique elements
# Find strings that appear only in one of the sets
    set1 = set(collection_names)
    set2 = set(used_names)

    # Find strings that appear only in one of the sets
    unique_collection_names = list(set1 - set2)

    # Iterate through each collection
    for collection_name in unique_collection_names:
        integrated_da_pairCompare(cleint_name, db_name_to, db_name_from, collection_name)

    # Close MongoDB connection
    mongo_client.close()

iterate_all_cllections(cleint_name, db_name_f, db_name_t)