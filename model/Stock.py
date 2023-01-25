from pymongo import MongoClient

class Stock:
    def __init__(self, symbol, name, price):
        self.symbol = symbol
        self.name = name
        self.price = price

    def to_dict(self):
        return {
            "symbol": self.symbol,
            "name": self.name,
            "price": self.price
        }

# client = MongoClient()
# db = client.stock_db
# stocks = db.stocks

# stock = Stock("AAPL", "Apple Inc.", 100)
# stock_id = stocks.insert_one(stock.to_dict()).inserted_id

