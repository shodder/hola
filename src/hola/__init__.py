
APP_NAME = __name__

from logbook import FileHandler, Logger

file_handler = FileHandler('hola.log', level='DEBUG')
file_handler.push_application()

from flask import Flask, make_response, jsonify

app = Flask(APP_NAME)

@app.route('/')
def index():

    return make_response(jsonify({'message': 'Hello World'}), 200)
