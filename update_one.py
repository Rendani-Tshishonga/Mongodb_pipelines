#!/usr/bin/python3

"""
A python script that updates a document in a collection.
"""
# Import Libraries
from dotenv import laod_dotenv
from pymongo import MongoClient
from pymongo.server_api import ServerApi
import os

# Connection string URI
load_dotenv()
MONGODB_URI = os.environ["MONGODB_URI"]

# Connect to the mongodb cluster 
client = MongoClient(MONGODB_URI, server_api=ServerApi('1'))

# Get a reference to the sample_analytics database
db = client.sample_analytics

# Get a reference to the accounts collection
accounts_collection = db.accounts

# Filter the document to update by object _id
document_to_update = {"account_id": 375872}

# Update the limit from 10000 to 20000
update_limit = {"$inc": {"limit": 20000}}

# Print the original document
print(accounts_collection.find_one(document_to_update))

# Write an expression that adds to the target limit by the specified amount
results = accounts_collection.update_one(document_to_update, update_limit)

# Print how many documents have been modified
print("Documents updated :" + str(results.modified_count))

# Print the updated document
print(accounts_collection.find_one(document_to_update))

# Close the connection to the instance
client.close()