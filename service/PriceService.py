from repository.PriceRepository import PriceRepository
from .StockService import StockService
from util.Singleton import Singleton
from datetime import datetime as dt

class PriceService(metaclass=Singleton):
    def __init__(self):
        self.price_repository = PriceRepository()
        self.stock_service = StockService()

    def insert_price(self, price, stock_symbol):
        # stock_exists = self.stock_service.get_stock_by_symbol(stock_symbol)
        # # if not stock_exists:
        # #     return "A stock with " + stock_symbol + " does not exist"
        price["date"] = dt.strptime(price["date"], '%Y-%m-%d')
        price_id = self.price_repository.insert_price(price)
        self.stock_service.update_stock_price(stock_symbol, price_id)
        
    def insert_all(self):
        self.price_repository.insert_all()
