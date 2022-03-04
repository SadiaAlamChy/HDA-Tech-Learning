from flask import Flask, jsonify, request

app = Flask(__name__)


# @app.route("/greetings")
# def greetings():
#     return "Hello Interns!!"

# @app.route("/greetings")
# def greetings():
#     return jsonify({"msg": "Hello Interns!!"})


@app.route("/greetings", methods=['GET'])
def greetings():
    return jsonify({"msg": "Hello Interns!!"})


@app.route("/greetings/customized", methods=['POST'])
def greetings_customized():
    data = {}
    data['name'] = request.json['name']
    return jsonify({"msg": "Hello " + data['name']})


# from services.q1 import Query1API
#
# app.add_url_rule("/api/q1", view_func=Query1API.as_view("Get division wise total sales"))
### How blueprint work??
from router import query_api

app.register_blueprint(query_api, url_prefix='/api/')

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
