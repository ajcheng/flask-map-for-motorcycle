#encoding: utf-8

import os

DEBUG = True
SECRET_KEY = os.urandom(24)

HOSTNAME = '192.168.1.10'
PORT = '3306'
DATABASE = 'map'
USERNAME = 'map'
PASSWORD = 'map@!@#$%^&*(SDAFDAFGD'
DB_URI = 'mysql+mysqldb://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False


#高德地图坐标获取
#http://lbs.amap.com/console/show/picker

#高德地图点标注说明
#http://lbs.amap.com/api/javascript-api/guide/draw-on-map/marker-point

