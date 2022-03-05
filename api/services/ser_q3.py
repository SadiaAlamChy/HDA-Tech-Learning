from flask import jsonify
from flask.views import MethodView
from api.querycontroller.q3 import Query3

class Query3_Api(MethodView):
    def __init__(self):
        self.q3 = Query3()

    def get(self):
        result = self.q3.execute()

        print(jsonify(result))
        return jsonify(result)