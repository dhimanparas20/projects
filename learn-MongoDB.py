#import pymongo and refer to "https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu/" for linux installation 
#mongo db cheetsheat "https://www.codewithharry.com/blogpost/mongodb-cheatsheet/"
import pymongo 

#Connecting to the  client local/cloud.
client = pymongo.MongoClient("mongodb://localhost:27017/")
'''client = pymongo.MongoClient("mongodb+srv://<username>:<password>@cluster1.n5hitou.mongodb.net/?retryWrites=true&w=majority")'''
print(client)

#Creating a collection/datafield
db = client["main"]  #name of DB
collection = db['api'] # name of collection

#Inserting single value to collection
'''dict = {"name":"Paras","api":"qwertyuiop"}
collection.insert_one(dict)
'''

#Inserting multiple value to collection
dict = [{"name":"Paras","api":"qwertyuiop","age":6},
        {"name":"Ansh","api":"asdfghjkl","age":66},
        {"name":"Arun","api":"zxcvbnm","age":56},
        {"name":"Nikhil","api":"qaz","age":99},
        {"name":"Nikhil","api":"wsx","age":34}              
] 
collection.insert_many(dict)


# Show all items inside collection
'''one = collection.find()
print(collection.count_documents({}))  #returns the total count of documents
for item in one:
  print(item)
'''

# Finding Single value from collection
'''one = collection.find_one({"name":"Arun"})
print(one)
'''

# Finding Multiple value from collection
'''one = collection.find({"name":"Nikhil"})
for item in one:
  print(item)
'''  

# modifiers/conditions  (lte,gte)
'''ab = collection.find({"age": {"$lte":1000}},{"_id":0})
print(collection.count_documents({"age": {"$lt":20}}))
print(ab)
'''

#Viewing only the fields you want to see and limiting it
'''one = collection.find({"name":"Nikhil"},{"_id":0}).limit(1)
print(collection.count_documents({"name":"Nikhil"}))
for item in one:
  print(item)
'''

# Updating single filed inside collection  
'''prev = {"name":"Arun"}
nxt = {"$set":{"name":"Tarun"}}
collection.update_one(prev,nxt)
'''

# Updating multiple fileds inside collection  
'''prev = {"name":"Abhay"}
nxt = {"$set":{"name":"Mia"}}
up = collection.update_many(prev,nxt)
print(up.modified_count)  #return no of rows/items edited
'''

# Deleting single fields
'''
up = collection.delete_one({"name":"Ansh"})
print(up.deleted_count)
'''

# Deleting multiple fields
'''up = collection.delete_many({"name":"Nikhil"})
print(up.deleted_count)
'''

# Deleting all fields
'''up = collection.delete_many({})
print(up.deleted_count)
'''

# Deleting a collection name and deleting Database name
''''db.drop_collection('api')
client.drop_database('main')
'''
