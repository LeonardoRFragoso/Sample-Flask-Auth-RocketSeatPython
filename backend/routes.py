from flask import Blueprint
from backend.auth import login, logout, create_user, read_user, update_user, delete_user

auth_bp = Blueprint('auth_bp', __name__)

auth_bp.route('/login', methods=["POST"])(login)
auth_bp.route('/logout', methods=['GET'])(logout)
auth_bp.route('/user', methods=["POST"])(create_user)
auth_bp.route('/user/<int:id_user>', methods=["GET"])(read_user)
auth_bp.route('/user/<int:id_user>', methods=["PUT"])(update_user)
auth_bp.route('/user/<int:id_user>', methods=["DELETE"])(delete_user)
