from flask import  Flask, jsonify, request
# from api.controllers.Q1 import Query1API

app = Flask(__name__)


@app.route("/greetings", methods=['GET'])
def greetings():
    return jsonify({'message':" Heloooo.................."})


@app.route("/greetings/customized", methods=['GET', 'POST'])
def greetings_customized():
    if request.method == 'POST':
        # return jsonify({"message": "Hello "})
        data = {
            'FirstName': request.json['FirstName'],
            'LastName': request.json['LastName'],
            'UserName': request.json['UserName']
        }
        return jsonify({"Name": data['FirstName'] + ' ' + data['LastName']})
    else:
        return jsonify({"message": "Get... "})


# app.add_url_rule('/api/q1', view_func=Query1API.as_view('Get division wise total sale'))
from router import query_api
app.register_blueprint(query_api, url_prefix='/api/')


if __name__ == '__main__':
    app.run(port=5000)



    # return jsonify({"msg" :"Hello Interns!!"})