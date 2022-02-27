from flask import jsonify
from flask.views import MethodView
from api.models.Q5 import Query5

class Query5API(MethodView):
    def __init__(self):
         self.q5 = Query5()

    def get(self):
        result = self.q5.execute()
        return jsonify(result)

    # def __pos__(self):
    # def __delete__(self):