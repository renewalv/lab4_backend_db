from my_project.config.db_config import get_db_connection

class CategoryDAO:
    def get_all(self):
        db = get_db_connection()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM categories")
        result = cursor.fetchall()
        db.close()
        return result

    def create(self, name):
        db = get_db_connection()
        cursor = db.cursor()
        cursor.execute("INSERT INTO categories (name) VALUES (%s)", (name,))
        db.commit()
        db.close()

    def get_products_by_category(self, category_id):
        db = get_db_connection()
        cursor = db.cursor(dictionary=True)
        query = """
            SELECT p.id, p.name, p.price, c.name as category 
            FROM products p 
            JOIN categories c ON p.category_id = c.id 
            WHERE c.id = %s
        """
        cursor.execute(query, (category_id,))
        result = cursor.fetchall()
        db.close()
        return result
    def update(self, category_id, name):
        db = get_db_connection()
        cursor = db.cursor()
        cursor.execute("UPDATE categories SET name = %s WHERE id = %s", (name, category_id))
        db.commit()
        db.close()

    def delete(self, category_id):
        db = get_db_connection()
        cursor = db.cursor()
        cursor.execute("DELETE FROM categories WHERE id = %s", (category_id,))
        db.commit()
        db.close()

    # Для зв'язку M:M (Товар -> Характеристики -> Атрибути)
    def get_product_characteristics(self, product_id):
        db = get_db_connection()
        cursor = db.cursor(dictionary=True)
        query = """
            SELECT a.name as attribute_name, pc.value as attribute_value
            FROM product_characteristics pc
            JOIN attributes a ON pc.attribute_id = a.id
            WHERE pc.product_id = %s
        """
        cursor.execute(query, (product_id,))
        result = cursor.fetchall()
        db.close()
        return result
