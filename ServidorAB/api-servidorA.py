from flask import Flask, jsonify, request, abort
from pymongo import MongoClient

client = MongoClient()
client = MongoClient('localhost', 80)
#client = MongoClient('mongodb://localhost:80/')

db = client.texto 
#db = client['texto']

collection = db.texto
#collection = db['texto']

app = Flask(__name__)

posts = db.posts

# Testing Route
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'response': 'pong3!'})

# Obtener datos del kernel
@app.route('/kernel', methods=['GET'])
def kernel():
    return jsonify({'response': 'kernelOn'})

# Agragar datos a la base de datos
@app.route('/insertA', methods=['POST'])
def insert():
    if not request.json or not 'autor' in request.json or not 'nota' in request.json:
        abort(400)
    print('------------')
    print(request.json)
    print('------------')
    
    #post = {"autor": "",
    #        "nota": "",}
    #post_id = posts.insert_one(post).inserted_id
    #data = posts.find_one({})
    
    #print(data)
    return jsonify({'response': 'datos insertados correctamente..'}), 201




if __name__ == '__main__':
    app.run(debug=True, port=4000)
