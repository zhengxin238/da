import numpy as np
import pandas
from matplotlib import pyplot as plt
from pymongo import MongoClient
import pandas as pd
import function_pair_compare
import plot_code
from get_36_plot_pairCompare_rising_committeesize_and_p.aggregate_collecttion_pairCompare import final_plot_rising_committee_size_36pics, \
    final_plot_rising_p_1pic

# cleint_name = "mongodb://localhost:27017/"
# db_name = "linux_temp"
# collection_name = '00006-00000003'

# get the basic df
# df = function_pair_compare.mergeGroup(cleint_name, db_name, collection_name)
# df.to_json('11-1.json', orient='records')
# z = plot_code.get_normalised_result(df)

# json_file_path = r"D:\TU Clausthal\Masterarbeit\da\chunked.json"
# i = pd.read_json(json_file_path)
#
# # chuncked = plot_code.chunk_dataframe(df)
#
# # for i in chuncked:
# #     i.to_json('chunked.json', orient='records')
# #     break
#
# step_size = 100 / len(i)
# print(len(i))
# print("Length of values:", len(np.arange(0, 100, step_size)[:len(i)]))
# print("Length of DataFrame (index):", len(i))
# i = i.copy()
# i.loc[:, 'Nomalised_committe_size'] = np.arange(0, 100, step_size)[:len(i)]
# i.set_index(i.iloc[:, -1], inplace=True)
# # Drop the last column
# i = i.iloc[:, :-1]
# print(df)
# # calculate the influence of rising p for each pair of methods
# percentage_rising_p = function_pair_compare.percentage_methods_compare(df)
# # print(percentage_rising_p)

# client = MongoClient('mongodb://localhost:27017/')
# db = client['PairCompare_RisingP']  # Select database
# collection = db['2']
#
# # insert into db
# function_pair_compare.insert_into_mongodb(client, db, collection, percentage_rising_p)

# ======================================================================
# above is with rising p,how likely would the pairs be same as each other
# ======================================================================
# below is with rising committee size_ we normalize the committe size from 1 to 10
# ======================================================================

# cleint_name = "mongodb://localhost:27017/"
# db_name_f = "linux_temp"
# db_name_t = "DataSet_36pairs"

# below is with rising committee size_ we normalize the committe size from 1 to 10
# ======================================================================
# dfList = plot_code.get_normalised_result(df) this df as parameter is the result of function_pair_compare.mergeGroup(cleint_name, db_name, collection_name) therefore the following version
# dfList = plot_code.get_normalised_result(function_pair_compare.mergeGroup(cleint_name, db_name, collection_name))
# plot_code.store_dfs_in_mongodb(dfList) this dfList as parameter is the result of the above function. dfList = plot_code.get_normalised_result(function_pair_compare.mergeGroup(cleint_name, db_name, collection_name))
# for df in dfList:
#
#      df.index.name = None
#      print (df)
#      break


"""

!!!!!!!Before running this func,  we need to run dfs_36_intoDB  and get the data ready for this func!!!!!

Aggregate DataFrames from multiple collections in MongoDB. """

database_name = "DataSet_36pairs"

final_plot_rising_committee_size_36pics(database_name)
file_name = "pairCompare_rising_p"
final_plot_rising_p_1pic(database_name,file_name)