from flask import Flask, render_template
from flask_mysqldb import MyQSL

app = Flask(__name__)
app.config['MYSQL_HOST'] ='localhost'
app.config['MYSQL_USER'] ='admin'
app.config['MYSQL_PASSWORD'] ='Bancosal1'
app.config['MYSQL_DB'] ='flaskcontacts'
mysql=MyQSL(app)

@app.route('/')
def Index():
	return ''

@app.route('/add_contact')
def add_contact():
	return 'Agregar contacto'

@app.route('/edit')
def edit_contact():
	return 'Editar contacto'

@app.route('/delete')
def delete_contact():
	return 'Borrar contacto'


if __name__ == '__main__':
	app.run(port = 3000, debug = True) 