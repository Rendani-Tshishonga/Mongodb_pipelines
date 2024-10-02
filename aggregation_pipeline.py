#!/usr/bin/python3

"""
A script that creates an aggregation pipeline
"""
# Import libraries
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.server_api import ServerApi
import os

# Mongodb URI
load_dotenv()
MONGODB_URI = os.environ["MONGODB_URI"]

# Create a connection to the mongodb instance 
client = MongoClient(MONGODB_URI, server_api=ServerApi('1'))

# Get a reference to the sample_analytics database
db = client.sample_analytics

# Get a reference to the accounts collection
accounts_collection = db.accounts

# Select documents with limit less than 3000
account_match = {"$match": {"limit": {"$lt": 30000}}}

# sort the results by account_id in descending order
sort_account_results = {"$sort": {"account_id": -1}}

# Limit the results to only the first 10 documents that are matched
limit_document_match = {"$limit": 10}

# Create ab aggregation pipeline using the account_match, sort_account_results and limit_document_match
pipeline = [
    account_match,
    sort_account_results,
    limit_document_match,
]

# Perform an aggregation on pipeline
results = accounts_collection.aggregate(pipeline)

# Print the results
for item in results:
    print(item)

# Close the connection to the mongodb instance
client.close()