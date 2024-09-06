from flask import request, jsonify
from models.user import User
from flask_login import login_user, logout_user, current_user, login_required
import bcrypt
from database.db import db

def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"message": "Por favor, preencha todos os campos."}), 400

    user = User.query.filter_by(username=username).first()
    if user and bcrypt.checkpw(str.encode(password), str.encode(user.password)):
        login_user(user)
        return jsonify({"message": "Autenticação realizada com sucesso!"})

    return jsonify({"message": "Credenciais inválidas"}), 400

@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logout realizado com sucesso!"})

# Funções para criação, leitura, atualização e exclusão de usuários
def create_user():
    # Lógica de criação de usuário
    pass

@login_required
def read_user(id_user):
    # Lógica de leitura de usuário
    pass

@login_required
def update_user(id_user):
    # Lógica de atualização de usuário
    pass

@login_required
def delete_user(id_user):
    # Lógica de exclusão de usuário
    pass
