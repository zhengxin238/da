import numpy as np
import pandas
from matplotlib import pyplot as plt
from pymongo import MongoClient
import pandas as pd
import function_pair_compare
import plot_code

cleint_name = "mongodb://localhost:27017/"
db_name = "DataTest_Voting_10"
collection_name = '00000009'

# get the basic df
df = function_pair_compare.mergeGroup(cleint_name, db_name, collection_name)

# print(df)

# calculate the influence of rising p for each pair of methods
percentage_rising_p = function_pair_compare.percentage_methods_compare(df)
# print(percentage_rising_p)

client = MongoClient('mongodb://localhost:27017/')
db = client['PairCompare_RisingP']  # Select database
collection = db['2']

# insert into db
function_pair_compare.insert_into_mongodb(client, db, collection, percentage_rising_p)


# ======================================================================
# above is with rising p,how likely would the pairs be same as each other
# ======================================================================
# below is with rising committee size_ we normalize the committe size from 1 to 10
# ======================================================================
client = MongoClient('mongodb://localhost:27017/')
db = client['PairCompare_RisingCommitteeSize']  # Select database
collection = db['2']


z = plot_code.get_normalised_result(df)


p = pandas.DataFrame()
for i in z:
    p = p._append(i)
df_sorted = p.sort_index()

# ======================================================================
# ======================================================================
# Remove duplicate indices and calculate mean
df_unique_indices = df_sorted.groupby(df_sorted.index).mean()
# ======================================================================
# ======================================================================

print (df_unique_indices)

# ======================================================================

# ======================================================================

# ======================================================================








#     for column in i.columns[:-1]:  # Exclude the last column
#         plt.plot(i['Nomalised_committe_size'], i[column], label=column)
#
#     plt.xlabel('Normalized Committee Size')
#     plt.ylabel('Value')
#     plt.title('Plot of Columns')
#     plt.legend()
#     plt.show()
#     break
