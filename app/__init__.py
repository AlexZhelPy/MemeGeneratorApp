from flask import Flask

def create_app():
    """
    Создает и возвращает экземпляр Flask-приложения.
    """
    app = Flask(__name__)
    from .routes import bp as main_routes
    app.register_blueprint(main_routes)
    return app
