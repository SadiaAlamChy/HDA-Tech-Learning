from flask import jsonify
from flask.views import MethodView
from querycontroller.query3 import Query3

class Query3API(MethodView):
    def __init__(self):
        self.query3 = Query3()

    def get(self):
        '''
        Get the data of querycontroller 3
        :return:
                {

                   ‘total_sales’: 1000

                }
        '''
        result = self.query3.execute() ## Dataframe
        # print(jsonify(result))
        return jsonify(result)