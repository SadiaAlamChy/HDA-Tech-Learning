from flask import jsonify,request
from flask.views import MethodView
from querycontroller.query7 import Query7

class Query7API(MethodView):
    def __init__(self):
        self.query7 = Query7(days=0)

    def post(self):
        '''
        Get the data of querycontroller 4
        :return:
                POST:

                {

                   ‘days’: 5

                }

                Response:

                {

                   ‘Items’: [‘i1’, ‘i2’........]

                }
               '''
        self.query7.days = request.json['days']
        result = self.query7.execute() ## Dataframe
        # print(jsonify(result))
        return jsonify(result)

    def __init__(self):
        self.q = Query7(days=0)

    def post(self):

        result = self.q.execute()
        return jsonify(result)
