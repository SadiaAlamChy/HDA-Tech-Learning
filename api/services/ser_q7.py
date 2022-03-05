from flask import jsonify,request
from flask.views import MethodView
from api.querycontroller.q7 import Query7

class Query7_Api(MethodView):
    def __init__(self):
        self.q7 = Query7(days=0)

    def post(self):
        self.q7.days = request.json['days']
        result = self.q7.execute()
        print(jsonify(result))
        return jsonify(result)

# data = {}
    # data['name'] = request.json['name']
    # return jsonify({"msg": "Hello " + data['name']})