import json
from itertools import combinations

import pymongo
import pandas as pd

import plot_code

# ======================================================================

"""

!!!!!!!Before running this func,  we need to run dfs_36_intoDB  and get the data ready for this func!!!!!

Aggregate DataFrames from multiple collections in MongoDB.

Args:
    database_name (str): Name of the MongoDB database.
    collection_names (list): List of collection names to aggregate.
    mongo_uri (str, optional): MongoDB connection URI. Defaults to 'mongodb://localhost:27017/'.

Returns:
    list: List of 36 integrated pandas DataFrames.
"""


# ======================================================================
#
def aggregate_collections(database_name, mongo_uri='mongodb://localhost:27017/'):
    """
    Aggregate DataFrames from multiple collections in MongoDB.

    Args:
        database_name (str): Name of the MongoDB database.
        collection_names (list): List of collection names to aggregate.
        mongo_uri (str, optional): MongoDB connection URI. Defaults to 'mongodb://localhost:27017/'.

    Returns:
        list: List of 36 integrated pandas DataFrames.
    """
    try:
        # Establish MongoDB connection
        client = pymongo.MongoClient(mongo_uri)
        db = client[database_name]

        # List all collections in the database
        collection_names = db.list_collection_names()
        # List to store integrated DataFrames
        integrated_dfs = [pd.DataFrame() for _ in range(36)]  # Assuming 36 DataFrames

        # Iterate over each collection
        for collection_name in collection_names:
            collection = db[collection_name]
            documents = list(collection.find())

            if len(documents) != 36:
                print(f"Warning: Collection '{collection_name}' does not contain 36 DataFrames.")

            # Combine DataFrames positionally
            collection = db[collection_name]
            documents = list(collection.find())
            x = 0
            for doc in documents:
                # Load DataFrame from JSON data
                df_json = doc['df_data']
                df = pd.read_json(json.dumps(df_json), orient='split')

                # Append DataFrame to the corresponding position in integrated_dfs
                integrated_dfs[x] = integrated_dfs[x]._append(df)
                integrated_dfs[x] = integrated_dfs[x].sort_index()

                # ======================================================================
                # ======================================================================
                # Remove duplicate indices and calculate mean
                integrated_dfs[x] = integrated_dfs[x].groupby(integrated_dfs[x].index).mean()
                x += 1

        client.close()
        return integrated_dfs

    except Exception as e:
        print(f"Error aggregating collections: {e}")
        return None









def aggregate_and_save_collections(integrated_dfs, mongo_uri='mongodb://localhost:27017/'):
    """
    Aggregate DataFrames and save them into a new database and collections in MongoDB.

    Args:
        integrated_dfs (list): List of DataFrames to be integrated.
        mongo_uri (str, optional): MongoDB connection URI. Defaults to 'mongodb://localhost:27017/'.
    """
    try:
        # Establish connection to the new database
        new_database_name = 'da_result_database'  # New database name
        new_collection_name = 'result_pair_plot'  # New collection name
        new_collection_name1 = 'result_integrated_plot'  # New integrated collection name

        # Establish connection to the new database
        new_client = pymongo.MongoClient(mongo_uri)
        new_db = new_client[new_database_name]

        # Insert each DataFrame into the 'result_pair_plot' collection
        for df in integrated_dfs:
            new_db[new_collection_name].insert_one(df.to_dict(orient='split'))

        # Integrate all DataFrames into one DataFrame
        init_df = integrated_dfs[0]
        for df in integrated_dfs[1:]:
            init_df = init_df._append(df)
            init_df = init_df.groupby(init_df.index).mean()

        # Insert the integrated DataFrame into the 'result_integrated_plot' collection
        new_db[new_collection_name1].insert_one(init_df.to_dict(orient='split'))

        # Close connection to the new database
        new_client.close()

    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage:
# Pass your list of integrated DataFrames as input to the function
# aggregate_and_save_collections(integrated_dfs)



# ======================================================================
# ======================================================================

def final_plot_rising_committee_size_36pics(database_name):

    df_list = aggregate_collections(database_name, mongo_uri='mongodb://localhost:27017/')
    aggregate_and_save_collections(df_list)
    list_of_combis_pd = list(combinations(list(range(0, 9)), 2))
    list_methods = ["avg_avg", "max_avg", "min_avg", "max_max", "min_min", "max_min", "min_max", "avg_min", "avg_max"]
    k = 0
    for i in df_list:
        plot_code.plot_columns(i,list_methods[list_of_combis_pd[k][0]] + " " + "vs" + " " + list_methods[
             list_of_combis_pd[k][1]] )
        plot_code.plot_columns_integrated(i, "integrated" + list_methods[list_of_combis_pd[k][0]] + " " + "vs" + " " + list_methods[
             list_of_combis_pd[k][1]] )
        k += 1





# ======================================================================
# ======================================================================

def final_plot_rising_p_1pic(database_name,file_name):
    df_list = aggregate_collections(database_name, mongo_uri='mongodb://localhost:27017/')
    df = pd.DataFrame()
    k = 0

    for i in df_list:
        avg_values = i.mean(axis=0)
        df1 = pd.DataFrame([avg_values], columns=avg_values.index)
        df = df._append(df1)
        k += 1
    list_n = ['avg_avg vs max_avg', 'avg_avg vs min_avg', 'avg_avg vs max_max', 'avg_avg vs min_min', 'avg_avg vs max_min',
              'avg_avg vs min_max', 'avg_avg vs avg_min', 'avg_avg vs avg_max', 'max_avg vs min_avg', 'max_avg vs max_max',
              'max_avg vs min_min', 'max_avg vs max_min', 'max_avg vs min_max', 'max_avg vs avg_min', 'max_avg vs avg_max',
              'min_avg vs max_max', 'min_avg vs min_min', 'min_avg vs max_min', 'min_avg vs min_max', 'min_avg vs avg_min',
              'min_avg vs avg_max', 'max_max vs min_min', 'max_max vs max_min', 'max_max vs min_max', 'max_max vs avg_min',
              'max_max vs avg_max', 'min_min vs max_min', 'min_min vs min_max', 'min_min vs avg_min', 'min_min vs avg_max',
              'max_min vs min_max', 'max_min vs avg_min', 'max_min vs avg_max', 'min_max vs avg_min', 'min_max vs avg_max',
              'avg_min vs avg_max']

    df.index = list_n

    new_database_name = 'da_result_database'  # New database name
    new_collection_name = 'result_p_plot'  # New collection name
    # Establish connection to the new database
    new_client = pymongo.MongoClient('mongodb://localhost:27017/')
    new_db = new_client[new_database_name]


    # Insert the integrated DataFrame into the 'result_integrated_plot' collection
    new_db[new_collection_name].insert_one(df.to_dict(orient='split'))

    # Close connection to the new database
    new_client.close()
    plot_code.plot_row(df,file_name)
    print(df)



