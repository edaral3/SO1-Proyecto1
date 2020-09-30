from flask import Flask, jsonify, request, abort
from pymongo import MongoClient
from bson.json_util import dumps

client = MongoClient()
client = MongoClient('mongodb://mongo:27017/')
db = client.notas 
collection = db.notas

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
    return jsonify({'response': data})

# obtener CPU2
@app.route('/cpu2', methods=['GET'])
def cpu2():
    f = open("/elements/procs/loadavg", "r")
    data = f.read()
    cpu = data.split(" ")
    porcentajeCPU = float(cpu[0])*100

    return jsonify({'response': porcentajeCPU})

# Agragar datos a la base de datos
@app.route('/insertar', methods=['POST'])
def insert():
    if not request.json or not 'autor' in request.json or not 'nota' in request.json:
        abort(400)
    try:
        collection.insert(request.json)
        data = []
        data = collection.find()
        return jsonify({'response': data.count()}), 201
    except:
        return jsonify({'response': 'Error al intentar insertar datos en el server'}), 500
   
# Obtener notas a la base de datos
@app.route('/notas', methods=['GET'])
def notas():
    try:
        data = []
        data = collection.find()
        return jsonify({'response': dumps(data)}), 201
    except Exception as err:
        return jsonify({'response': "Error al obtener las notas"}), 500
      
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8080)
