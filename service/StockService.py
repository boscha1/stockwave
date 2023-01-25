from model.StockDTO import StockDTO
from repository.StockRepository import StockRepository

class StockService:
    def __init__(self):
        self.stock_repository = StockRepository()

    def get_all_stocks(self):
        stocks = self.stock_repository.get_all_stocks()
        return stocks

    def insert_stock(self, stock_dto: StockDTO):
        self.stock_repository.insert_stock(stock_dto)
        
    def insert_all(self):
        self.stock_repository.insert_all()
        
    def delete_all(self):
        self.stock_repository.delete_all()
