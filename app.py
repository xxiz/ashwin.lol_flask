from flask import Flask, request
from web.content import index_page, projects_page, about_page, get_project_page
web = Flask(__name__)
web.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@web.route('/')
def index():
    return index_page()

@web.route('/projects')
def projects():
    return projects_page()

@web.route('/projects/<string:project_name>', methods=['GET'])
def get_project(project_name):
    return get_project_page(project_name)

@web.route('/about')
def about():
    return about_page()
