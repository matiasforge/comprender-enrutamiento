from flask import Flask

app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return "¡Hola Mundo!"

@app.route('/dojo')
def dojo():
    return "¡Dojo!"

@app.route('/say/<nombre>')
def hola_nombre(nombre):
    return "¡Hola, " + nombre + "!"

@app.route('/repeat/<int:veces>/<mensaje>')
def repetir_mensaje(veces, mensaje):
    return mensaje * veces

# Ruta de error para manejar cualquier otra URL
@app.errorhandler(404)
def pagina_no_encontrada(error):
    return "¡Lo siento! No hay respuesta. Inténtalo otra vez.", 404

if __name__ == "__main__":
    app.run(debug=True)
