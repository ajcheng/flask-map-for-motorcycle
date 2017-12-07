#encoding: utf-8

from flask import Flask,render_template,request,redirect,url_for,session
import config
from models import User,Mapinfo,Comment
from exts import db
from decorators import login_required
from sqlalchemy import or_

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/list.js')
def list():
    context = {
        'mapinfos':Mapinfo.query.all()
    }
    return render_template('list.html',**context)

@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter(User.username == username).first()
        if user and user.check_passwd(password):
            session['user_id'] = user.id
            session.permanent = True
            return redirect(url_for('index'))
        else:
            return u'用户名密码错误，请重新输入'

@app.route('/regist/',methods=['GET','POST'])
def regist():
    if request.method == 'GET':
        return render_template('regist.html')
    else:
        tel = request.form.get('tel')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        #用户名验证
        user = User.query.filter(User.username == username).first()
        if user:
            return u'用户名已存在'
        else:
            #passwd判断
            if password1 != password2:
                return u'两次密码输入有误'
            else:
                user = User(tel=tel,username=username,password=password1)
                db.session.add(user)
                db.session.commit()
                print "注册成功"
                return redirect(url_for('login'))

@app.route('/logout/')
def logout():
    session.pop('user_id')
    return redirect(url_for('index'))

@app.route('/add/',methods=['GET','POST'])
@login_required
def add_map():


    if request.method == 'GET':
        return render_template('map_add.html')
    else:
        position = request.form.get('position')
        content = request.form.get('content')
        mapinfo = Mapinfo(position=position,content=content)
        user_id = session.get('user_id')
        user = User.query.filter(User.id == user_id).first()
        mapinfo.author = user
        db.session.add(mapinfo)
        db.session.commit()
        return redirect(url_for('index'))


@app.route('/user/<user_id>/')
@login_required
def user(user_id):
    user_id = session.get('user_id')
    mapinfos = Mapinfo.query.filter(Mapinfo.author_id == user_id)
    return render_template('user.html', mapinfos=mapinfos)



@app.context_processor
def my_context_processor():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter(User.id == user_id).first()
        if user:
            return {'user':user}
    return {}

if __name__ == '__main__':
    app.run()