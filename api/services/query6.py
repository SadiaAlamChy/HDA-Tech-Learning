from flask import jsonify
from flask.views import MethodView
from querycontroller.query6 import Query6

class Query6API(MethodView):
    def __init__(self):
        self.query6 = Query6()

    def get(self):
        '''
        Get the data of querycontroller 4
        :return:
                [{

                  ‘store’: “store name/key”,

                   ‘items’: [‘i1’, ‘i2’, ‘i3’]

                 },....

                ]
                 '''
        result = self.query6.execute() ## Dataframe
        # print(jsonify(result))
        return jsonify(result)