from flask import Flask, Response, render_template, request
import json
from flask_cors import CORS
import os
from app.secretsanta import SecretSantaService
from dotenv import load_dotenv
import psycopg2

DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL)

app = Flask(__name__, static_folder="../client/build/static", template_folder="../client/build")
CORS(app)

load_dotenv()

@app.route('/')
def serve_app():
    env = os.getenv('FLASK_ENV')
    if (env is not None and env == 'prod'):
        print('App running in production')
        return render_template('index.html')
    else:
        return Response('Development server. Frontend can be found at localhost:3000', mimetype='text/plain')

@app.route('/load-data')
def load_data():
    result = {'data': 'hello'}
    return Response(json.dumps(result), mimetype='application/json')

'''
GET MY SANTAEE
    body: 
        code -> secret code for the santaee
'''
@app.route('/get-my-santaee', methods=['POST'])
def get_santaee():
    service = SecretSantaService(conn)
    body = request.json
    print("code: " + body['code'])
    santaee = service.get_santaee_from_code(body['code'])
    return Response(santaee, mimetype='text/plain')

# pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org flask_cors==3.0.7