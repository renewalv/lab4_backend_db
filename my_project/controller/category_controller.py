from flask import Blueprint, request, jsonify
from my_project.service.category_service import CategoryService

category_bp = Blueprint('category', __name__)
service = CategoryService()

@category_bp.route('/categories', methods=['GET'])
def get_categories():
    return jsonify(service.get_all_categories()), 200

@category_bp.route('/categories', methods=['POST'])
def create_category():
    data = request.get_json()
    service.create_category(data['name'])
    return jsonify({"message": "Category created successfully"}), 201

@category_bp.route('/categories/<int:id>/products', methods=['GET'])
def get_products(id):
    return jsonify(service.get_category_products(id)), 200

# Обновлення даних у таблицях (PUT)
@category_bp.route('/categories/<int:id>', methods=['PUT'])
def update_category(id):
    data = request.get_json()
    service.update_category(id, data['name'])
    return jsonify({"message": "Category updated successfully"}), 200

# Видалення даних з таблиці (DELETE)
@category_bp.route('/categories/<int:id>', methods=['DELETE'])
def delete_category(id):
    service.delete_category(id)
    return jsonify({"message": "Category deleted successfully"}), 200

# Вивід даних зі стикувальної таблиці зв'язку M:M
@category_bp.route('/products/<int:id>/characteristics', methods=['GET'])
def get_product_characteristics(id):
    return jsonify(service.get_product_characteristics(id)), 200