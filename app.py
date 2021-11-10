from flask import Flask, request
from web.content import index_page, projects_page, about_page
web = Flask(__name__)
web.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@web.route('/')
def index():
    return index_page()

@web.route('/projects')
def projects():
    return projects_page()

@web.route('/about')
def about():
    return about_page()
# @web.route('/files')
# def files():
#     return file_page()