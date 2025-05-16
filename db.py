from flask_sqlalchemy import SQLAlchemy
from flask import Flask

# 创建统一的 SQLAlchemy 实例（全局只需要一个）
db = SQLAlchemy()

def init_db(app: Flask):
    """把数据库实例挂到 app 上"""
    app.config['SQLALCHEMY_DATABASE_URI'] = (
        "mysql+pymysql://root:123456@127.0.0.1/tododb"
    )
    # 关闭 SQLAlchemy 的对象修改跟踪功能，减少内存开销（通常在生产环境中关闭）
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    with app.app_context():
        db.create_all()          # 第一次运行自动建表（轻量开发做法）
