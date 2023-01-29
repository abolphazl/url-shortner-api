from flask_restful import Resource
from flask import jsonify, request

class ping(Resource):
    def get(self):
        return jsonify("pong")