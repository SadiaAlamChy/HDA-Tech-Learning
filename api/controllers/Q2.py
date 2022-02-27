from flask import jsonify
from flask.views import MethodView
from api.models.Q2 import Query2

class Query2API(MethodView):
    def __init__(self):
         self.q2 = Query2()

    def get(self):
        result = self.q2.execute()
        return jsonify(result)

    # def __pos__(self):
    # def __delete__(self):