#!/usr/bin/python3

"""
A script that deletes multiple documents in a collection
"""
# Import Libraries
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.server_api import ServerApi
import os

# Mongodb_uri
load_dotenv()
MONGODB_URI = os.eviron["MONGODB_URI"]

# Create a connection to the mongodb cluster 
client = MongoClient(MONGODB_URI, server_api=ServerApi('1'))

# Get a reference to the sample_analytics database
db = client.sample_analytics

# Get a reference to the accounts collection
accounts_collection = db.accounts

#
