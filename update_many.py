#!/usr/bin/python3

"""
A python script that updates many documents in a collection.
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
db = client.sample_airbnb

# Get a reference to the listingsAndReviews collection
listings_collection = db.listingsAndReviews

# Filter the document to update by object _id
document_to_update = {"minimum_nights": "2"}

# Update the limit from 10000 to 20000
set_field = {"$set": {"bed_type": "fake bed"}}

# Write an expression that adds to the target limit by the specified amount
results = listings_collection.update_many(document_to_update, set_field)

# Print how many documents were matched
print("Documents matched : " + str(results.matched_count))

# Print how many documents have been modified
print("Documents updated : " + str(results.modified_count))

# Close the connection to the instance
client.close()