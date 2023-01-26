from flask import Flask
from controller.StockController import stock_blueprint


app = Flask(__name__)
app.register_blueprint(stock_blueprint)


if __name__ == '__main__':
    app.run()
