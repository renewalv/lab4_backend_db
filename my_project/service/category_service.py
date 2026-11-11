from my_project.dao.category_dao import CategoryDAO
from my_project.domain.category import CategoryDTO

class CategoryService:
    def __init__(self):
        self.dao = CategoryDAO()

    def get_all_categories(self):
        data = self.dao.get_all()
        return [CategoryDTO(**row).model_dump() for row in data]

    def create_category(self, name):
        self.dao.create(name)

    def get_category_products(self, category_id):
        return self.dao.get_products_by_category(category_id)
    def update_category(self, category_id, name):
        self.dao.update(category_id, name)

    def delete_category(self, category_id):
        self.dao.delete(category_id)

    def get_product_characteristics(self, product_id):
        return self.dao.get_product_characteristics(product_id)
