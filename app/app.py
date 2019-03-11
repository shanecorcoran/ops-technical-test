#!/usr/bin/env python2.7

import os
from flask import Flask, jsonify, send_file
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

UPLOAD_DIRECTORY = "/var/lib/jenkins/workspace/MYOB/1_MYOB_hello_world_deploy_pipeline/app"
filename = "resume.docx"
path = os.path.join(UPLOAD_DIRECTORY, filename)

@app.route('/todo/api/v1.0/myapplication', methods=['GET'])
def get_tasks():
    return jsonify({'myapplication': myapplication})

@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/resume')
def return_file():
    try:
        return send_file(path)
    except Exception as e:
	    return str(e)

def app_available():
    return True, "A-OK."

health.add_check(app_available)

if __name__ == '__main__':
    app.run(host='0.0.0.0')