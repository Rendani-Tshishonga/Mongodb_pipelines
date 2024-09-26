#!/usr/bin/python3

"""
A MongoDB pipeline to insert a document in a collection
"""
# Import Libraries
import datetime
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.server_api import ServerApi
import os


# Load config from .env file
load_dotenv()
MONGODB_URI = os.environ["MONGODB_URI"]

# Connect to MongoDB cluster with MongoClient
client = MongoClient(MONGODB_URI, server_api=ServerApi('1'))

# Get a reference to the 'sample_analytics' database
db = client.sample_analytics

# Get a reference to the 'accounts' collection
customer_collection = db.customers

# Create a new customer document
new_customer = {
    "username": "refilwem",
    "name": "Thomas Edison",
    "address": "13 Bryston drive, Sandton",
    "birthdate": datetime.datetime.utcnow(),
    "email": "fakeemail@gmail.com",
    "account": [729195, 789701, 346396]
}

# Write an expression that inserts the new_customer document into the "customers" collection
results = customer_collection.insert_one(new_customer)

# Store the new inserted document id in the variable document_id
document_id = results.inserted_id
print(f"_id of the inserted document: {document_id}")

# Close the connection
client.close()