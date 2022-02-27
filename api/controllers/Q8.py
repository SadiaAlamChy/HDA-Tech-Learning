from flask import jsonify
from flask.views import MethodView
from api.models.Q8 import Query8

class Query8API(MethodView):
    def __init__(self):
         self.q8 = Query8()

    def get(self):
        result = self.q8.execute()
        return jsonify(result)

    # def __pos__(self):
    # def __delete__(self):