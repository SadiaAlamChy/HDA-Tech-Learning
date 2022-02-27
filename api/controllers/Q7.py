from flask import jsonify
from flask.views import MethodView
from api.models.Q7 import Query7
from flask import Flask, jsonify, request

class Query7API(MethodView):
    # def __init__(self):
         # self.q7 = Query7(395)

    # def get(self):
        # result = self.q7.execute()
        # return jsonify(result)

    def post(self):
            days = request.json['days']
            self.q7 = Query7(days)
            result = self.q7.execute()
            # print(result)
            return jsonify(result)



    # return jsonify({"days": days})
    # return "in post"

    # def __delete__(self):