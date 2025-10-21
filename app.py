from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

app.config['SECRET_KEY'] = 'una_clave_muy_secreta_muy_larga_y_dificl_de_adivinar'

@app.route("/")
def inicio():
    return render_template('inicio.html')

@app.route("/animales")
def animales():
    return render_template('animales.html')

@app.route("/vehiculos")
def vehiculos():
    return render_template('vehiculos.html')

@app.route("/maravillas")
def maravillas():
    return render_template('maravillas.html')

@app.route("/acerca")
def acerca():
    return render_template('acerca.html')

@app.route("/registro")
def registro():
    return render_template('registro.html')

@app.route("/iniciar")
def iniciar():
    return render_template('iniciar.html')

@app.route("/registrar", methods = ("GET", "POST"))
def registrar():
    if request.method == "POST":
        error=None
        nombre = request.form.get("nombre")
        apellido = request.form.get("apellido")
        dia = request.form.get("dia")
        mes = request.form.get("mes")
        year = request.form.get("year")
        correo = request.form.get("correo")
        password = request.form.get("password")
        confirmPassword = request.form.get("confirmPassword")
        genero = request.form.get("genero")
        
        if password != confirmPassword:
            error = "la contraseña es incorrecta"
        if error is not None:
            flash(error)
            return render_template('registro.html')
        else:
            flash(f"Registro exitoso: {nombre}")
            return render_template('inicio.html')

if __name__ == '__main__':
    app.run(debug=True)