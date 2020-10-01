from flask import Flask, jsonify, request, abort
import requests

urlA = 'http://13.58.195.101'
urlB = 'http://13.58.15.216'

app = Flask(__name__)


@app.route('/')
def index():
    return "activo"

#Insertar Nota
@app.route('/insertar', methods=['POST'])
def insertar():
    if not request.json or not 'autor' in request.json or not 'nota' in request.json:
        abort(400)
    try:
        data = request.json
        servidor = True
        cantidadNotasA = requests.get(urlA+"/cantidadNotas").json()['response']
        cantidadNotasB = requests.get(urlB+"/cantidadNotas").json()['response']
        if (cantidadNotasA!=cantidadNotasB):
            if (cantidadNotasA>cantidadNotasB):
                servidor = False
        else:
            porcentajeRamA = requests.get(urlA+"/ram").json()['response']
            porcentajeRamB = requests.get(urlB+"/ram").json()['response']
            if (porcentajeRamA!=porcentajeRamB):
                if (porcentajeRamA>porcentajeRamB):
                    servidor = False
            else:
                porcentajeCPUA = requests.get(urlA+"/cpu2").json()['response']
                porcentajeCPUB = requests.get(urlB+"/cpu2").json()['response']
                if (porcentajeCPUA!=porcentajeCPUB):
                    if (porcentajeCPUA>porcentajeCPUB):
                        servidor = False
        if (servidor):
            requests.post(urlA+"/insertar", json=data)
        else:
            requests.post(urlB+"/insertar", json=data)
        
        return jsonify({'response': "datos insertados correctamente"})
    except:
        return jsonify({'response': "Error al intentar insertar notas"})



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8080)
