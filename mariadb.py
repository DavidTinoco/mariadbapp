import MySQLdb as mariadb
from bottle import Bottle,route,run,request,template,static_file,redirect,get,post,default_app,response,get,post

@route('/')
def connect():
    return template('inicio.tpl')

@post('/select')
def select():
    user = request.forms.get("user")
    key = request.forms.get("key")
    table = request.forms.get("table")
    try:
        connection = mariadb.connect("10.0.0.16",user,key,"practicabd")
    except mariadb.Error:
        return template('error.tpl')
    cursor = connection.cursor()
    cursor.execute("SELECT * from " + table)
    return template('select.tpl',cursor = cursor, table = table)

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')

run(host = '0.0.0.0', port = 8081)
