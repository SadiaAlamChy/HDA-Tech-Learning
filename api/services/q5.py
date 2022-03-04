from flask import jsonify
from flask.views import MethodView
from query.q5 import Query5


class Query5API(MethodView):
    def __init__(self):
        self.q5 = Query5()

    def get(self):
        '''
        Get the data of query 1
        :return: [{

             ‘total_sales’: 1000

            },....
        ]
        '''
        result = self.q5.execute()  ## Dataframe
        # print(jsonify(result))
        return jsonify(result)

    # def post(self):
    # def delete(self):
