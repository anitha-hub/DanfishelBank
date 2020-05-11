from flask import Flask
from flask_mongoengine import MongoEngine
from mongoengine import connect
from mongoengine.connection import disconnect

app = Flask(__name__)
app.config['MONGODB_DB'] = 'employee_service'
app.config['SECRET_KEY'] = 'Th1s1ss3cr3t'
db = MongoEngine(app)
connect('db', host='localhost', port=27017, alias='employeeservicedb')
disconnect(alias='employeeservicedb')