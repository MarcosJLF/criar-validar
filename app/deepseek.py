from flask import Flask, jsonify, request
import model
import secrets
import string

app = Flask(__name__)

# Dicionário para armazenar senhas temporariamente (em um ambiente real, use um banco de dados)
passwords = {}

def generate_password(length):
    """Gera uma senha aleatória segura."""
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))

@app.route('/password', methods=['GET'])
def generate_default_password():
    """Gera uma senha com o tamanho padrão de 10 caracteres."""
    password = generate_password(10)
    passwords['last_generated'] = password
    return jsonify({'Tamanho': 10, 'Senha gerada': password}), 200

@app.route('/password/<int:length>', methods=['GET'])
def generate_custom_password(length):
    """Gera uma senha com o tamanho especificado."""
    if length < 8:
        return jsonify({'Erro': 'O tamanho da senha deve ser pelo menos 8 caracteres'}), 400
    
    password = generate_password(length)
    passwords['last_generated'] = password
    return jsonify({'Tamanho': length, 'Senha gerada': password}), 200

@app.route('/password/validar', methods=['POST'])
def validate_password():
    """Valida a senha enviada pelo usuário."""
    if 'senha' not in request.json:
        return jsonify({'Erro': 'Campo "senha" não encontrado no JSON'}), 400
    
    user_password = request.json['senha']
    last_generated_password = passwords.get('last_generated')
    
    if not last_generated_password:
        return jsonify({'Erro': 'Nenhuma senha foi gerada recentemente'}), 400
    
    if user_password == last_generated_password:
        return jsonify({'Mensagem': 'Senha válida'}), 200
    else:
        return jsonify({'Mensagem': 'Senha inválida', 'Senha correta': last_generated_password, 'Senha digitada': user_password}), 400

if __name__ == '__main__':
    app.run(debug=True)