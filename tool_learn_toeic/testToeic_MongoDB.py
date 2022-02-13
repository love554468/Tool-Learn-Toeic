from pymongo import MongoClient

# cluster = "mongodb+srv://binhnd:binhnd123@cluster0.3ua9k.mongodb.net/testToeic?retryWrites=true&w=majority"
cluster = "mongodb+srv://binhnd:FdGYeMBFYD1gRqN4@cluster0.3ua9k.mongodb.net/testToeic&retryWrites=true&w=majority?ssl=true&ssl_cert_reqs=CERT_NONE"
# duatrebanron gmail
client = MongoClient(cluster)
print(client.list_database_names())
db = client.testToeic
print(db.list_collection_names())