#!/usr/bin/env python2.7

import os
import logging
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
log_file = os.path.join(UPLOAD_DIRECTORY, 'example.log')

logging.basicConfig(filename=log_file, level=logging.DEBUG)

@app.route('/todo/api/v1.0/myapplication', methods=['GET'])
def get_tasks():
    return jsonify({'myapplication': myapplication})

@app.route('/')
def hello_world():
    return "Hello MYOB."

@app.route('/download/', methods=['GET'])
def return_file():
    try:
        return send_file(path)
        #return path
    except Exception as e:
	    return str("Error with the send_file function" & e)

def app_available():
    return True, "A-OK."

health.add_check(app_available)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)