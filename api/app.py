from flask import Flask, jsonify, request
app=Flask(__name__)

@app.route("/greetings", methods=['GET'])
def greetings():
    return jsonify({"msg" :"Hello Interns!!"})

# @app.route("/greetings/customized", methods=['POST'])
# def greetings_customized():
#     data = {}
#     data['name'] = request.json['name']
#     return jsonify({"msg" :"Hello "+ data['name']})




               # Query1
from api.services.q1 import Query1API
app.add_url_rule("/api/q1", view_func=Query1API.as_view("Get division wise total sales"))

              ##  Query 2
from api.services.ser_q2 import Query2_Api
app.add_url_rule("/api/q2", view_func=Query2_Api.as_view("Transaction wise total sales"))

             ##Query 3

from api.services.ser_q3 import Query3_Api
app.add_url_rule("/api/q3",view_func=Query3_Api.as_view("Total sales in Barisal"))

            ##Query 4

from api.services.ser_q4 import Query4_Api
app.add_url_rule("/api/q4",view_func=Query4_Api.as_view("Total sales in 2015"))

            ##Query 5

from api.services.ser_q5 import Query5_Api
app.add_url_rule("/api/q5",view_func=Query5_Api.as_view("Total sales of Barisal in 2015"))

            ##Query 7
from api.services.ser_q7 import Query7_Api
app.add_url_rule("/api/q7",view_func=Query7_Api.as_view("getting x days"))
#
# @app.route("/api/q7", methods=['POST'])
# def greetings_customized():
#     data = {}
#     data['name'] = request.json['name']
#     return jsonify({"msg" :"Hello "+ data['name']})
# from api.services.ser_q7 import Query7_Api
# app.add_url_rule("/api/q7",view_func=Query7_Api.as_view("Total sales in X days"))

            ##Query6

from api.querycontroller.q6 import Query6_Api
app.add_url_rule("/api/q6",view_func=Query6_Api.as_view("Best 3 sales"))

           ##Query8

from api.querycontroller.q8 import Query8_Api
app.add_url_rule("/api/q8",view_func=Query8_Api.as_view("worst season for an item"))

          ##Query9

from api.querycontroller.q9 import Query9_Api
app.add_url_rule("/api/q9",view_func=Query9_Api.as_view("division wise total sales"))


          ##Query10

from api.querycontroller.q10 import Query10_Api
app.add_url_rule("/api/q10",view_func=Query10_Api.as_view("average sells by stores"))





### How blueprint work??
from router import query_api
app.register_blueprint(query_api, url_prefix='/api/')

if __name__ == '__main__':
    app.run(host='localhost', port=5000)