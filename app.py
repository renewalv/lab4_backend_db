from flask import Flask
from my_project.controller.category_controller import category_bp

app = Flask(__name__)

app.register_blueprint(category_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
