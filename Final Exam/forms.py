from datetime import datetime
from flaskblog import db, login_managerr
from flask_login import UserMixin
from flask import Flask


app= Flask(__name__)
app.secret_key = 'jumpjacks'
