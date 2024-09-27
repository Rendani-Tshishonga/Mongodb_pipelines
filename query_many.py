#!/usr/bin/python3

"""
A MongoDB script to query a document in the listingsAndReviews collection
"""
# Import Libraries
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.server_api import ServerApi
import os

# Load Config from .env file
load_dotenv()
MONGODB_URI = os.environ["MONGODB_URI"]

# Create a connection the MongoDB instance
client = MongoClient(MONGODB_URI, server_api=ServerApi('1'))

# Get a reference to the sample_airbnb database
db = client.sample_analytics

#Get a reference to the listingsAndReviews collection
accounts_collection = db.accounts

# Query a document by filtering the withdrawal limit which is equal to 1000
document_to_find = {"limit": {"$eq": 10000}}

# Write and expression that retrieves the document matching the query constraint in the accounts collection
account_list = accounts_collection.find(document_to_find)

# Create a counter for the number of documents
num_docs = 0
for documents in account_list:
    num_docs += 1
    print(documents)
    print()

# Print the result to standard output
print("# of documents found:" + str(num_docs))

# Close connection to instance
client.close()