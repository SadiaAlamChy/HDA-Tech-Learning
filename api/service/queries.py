import json

from flask import jsonify, request
from flask.views import MethodView
from controller.q1 import Query1
from controller.q2 import Query2
from controller.q3 import Query3
from controller.q4 import Query4
from controller.q5 import Query5
from controller.q6 import Query6
from controller.q7 import Query7


class Query1API(MethodView):
    def __init__(self):
        self.q = Query1()

    def get(self):
        result = self.q.execute()
        return jsonify(result)


class Query2API(MethodView):
    def __init__(self):
        self.q = Query2()

    def get(self):
        result = self.q.execute()
        return jsonify(result)


class Query3API(MethodView):
    def __init__(self):
        self.q = Query3()

    def get(self):
        result = self.q.execute()
        return jsonify(result)


class Query4API(MethodView):
    def __init__(self):
        self.q = Query4()

    def get(self):
        result = self.q.execute()
        return jsonify(result)


class Query5API(MethodView):
    def __init__(self):
        self.q = Query5()

    def get(self):
        result = self.q.execute()
        return jsonify(result)


class Query6API(MethodView):
    def __init__(self):
        self.q = Query6()

    def get(self):
        result = self.q.execute()
        return jsonify(result)


class Query7API(MethodView):
    def __init__(self):
        self.q = Query7(days=0)

    def post(self):
        self.q.days = request.json['days']
        result = self.q.execute()
        return jsonify(result)

    # def get(self):
    #     result = self.q.execute()
    #     return jsonify(result)
#
#
# class Query8API(MethodView):
#     def __init__(self):
#         self.q1 = Query1()
#
#     def get(self):
#         result = self.q1.execute()
#         return jsonify(result)
#
#
# class Query9API(MethodView):
#     def __init__(self):
#         self.q1 = Query1()
#
#     def get(self):
#         result = self.q1.execute()
#         return jsonify(result)
#
#
# class Query10API(MethodView):
#     def __init__(self):
#         self.q1 = Query1()
#
#     def get(self):
#         result = self.q1.execute()
#         return jsonify(result)
