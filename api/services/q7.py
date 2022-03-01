from flask import jsonify
from flask.views import MethodView
from query.q7 import Query7
class Query7API(MethodView):
    def __init__(self):
        self.q7 = Query7()

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
        result7 = self.q7.execute() ## Dataframe
        print(jsonify(result7))
        return jsonify(result7)