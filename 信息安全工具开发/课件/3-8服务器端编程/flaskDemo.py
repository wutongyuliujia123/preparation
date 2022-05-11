from flask import Flask, url_for

#简单的Web路由示例
# app = Flask(__name__)
# @app.route('/')
# def index():
#     return 'Index Page'
# @app.route('/hello')
# def hello():
#     return 'Hello World!'
# if __name__ == "__main__":
#     app.run()
#URL装饰器，参数传递
app = Flask(__name__)
@app.route('/user/<username>')#传递字符串型参数
def show_user_profile(username):
    return 'User %s' % username
# @app.route('/post/<int:post_id>')#传递整形参数
# def show_post(post_id):
#     return 'Post %d' % post_id
# #URL前缀相同，可改变后面传入的参数类型，调用不同的路由响应，类似于面向对象的重载
# @app.route('/post/<float:post_float>')#传递浮点型参数
# def show_post_float(post_float):
#     return 'Post folat %f' % post_float
# # if __name__ == "__main__":
# #     app.run()
#
# @app.route('/projects/')
# def projects():
#     return 'The project page'
# @app.route('/about')
# def about():
#     return 'The about page'
# if __name__ == "__main__":
#     app.run()
app = Flask(__name__)
@app.route('/')
def index():
    pass
@app.route('/login')
def login():
    pass
@app.route('/user/<username>')
def profile(username):
    pass
with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login',next = 'bbn',to = 'anb'))
    print(url_for('profile',username='John Boe'))
