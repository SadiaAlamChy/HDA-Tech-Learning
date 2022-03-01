from flask import jsonify
from flask.views import MethodView
from querycontroller.query8 import Query8

class Query8API(MethodView):
    def __init__(self):
        self.query8 = Query8()

    def get(self):
        '''
                    [{

               ‘item’: ‘item name’,

               ‘quarter’: ‘Q1’

            },....

            ]
                 '''
        result = self.query8.execute() ## Dataframe
        # print(jsonify(result))
        return jsonify(result)