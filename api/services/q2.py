from flask import jsonify
from flask.views import MethodView
from query.q2 import Query2
class Query2API(MethodView):
    def __init__(self):
        self.q2 = Query2()

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
        result2 = self.q2.execute() ## Dataframe
        print(jsonify(result2))
        return jsonify(result2)

    # def post(self):

    # def delete(self):
