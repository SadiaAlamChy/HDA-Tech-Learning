from flask import jsonify
from flask.views import MethodView
from query.q4 import Query4
class Query4API(MethodView):
    def __init__(self):
        self.q4 = Query4()

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
        result4 = self.q4.execute() ## Dataframe
        print(jsonify(result4))
        return jsonify(result4)