from flask import Flask, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy

import json, datetime, decimal
from sqlalchemy.exc import OperationalError, ProgrammingError

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

def custom_serializer(o):
    if isinstance(o, decimal.Decimal):
        return int(o)
    elif isinstance(o, (datetime.date, datetime.datetime)):
        return str(o)
    
def pretty_print(o):
    return jsonify(json.loads(json.dumps(o, default=custom_serializer)))
   
def sqlalchemy_error(error): 
    if error.__class__ == OperationalError:
        return internal_server_error("SQLAlchemy: Unable to connect to the database")
    elif error.__class__ == ProgrammingError:
        return internal_server_error("SQLAlchemy: Failed to execute database query")
    else:
        return internal_server_error(error.orig.args)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error':'not found'}), 404)

@app.errorhandler(500)
def internal_server_error(error):
    return make_response(jsonify({'error':error}), 500)