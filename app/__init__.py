from flask import Flask, Response, render_template
import json
from flask_cors import CORS

app = Flask(__name__, static_folder="../client/build/static", template_folder="../client/build")
CORS(app)

@app.route('/')
def serve_app():
    return render_template('index.html')
# def getData():
    # result = {'value': 'the data'}
    # return Response(json.dumps(result), mimetype='application/json')

# @app.route('/load-data')
# def load_data():


# pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org flask_cors==3.0.7