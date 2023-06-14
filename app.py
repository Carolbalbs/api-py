#DEFINIR 4 PONTOS PARA API
# 1. Objetivo - Criar uma api que disponibiliza a consulta, criação, edição e exlusão de livros.
# 2. URL base - localhost 
# 3. Endpoint
# - localhost/livros (GET)
# - localhost/livros/id (GET)
# - localhost/livros/id (POST)
# - localhost/livro/id (PUT)
# - localhost/livro/id (DELETE)
# 4. Quais recursos - Livros
from  flask import Flask, jsonify, request
 
app = Flask(__name__)

livros = [
{    'id': 1,
    'titulo': 'Harry Potter ',
    'autor': 'JK Rowling'
},
{    'id': 2,
    'titulo': 'Querido diario otario ',
    'autor': 'Lindsey'
},
{    'id': 3,
    'titulo': 'Diario de um banana ',
    'autor': 'Jeffre'
}
]
# #consultar(todos)
# @app.route('/livros')
# def obter_livros():
#     return jsonify(livros)

# #consultar(id)
# @app.route('/livros/id')
# def obter_livros():
#     return jsonify(livros)
# #editar
# @app.route('/livros')
# def editar_livros():
#     return jsonify()
# #excluir

app.run(port=5000,host='localhost',debug=True)

funcao(wefnsnjnkjdfnbkjdfnbjdfnjbkndfjbndfjb)