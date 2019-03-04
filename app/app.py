#!/usr/bin/env python2.7

from flask import Flask, jsonify
from healthcheck import HealthCheck

app = Flask(__name__)
health = HealthCheck(app, "/healthcheck")

myapplication = [
    {
        'version': u'1.0',
        'description': u'pre-interview technical test', 
        'lastcommitsha': u'abc57858585'
    }
]

@app.route('/todo/api/v1.0/myapplication', methods=['GET'])
def get_tasks():
    return jsonify({'myapplication': myapplication})

@app.route('/')
def hello_world():
    return "Hello World"

def app_available():
    return True, "A-OK."

health.add_check(app_available)

if __name__ == '__main__':
    app.run(host='0.0.0.0')