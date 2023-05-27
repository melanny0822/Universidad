from urllib import request
from flask import render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import redirect
from flask import Flask
from flask import request
from datetime import datetime


#Configuración de la aplicación: Se crea una instancia de la aplicación Flask y
# se configura la conexión a la base de datos PostgreSQL.
app = Flask(__name__)
app.secret_key = 'admin'

# ingresar a la bd
USER_DB = 'postgres'
PASS_DB = 'admin'
URL_DB = 'localhost'
NAME_DB = 'universidad'
FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'


app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

migrate = Migrate()
migrate = Migrate(app, db)
migrate.init_app(app, db)


#Se definen tres modelos de base de datos utilizando la extensión SQLAlchemy
class Registro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    correo = db.Column(db.String(50), nullable=False)

    def __str__(self):
        return f'<Registro {self.id}: {self.nombre} {self.apellido}>'


class Matricula(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    facultad = db.Column(db.String(50), nullable=False)
    jornada = db.Column(db.String(50), nullable=False)
    modalidad = db.Column(db.String(50), nullable=False)

    def __str__(self):
        return f'<Matricula {self.id}: {self.nombre} {self.apellido}>'


class PQRS(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(50), nullable=False)
    descripcion = db.Column(db.String(255), nullable=False)
    fecha = db.Column(db.DateTime)

    def __str__(self):
        return f'<PQRS {self.id}: {self.tipo} {self.descripcion}>'


# Rutas
@app.route('/')
def inicio():
    return render_template('Inicio_TDEA.html')


@app.route('/Registros', methods=['GET', 'POST'])
def registros():
    registros = Registro.query.all()
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        correo = request.form['correo']
        registro = Registro(nombre=nombre, apellido=apellido, correo=correo)
        db.session.add(registro)
        db.session.commit()
        return redirect('/Registros')
    return render_template('Registros.html', registros=registros)


@app.route('/Matriculas', methods=['GET', 'POST'])
def matriculas():
    matriculas = Matricula.query.all()
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        facultad = request.form['facultad']
        jornada = request.form['jornada']
        modalidad = request.form['modalidad']
        matricula = Matricula(nombre=nombre, apellido=apellido, facultad=facultad, jornada=jornada, modalidad=modalidad)
        db.session.add(matricula)
        db.session.commit()
        return redirect('/Matriculas')
    return render_template('Matriculas.html', matriculas=matriculas)


@app.route('/PQRS', methods=['GET', 'POST'])
def pqrs():
    pqrs = PQRS.query.all()
    if request.method == 'POST':
        tipo = request.form['tipo']
        descripcion = request.form['descripcion']
        fecha = datetime.now()
        pqrs = PQRS(tipo=tipo, descripcion=descripcion, fecha=fecha)
        db.session.add(pqrs)
        db.session.commit()
        return redirect('/PQRS')
    return render_template('PQRS.html', pqrs=pqrs)


@app.route('/Consultas')
def consultas():
    registros = Registro.query.all()
    matriculas = Matricula.query.all()
    pqrs = PQRS.query.all()
    return render_template('Consultas.html', registros=registros, matriculas=matriculas, pqrs=pqrs)


if __name__ == '__main__':
    app.run()



