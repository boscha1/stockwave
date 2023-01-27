from flask import Flask
from controller import stock_blueprint, price_blueprint


app = Flask(__name__)
app.register_blueprint(stock_blueprint)
app.register_blueprint(price_blueprint)


if __name__ == '__main__':
    app.run()
