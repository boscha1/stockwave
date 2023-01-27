from pymongo import MongoClient

client = MongoClient("mongodb://root:rootpassword@localhost:27017/")
db = client["stockdb"]

def create_stock_collection():
    stock_validator = {
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["symbol", "name", "prices"],
            "properties": {
                "symbol": {
                    "bsonType": "string",
                    "description": "must be a string and is required"
                },
                "name": {
                    "bsonType": "string",
                    "description": "must be a string and is required"
                },
                "prices": {
                    "bsonType": "array",
                    "items": {
                        "bsonType": "objectId",
                        "description": "must be an objectId and is required"
                    }
                }
            }
        }
    }

    try:
        db.create_collection("stock")
    except Exception as e:
        print(e)
        
    db.command("collMod", "stock", validator=stock_validator)
    

def create_price_collection():
    price_validator = {
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["date", "open_at", "close_at"],
            "properties": {
                "date": {
                    "bsonType": "date",
                    "description": "must be a date and is required"
                },
                "open_at": {
                    "bsonType": "double",
                    "description": "must be a float and is required"
                },
                "close_at": {
                    "bsonType": "double",
                    "description": "must be a float and is required"
                }
            }
        }
    }
    
    try:
        db.create_collection("price")
    except Exception as e:
        print(e)
        
    db.command("collMod", "price", validator=price_validator)

create_stock_collection()
create_price_collection()