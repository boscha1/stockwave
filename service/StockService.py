from repository.StockRepository import StockRepository
from util.Singleton import Singleton

class StockService(metaclass=Singleton):
    def __init__(self):
        self.stock_repository = StockRepository()
        
    def get_stock_by_symbol(self, symbol):
        return self.stock_repository.get_stock_by_symbol(symbol)

    def get_all_stocks(self):
        stocks = self.stock_repository.get_all_stocks()
        return stocks

    def insert_stock(self, stock):
        self.stock_repository.insert_stock(stock)
        
    def insert_all(self):
        self.stock_repository.insert_all()
        
    def delete_all(self):
        self.stock_repository.delete_all()
        
    def update_stock_price(self, stock_symbol, price_id):
        self.stock_repository.update_stock(stock_symbol, price_id)
