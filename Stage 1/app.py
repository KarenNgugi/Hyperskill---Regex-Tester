from flask import Flask
import sys
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

# write your code here
db = SQLAlchemy(app)
Base = declarative_base()


class Record(Base):
    __tablename__ = "record"

    id = Column('id', Integer, primary_key=True)
    regex = Column('regex', String(50))
    text = Column('text', String(1024))
    result = Column('result', Boolean)


# don't change the following way to run flask:
if __name__ == '__main__':
    if len(sys.argv) > 1:
        arg_host, arg_port = sys.argv[1].split(':')
        app.run(host=arg_host, port=arg_port)
    else:
        app.run()
