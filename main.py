from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    nombre = None
    total_sin_descuento = None
    total_descuento = None
    total_a_pagar = None

    if request.method == "POST":
        nombre = request.form["nombre"]
        edad = int(request.form["edad"])
        tarros = int(request.form["tarros"])

        total_sin_descuento = tarros * 9000

        descuento = 0
        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25

        total_descuento = total_sin_descuento * descuento
        total_a_pagar = total_sin_descuento - total_descuento

    return render_template(
        "ejercicio1.html",
        nombre=nombre,
        total_sin_descuento=total_sin_descuento,
        total_descuento=total_descuento,
        total_a_pagar=total_a_pagar
    )


@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    mensaje = None

    usuarios = {
        "juan": "admin",
        "pepe": "user"
    }

    if request.method == "POST":
        nombre = request.form["nombre"]
        password = request.form["password"]

        if nombre in usuarios and usuarios[nombre] == password:
            if nombre == "juan":
                mensaje = "Bienvenido administrador juan"
            else:
                mensaje = f"Bienvenido usuario {nombre}"
        else:
            mensaje = "Usuario o contraseña incorrectos"

    return render_template("ejercicio2.html", mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)