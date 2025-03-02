from crypt import methods

from flask import Flask, jsonify, request
#jsonify package converts python objects into JSON
from http import HTTPStatus

# creating an instance of FLASK Class
app = Flask(__name__)

#Define the recepies list

recepies = [
    {

    "id" : 1,
    'name': 'Egg Salad',
    'description': 'This is egg salad recipe'
},
    {
        "id": 2,
        'name': 'Tomato Salad',
        'description': 'This is a Tomato Salad recipe'
    }
]

#route decorator
@app.route('/recepies', methods = ['GET'])

def get_recipies():
    return jsonify({'data': recepies})
if __name__ == "__main__":
    app.run()

#changed
