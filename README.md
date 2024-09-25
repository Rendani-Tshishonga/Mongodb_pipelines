# MongoDB Python Data Pipelines

Mongodb is a NoSQL database which stores data in the form of documents which are formatted in a BSON format. There are similarities to the JSON format which are work with in relation to API. 
## BSON
    1. This is an extension of JSON.
    2. BSON is optimized for storage, retrieval and transmission across the wire.
    3. More secure that JSON.
    4. Supports more data types than JSON.

We will connect to our Mongodb instances using the Pymongo driver which will help us  to request BSON documents as python dictionaries. Pymongo will allow us to work with native python data types, pymongo automatically converts python data types to and from BSON.

We will seek to build CRUD pipelines (create, update, delete) by importing the MongoClient from the pymongo library which allows us to create a connection to our MongoDB instance through a connection string.