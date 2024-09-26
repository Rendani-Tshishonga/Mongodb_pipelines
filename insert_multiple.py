#!/usr/bin/python3

"""
A script to add multiple documents to the customer collection
"""
# Import libraries
import datetime
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.server_api import ServerApi
import os

# Load Config fron.env file
load_dotenv()
MONGODB_URI = os.eviron["MONGODB_URI"]

# Connect to MongoDB cluster with MongoClient
client = MongoClient(MONGODB_URI)

# Get a reference to the sample_analytics database
db = client.sample_analytics

# Get a reference to the customers collection
customer_collection = db.customers

# Create new customer documents
new_customers = [
    {
        "username": "dominicTorrento",
        "name": "Victor Wanyama",
        "address": "19 Midrand drive, Vanderbijlpark, 1900",
        "birthdate": datetime.datetime.utcnow(),
        "email": "victorm@gmail.com",
        "account": [830206, 890812, 457406]
    },
    {
        "username": "WhyMeTorrento",
        "name": "Teboho Mang",
        "address": "18 Hours to Italy, Sebokeng, 1900",
        "birthdate": datetime.datetime.utcnow(),
        "email": "whymefake@gmail.com",
        "account": [450206, 890809, 455406]
    }
]

# Write an expression that inserts the documents in the new customers documents in the customers collection
results = customer_collection.insert_many(new_customers)

# Verify by printing the number of inserted_ids in a variable document_ids
document_ids = results.inserted_ids

# Print the number of inserted ids 
print("The number of inserted documents: " + str(len(document_ids)))

#Print the inserted ids
print(f"_ids of inserted documents: {document_ids}")

# Close the connection
client.close()