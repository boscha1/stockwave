from pymongo import MongoClient

client = MongoClient("mongodb://root:rootpassword@localhost:27017/")
db = client["stockdb"]

# validate schema
validator = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["symbol", "name", "price"],
        "properties": {
            "symbol": {"bsonType": "string"},
            "name": {"bsonType": "string"},
            "price": {"bsonType": "double"}
        }
    }
}

# db.create_collection("stocks", validator=validator, validation_level="strict")

# init collections
stock_collection = db["stocks"]
user_collection = db["users"]