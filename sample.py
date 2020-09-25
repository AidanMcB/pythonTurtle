from flask import Flask, jsonify 

app=Flask(__name__)

airlines = [
    {
        "id": 1,
        "name": 'United'
    },
    {   "id":  2, 
        "name": 'Spirit'
    },
    {
        "id": 3,
        "name": "Frontier"
    }
]

@app.route('/airlines')
def hi():
    return jsonify(airlines)

@app.route('/airlines/<id>')
def second(id):
    for airline in airlines:
        if airline['id'] == int(id):
            return jsonify(airline)
