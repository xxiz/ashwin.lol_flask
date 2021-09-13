from flask import Flask, request
from web.content import index_page
web = Flask(__name__)
web.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@web.route('/')
def index():
    return index_page()