from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)

api = Api(app)

class HelloWorld(Resource):
	def get(self):
		data={"data":"Hello World"}
		return data

api.add_resource(HelloWorld,'/hello')


if __name__=='__main__':
	app.run(debug=True)


"""
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/hello', methods=['GET'])
def helloworld():
	if(request.method == 'GET'):
		data = {"data": "Hello World"}
		return jsonify(data)


if __name__ == '__main__':
	app.run(debug=True)
"""