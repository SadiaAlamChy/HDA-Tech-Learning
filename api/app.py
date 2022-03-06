from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/greeting", methods  = ['GET'])

def greeting():
    return jsonify({"msg":"Hello Sultan"})


@app.route("/greeting/customized", methods  = ['POST'])

def greeting_customized():
    data = {}
    data['name'] = request.json['name']
    return jsonify({"msg":"Hello Sultan" + data['name']})

if __name__ == '__main__':
    app.run(port = 5000)