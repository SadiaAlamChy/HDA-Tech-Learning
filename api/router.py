from api.controllers.Q1 import Query1API
from api.controllers.Q2 import Query2API
from api.controllers.Q3 import Query3API
from api.controllers.Q4 import Query4API
from api.controllers.Q5 import Query5API
from api.controllers.Q6 import Query6API
from api.controllers.Q7 import Query7API
from api.controllers.Q8 import Query8API
from api.controllers.Q9 import Query9API
from api.controllers.Q10 import Query10API

from flask import Blueprint
# from flask_cors import CORS

query_api = Blueprint('queryapi', __name__)

query_api.add_url_rule('/q1', view_func=Query1API.as_view('Query 1 result'))
query_api.add_url_rule('/q2', view_func=Query2API.as_view('Query 2 result'))
query_api.add_url_rule('/q3', view_func=Query3API.as_view('Query 3 result'))
query_api.add_url_rule('/q4', view_func=Query4API.as_view('Query 4 result'))
query_api.add_url_rule('/q5', view_func=Query5API.as_view('Query 5 result'))
query_api.add_url_rule('/q6', view_func=Query6API.as_view('Query 6 result'))
query_api.add_url_rule('/q7', view_func=Query7API.as_view('Query 7 result'))
query_api.add_url_rule('/q8', view_func=Query8API.as_view('Query 8 result'))
query_api.add_url_rule('/q9', view_func=Query9API.as_view('Query 9 result'))
query_api.add_url_rule('/q10',view_func=Query10API.as_view('Query 10 result'))

