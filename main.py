from readFromSql import getFromSql
import pandas as pd
from flask import Flask, Response

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    return "Hello World!"

@app.route('/get', methods=['GET'])
def getData():
    return Response(getFromSql('PersonData').to_json(orient="records"), mimetype='application/json')

if __name__ == '__main__':
    app.run()