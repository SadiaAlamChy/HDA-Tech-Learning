from flask import jsonify
from flask.views import MethodView
from querycontroller.query4 import Query4

class Query4API(MethodView):
    def __init__(self):
        self.query4 = Query4()

    def get(self):
        '''
        Get the data of querycontroller 4
        :return:
                {

                   ‘total_sales’: 1000

                }
                 '''
        result = self.query4.execute() ## Dataframe
        # print(jsonify(result))
        return jsonify(result)