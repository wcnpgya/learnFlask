from flask import Flask, render_template, request, redirect

#实例化Flask对象
app = Flask(__name__)
app.debug = True
USERS = {
    1:{'name' : '詹桂坤', 'age' : 18,'gender' : '男', 'text' : '【相互宝上线新互助计划，这次面向慢病人群！】刚刚，相互宝宣'},
    2:{'name' : '王健林', 'age' : 55,'gender' : '男', 'text' : '支持拥护党和国家的方针政策，支持新婚姻法，'},
    3:{'name' : '李元芳', 'age' : 20,'gender' : '女', 'text' : '#吃不到新鲜竹子旅加大熊猫将提前归国##四川再次拍摄到野生大熊猫#最近国宝大熊猫有点火'}
}
@app.route('/detail/<int:nid>', methods=['GET'])
def detail(nid):
    info = USERS.get(nid)
    return render_template('detail.html', info=info)


@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html', user_dict=USERS)


@app.route('/login', methods=['GET', 'POST'])
def login():
    user = {'nickname': 'MIKE'}
    if request.method == "GET":
        return render_template("login.html", title='login', user=user)
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        if username == 'alex' and password == '123':
            return redirect('http://www.luffycity.com')
        return render_template("login.html", title='login', user=user, error='用户名或密码错误')


if  __name__ == '__main__':
    app.run()