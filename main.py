#!/usr/bin/python
from flask import Flask, render_template, request,jsonify
import time
import urllib.parse
app = Flask(__name__)
import urllib.parse
import json
@app.route("/")
def index():
	return render_template('index.html')

@app.route("/target_endpoint")
def target():
	return render_template('loading.html')

@app.route("/processing")
def processing():
	time.sleep(0)
	return render_template('success.html')


# @app.route("/run", methods=['POST'])
# def run():
#     if request.method == 'POST':
#         code = request.json['code']
#         try:
#             # Execute the input code and capture its output
#             output = str(eval(code))
#             return jsonify({'output': output})
#         except Exception as e:
#             return jsonify({'output': str(e)})


@app.route('/test')
def test():
	return render_template('test.html')
if __name__ == '__main__':
	app.run(host = '0.0.0.0', debug=True)
