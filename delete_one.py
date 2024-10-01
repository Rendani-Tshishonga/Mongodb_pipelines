#!/usr/bin/python3

"""
A python script that deletes a document in a collection
"""
# Import Libraries
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
import os

# Connection String
load_dotenv()
MONGODB_URI = os.environ["MONGODB_URI"]

# Connect to the Mongodb instance
client = MongoClient(MONGODB_URI, server_api=ServerApi('1'))

# Get a reference to the sample_analytics database
db = client.sample_analytics

# Get a reference to the customers collection
customer_collection = db.customers

# The document to delete
document_to_delete = {"_id": ObjectId('66f56145970936296d2ff056')}

# Search and print the document to delete
print(customer_collection.find_one(document_to_delete))

# Write an expression that deletes the target account
results = customer_collection.delete_one(document_to_delete)

# Print the deleted document count from the results variable
print("Documents deleted: " + str(results.deleted_count))

