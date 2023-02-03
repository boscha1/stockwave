from marshmallow import ValidationError
from flask import Response, Blueprint
from bson.json_util import dumps
from service.StockService import StockService
from flask_restful import Api, Resource, reqparse
from exception.CustomExceptions import AlreadyExistsException, InvalidStockException, NotFoundException
from util.CreateResponse import create_response

stock_blueprint = Blueprint("stock", __name__)
api = Api(stock_blueprint)

@api.resource('/stock/<string:symbol>', '/stock')
class StockController(Resource):
    def __init__(self):
        self.stock_service = StockService()
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('symbol', type=str, required=True, help='No symbol provided', location='json')
        self.reqparse.add_argument('name', type=str, required=True, help='No name provided', location='json')
        super().__init__()


    def get(self, symbol=None):
        try:   
            if symbol:
                stock = self.stock_service.get_stock_by_symbol(symbol)
                return create_response(stock, 200)
            else:
                stocks = self.stock_service.get_all_stocks()
                return create_response(stocks, 200)
        except NotFoundException as err:
            return create_response(err.args, 404)
    
    
    def post(self):
        try:
            stock = self.reqparse.parse_args()
            self.stock_service.insert_stock(stock)
            return create_response(stock, 201)
        except ValidationError as err:
            return create_response(err.args, 400)
        except AlreadyExistsException as err:
            return create_response(err.args, 409)
        except InvalidStockException as err:
            return create_response(err.args, 400)
        except Exception as err:
            return create_response(err.args, 500)
        
        
    def delete(self, symbol=None):
        try:     
            if symbol:
                stock = self.stock_service.get_stock_by_symbol(symbol)
                self.stock_service.delete_stock(stock["symbol"])
                return create_response({"message": stock["symbol"] + " deleted"}, 204)
            else:
                self.stock_service.delete_all()
            return create_response({"message": "deleted"}, 204)
        except NotFoundException as err:
            return create_response(err.args, 404)