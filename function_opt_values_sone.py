import numpy as np
import pandas as pd
import pymongo
from itertools import combinations
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', None)  # Show all rows
pd.set_option('display.max_columns', None)  # Show all columns
pd.set_option('display.width', None)  # Auto-detect width


cleint_name = "mongodb://localhost:27017/"
db_name = "linux_temp"
collection_name = "00006-00000003"

# the order of the 9 dfs for each sample is "avg_avg", "max_avg", "min_avg", "max_max", "min_min", "max_min", "min_max", "avg_min", "avg_max"

def generate_rising_sums(n):
    return [sum(range(n, n - i, -1)) for i in range(n, 0, -1)]

def get_stepone_df(cleint_name, db_name, collection_name):
    df = pd.DataFrame(
        columns=["avg_avg", "max_avg", "min_avg", "max_max", "min_min", "max_min", "min_max", "avg_min", "avg_max"])

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
                list_of_best_FSI = []
                for key_3, value_3 in value_2.items():
                    # print(key_3)
                    items = list(value_3.items())
                    best_FSI_value = items[1][1]
                    # print(best_FSI_value)

                    list_of_best_FSI.append(best_FSI_value)
                df.loc[len(df)] = list_of_best_FSI

    chunk_size = len(df) // 10
    chunks = [df[i:i + chunk_size] for i in range(0, len(df), chunk_size)]
    df_init = chunks[0]

    for i in chunks[1:]:
        i.reset_index(drop=True, inplace=True)
        df_init.reset_index(drop=True, inplace=True)
        df_init = (df_init + i) / 2

    return df_init


df = get_stepone_df(cleint_name, db_name, collection_name)


def chunk_dataframe(df):
    column_names = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    # Calculate the integer chunk size
    chunk_size = 10
    num_chunks = len(df) // chunk_size

    chunked_dfs = []  # List to store chunked DataFrames

    for i in range(num_chunks):
        # Calculate start and end index for the chunk
        start_idx = i * chunk_size
        end_idx = (i + 1) * chunk_size

        # Handle the last chunk to include any remaining rows
        if i == num_chunks - 1:
            end_idx = len(df)  # Set end index to the last row index

        # Slice the DataFrame to get the chunk
        chunk = df.iloc[start_idx:end_idx]
        transposed_df = chunk.transpose()
        transposed_df.columns = column_names
        chunked_dfs.append(transposed_df)  # Append the chunk to the list of chunked DataFrames

    return chunked_dfs


list_of_chunked_fds = chunk_dataframe(df)

for i in list_of_chunked_fds:
    print(i)

def get_resultdf_original(list_of_chunked_fds):
    df0 = pd.DataFrame(columns=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
    df1 = pd.DataFrame(columns=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
    df2 = pd.DataFrame(columns=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
    df3 = pd.DataFrame(columns=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
    df4 = pd.DataFrame(columns=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
    df5 = pd.DataFrame(columns=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
    df6 = pd.DataFrame(columns=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
    df7 = pd.DataFrame(columns=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
    df8 = pd.DataFrame(columns=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])

    dfs = [df0, df1, df2, df3, df4, df5, df6, df7, df8]

    for i in list_of_chunked_fds:
        m = 0
        for index, row in i.iterrows():
            dfs[m] = dfs[m]._append(row, ignore_index=True)
            m += 1
    return dfs

dfs = get_resultdf_original(list_of_chunked_fds)
for i in dfs:
    print(i)
def get_normalised_result(dfs):
    normalised_dfs_list = []
    for i in dfs:
        step_size = 100 / len(i)
        i = i.copy()
        i.loc[:, 'Nomalised_committe_size'] = np.arange(0, 100, step_size)[:len(i)]
        i.set_index(i.iloc[:, -1], inplace=True)
        # Drop the last column
        i = i.iloc[:, :-1]
        i.index.name = None
        normalised_dfs_list.append(i)
    for i in normalised_dfs_list:
        print(i)
    for i in normalised_dfs_list:
        sum_list = sorted(generate_rising_sums(len(i)))

        for index, divisor in enumerate(sum_list):
            i.iloc[index] = i.iloc[index] / divisor
    for i in normalised_dfs_list:
        print(i)
    return normalised_dfs_list

normorlised_dfs = get_normalised_result(dfs)

for i in normorlised_dfs:
    print(i)
