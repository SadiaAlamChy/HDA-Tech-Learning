from flask import jsonify
from flask.views import MethodView
from query.q6 import Query6


class Query6API(MethodView):
    def __init__(self):
        self.q6 = Query6()

    def get(self):
        '''
        Get the data of query 1
        :return: [{

             ‘store’: “store name/key”,
            ‘items’: [‘i1’, ‘i2’, ‘i3’]

            },....
        ]
        '''
        result = self.q6.execute()  ## Dataframe
        # print(jsonify(result))
        return jsonify(result)

    # def post(self):
    # def delete(self):

