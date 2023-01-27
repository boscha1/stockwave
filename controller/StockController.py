from marshmallow import ValidationError
from flask import Response, Blueprint
from bson.json_util import dumps
from service.StockService import StockService
from flask_restful import Api, Resource, reqparse

stock_blueprint = Blueprint("stock", __name__)
api = Api(stock_blueprint)

@api.resource('/stock/<string:symbol>', '/stock')
class StockController(Resource):
    def __init__(self):
        self.stock_service = StockService()
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('symbol', type=str, required=True, help='No symbol provided', location='json')
        self.reqparse.add_argument('name', type=str, required=True, help='No name provided', location='json')
        self.reqparse.add_argument('prices', type=list, required=True, help='Prices not provided', location='json')
        super().__init__()


    def get(self):
        stocks = self.stock_service.get_all_stocks()
        return create_response(stocks, 200)
    
    
    def post(self):
        try:
            stock = self.reqparse.parse_args()
            exists = self.stock_service.get_stock_by_symbol(stock['symbol'])
            if exists:
                return create_response("A stock with " + stock['symbol'] + " already exists", 400)
            self.stock_service.insert_stock(stock)
            return create_response(stock, 201)
        except ValidationError as err:
            return err.messages, 400
        
        
    def delete(self):
        self.stock_service.delete_all()
        return create_response({"message": "deleted"}, 204)

        
def create_response(data, status_code):
    return Response(
        response=dumps(data),
        status=status_code,
        mimetype="application/json"
    )