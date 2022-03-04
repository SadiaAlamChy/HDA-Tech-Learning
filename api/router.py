from services.q1 import Query1API
from services.q2 import Query2API
from services.q3 import Query3API
from services.q4 import Query4API
from services.q5 import Query5API
from services.q6 import Query6API
from services.q7 import Query7API
from services.q8 import Query8API
from services.q9 import Query9API
from services.q10 import Query10API
from flask import Blueprint
# from flask_cors import CORS

query_api = Blueprint('queryapi', __name__)
# CORS(dengue_timeseries_api)

query_api.add_url_rule("/q1", view_func=Query1API.as_view("Get division wise total sales"))
query_api.add_url_rule("/q2", view_func=Query2API.as_view("Get transaction(cash/mobile/card) wise total sales"))
query_api.add_url_rule("/q3", view_func=Query3API.as_view("Get Total sales in Barisal"))
query_api.add_url_rule("/q4", view_func=Query4API.as_view("Get Total sales in 2015"))
query_api.add_url_rule("/q5", view_func=Query5API.as_view("Get Total sales of Barisal in 2015"))
query_api.add_url_rule("/q6", view_func=Query6API.as_view("Get the top three products"))
query_api.add_url_rule("/q7", view_func=Query7API.as_view("Get the products that have been sold since X days?"))
query_api.add_url_rule("/q8", view_func=Query8API.as_view("Get the season(quarter)that is the worst for each product item?"))
query_api.add_url_rule("/q9", view_func=Query9API.as_view("Get the total sales of items geographically (division-wise)"))
query_api.add_url_rule("/q10", view_func=Query10API.as_view("Get the average sales of products sales per store monthly"))