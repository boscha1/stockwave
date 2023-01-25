# stock_repository.py
from config.db import stock_collection

class StockRepository:
    def __init__(self):
        self.stock_collection = stock_collection

    def get_stock(self, symbol):
        return self.stock_collection.find_one({"symbol": symbol})

    def get_all_stocks(self):
        return self.stock_collection.find({}, {"_id": 0})

    def add_stock(self, stock):
        self.stock_collection.insert_one(stock)

    def update_stock(self, symbol, stock):
        self.stock_collection.update_one({"symbol": symbol}, {"$set": stock})

    def delete_stock(self, symbol):
        self.stock_collection.delete_one({"symbol": symbol})
        
    def delete_all(self):
        self.stock_collection.delete_many({})
        
    def insert_all(self):
        stocks = [{"symbol": "AAPL", "name": "Apple Inc.", "price": 113.4},
          {"symbol": "GOOG", "name": "Alphabet Inc.", "price": 2234.6},
          {"symbol": "AMZN", "name": "Amazon.com Inc.", "price": 3456.7}]

        self.stock_collection.insert_many(stocks)
