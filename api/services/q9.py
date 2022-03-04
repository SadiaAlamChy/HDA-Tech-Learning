from flask import jsonify
from flask.views import MethodView
from query.q9 import Query9


class Query9API(MethodView):
    def __init__(self):
        self.q9 = Query9()

    def get(self):
        '''
        Get the data of query 1
        :return: [{
                ‘item’: “item name”,
                 ‘sales’: [{

             ‘division’: ‘Dhaka’,
             ‘total_sales’: 1000
            },
            {
            ‘division’: ‘Barisal’,
            ‘total_sales’: 1000
            },....
            ]
             },.....
        ]
        '''
        result = self.q9.execute()  ## Dataframe
        # print(jsonify(result))
        return jsonify(result)

    # def post(self):
    # def delete(self):

