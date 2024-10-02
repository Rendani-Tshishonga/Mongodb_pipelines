#!/usr/bin/python3

"""
A script that deletes multiple documents in a collection
"""
# Import Libraries
from pymongo import MongoClient
from pymongo.server_api import ServerApi

# Mongodb_uri
MONGODB_URI = "mongodb+srv://myAtlasDBUser:TXR029w7QVCajDSQ@myatlasclusteredu.3xgmh1o.mongodb.net/?retryWrites=true&w=majority&appName=myAtlasClusterEDU"

# Create a connection to the mongodb cluster 
client = MongoClient(MONGODB_URI, server_api=ServerApi('1'))

# Get a reference to the sample_analytics database
db = client.sample_analytics

# Get a reference to the accounts collection
accounts_collection = db.accounts

#