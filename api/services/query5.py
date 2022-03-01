from flask import jsonify
from flask.views import MethodView
from querycontroller.query5 import Query5

class Query5API(MethodView):
    def __init__(self):
        self.query5 = Query5()

    def get(self):
        '''
        Get the data of querycontroller 4
        :return:
                {

                   ‘total_sales’: 1000

                }
                 '''
        result = self.query5.execute() ## Dataframe
        # print(jsonify(result))
        return jsonify(result)