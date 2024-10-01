# MongoDB Python Data Pipelines

Mongodb is a NoSQL database which stores data in the form of documents which are formatted in a BSON format. There are similarities to the JSON format which are work with in relation to API. 

## BSON

    1. This is an extension of JSON.
    2. BSON is optimized for storage, retrieval and transmission across the wire.
    3. More secure that JSON.
    4. Supports more data types than JSON.

We will connect to our Mongodb instances using the Pymongo driver which will help us  to request BSON documents as python dictionaries. Pymongo will allow us to work with native python data types, pymongo automatically converts python data types to and from BSON.

We will seek to build CRUD pipelines (create, update, delete) by importing the MongoClient from the pymongo library which allows us to create a connection to our MongoDB instance through a connection string.

## Data Types
The data types that need to use PyMongo's bson package include
We would need to import the bson package to access these data types by:

```
from bson.objectid import ObjectId
```
    1. ObjectId
    2. Int64
    3. Decimal128
    4. Regex(regular expressions)

We are not restricted to using the bson package data types, we can also incorporate native Python types when working with Mongodb by using Pymongo.

## Insert a document

In MongoDB to insert a document into a collection we will need to append the insert_one() method to the collection object to return a result. The inser_one() method accepts a document as an argument and returns a result.

## Insert documents

We might be required to insert mutliple documents into a collection and Pymongo provides a method to do just that, like the inser_one method which accepts a document, we would use the insert_many() method and pass an array of documents as argument to insert multiple documents to the collection with unique objectId's to represent each unique document.

## Querying a MongoDB collection for a single document

We can return a single document that matches a query by appending the method find_one() to the collection object. The find_one method can accept a filter argument that specifies the query to be performed. The find_one method with parse through the collection to and return the documents which matches the query, or it returns none if there are no matches.

## Querying for multiple documents

We can return multiple documents that match a query and append find() to the collection object. The find method can accept a filter argument that specifies the query to be perfomed on the collection. The find method returns a cursor instance, which allows us to iterate over all matching documents. We will use the cursor instance to print out the document that matched the query as well as the total number of documents found.

## Update One document

When updating a single document which matches a query we would need to append the update_one method to the collection object. The update_one method has two required parameters, firstly a filter document that matches the document to update and secondly an update that specifies the modifications to apply to the matching document.

## Update many documents

When updating multiple documents that match a specific query we would need to append the update_many method to the collection object. The update_many method also has two required parameters, firtly the filter that matches the document to update and an update document that specifies the modifications to apply to the matching document.

## Delete a Single document

We can delete a single document that matches a query by appending the delete_one method to the collection object. The delete_one method has a parameter, which is a filter that matches the document to delete. **We need to note something important about the delete_one method in that if you do not provide a parameter the delete_one method will delete the first document in the collection.**

## Aggregation Operators

The collecton and the summary of data can be done through operators which enable developers to use built-in methods that can be computed on the data but does not permanently alter it. We can combine the various stages to create a an aggregation pipeline to allow the data to be **filetered**, **stored**, **grouped**, **transformed**.

### Structure of an Aggregation Pipeline

```
db.collection.aggregate([{
    $stage1: {
        {expression 1},
        {expression 2},
    },
    $stage2: {
        {expression 1}
    }
}])

```
The documents that are output of one stage act as input for the next stage of the aggregation pipeline.

### **$match**
filters for data that matches criteria

```
$match {
    "student_id": 1234
}
```


