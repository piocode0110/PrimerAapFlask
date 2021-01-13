from flask import Flask, render_template

app = Flask(__name__)

#RUTA INICIO
@app.route("/")
def inicio():
    return render_template("inicio.html")

#RUTA REGISTRO
@app.route("/registro.html")
def registro():
    return render_template("registro.html") 

#RUTA CONTACTO
@app.route("/contacto.html")
def contacto():
    return render_template("contacto.html")


if __name__ == "__main__":
    app.run(debug = True, port=4000)