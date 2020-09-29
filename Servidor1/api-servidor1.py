from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Testing Route
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'response': 'pong!'})

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

# prueba
@app.route('/lista', methods=['GET'])
def lista():
    return jsonify({"lista":[{"autor":"Edgar Aldana2","nota":"asdfghj"},{"autor":"Edgar Aldana2","nota":"aaaaaaaaa"},{"autor":"Edgar Aldana2","nota":"ggggggggg"}]})


if __name__ == '__main__':
    app.run(debug=True, port=4000)
