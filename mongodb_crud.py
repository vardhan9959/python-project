# import pymongo 
# connection = pymongo.MongoClient("mongodb://localhost:27017")
# mydb = connection["students"]
# mycol = mydb["info"]

# dict = {
#     "name":"loveleen",
#     "address":"punjab"
# }

# x = mycol.insert_one(dict)
# print("data added")
# print(x.inserted_id)

# import pymongo 

# myclient = pymongo.MongoClient("mongodb://localhost:27017")

# mydb = myclient["mydatabase"]
# ab=mydb["business man"]
# dic={
#     "name":"nayan",
#     "address":"ts"
# }
# ab.insert_one(dic)
# print("successfully added")

# import pymongo 

# connection = pymongo.MongoClient("mongodb://localhost:27017")

# mydb = connection["mydatabase"]
# mytb = mydb["info"]

# dic = {
#     "name":"anusha",
#     "address":"telangana"
    
# }
# x = mytb.insert_one(dic)
# print("table created sucessfully")

# print(x.inserted_id)

# import pymongo 
# connection = pymongo.MongoClient("mongodb://localhost:27017")
# mydb = connection["data"]
# mytb = mydb["student"]

# dic = [
#     {"name":"gopi","address":"khammam"},
#     {"name":"sai","address":"kunchaparthy"},
#     {"name":"venu","address":"vemsoor"},
#     {"name":"ravi","address":"ap"},
#     {"name":"vamsi","address":"npd"},
#  {"name":"siva","address":"kmm"}
# ]
# x = mytb.insert_many(dic)
# print(x.inserted_ids)


# import pymongo 

# connection = pymongo.MongoClient("mongodb://localhost:27017")
# mydb = connection["practice"]
# mytb = mydb["info"]

# dic = [
#     {"id":10,"name":"prabhas","address":"guntur"},
#     {"id":20,"name":"Adya","address":"india"},
#     {"id":30,"name":"mahesh babu","address":"chennai"},
#     {"id":40,"name":"Natasha","address":"usa"},
#     {"id":50,"name":"Trisha","address":"canada"},
#     {"id":60,"name":"shah rukh khan","address":"mumbai"}
    
# ]

# x = mytb.insert_many(dic)
# print(x.inserted_ids)


# import pymongo 
# connection = pymongo.MongoClient("mongodb://localhost:27017")
# mydb = connection["practice"]
# mytb = mydb["info"]

# x = mytb.find_one()
# print(x)

# x = mytb.find() 
# for i in x:
#     print(i)

# import pymongo

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase"]
# mycol = mydb["customers"]

# dict = [ 
#         {"name":"kholi","address":"rcb"},
#         {"name":"rohit","address":"mi"},
#         {"name":"hardik","address":"gt"},
#         {"name":"suresh raina","address":"csk"},
#         {"name":"bhuvi","address":"srh"},
#         {"name":"warner","address":"srh"}
# ]

# mycol.insert_many(dict)
# myquery = { "address": "srh" }

# mydoc = mycol.find(myquery)

# for x in mydoc:
#   print(x)

# import pymongo
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase"]
# mycol = mydb["customers"]

# myquery = { "address": { "$regex": "^S" } }

# mydoc = mycol.find(myquery)

# for x in mydoc:
#   print(x)

# import pymongo

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase"]
# mycol = mydb["customers"]

# mydoc = mycol.find().sort("name")

# for x in mydoc:
#   print(x)

# import pymongo

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase"]
# mycol = mydb["customers"]

# myquery = { "address": "gt" }
# newvalues = { "$set": { "address": "mi" } }

# mycol.update_one(myquery, newvalues)
# for x in mycol.find():
#   print(x)


# import pymongo

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase"]
# mycol = mydb["customers"]

# myquery = { "address": { "$regex": "^P" } }
# newvalues = { "$set": { "name": "jaiswal" } }

# x = mycol.update_many(myquery, newvalues)

# print(x.modified_count, "documents updated.")

# import pymongo
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase"]
# mycol = mydb["customers"]

# myquery = { "address": "mi" }

# mycol.delete_one(myquery)

# import pymongo

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase"]
# mycol = mydb["customers"]

# myquery = { "address": {"$regex": "^U"} }

# x = mycol.delete_many(myquery)

# print(x.deleted_count, " documents deleted.")

# import pymongo

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase"]
# mycol = mydb["customers"]

# x = mycol.delete_many({})

# print(x.deleted_count, " documents deleted.")

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mycol.drop()
