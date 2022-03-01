from flask import jsonify
from flask.views import MethodView
from querycontroller.query2 import Query2

class Query2API(MethodView):
    def __init__(self):
        self.query2 = Query2()

    def get(self):
        '''
        Get the data of querycontroller 2
        :return:
                [{

                  ‘trans_type’: “Cash”,

                   ‘total_sales’: 1000

                 },

                {

                  ‘trans_type’: “Mobile”,

                   ‘total_sales’: 1000

                 },....

                ]
        '''
        result = self.query2.execute() ## Dataframe
        # print(jsonify(result))
        return jsonify(result)