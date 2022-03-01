from flask import jsonify
from flask.views import MethodView
from querycontroller.query10 import Query10

class Query10API(MethodView):
    def __init__(self):
        self.query10 = Query10()

    def get(self):
        '''
            [{

              ‘item’: “item name”,

              ‘sales’: [

                 {

                   ‘month’: ‘January’,

                   ‘total_sales’: 1000

                 },

                 {

                 ‘month’: ‘February’,

                   ‘total_sales’: 1000

                 },....

               ]

             },.....

            ]
                 '''
        result = self.query10.execute() ## Dataframe
        # print(jsonify(result))
        return jsonify(result)