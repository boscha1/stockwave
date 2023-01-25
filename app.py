from crypt import methods
import json
from flask import Flask, Response, jsonify
from bson.json_util import dumps
from service.StockService import StockService

app = Flask(__name__)

stock_service = StockService()

@app.route("/stock/<symbol>", methods=["GET"])
def get_stock(symbol):
    stock = stock_service.get_stock(symbol)
    return dumps(stock)

@app.route("/stock", methods=["GET"])
def get_all_stocks():
    stocks = list(stock_service.get_all_stocks())
    
    return Response(
        response=json.dumps(stocks),
        status=200,
        mimetype="application/json"
    )
    
@app.route('/stock', methods=['DELETE'])
def delete_all_stocks():
    stock_service.delete_all()
    return jsonify({"message": "All stocks have been deleted"}), 200

@app.route('/stock-dummy', methods=['POST'])
def insert_dummy_data():
    stock_service.insert_all()
    return Response(
        response="created",
        status=201,
        mimetype="application/json"
    )

# @app.route("/stock", methods=["POST"])
# def add_stock():
#     stock = request.json
#     stock_repository.add_stock(stock)
#     return jsonify({"status": "success"})


if __name__ == '__main__':
    app.run()
