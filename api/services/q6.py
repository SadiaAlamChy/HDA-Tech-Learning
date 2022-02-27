from flask import jsonify
from flask.views import MethodView
from query.q6 import Query6
class Query6API(MethodView):
    def __init__(self):
        self.q6 = Query6()

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
        result6 = self.q6.execute() ## Dataframe
        print(jsonify(result6))
        return jsonify(result6)