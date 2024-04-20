import pandas as pd
import pymongo
from itertools import combinations
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', None)  # Show all rows
pd.set_option('display.max_columns', None)  # Show all columns
pd.set_option('display.width', None)  # Auto-detect width



# cleint_name = "mongodb://localhost:27017/"
# db_name = "DataTest_Voting_10"
# collection_name = '00000001'
# chunksize = 9


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


#    (0, 1)    (0, 2)    (0, 3)    (0, 4)    (0, 5)    (0, 6)    (0, 7)    (0, 8)    (1, 2)    (1, 3)    (1, 4)  (1, 5)    (1, 6)    (1, 7)    (1, 8)    (2, 3)    (2, 4)    (2, 5)    (2, 6)    (2, 7)    (2, 8)    (3, 4)    (3, 5)    (3, 6)    (3, 7)    (3, 8)    (4, 5)    (4, 6)    (4, 7)    (4, 8)    (5, 6)    (5, 7)    (5, 8)    (6, 7)    (6, 8)    (7, 8)
# 0    1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000     1.0  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000
# 1    1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000     1.0  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000
# 2    1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000     1.0  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000
# 3    1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000     1.0  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000
# 4    1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000     1.0  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000
# 5    1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000     1.0  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000
# 6    1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000     1.0  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000
# 7    1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000     1.0  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000
# 8    1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000     1.0  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000
# 9    0.500000  0.500000  0.500000  0.500000  0.500000  0.500000  0.500000  1.000000  0.500000  1.000000  0.500000     1.0  1.000000  0.500000  0.500000  0.500000  1.000000  0.500000  0.500000  1.000000  0.500000  0.500000  1.000000  1.000000  0.500000  0.500000  0.500000  0.500000  1.000000  0.500000  1.000000  0.500000  0.500000  0.500000  0.500000  0.500000
# 10   0.500000  0.500000  0.500000  0.500000  0.500000  0.500000  0.500000  1.000000  0.500000  1.000000  0.500000     1.0  1.000000  0.500000  0.500000  0.500000  1.000000  0.500000  0.500000  1.000000  0.500000  0.500000  1.000000  1.000000  0.500000  0.500000  0.500000  0.500000  1.000000  0.500000  1.000000  0.500000  0.500000  0.500000  0.500000  0.500000
# 11   0.500000  0.500000  0.500000  0.500000  0.500000  0.500000  0.500000  0.500000  0.500000  1.000000  0.500000     1.0  1.000000  0.500000  1.000000  0.500000  1.000000  0.500000  0.500000  1.000000  0.500000  0.500000  1.000000  1.000000  0.500000  1.000000  0.500000  0.500000  1.000000  0.500000  1.000000  0.500000  1.000000  0.500000  1.000000  0.500000
# 12   0.500000  0.500000  0.500000  0.500000  0.500000  0.500000  0.500000  1.000000  0.500000  1.000000  0.500000     1.0  1.000000  0.500000  0.500000  0.500000  1.000000  0.500000  0.500000  1.000000  0.500000  0.500000  1.000000  1.000000  0.500000  0.500000  0.500000  0.500000  1.000000  0.500000  1.000000  0.500000  0.500000  0.500000  0.500000  0.500000
# 13

# function to compare each pair of methods get the result like above
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



# print(get_similarity_inPercent(cleint_name, db_name, collection_name))

# calculate a df with avg value for 10 or 9 rounds of calculation, each setting will be calculated 10 times
# get the following result
#    0.1       0.2       0.3       0.4       0.5       0.6       0.7       0.8       0.9
# Original_Index
# (0, 1)_1        1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000
# (0, 1)_2        0.500000  0.500000  0.500000  0.500000  0.500000  0.500000  0.500000  0.500000  0.500000
# (0, 1)_3        0.333333  0.333333  0.333333  0.333333  0.333333  0.333333  0.333333  0.333333  0.333333
# (0, 1)_4        0.500000  0.500000  0.500000  0.500000  0.500000  0.500000  0.500000  0.500000  0.500000
# (0, 1)_5        0.600000  0.600000  0.600000  0.600000  0.600000  0.600000  0.600000  0.600000  0.600000
# (0, 1)_6        0.666667  0.666667  0.666667  0.666667  0.666667  0.666667  0.666667  0.666667  0.666667
# (0, 1)_7        0.857143  0.857143  0.857143  0.857143  0.857143  0.857143  0.857143  0.857143  0.857143
# (0, 1)_8        1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000
# (0, 2)_1        1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000
# (0, 2)_2        0.500000  0.500000  0.500000  0.500000  0.500000  0.500000  0.500000  0.500000  0.500000
def mergeGroup(cleint_name, db_name, collection_name):
    df = rising_p_for_similarity(get_similarity_inPercent(cleint_name, db_name, collection_name))
    sub_group_size = int(len(df) / 36)
    inner_sub_group_size = int(len(df) / 360)
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
# df = mergeGroup(cleint_name, db_name, collection_name)
# print(df)
# calculate a df with avg value for 10 or 9 rounds of calculation, each setting will be calculated 10 times
# get the following result
#    0.1       0.2       0.3       0.4       0.5       0.6       0.7       0.8       0.9
# Original_Index
# (0, 1)_1        1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000
# (0, 1)_2        0.500000  0.500000  0.500000  0.500000  0.500000  0.500000  0.500000  0.500000  0.500000
# (0, 1)_3        0.333333  0.333333  0.333333  0.333333  0.333333  0.333333  0.333333  0.333333  0.333333
# (0, 1)_4        0.500000  0.500000  0.500000  0.500000  0.500000  0.500000  0.500000  0.500000  0.500000
# (0, 1)_5        0.600000  0.600000  0.600000  0.600000  0.600000  0.600000  0.600000  0.600000  0.600000
# (0, 1)_6        0.666667  0.666667  0.666667  0.666667  0.666667  0.666667  0.666667  0.666667  0.666667
# (0, 1)_7        0.857143  0.857143  0.857143  0.857143  0.857143  0.857143  0.857143  0.857143  0.857143
# (0, 1)_8        1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000
# (0, 2)_1        1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000
# (0, 2)_2        0.500000  0.500000  0.500000  0.500000  0.500000  0.500000  0.500000  0.500000  0.500000
def check_percentage_stable_value(df):
    # Align the DataFrame with its first column
    df_aligned = df.eq(df.iloc[:, 0], axis=0)

    # Check if all values in each row are the same
    all_same = df_aligned.all(axis=1)

    # Calculate the percentage of rows where all values are the same
    percent_same = (all_same.sum() / len(df)) * 100

    print(f"{percent_same:.2f}% of the comparisons between this pair stay stable with rising p.")
    return percent_same


def add_column_avg(df):
    df['Row_Average'] = df.mean(axis=1)
    return df


def percentage_methods_compare(df_func_merge_group):
    list_of_combis_pd = list(combinations(list(range(0, 9)), 2))
    # Initialize a list to store the percentages for each chunk
    percentage_list = []
    percentage_dict = {}
    chunk_size = int(len(df_func_merge_group)/36)
    print(chunk_size)
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


def insert_into_mongodb(client, db, collection, data):
    collection.insert_one(data)
    # Close connection
    client.close()
