from pymongo import MongoClient

# #loading database

my_client = MongoClient("localhost",27017)
my_db=my_client["cse4"]
my_collection = my_db["student"]


# #insertind dara to collection

# my_collection.insert_one({"name":"tiru","city":"pdl"})

#my_collection.insert_many([{"name":"ashok","city":"ong"},
#                          {"name":"siri","city":"kdk"}])


# #updating documents in collection
#my_collection.update_many({"city":"ong"},{"$set":{"city":"ongole"}})

# #deleting documents in collection
#my_collection.delete_one({"name":"ashok"})


op=list(my_collection.find())
print(op)