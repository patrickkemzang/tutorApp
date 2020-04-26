import os
# csv (comma separated values) file
import csv

from flask import Flask, render_template, request, session
from flask_session import Session

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# creating a session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route('/', methods=[])
def index:
	pass

@app.route('/signup', methods=[])
def signup:
	pass

@app.route('/login', methods = [])
def login:
	pass




def main():
	pass


if __name__ == '__main__':
	main()