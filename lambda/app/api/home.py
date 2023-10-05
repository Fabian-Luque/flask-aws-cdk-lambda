from flask import jsonify, request

from . import api

@api.route('/')
def home():
    return jsonify({'hello': 'it works!'})

@api.route('/post', methods=['POST'])
def post():
    print("print the request")
    print(request.json)
    return request.json