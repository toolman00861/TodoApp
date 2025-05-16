from flask import Flask
from db import init_db
from router import bp

app = Flask(__name__)
init_db(app)                 # 配置并建立数据库
app.register_blueprint(bp)   # 挂载所有 /todos 路由

if __name__ == "__main__":
    app.run(debug=True)
