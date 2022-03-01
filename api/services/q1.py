from flask import jsonify
from flask.views import MethodView
from querycontroller.q1 import Query1

class Query1API(MethodView):
    def __init__(self):
        self.q1 = Query1()

    def get(self):
        '''
        Get the data of querycontroller 1
        :return: [{
                  ‘division’: “Dhaka”,
                  'total_sales’: 1000
                  },
                 {
                  ‘division’: “Rangpur”,
                  ‘total_sales’: 1000
                 },....
                ]
        '''
        result = self.q1.execute() ## Dataframe
        # print(jsonify(result))
        return jsonify(result)

    # def post(self):

    # def delete(self):
