# Importar
from flask import Flask, render_template, request


app = Flask(__name__)


def result_calculate(size, lights, device):
    # Variables que permiten calcular el consumo energético de los aparatos
    home_coef = 100
    light_coef = 0.04
    devices_coef = 5

    return size * home_coef + lights * light_coef + device * devices_coef


# La primera página
@app.route('/')
def index():
    return render_template('index.html')


# Guardar los datos del formulario
@app.route('/submit_form', methods=['POST'])
def submit_form():

    size = request.form['size']
    lights = request.form['lights']
    device = request.form['device']

    # Guardar todos los datos en form.txt
    with open('form.txt', 'a') as f:
        f.write('Tamaño: ' + size + '\n')
        f.write('Luces: ' + lights + '\n')
        f.write('Aparatos: ' + device + '\n')
        f.write('--------------------\n')

    # Calcular el resultado
    result = result_calculate(
        int(size),
        int(lights),
        int(device)
    )

    # Mostrar los datos en la página HTML
    return render_template(
        'form_result.html',
        size=size,
        lights=lights,
        device=device,
        result=result
    )


app.run(debug=True)
