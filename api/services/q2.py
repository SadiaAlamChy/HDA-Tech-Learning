from flask import jsonify
from flask.views import MethodView
from query.q2 import Query2


class Query2API(MethodView):
    def __init__(self):
        self.q2 = Query2()

    def get(self):
        '''
        Get the data of query 1
        :return: [{
                  ‘trans_type’: “Cash”,
                  ‘total_sales’: 1000
                  },
                 {
                  ‘trans_type’: “Mobile”,
                  ‘total_sales’: 1000
                 },....
                ]
        '''
        result = self.q2.execute()  ## Dataframe
        # print(jsonify(result))
        return jsonify(result)

    # def post(self):

    # def delete(self):
