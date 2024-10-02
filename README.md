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

Example:
```
from bson.objectid import ObjectId
```
    1. ObjectId
    2. Int64
    3. Decimal128
    4. Regex(regular expressions)

We are not restricted to using the bson package data types, we can also incorporate native Python types when working with Mongodb by using Pymongo.

### Create a connection to the Mongodb cluster

We can create a connection to the Mongodb cluster by installing the mongodb compass on your local server to ensure that we have a runtime variable which points to the connection string used to create a connection to the cluster without exposing your passwd externally. This provides a great benefit as you will be able to use environment variables to create connections to your instance and will allow you to query your databases interactively through your local server. We will use the load_dotenv to load the various .env files which contain all variables thats should be loaded into your test or production environments.

Example:
```
from dotenv import load_dotenv
import os # to access the enviroment variable uri

load_dotenv()
MONGODB_URI = os.environ["MONGODB_URI]
```

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

### Structure of a Pipeline

Example:
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
The documents that are output of one stage act as input for the next stage of the pipeline.

### **$match**

filters for data that matches criteria

Example:
```
$match {
    "student_id": 1234
}
```
### $group

The $group operator groups documents by a group key

Example:
```
{
    $group:
    {
        "_id": expression, # group key
        <field>: {<accumulator>: <expression>}
    }
}
```
### $sort

The sort all input documents and passes them through the pipeline in sorted order.

1: Ascending order
-1: descending order

Example:
```
{
    $sort: {
        "field-name": 1
    }
}
```
### $project

The $project stage specifies the fields of the output documents that you want to show in the results of your pipeline output.
1 - means that the field should be included
0 - means that the field should be supressed

Example:
```
{
    $project: {
        state: 1,
        zip: 1,
        population: "$pop",
        _id = 0
    }
}
```
### $set

The $set stage creates new fields or changes the value of the existing fields, then outputs the documents with the new fields

Example:
```
{
    $set: {
        place: {
            $concat: ["$city" , "," , "$state"]
        }
    }
}
```
### $count

The $count stage creates a new document, with the number of documents at that stage in the pipeline assigned to the specified field name

Example:
```
$count: "total_zips"
```
### $out

The $out operator writes documents that are returned by the pipeline into a new collection. When a collection already exists the $out operator replaces the existing collection with new data. We must note that the $out operator should be used as the last stage within the pipeline to ensure results are obtained to populate the new collection.

Example:
```
[{
    $group: {
        _id: $state,
        total_pop: {$sum: "$pop"}
    }
},
{
    $match: {
        total_pop: {$lt: 100000}
    }
},
{
    $out: "small_status"
}]
```
### Close

When we have an active connection to our Mongodb database instance we need to ensure we close our connection using the close() method to ensure we do not have any persisting connections to the instance.