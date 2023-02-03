from repository.PriceRepository import PriceRepository
from .StockService import StockService
from util.Singleton import Singleton
from datetime import datetime as dt
from exception.CustomExceptions import NotFoundException

class PriceService(metaclass=Singleton):
    def __init__(self):
        self.price_repository = PriceRepository()
        self.stock_service = StockService()
        
    
    def get_all_prices(self):
        return self.price_repository.get_all_prices()

    def insert_price(self, price):
        stock_exists = self.stock_service.get_stock_by_symbol(price["symbol"].upper())
        if not stock_exists:
            raise NotFoundException(price["symbol"])
    
        stock_prices = stock_exists["prices"]        
        price["date"] = dt.strptime(price["date"], '%Y-%m-%d')
        
        if stock_prices is not None:
            for stock_price in stock_prices:
                if stock_price["date"] == price["date"]:
                    raise Exception("Date already exists")        
                
        self.price_repository.insert_price(price)
        
    def insert_all(self):
        self.price_repository.insert_all()
