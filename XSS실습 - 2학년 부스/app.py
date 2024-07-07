from flask import Flask, render_template, request, redirect, url_for, make_response

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# 사용자 정보를 간단한 딕셔너리로 저장 (실제로는 데이터베이스 사용 권장)
users = {
    'user1': 'password1',
    'user2': 'password2'
}

# 간단한 메모리 내 데이터베이스로 사용할 리스트
posts = []

@app.route('/')
def index():
    return render_template('index.html', posts=posts)

@app.route('/post/<int:post_id>')
def post(post_id):
    post = posts[post_id]
    return render_template('post.html', post=post)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.cookies.get('username') is None:
        return redirect(url_for('login'))

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        if title and content:
            # 새로운 글을 리스트에 추가
            posts.append({'title': title, 'content': content})
            return redirect(url_for('index'))
    return render_template('create.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            response = make_response(redirect(url_for('index')))
            response.set_cookie('username', username)
            response.set_cookie('password', password)
            return response
        else:
            return render_template('login.html', error='Invalid username or password')
    return render_template('login.html')

@app.route('/logout')
def logout():
    response = make_response(redirect(url_for('index')))
    response.set_cookie('username', '', expires=0)
    return response

if __name__ == '__main__':
    app.run(debug=True)
