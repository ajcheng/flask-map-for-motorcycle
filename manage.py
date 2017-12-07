#encoding: utf-8

from flask_script import Manager
from flask_migrate import  Migrate,MigrateCommand
from run import app
from exts import db
from models import User,Comment,Mapinfo

manager = Manager(app)

#使用migrate绑定app和db
migrate = Migrate(app,db)

#添加迁移脚本的命令到manager中
manager.add_command('db',MigrateCommand)


if __name__ == "__main__":
    manager.run()

#数据库初始化操作
#python manage.py db init
#python manage.py db upgrade
#python manage.py db migrate
#  Generating /home/aj/PycharmProjects/map/migrations/versions/3cf5230ae414_.py ... done
#cd migrations/versions/
#python 3cf5230ae414_.py