from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
USUARIOS_REGISTRADOS = {
    'admin@correo.com':{
        'password': 'admin123',
        'nombre': 'administrador',
        }
}

app.config['SECRET_KEY'] = 'una_clave_muy_secreta_muy_larga_y_dificl_de_adivinar_lel_ses_me_cai'

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
    if session.get('logueado'):
        return render_template('iniciar.html')
    return render_template('iniciar.html')

@app.route('/validaLogin', methods=['GET','POST'])
def validar():
    if request.method == "POST":
        correo = request.form.get("correo", '').strip()
        password = request.form.get("password", '')
        
        if not correo or not password:
            flash('Por favor ingresa email y contraseña', 'error')
            return render_template('iniciar.html')
        
        elif correo in USUARIOS_REGISTRADOS:
            usuario = USUARIOS_REGISTRADOS[correo]
            if usuario['password'] == password:
                session['logueado'] = True
                session['usuario'] = usuario['nombre']
                session['usuario_correo'] = correo
                flash(f'¡Bienvenido {usuario["nombre"]}!', 'success')
                return redirect(url_for('inicio'))
            else:
                flash('Contraseña incorrecta', 'error')
        else:
            flash('Usuario no encontrado', 'error')
        
        return render_template('iniciar.html')
    
    return redirect(url_for('iniciar'))

@app.route("/logout")
def logout():
    session.clear()
    flash('Has cerrado sesión correctamente', 'info')
    return redirect(url_for('inicio'))

@app.route("/registrar", methods = ("GET", "POST"))
def registrar():
    if request.method == "POST":
        error = None
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
            error = "Las contraseñas no coinciden"
        elif correo in USUARIOS_REGISTRADOS:
            error = "Este correo ya está registrado"
        
        if error is not None:
            flash(error, 'error')
            return render_template('registro.html')
        else:

            USUARIOS_REGISTRADOS[correo] = {
                'password': password,
                'nombre': f"{nombre} {apellido}",
            }
            flash(f"Registro exitoso: {nombre}. Ahora puedes iniciar sesión.", 'success')
            return redirect(url_for('iniciar'))

if __name__ == '__main__':
    app.run(debug=True)