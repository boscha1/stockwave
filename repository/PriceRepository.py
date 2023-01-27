# stock_repository.py
from config.db import db
from util.Singleton import Singleton

class PriceRepository(metaclass=Singleton):
    def __init__(self):
        self.price_collection = db.price

    def insert_price(self, price):
        return self.price_collection.insert_one(price).inserted_id
        
    def insert_prices(self, prices):
        return self.price_collection.insert_many(prices).inserted_ids