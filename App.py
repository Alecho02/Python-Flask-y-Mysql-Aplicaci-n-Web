from flask import Flask

app = Flask(__name__)

@app.route('/')
def Index():
	return 'Hola Mundo'

@app.route('/add_contact')
def add_contact():
	return 'Agregar contacto'

@app.route('/edit')
def edit_contact():
	return 'Editar contacto'

@app.route('/add_contact')
def add_contact():
	return 'Agregar contacto'


if __name__ == '__main__':
	app.run(port = 3000, debug = True) 