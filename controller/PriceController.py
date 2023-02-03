from marshmallow import ValidationError
from flask import Blueprint
import yfinance as yf
from bson.json_util import dumps
from service import PriceService
from flask_restful import Api, Resource, reqparse
from exception.CustomExceptions import NotFoundException
from util.CreateResponse import create_response


price_blueprint = Blueprint("price", __name__)
api = Api(price_blueprint)

@api.resource('/price/<string:symbol>', '/price')
class PriceController(Resource):
    def __init__(self):
        self.price_service = PriceService()
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('date', type=str, required=True, help='No date provided', location='json')
        self.reqparse.add_argument('open_at', type=float, required=True, help='No open_at provided', location='json')
        self.reqparse.add_argument('close_at', type=float, required=True, help='No close_at provided', location='json')
        self.reqparse.add_argument('symbol', type=str, required=True, help='No symbol provided', location='json')
        super().__init__()
        
    
    def get(self):
        prices = self.price_service.get_all_prices()
        return create_response(prices, 200)
            
    
    def post(self):
        try:
            price = self.reqparse.parse_args()
            self.price_service.insert_price(price)
            return create_response(price, 201)
        except ValidationError as err:
            return create_response(err.messages, 400)
        except NotFoundException as err:
            return create_response(err.args, 404)
        except Exception as err:
            return create_response(err.args, 500)
            