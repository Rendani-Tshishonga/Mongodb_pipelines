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
MONGODB_URI =  os.environ["MONGODB_URI"]

# Create a connection the MongoDB instance
client = MongoClient(MONGODB_URI, server_api=ServerApi('1'))

# Get a reference to the sample_airbnb database
db = client.sample_airbnb

#Get a reference to the listingsAndReviews collection
listings_collection = db.listingsAndReviews

# Query a document by filtering it by _id key
document_to_find = {"_id": "10082422"}

# Write and expression that retrieves the document matching the query constraint in the listingsAndReviews collection
result = listings_collection.find_one(document_to_find)

# Print the result to standard output
print(result)