from flask import Flask, jsonify, request, make_response
import db

# 初始化数据库连接
conn = db.DBHelper(host="127.0.0.1", port=3306,
                   user="root", password="123456", db="LoL")

app = Flask(__name__)


def search_heroes(keyword):
    """模糊搜索英雄"""
    results = conn.fetch_all(
        "SELECT * FROM main WHERE hero_name LIKE %s",
        (f"%{keyword}%",)
    )
    return results


@app.route("/hero_img_get", methods=["GET", "POST"])
def hero_img_get():
    # 从请求参数获取name值（不再设置默认值）
    if request.method == 'GET':
        name = request.args.get('name')
    else:  # POST
        name = request.form.get('name')

    # 检查是否传入了name参数
    if not name:
        return jsonify({
            'code': 400,
            'message': '缺少参数name',
            'data': None
        }), 400

    matches = search_heroes(name)
    print(f"搜索 '{name}' 的结果: {len(matches)}条记录")

    # 构建响应
    resp = make_response(jsonify({
        'code': 200,
        'message': 'success',
        'data': matches
    }))
    resp.headers['Content-Type'] = 'application/json'
    resp.headers['Access-Control-Allow-Origin'] = '*'

    return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)