from flask import jsonify
from flask.views import MethodView
from query.q10 import Query10
class Query10API(MethodView):
    def __init__(self):
        self.q10 = Query10()

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
        result10 = self.q10.execute() ## Dataframe
        print(jsonify(result10))
        return jsonify(result10)