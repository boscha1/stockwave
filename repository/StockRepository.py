# stock_repository.py
from config.db import db
from util.Singleton import Singleton

class StockRepository(metaclass=Singleton):
    def __init__(self):
        self.stock_collection = db.stock
        self.price_collection = db.stock_price_data

    def get_stock_by_symbol(self, symbol):
        # stock = self.stock_collection.find_one({"symbol": symbol.upper()})
        # # return stock
        value = list(self.stock_collection.aggregate([{
            "$lookup": {
                "from": "stock_price_data",
                "localField": "symbol",
                "foreignField": "symbol",
                "as": "prices"
            }
        },
        { "$unset": "prices.symbol"},
        { "$match" : { "symbol" : symbol.upper() } }]))
        
        if len(value) == 1:
            return value[0]
        return None

    def get_all_stocks(self):
        return self.stock_collection.find({}, {"_id": 0})

    def insert_stock(self, stock):
        self.stock_collection.insert_one(stock)

    def update_stock(self, symbol, price_id):
        self.stock_collection.update_one({"symbol": symbol.upper()}, {"$push": { "prices": price_id }})

    def delete_stock(self, symbol):
        result = self.stock_collection.delete_one({"symbol": symbol})
        if result.deleted_count > 0:
            self.price_collection.delete_many({"symbol": symbol})
        
    def delete_all(self):
        self.stock_collection.delete_many({})
