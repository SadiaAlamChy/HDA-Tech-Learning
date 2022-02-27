from services.q1 import Query1API
from services.q2 import Query2API
from services.q3 import Query3API
from services.q4 import Query4API
from services.q5 import Query5API
from services.q6 import Query6API


from flask import Blueprint
# from flask_cors import CORS

query_api = Blueprint('queryapi', __name__)
# CORS(dengue_timeseries_api)

query_api.add_url_rule("/q1", view_func=Query1API.as_view("Get division wise total sales"))
query_api.add_url_rule("/q2", view_func=Query2API.as_view("Get transaction(cash/mobile/card) wise total sales"))
query_api.add_url_rule("/q3", view_func=Query3API.as_view("Query 3"))
query_api.add_url_rule("/q4", view_func=Query4API.as_view("Query 4"))
query_api.add_url_rule("/q5", view_func=Query5API.as_view("Query 5"))
query_api.add_url_rule("/q6", view_func=Query6API.as_view("Query 6"))