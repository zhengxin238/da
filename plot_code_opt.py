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






# Function to chunk a DataFrame into smaller DataFrames with 8-row chunks








def plot_row(df, j):
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
    plt.savefig(f"{j}_marks.png")

    # Show the plot
    plt.show()


def plot_columns_integrated(df, j):
    # Create a larger square-shaped plot
    plt.figure(figsize=(8, 8))

    markers = cycle(['o', 's', '^', 'd', 'x'])  # Generate markers dynamically

    for column in df.columns:
        marker = next(markers)  # Get the next marker from the cycle
        plt.plot(df.index, df[column], marker=marker, linestyle='', label=column, markersize=2)

    plt.xlabel('committe_size in percentage')  # Customize the x-axis label as needed
    plt.ylabel('value in percentage')  # Customize the y-axis label as needed
    plt.title(f'{j}')  # Customize the plot title as needed
    plt.legend()  # Adjust legend position

    # Adjust layout to prevent overlapping elements
    plt.tight_layout()
    plt.savefig(f'{j}_plot.png')
    # Show the plot
    plt.show()

def plot_columns_integrated(df, j):
    # Create a larger square-shaped plot
    plt.figure(figsize=(8, 8))

    markers = cycle(['o', 's', '^', 'd', 'x'])  # Generate markers dynamically

    for column in df.columns:
        marker = next(markers)  # Get the next marker from the cycle
        plt.plot(df.index, df[column], marker=marker, linestyle='', label=column, markersize=2)

    plt.xlabel('committe_size in percentage')  # Customize the x-axis label as needed
    plt.ylabel('similarity in percentage')  # Customize the y-axis label as needed
    plt.title(f'integrated_{j}')  # Customize the plot title as needed
    plt.legend()  # Adjust legend position

    # Adjust layout to prevent overlapping elements
    plt.tight_layout()
    plt.savefig(f'integrated_{j}_plot.png')
    # Show the plot
    plt.show()

def plot_columns(df, j):
    markers = cycle(['o', 's', '^', 'd', 'x'])  # Generate markers dynamically

    for column in df.columns:
        plt.figure(figsize=(8, 8))  # Create a new figure for each column
        marker = next(markers)  # Get the next marker from the cycle
        plt.plot(df.index, df[column], marker=marker, linestyle='', label=column)
        plt.xlabel('committe_size in percentage')  # Customize the x-axis label as needed
        plt.ylabel('value in percentage')  # Customize the y-axis label as needed
        plt.title(f'{j} - {column}')  # Customize the plot title as needed
        plt.legend()  # Adjust legend position
        # Adjust layout to prevent overlapping elements
        plt.tight_layout()
        plt.savefig(f'{j}_{column}_plot.png')
        # Show the plot
        plt.show()





