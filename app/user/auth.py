from flask import abort, jsonify

from . import user


@user.route('/', methods=['GET'])
@user.route('/login', methods=['POST'])
def login():
    # abort(404)
    return jsonify({"title": "登入成功"})


@user.errorhandler(404)
def page_not_found(e):
    return jsonify({"title": "登入失败"}), 404
