import pandas as pd
import pymongo
from itertools import combinations
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', None)  # Show all rows
pd.set_option('display.max_columns', None)  # Show all columns
pd.set_option('display.width', None)  # Auto-detect width


def compare_candidates(dict1, dict2):
    keys_dict1 = [key for key, value in dict1.items() if value == 1.0]
    keys_dict2 = [key for key, value in dict2.items() if value == 1.0]
    # Count the number of keys with value 1.0 that are the same in both dictionaries
    count_same = sum(1 for key in keys_dict1 if key in keys_dict2)
    percentage_same = count_same / len(keys_dict1)
    return percentage_same


def split_into_groups(column):
    groups = []
    for i in range(0, len(column), 9):
        groups.append(column[i:i + 9].values)
    return groups


cleint_name = "mongodb://localhost:27017/"
db_name = "DataTest_Voting"
collection_name = 'all_methods_00009-00000001'


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

                list_of_combis = list(combinations(list(range(len(list_of_chosen_candidate))), 2))
                row_values = []
                for combi in list_of_combis:
                    percentage_value = compare_candidates(list_of_chosen_candidate[combi[0]],
                                                          list_of_chosen_candidate[combi[1]])
                    row_values.append(percentage_value)
                percentage_df.loc[len(percentage_df)] = row_values
    return percentage_df


def percentage_avg(similarity_inPercent):
    column_averages = similarity_inPercent.mean()
    print(similarity_inPercent)
    print(column_averages)
    return column_averages


def rising_p_for_similarity(similarity_inPercent_df):
    grouped_df = pd.DataFrame()
    for pairs in similarity_inPercent_df.columns:
        grouped_df[pairs] = split_into_groups(similarity_inPercent_df[pairs])
    grouped_array = grouped_df.to_numpy()
    print(grouped_array)
    print(grouped_df)
    return grouped_array


df = get_similarity_inPercent(cleint_name, db_name, collection_name)

column_names = ["0.1", "0.2", "0.3", "0.4", "0.5", "0.6", "0.7", "0.8", "0.9"]

column_names = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
groups_df = pd.DataFrame(columns=column_names)  # Initialize an empty DataFrame if it's not initialized already

# Assuming you want to append rows from 'df' to 'groups_df' using slicing based on 'pairs' columns and index 'i'


for pairs in df.columns:
    chunk_size = 9
    # print(df[pairs])
    j = 1
    for i in range(0, len(df[pairs]), chunk_size):

        new_row = pd.DataFrame(df[pairs].values[i:i + chunk_size]).transpose()
        print()
        new_row_df = pd.DataFrame(new_row.to_numpy(), columns=groups_df.columns, index=[f"{pairs}_{j}"])

        groups_df = groups_df._append(new_row_df, ignore_index=False)
        j += 1
print(groups_df)
print(df)
# get_similarity_inPercent(cleint_name,db_name,collection_name)
