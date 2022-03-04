from flask import jsonify
from flask.views import MethodView
from query.q4 import Query4


class Query4API(MethodView):
    def __init__(self):
        self.q4 = Query4()

    def get(self):
        '''
        Get the data of query 1
        :return: [{

             ‘total_sales’: 1000

            },....
        ]
        '''
        result = self.q4.execute()  ## Dataframe
        # print(jsonify(result))
        return jsonify(result)

    # def post(self):
    # def delete(self):
