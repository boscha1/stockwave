from repository import StockRepository, PriceRepository
import yfinance as yf
from util.Singleton import Singleton
from exception.CustomExceptions import AlreadyExistsException, InvalidStockException, NotFoundException
from config import client

class StockService(metaclass=Singleton):
    def __init__(self):
        self.stock_repository = StockRepository()
        self.price_repository = PriceRepository()
        
    def get_stock_by_symbol(self, symbol):
        stock = self.stock_repository.get_stock_by_symbol(symbol)
        if stock is None:
            raise NotFoundException(symbol)
        return stock

    def get_all_stocks(self):
        return self.stock_repository.get_all_stocks()


    def insert_stock(self, stock):
        symbol = stock["symbol"]
        yahoo_data = yf.download(symbol)
        if self.stock_repository.stock_exists(symbol):
            raise AlreadyExistsException(symbol)
        if yahoo_data.empty:
            raise InvalidStockException(symbol)
        
        prices = []
        for index, row in yahoo_data.iterrows():
            price = {
                "symbol": symbol,
                "date": index,
                "open_at": row["Open"],
                "close_at": row["Close"]
            }
            prices.append(price)

        with client.start_session() as session:
            session.start_transaction()
            
            try:
                self.stock_repository.insert_stock(stock)
                self.price_repository.insert_prices(prices)
            except Exception as e:
                session.abort_transaction()
                raise e

        
    def delete_stock(self, symbol):
        self.stock_repository.delete_stock(symbol)
        
    def delete_all(self):
        self.stock_repository.delete_all()
        
    def update_stock_price(self, stock_symbol, price_id):
        self.stock_repository.update_stock(stock_symbol, price_id)
