import os
from contextlib import contextmanager
from psycopg2 import connect, extras

from flask import Flask, request, render_template, redirect, url_for, flash
import psycopg2



app = Flask(__name__, static_folder='static', template_folder='templates')


app.config['SECRET_KEY'] = os.urandom(16)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://dbname=encuesta host=localhost user=postgres password=Z4dk13l2017**"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



@app.route('/')
def index():
    return 'Hola Index'


@app.route('/success', methods=['GET'])
def success():
    return render_template('success.html')



@app.route('/encuesta', methods=['GET', 'POST'])
def encuesta():
    title = 'Registro de Encuesta'
    if request.method == 'POST':
        folio = request.form['folio']
        matricula = request.form['matricula']
        nombre = request.form['nombre']
        choices = request.form['choices']
        print(folio, choices)
        con = psycopg2.connect("dbname=encuesta host=localhost user=postgres password=Z4dk13l2017**")
        cur = con.cursor()
        cur.execute("INSERT INTO encuestatbl(folio, matricula, nombre, choices) VALUES(%s, %s, %s, %s)", (int(folio), matricula, nombre, choices))
        con.commit()
        cur.close()
        con.close()

        flash('Respuestas Enviadas Correctamente')
        return redirect(url_for('encuesta'))
    return render_template('encuesta.html', title=title)



if __name__ == '__main__':
    app.run(debug=True)
