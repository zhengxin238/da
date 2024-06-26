import os
from itertools import combinations
import json
import pymongo
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from itertools import cycle


def insert_into_mongodb(client, db, collection, data):
    collection.insert_one(data)
    # Close connection
    client.close()
def interpolate_and_merge(dfs_list, num_points):
    # Create a common x-axis grid
    x_values = np.linspace(min(df.index.min() for df in dfs_list), max(df.index.max() for df in dfs_list), num_points)

    # Initialize an empty DataFrame to store interpolated and merged data
    merged_df = pd.DataFrame(index=x_values)

    # Interpolate and merge data for each DataFrame
    for df in dfs_list:
        # Interpolate data onto the common x-axis grid using cubic spline interpolation
        interpolated_df = df.reindex(x_values).interpolate(method='spline', order=3)

        # Merge interpolated data into the merged DataFrame
        merged_df = pd.concat([merged_df, interpolated_df], axis=1)

    # Calculate the mean across all samples
    avg_merged_df = merged_df.mean(axis=1)

    return avg_merged_df


# # Example usage:
# dfs = [df1, df2, df3]  # List of DataFrames
# num_points = 100  # Number of points on the common x-axis grid
# result_df = interpolate_and_merge(dfs, num_points)
# print(result_df)




# Function to chunk a DataFrame into smaller DataFrames with 8-row chunks
def chunk_dataframe(df, num_chunks=36):
    # Calculate the integer chunk size
    chunk_size = len(df) // num_chunks

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
        chunked_dfs.append(chunk)  # Append the chunk to the list of chunked DataFrames

    return chunked_dfs


# def relax_rows_to_fixed_number(df, num_points):
#     # Create a common index for interpolation
#     new_index = np.linspace(df.index.min(), df.index.max(), num_points)
#
#     # Interpolate along the columns using spline interpolation
#     interpolated_df = pd.DataFrame(index=new_index)
#     for col in df.columns:
#         spline = UnivariateSpline(df.index, df[col])
#         interpolated_values = spline(new_index)
#         interpolated_df[col] = interpolated_values
#
#     return interpolated_df


def interpolate_and_merge(dfs, num_points):
    # Create a common x-axis grid
    x_values = np.linspace(min(df.index.min() for df in dfs), max(df.index.max() for df in dfs), num_points)

    # Initialize an empty DataFrame to store interpolated and merged data
    merged_df = pd.DataFrame(index=x_values)

    # Interpolate and merge data for each DataFrame
    for df in dfs:
        # Interpolate data onto the common x-axis grid using cubic spline interpolation
        interpolated_df = df.reindex(x_values).interpolate(method='spline', order=3)

        # Merge interpolated data into the merged DataFrame
        merged_df = pd.concat([merged_df, interpolated_df], axis=1)

    # Calculate the mean across all samples
    avg_merged_df = merged_df.mean(axis=1)

    return avg_merged_df


import matplotlib.pyplot as plt
from itertools import cycle

def plot_row(df, j):
    # Ensure the output directory exists
    output_dir = 'D:/output_final/da_one_rows/'
    os.makedirs(output_dir, exist_ok=True)  # Create the directory if it doesn't exist

    markers = cycle(['o', 's', '^', 'd', 'x'])  # Generate markers dynamically
    # Iterate over each row in the DataFrame
    for index, row in df.iterrows():
        # Create a new figure for each row
        plt.figure(figsize=(8, 8))  # Adjust figure size as needed
        marker = next(markers)
        plt.scatter(df.columns, row, label=index, marker=marker, s=20)  # Plot marks for each row with a label

        # Set the y-axis limits to range from 0 to 1
        plt.ylim(0, 1)

        # Set aspect ratio to be equal (to make the plot square)
        plt.gca().set_aspect('equal', adjustable='box')

        # Add labels and legend
        plt.xlabel('rising_p')
        plt.ylabel('difference in percentage')
        plt.legend(loc='best', fontsize='small')  # Adjust legend position and font size
        plt.title(f"{j}_{index}")

        # Save the plot
        plt.savefig(f"{output_dir}/{j}_{index}_marks.png")

        # Close the plot to release memory
        plt.close()





