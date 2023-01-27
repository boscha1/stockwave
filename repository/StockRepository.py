# stock_repository.py
from config.db import db
from util.Singleton import Singleton

class StockRepository(metaclass=Singleton):
    def __init__(self):
        self.stock_collection = db.stock

    def get_stock_by_symbol(self, symbol):
        stock = self.stock_collection.find_one({"symbol": symbol.upper()})
        return stock

    def get_all_stocks(self):
        return self.stock_collection.find({}, {"_id": 0})

    def insert_stock(self, stock):
        self.stock_collection.insert_one(stock, {"$addToSet": {'prices': stock['prices']}})

    def update_stock(self, symbol, price_id):
        self.stock_collection.update_one({"symbol": symbol.upper()}, {"$push": { "prices": price_id }})

    def delete_stock(self, symbol):
        self.stock_collection.delete_one({"symbol": symbol})
        
    def delete_all(self):
        self.stock_collection.delete_many({})
        
    def insert_all(self):
        stocks = [
          {"symbol": "AAPL", "name": "Apple Inc.", "prices": []},
          {"symbol": "GOOG", "name": "Alphabet Inc.", "prices": []},
          {"symbol": "AMZN", "name": "Amazon.com Inc.", "prices": []}
        ]

        self.stock_collection.insert_many(stocks)
