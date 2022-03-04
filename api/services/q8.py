from flask import jsonify
from flask.views import MethodView
from query.q8 import Query8


class Query8API(MethodView):
    def __init__(self):
        self.q8 = Query8()

    def get(self):
        '''
        Get the data of query 1
        :return: [{

                ‘item’: ‘item name’,

                ‘quarter’: ‘Q1’

             },....

           ]
        '''
        result = self.q8.execute()  ## Dataframe
        # print(jsonify(result))
        return jsonify(result)

    # def post(self):
    # def delete(self):

