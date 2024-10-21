from flask import flask 
from flask_restful import Api
from flask_cors import CORS
from Data.robotics import robotics

app = flask(__name__)
CORS(app)
api = Api(app)

api.add_ressource(robotics, "/robotics")

if __name__=="api":
    app.run(debug=True, port=5000, host='0.0.0.0')
