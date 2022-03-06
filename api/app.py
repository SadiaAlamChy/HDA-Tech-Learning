from flask import Flask, jsonify, request

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


from router import query_api
app.register_blueprint(query_api, url_prefix='/api/')

if __name__ == '__main__':
    app.run(debug=True, port=5000)



    # return jsonify({"msg" :"Hello Interns!!"})