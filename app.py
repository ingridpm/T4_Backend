from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import json
import os 

app = Flask(__name__)
CORS(app)
peliculas = []

@app.route('/', methods=['GET'])
def principal():
    return "<h1>Conectado</h1>"

@app.route('/peliculas', methods=['GET'])
def getPeliculas():
    return jsonify(peliculas)

@app.route('/leerArchivo', methods=['POST'])
def leerArchivo():
    cuerpo = request.get_json()
    contenido = cuerpo['contenido']
    filas = contenido.split("\r\n")
    global peliculas
    for fila in filas:
        columnas = fila.split(",")
        peliculas.append({'nombre':columnas[0], 'puntuacion':columnas[1]})
    return jsonify(peliculas)

if __name__ == '__main__':
    puerto = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0',port=puerto)