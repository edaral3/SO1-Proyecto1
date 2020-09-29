from flask import Flask, jsonify, request

app = Flask(__name__)

# Testing Route
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'response': 'pong!'})


if __name__ == '__main__':
    app.run(debug=True, port=4000)
