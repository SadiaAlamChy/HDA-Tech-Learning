from flask import jsonify
from flask.views import MethodView
from query.q10 import Query10


class Query10API(MethodView):
    def __init__(self):
        self.q10 = Query10()

    def get(self):
        '''
        Get the data of query 10
        :return: [{
        ‘item’: “item name”,
        ‘sales’: [{
        month’: ‘January’,
        ‘total_sales’: 1000
        },{
        ‘month’: ‘February’,
        ‘total_sales’: 1000
        },....]},.....]
        '''
        result = self.q10.execute()  ## Dataframe
        # print(jsonify(result))
        return jsonify(result)

    # def post(self):
    # def delete(self):

