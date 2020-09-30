from flask import Flask, jsonify, request, abort
from pymongo import MongoClient

client = MongoClient()
client = MongoClient('localhost', 80)
db = client.texto 
collection = db.texto

app = Flask(__name__)

#obtener RAM
@app.route('/ram', methods=['GET'])
def ram():
    f = open("/elements/procs/test-module", "r")
    data = f.read()

    ram = data.split('-')
    
    totalRam = int(ram[0].lstrip())
    freeRam = int(ram[1].lstrip())

    porcentajeRam = 100-((freeRam/totalRam)*100)

    return jsonify({'response': porcentajeRam})

# obtener CPU
@app.route('/cpu', methods=['GET'])
def cpu():
    f = open("/elements/procs/cpu-module", "r")
    data = f.read()
    print(data)
    return jsonify({'response': data})

# obtener CPU2
@app.route('/cpu2', methods=['GET'])
def cpu2():
    f = open("/elements/procs/loadavg", "r")
    data = f.read()
    print(data)
    cpu = data.split(" ")
    print(cpu[0])
    porcentajeCPU = float(cpu[0])*100

    return jsonify({'response': porcentajeCPU})

# Agragar datos a la base de datos
@app.route('/insertar', methods=['POST'])
def insert():
    if not request.json or not 'autor' in request.json or not 'nota' in request.json:
        abort(400)
    try:
        data = []
        collection.insert_one(request.json).inserted_id
        data = collection.find()
        return jsonify({'response': data.count()}), 201
    except:
        return jsonify({'response': 'Error al intentar insertar datos en el server'}), 500
   
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8080)
