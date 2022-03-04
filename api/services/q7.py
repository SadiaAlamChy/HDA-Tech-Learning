from flask import jsonify
from flask.views import MethodView
from query.q7 import Query7


class Query7API(MethodView):
    def __init__(self):
        self.q7 = Query7()

    def get(self):
        '''
        Get the data of query 1
        :return: [{

             ‘store’: “store name/key”,
            ‘items’: [‘i1’, ‘i2’, ‘i3’]

            },....
        ]
        '''
        result = self.q7.execute()  ## Dataframe
        # print(jsonify(result))
        return jsonify(result)

    # def post(self):
    # def delete(self):

