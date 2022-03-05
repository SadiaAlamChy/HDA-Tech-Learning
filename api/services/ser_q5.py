from flask import jsonify
from flask.views import MethodView
from api.querycontroller.q5 import Query5

class Query5_Api(MethodView):
    def __init__(self):
        self.q5 = Query5()

    def get(self):
        result = self.q5.execute()

        print(jsonify(result))
        return jsonify(result)