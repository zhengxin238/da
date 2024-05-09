import json

import pandas as pd
import pymongo

import plot_code
import plot_code_opt


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
        integrated_dfs = [pd.DataFrame() for _ in range(9)]  # Assuming 36 DataFrames

        # Iterate over each collection
        for collection_name in collection_names:
            collection = db[collection_name]
            documents = list(collection.find())

            if len(documents) != 9:
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

def final_plot_opt_9pics(database_name):

    df_list = aggregate_collections(database_name, mongo_uri='mongodb://localhost:27017/')

    list_methods = ["avg_avg", "max_avg", "min_avg", "max_max", "min_min", "max_min", "min_max", "avg_min", "avg_max"]
    k = 0
    for i in df_list:
        plot_code_opt.plot_columns(i,list_methods[k])
        plot_code_opt.plot_columns_integrated(i,list_methods[k])
        plot_code_opt.plot_row(i, list_methods[k])
        k += 1

final_plot_opt_9pics("DataSet_9_opt_value")