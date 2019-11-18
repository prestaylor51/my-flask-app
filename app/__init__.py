from flask import Flask, Response
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def getData():
    result = {'value': 'the data'}
    return Response(json.dumps(result), mimetype='application/json')

# @app.route('/load-data')
# def load_data():


# pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org flask_cors==3.0.7