def plot_row_integrated(df, j):
    # Ensure the output directory exists
    output_dir = 'D:/output_final/da_one_rows/'
    os.makedirs(output_dir, exist_ok=True)  # Create the directory if it doesn't exist

    # Create a larger square-shaped plot
    plt.figure(figsize=(8, 8))
    markers = cycle(['o', 's', '^', 'd', 'x'])  # Generate markers dynamically
    # Iterate over each row in the DataFrame
    for index, row in df.iterrows():
        marker = next(markers)
        plt.scatter(df.columns, row, label=index, marker=marker, s=2)  # Plot marks for each row with a label

    # Set the y-axis limits to range from 0 to 1
    plt.ylim(0, 1)

    # Set aspect ratio to be equal (to make the plot square)
    plt.gca().set_aspect('equal', adjustable='box')

    # Add labels and legend
    plt.xlabel('rising_p')
    plt.ylabel('difference in percentage')
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize='small')  # Adjust legend position
    plt.title(f"{j}")

    # Adjust layout to prevent overlapping elements
    plt.tight_layout()

    # Save the plot
    plt.savefig(f"{output_dir}/{j}_marks.png")

    # Show the plot
    plt.show()


def plot_columns_integrated(df, j):
    # Ensure the output directory exists
    output_dir = 'D:/output_final/da_one_columns/'
    os.makedirs(output_dir, exist_ok=True)  # Create the directory if it doesn't exist

    # Create a larger square-shaped plot
    plt.figure(figsize=(8, 8))

    markers = cycle(['o', 's', '^', 'd', 'x'])  # Generate markers dynamically

    for column in df.columns:
        marker = next(markers)  # Get the next marker from the cycle
        plt.plot(df.index, df[column], marker=marker, linestyle='', label=column, markersize=2)

    plt.xlabel('committe_size in percentage')  # Customize the x-axis label as needed
    plt.ylabel('similarity in percentage')  # Customize the y-axis label as needed
    plt.title(f'{j}')  # Customize the plot title as needed
    plt.legend()  # Adjust legend position

    # Adjust layout to prevent overlapping elements
    plt.tight_layout()
    plt.savefig(f'{output_dir}/{j}_plot.png')
    # Show the plot
    plt.show()


def plot_columns(df, j):

    # Ensure the output directory exists
    output_dir = 'D:/output_final/da_one_columns/'
    os.makedirs(output_dir, exist_ok=True)  # Create the directory if it doesn't exist

    markers = cycle(['o', 's', '^', 'd', 'x'])  # Generate markers dynamically

    for column in df.columns:
        plt.figure(figsize=(8, 8))  # Create a new figure for each column
        marker = next(markers)  # Get the next marker from the cycle
        plt.plot(df.index, df[column], marker=marker, linestyle='', label=column)
        plt.xlabel('committe_size in percentage')  # Customize the x-axis label as needed
        plt.ylabel('similarity in percentage')  # Customize the y-axis label as needed
        plt.title(f'{j} - {column}')  # Customize the plot title as needed
        plt.legend()  # Adjust legend position
        # Adjust layout to prevent overlapping elements
        plt.tight_layout()
        plt.savefig(f'{output_dir}/{j}_{column}_plot.png')
        # Show the plot
        plt.show()

def get_normalised_result(df):
    chunked_dfs = chunk_dataframe(df)
    normalised_dfs_list = []

    for i in chunked_dfs:

        step_size = 100 / len(i)
        i = i.copy()
        i.loc[:, 'Nomalised_committe_size'] = np.arange(0, 100, step_size)[:len(i)]
        i.set_index(i.iloc[:, -1], inplace=True)
        # Drop the last column
        i = i.iloc[:, :-1]
        i.index.name = None
        normalised_dfs_list.append(i)

    return normalised_dfs_list


def store_dfs_in_mongodb(cleint_name_t,database_name_t, collection_name_t, list_of_dfs):
    """
    Store a list of pandas DataFrames into MongoDB.

    Parameters:
    - uri (str): MongoDB connection URI (e.g., 'mongodb://localhost:27017/')
    - database_name (str): Name of the MongoDB database
    - collection_name (str): Name of the MongoDB collection to store DataFrames
    - list_of_dfs (list): List of pandas DataFrames to store in MongoDB
    """
    # Connect to MongoDB
    mongo_client = pymongo.MongoClient(cleint_name_t)

    # Access the specified database and collection
    db = mongo_client[database_name_t]
    collection = db[collection_name_t]

    try:
        # Store each DataFrame in MongoDB
        for idx, df in enumerate(list_of_dfs):
            # Convert DataFrame to JSON string
            df_json = df.to_json(orient='split')
            # Insert JSON data into MongoDB
            collection.insert_one({'df_id': idx, 'df_data': json.loads(df_json)})

        print("DataFrames stored successfully in MongoDB.")

    except Exception as e:
        print(f"Error occurred while storing DataFrames in MongoDB: {e}")

    finally:
        # Close MongoDB connection
        mongo_client.close()

def plot_normalised_result(normalised_dfs_list):
    namel = list(combinations(list(range(0, 9)), 2))
    j = 0
    for i in normalised_dfs_list:
        plot_columns(i,namel[j])
        j += 1

