from flask_restful import Resource, Api
from flask import Flask, jsonify
from flask_cors import CORS
from plugins import url

app = Flask(__name__)
CORS(app)
api = Api(app)

# handlers
api.add_resource(url.ping, '/ping')


# driver
if __name__ == "__main__":
    app.run(debug=True)