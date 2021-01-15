from flask import Flask, render_template

app = Flask(__name__)

#RUTA INICIO
@app.route("/")
def inicio():
    return render_template("inicio.html")

#RUTA REGISTRO
@app.route("/registro")
def registro():
    return render_template("registro.html") 

#RUTA CONTACTO
@app.route("/contacto")
def contacto():
    return render_template("contacto.html")

#RUTA EQUIPOS
@app.route("/equipos")
def equipos():
    return render_template("equipos.html")

#RUTA NUEVOS USUARIOS
@app.route("/nusuarios")
def usuarios():
    return render_template("nusarios.html")

if __name__ == "__main__":
    app.run(debug = True, port=4000)