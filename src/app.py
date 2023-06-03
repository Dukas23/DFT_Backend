"""Modulo de flask Backend"""
from flask import Flask, request, jsonify
from flask_cors import CORS
from ctypes import CDLL, c_int, POINTER, c_double, Structure
import ctypes


from fft.dft import dft


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "http://52.87.153.247:8083",
            "expose_headers": "X-Custom-Header", "methods": ["GET", "POST"], "supports_credentials": True}})


# Se define la estructura Complex en Python
class Complex(ctypes.Structure):
    _fields_ = [
        ('real', ctypes.c_double),
        ('imag', ctypes.c_double)
    ]


# Ruta para el llamado de la apiRest de lenguaje C
@app.route('/calcular-fft-c', methods=['POST'])
def calcular_fft_c():
    # Se recibe el JSON enviado en la solicitud POST
    data = request.get_json()

    # Se extrae la lista de valores del JSON
    lista = data['data']

    # Cargamos la librería C con la función dft
    lib = CDLL('/home/ubuntu/Proyectos/dft.so')

    # Define el tipo de retorno de la función dft
    lib.dft.restype = POINTER(Complex)

    # Convertimos la lista a un array de tipo double en C
    arr = (c_double * len(lista))(*lista)

    # Llamamos a la función dft de la librería C
    resultados_ptr = lib.dft(arr, c_int(len(lista)))

    # Obtiene los resultados de la parte real e imaginaria en Python
    resultados = [resultados_ptr[i] for i in range(len(lista))]

    # Separamos los resultados en formato JSON en la parte real e imaginaria
    response = {
        'real': [r.real for r in resultados],
        'imaginary': [r.imag for r in resultados]
    }

    # Liberamos la memoria asignada en C
    lib.free(resultados_ptr)

    # Se retorna la respuesta en formato JSON
    return jsonify(response)


# Ruta para el llamado de la apiRest de lenguaje Python
@app.route('/calcular-fft-python', methods=['POST'])
def calcular_fft():
    # Obtemos el JSON recibido del cuerpo de la solicitud
    data = request.json['data']

    # Realizamos la FFT en la lista de datos
    result = dft(data)

    # Sacamos la parte real e imaginaria por separado
    real = [x.real for x in result]
    imaginary = [x.imag for x in result]
    # Creamos un nuevo JSON con los resultados de la FFT
    json_result = {
        'real': real,
        'imaginary': imaginary
    }
    # Devuelve el JSON como respuesta
    return jsonify(json_result)


if __name__ == '__main__':
    app.run(host="0.0.0.0")
