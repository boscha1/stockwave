from marshmallow import Schema, fields

class StockDTO(Schema):
    symbol = fields.Str(required=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)
