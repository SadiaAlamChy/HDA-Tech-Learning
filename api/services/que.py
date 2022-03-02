from flask import jsonify,request
from flask.views import MethodView
from api.query.q1 import Query1
from api.query.q2 import Query2
from api.query.q3 import Query3
from api.query.q4 import Query4
from api.query.q5 import Query5
from api.query.q6 import Query6
from api.query.q7 import Query7
from api.query.q8 import Query8
from api.query.q9 import Query9
from api.query.q10 import Query10

class Query1API(MethodView):
    def __init__(self):
        self.q1 = Query1()

    def get(self):
        result = self.q1.execute() ## Dataframe
        return jsonify(result)



    # def post(self):

    # def delete(self):

class Query2API(MethodView):
    def __init__(self):
        self.q2 = Query2()

    def get(self):
        result = self.q2.execute() ## Dataframe
        return jsonify(result)

class Query3API(MethodView):
    def __init__(self):
        self.q3 = Query3()

    def get(self):
        result = self.q3.execute() ## Dataframe
        return jsonify(result)

class Query4API(MethodView):
    def __init__(self):
        self.q4 = Query4()

    def get(self):
        result = self.q4.execute() ## Dataframe
        return jsonify(result)

class Query5API(MethodView):
    def __init__(self):
        self.q5 = Query5()

    def get(self):
        result = self.q5.execute() ## Dataframe
        return jsonify(result)



class Query6API(MethodView):
    def __init__(self):
        self.q6 = Query6()

    def get(self):
        result = self.q6.execute()  ## Dataframe
        return jsonify(result)

class Query7API(MethodView):
    def __init__(self):
        self.q = Query7(data=0)

    def post(self):
        self.q.data = request.json['data']
        result = self.q.execute()
        return jsonify(result)

class Query8API(MethodView):
    def __init__(self):
        self.q8 = Query8()

    def get(self):
        result = self.q8.execute() ## Dataframe
        return jsonify(result)

class Query9API(MethodView):
    def __init__(self):
        self.q9 = Query9()

    def get(self):
        result = self.q9.execute() ## Dataframe
        return jsonify(result)

class Query10API(MethodView):
    def __init__(self):
        self.q10 = Query10()

    def get(self):
        result = self.q10.execute() ## Dataframe
        return jsonify(result)