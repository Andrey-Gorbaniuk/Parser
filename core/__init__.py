from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import fake_useragent
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

conn_url = 'postgresql+psycopg2://yourUserDBName:yourUserDBPassword@yourDBDockerContainerName/yourDBName'
engine = create_engine(conn_url)
db_s = scoped_session(sessionmaker(bind=engine))
app = Flask(__name__)
app.secret_key = '*8+nb7,^&'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///web-site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ua = fake_useragent.UserAgent()

from core import models, routes