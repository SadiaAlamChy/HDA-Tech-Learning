from flask import jsonify
from flask.views import MethodView
from api.models.Q3 import Query3

class Query3API(MethodView):
    def __init__(self):
         self.q3 = Query3()

    def get(self):
        result = self.q3.execute()
        return jsonify(result)

    # def __pos__(self):
    # def __delete__(self):