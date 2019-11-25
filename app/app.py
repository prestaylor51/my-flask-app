from flask import Flask, Response, render_template, request
import json
from flask_cors import CORS
import os
from secretsanta import SecretSantaService

myapp = Flask(__name__, static_folder="../client/build/static", template_folder="../client/build")
CORS(myapp)

@myapp.route('/')
def serve_app():
    env = os.getenv('FLASK_ENV')
    if (env is not None and env == 'prod'):
        print('App running in production')
        return render_template('index.html')
    else:
        return Response('Development server. Frontend can be found at localhost:3000', mimetype='text/plain')

@myapp.route('/load-data')
def load_data():
    result = {'data': 'hello'}
    return Response(json.dumps(result), mimetype='application/json')

'''
GET MY SANTAEE
    body: 
        code -> secret code for the santaee
'''
@myapp.route('/get-my-santaee', methods=['POST'])
def get_santaee():
    service = SecretSantaService()
    body = request.json
    print("code: " + body['code'])
    santaee = service.get_santaee_from_code(body['code'])
    return Response(santaee, mimetype='text/plain')

# pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org flask_cors==3.0.7