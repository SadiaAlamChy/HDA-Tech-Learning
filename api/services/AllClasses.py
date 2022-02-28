from flask import jsonify, request
from flask.views import MethodView
from querycontroller.q1 import Query1
from querycontroller.q2 import Query2
from querycontroller.q3 import Query3
from querycontroller.q4 import Query4
from querycontroller.q5 import Query5
from querycontroller.q6 import Query6
from querycontroller.q7 import Query7
from querycontroller.q8 import Query8
from querycontroller.q9 import Query9
from querycontroller.q10 import Query10

class Query1API(MethodView):
    def __init__(self):
        self.q1 = Query1()

    def get(self):
        result = self.q1.execute() ## Dataframe
        # print(jsonify(result))
        return jsonify(result)

class Query2API(MethodView):
    def __init__(self):
        self.q2 = Query2()

    def get(self):
        result = self.q2.execute() ## Dataframe
        # print(jsonify(result))
        return jsonify(result)

class Query3API(MethodView):
    def __init__(self):
        self.q3 = Query3()

    def get(self):
        result = self.q3.execute() ## Dataframe
        # print(jsonify(result))
        return jsonify(result)

class Query4API(MethodView):
    def __init__(self):
        self.q4 = Query4()

    def get(self):
        result = self.q4.execute() ## Dataframe
        # print(jsonify(result))
        return jsonify(result)

class Query5API(MethodView):
    def __init__(self):
        self.q5 = Query5()

    def get(self):
        result = self.q5.execute() ## Dataframe
        # print(jsonify(result))
        return jsonify(result)

class Query6API(MethodView):
    def __init__(self):
        self.q6 = Query6()

    def get(self):
        result = self.q6.execute() ## Dataframe
        # print(jsonify(result))
        return jsonify(result)

class Query7API(MethodView):
    # def __init__(self):
    #     self.q7 = Query7(days=0)

    def post(self):
        days = request.json['days']
        self.q7 = Query7(days)
        result = self.q7.execute() ## Dataframe
        # print(jsonify(result))
        return jsonify(result)


class Query8API(MethodView):
    def __init__(self):
        self.q8 = Query8()

    def get(self):
        result = self.q8.execute() ## Dataframe
        # print(jsonify(result))
        return jsonify(result)

class Query9API(MethodView):
    def __init__(self):
        self.q9 = Query9()

    def get(self):
        result = self.q9.execute() ## Dataframe
        # print(jsonify(result))
        return jsonify(result)

class Query10API(MethodView):
    def __init__(self):
        self.q10 = Query10()

    def get(self):
        result = self.q10.execute() ## Dataframe
        # print(jsonify(result))
        return jsonify(result)

    # def post(self):

    # def delete(self):
