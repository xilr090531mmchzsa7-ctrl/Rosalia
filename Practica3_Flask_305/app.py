from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('triangulo.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    base = float(request.form['base'])
    altura = float(request.form['altura'])

    area = (base * altura) / 2
    perimetro = lado * 4

    return render_template(
        'triangulo.html',
        area=area,
        perimetro=perimetro
    )

if __name__ == '__main__':
    app.run(debug=True)