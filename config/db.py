from pymongo import MongoClient
import yfinance as yf

client = MongoClient("mongodb://root:rootpassword@localhost:27017/")
db = client["stockdb"]

def create_stock_collection():
    stock_validator = {
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["symbol", "name"],
            "properties": {
                "symbol": {
                    "bsonType": "string",
                    "description": "must be a string and is required"
                },
                "name": {
                    "bsonType": "string",
                    "description": "must be a string and is required"
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
            "required": ["date", "open_at", "close_at", "symbol"],
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
                },
                "symbol": {
                    "bsonType": "string",
                    "description": "must be a string and is required"
                }
            }
        }
    }
    
    try:
        db.create_collection("stock_price_data")
    except Exception as e:
        print(e)
        
    db.command("collMod", "stock_price_data", validator=price_validator)

create_stock_collection()
create_price_collection()