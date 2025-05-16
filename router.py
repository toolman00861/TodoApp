from flask import Blueprint, request, jsonify, abort
from db import db
from models import Todo

bp = Blueprint("bp", __name__)


@bp.route("/")
def index():
    return "Hello Flex!"

# 新建
@bp.route("/todos", methods=["POST"])
def create_todo():
    data = request.get_json(force=True)
    if not data.get("title"):
        abort(400, "title is required")
    todo = Todo(title=data["title"])
    db.session.add(todo)
    db.session.commit()
    return jsonify({"id": todo.id, "title": todo.title, "completed": todo.completed}), 201


# 查询全部
@bp.route("/todos", methods=["GET"])
def list_todos():
    todos = Todo.query.order_by(Todo.id.desc()).all()
    return jsonify([{"id": t.id, "title": t.title, "completed": t.completed} for t in todos])


# 更新
@bp.route("/todos/<int:todo_id>", methods=["PUT"])
def update_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    data = request.get_json(force=True)
    todo.title = data.get("title", todo.title)
    todo.completed = data.get("completed", todo.completed)
    db.session.commit()
    return jsonify({"message": "updated"})


# 删除
@bp.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return jsonify({"message": "deleted"})
