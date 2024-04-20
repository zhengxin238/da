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


# Example usage:
if __name__ == "__main__":
    # MongoDB settings
    database_name = 'your_database_name'
    collection_names = ['collection1', 'collection2', 'collection3']  # List of collection names

    # Aggregate DataFrames from collections
    aggregated_dfs = aggregate_collections(database_name, collection_names)
    if aggregated_dfs:
        print("DataFrames aggregated successfully!")
        # aggregated_dfs now contains a list of 36 integrated pandas DataFrames
        for idx, df in enumerate(aggregated_dfs):
            print(f"DataFrame {idx + 1} shape: {df.shape}")

        # Perform further processing on aggregated_dfs as needed
    else:
        print("Error aggregating DataFrames from collections.")

# ======================================================================
# ======================================================================


database_name = "DataSet_36pairs"

l = aggregate_collections(database_name, mongo_uri='mongodb://localhost:27017/')

list_of_combis_pd = list(combinations(list(range(0, 9)), 2))
list_methods = ["avg_avg", "max_avg", "min_avg", "max_max", "min_min", "max_min", "min_max", "avg_min","avg_max"]
k = 0
for i in l:
    plot_code.plot_columns(i, list_methods[list_of_combis_pd[k][0]] + " " + "vs" + " " + list_methods[
        list_of_combis_pd[k][1]])
    k += 1
