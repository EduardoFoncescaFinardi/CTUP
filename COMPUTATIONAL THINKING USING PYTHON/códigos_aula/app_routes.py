from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def index():
    return 'Pedro suga aqui'

@app.route("/hello/<name>")
def hello_name(name):
    #return 'Hello, {name} %s' % name
    return f'Hello, {name}'

@app.route('/soma/<int:n1>/<int:n2>')
def soma(n1, n2):
    return f'A soma de {n1} com {n2} = {n1 + n2}'

@app.route('/status/')
def status():
    return {"status":"ok"}

@app.route("/st")
def home_page():
    return jsonify({"statusSsssSs":"ok"})

@app.route("/todo")
def todo_list():
    return jsonify(
    {"tafera 1" : "Estudar Python",
     "tarefa 2" : "Estudar Java",
     "tarefa 3" : "Ir para a FIAP",
     "tarefa 2" : "Entregar o CP de Python",
     "tarefa 5" : "Estudar API Rest"
     }
    )
#Principal
if __name__ == "__main__":
    app.run()