from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)
    # 将蓝图统一注册到app上
    return app


def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web)
