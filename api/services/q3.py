from flask import jsonify
from flask.views import MethodView
from query.q3 import Query3


class Query3API(MethodView):
    def __init__(self):
        self.q3 = Query3()

    def get(self):
        '''
        Get the data of query 1
        :return: [{

             ‘total_sales’: 1000

            },....
        ]
        '''
        result = self.q3.execute()  ## Dataframe
        # print(jsonify(result))
        return jsonify(result)

    # def post(self):
    # def delete(self):
