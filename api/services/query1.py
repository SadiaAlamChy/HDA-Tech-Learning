from flask import jsonify
from flask.views import MethodView
from querycontroller.query1 import Query1

class Query1API(MethodView):
    def __init__(self):
        self.query1 = Query1()

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
        result = self.query1.execute() ## Dataframe
        # print(jsonify(result))
        return jsonify(result)