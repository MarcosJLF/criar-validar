from flask import Flask, jsonify, request
import model

app = Flask(__name__)

arr = {}

@app.route('/password', methods=['GET'])
def password():
    password = model.insert_all(10)
    messagem = {'Tamanho':10,
                'Senha gerada': password}
    arr['senha'] = password
    return jsonify(messagem), 200


@app.route('/password/<int:tamanho>', methods=['GET'])
def passwordd(tamanho):
    password = model.insert_all(tamanho)
    messagem = {'Tamanho':tamanho,
                'Senha gerada': password}
    arr['senha'] = password
    print(arr)
    return jsonify(messagem), 200

@app.route('/password/validar', methods=['POST'])

def validar():
    senha = request.json['senha']
    print(senha)
    print(arr) 
    if senha == arr['senha']:
        return jsonify({'Mensagem':'Senha válida'}), 200
    else:
        return jsonify({'Mensagem':'Senha inválida', 'Senha correta': senha, 'Senha digitada': arr}), 400


if __name__=='__main__':
    app.run(debug=True)

