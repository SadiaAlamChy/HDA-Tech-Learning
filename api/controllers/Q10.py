from flask import jsonify
from flask.views import MethodView
from api.models.Q10 import Query10

class Query10API(MethodView):
    def __init__(self):
         self.q10 = Query10()

    def get(self):
        result = self.q10.execute()
        return jsonify(result)

    # def __pos__(self):
    # def __delete__(self):