"""Modulo de flask"""
from flask import Flask, request, jsonify, redirect, url_for,render_template
from flask_cors import CORS 


from fft.dft import dft
from config import config


app = Flask(__name__)

CORS(app)   


@app.route('/')
def index():
    return render_template("index.html")



#TODO: Hacer método para hacer el llamado a la librería en C
@app.route('/calcular-fft', methods=['POST'])
def calcular_fft():
    # Obtén el JSON recibido del cuerpo de la solicitud
    data = request.json['data']

    # Realiza la FFT en la lista de datos
    result = dft(data)

    real = [x.real for x in result]
    imaginary = [x.imag for x in result]
    # Crea un nuevo JSON con los resultados de la FFT
    json_result = {
        'real': real,
        'imaginary': imaginary
    }
    # print(f'contendio del json es {json_result}')
    # Devuelve el JSON como respuesta
    return jsonify(json_result)


def not_found(error):
    # al no encontrar la pagina lo enviamos a index
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, not_found)
    app.run()
