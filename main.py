import pandas as pd
import pymongo
from itertools import combinations


def compare_candidates(dict1, dict2):
    keys_dict1 = [key for key, value in dict1.items() if value == 1.0]
    keys_dict2 = [key for key, value in dict2.items() if value == 1.0]
    # Count the number of keys with value 1.0 that are the same in both dictionaries
    count_same = sum(1 for key in keys_dict1 if key in keys_dict2)
    percentage_same =  count_same/len(keys_dict1)
    return percentage_same


# cleint_name="mongodb://localhost:27017/"
# db_name="DataTest_Voting"
# collection_name='all_methods_00009-00000001'


def get_similarity_inPercent(cleint_name,db_name,collection_name):

    list_of_combis_pd = list(combinations(list(range(0,9)),2))

    percentage_df = pd.DataFrame(columns= list_of_combis_pd)

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
                list_of_chosen_candidate = []
                for key_3, value_3 in value_2.items():
                        items = list(value_3.items())
                        best_committee = items[0][1]
                        list_of_chosen_candidate.append(best_committee)
                list_of_combis = list(combinations(list(range(len(list_of_chosen_candidate))),2))
                row_values =[]
                for combi in list_of_combis:
                    percentage_value = compare_candidates(list_of_chosen_candidate[combi[0]],list_of_chosen_candidate[combi[1]])
                    row_values.append(percentage_value)
                percentage_df.loc[len(percentage_df)] = row_values

    column_averages = percentage_df.mean()
    print(column_averages)
    return column_averages

# get_similarity_inPercent(cleint_name,db_name,collection_name)
