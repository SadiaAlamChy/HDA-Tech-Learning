from flask import jsonify
from flask.views import MethodView
from api.querycontroller.q4 import Query4

class Query4_Api(MethodView):
    def __init__(self):
        self.q4 = Query4()

    def get(self):
        result = self.q4.execute()

        print(jsonify(result))
        return jsonify(result)