from api.controllers.Q1 import Query1API
from flask import Blueprint
# from flask_cors import CORS

query_api = Blueprint('queryapi', __name__)

query_api.add_url_rule('/q1', view_func=Query1API.as_view('Get division wise total sale'))
# query_api.add_url_rule('/q2', view_func=Query1API.as_view('Get division wise total sale'))
