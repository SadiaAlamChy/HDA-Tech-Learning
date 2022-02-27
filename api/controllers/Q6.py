from flask import jsonify
from flask.views import MethodView
from api.models.Q6 import Query6

class Query6API(MethodView):
    def __init__(self):
         self.q6 = Query6()

    def get(self):
        result = self.q6.execute()
        return jsonify(result)

    # def __pos__(self):
    # def __delete__(self):