from marshmallow import ValidationError
from flask import Blueprint, Response
from bson.json_util import dumps
from service import PriceService
from flask_restful import Api, Resource, reqparse


price_blueprint = Blueprint("price", __name__)
api = Api(price_blueprint)

@api.resource('/price/stock/<string:symbol>', '/price')
class PriceController(Resource):
    def __init__(self):
        self.price_service = PriceService()
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('date', type=str, required=True, help='No date provided', location='json')
        self.reqparse.add_argument('open_at', type=float, required=True, help='No openAt provided', location='json')
        self.reqparse.add_argument('close_at', type=float, required=True, help='No closeAt provided', location='json')
        super().__init__()
        
    
    def post(self, symbol):
        try:
            price = self.reqparse.parse_args()
            self.price_service.insert_price(price, symbol)
            return create_response(price, 201)
        except ValidationError as err:
            return err.messages, 400
        
def create_response(data, status_code):
    return Response(
        response=dumps(data),
        status=status_code,
        mimetype="application/json"
    )