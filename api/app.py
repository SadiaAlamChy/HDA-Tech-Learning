from flask import Flask, jsonify, request
app=Flask(__name__)

@app.route("/greetings", methods=['GET'])
def greetings():
    return jsonify({"msg" :"Hello Interns!!"})

@app.route("/greetings/customized", methods=['POST'])
def greetings_customized():
    data = {}
    data['name'] = request.json['name']
    return jsonify({"msg" :"Hello "+ data['name']})



from router import query_api
app.register_blueprint(query_api, url_prefix='/api/')

if __name__ == '__main__':
    app.run(host='localhost', port=5050)
