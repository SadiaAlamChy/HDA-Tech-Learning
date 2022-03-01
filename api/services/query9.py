from flask import jsonify
from flask.views import MethodView
from querycontroller.query9 import Query9

class Query9API(MethodView):
    def __init__(self):
        self.query9 = Query9()

    def get(self):
        '''
          [{

          ‘item’: “item name”,

          ‘sales’: [

             {

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
        result = self.query9.execute() ## Dataframe
        # print(jsonify(result))
        return jsonify(result)