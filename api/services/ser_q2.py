from flask import jsonify
from flask.views import MethodView
from api.querycontroller.q2 import Query2

class Query2_Api(MethodView):
    def __init__(self):
        self.q2 = Query2()

    def get(self):
        result = self.q2.execute()
        print(jsonify(result))
        return jsonify(result)

