from flask import render_template
import json

# Page Content
prefix = "Ashwin Charathsandran — "

# Meta Tags
preview_message = "Expressing my undying passion for technology by researching, designing, and creating applications that solve problems."
preview_title = prefix + "Student & Developer"
preview_image = "/static/me.jpg"

technologies = {
    "Python",
    "Flask",
    "Java",
    "jQuery",
    "UIKit",
    "Python",
    "HTML",
    "CSS",
    "Javascript",
    "PHP",
    "MustacheJS",
    "Git Bash",
    "Linux CLI",
    "Google Colab",
    "Google Workspace",
    "PostgresSQL"
}

with open('web/projects.json', 'r') as file:
    projects = json.load(file)

def index_page():
    return render_template('index.html',
    title = prefix + "Welcome!",
    sample_projects = projects[0:3],
    technologies = technologies,
    preview_title = preview_title,
    preview_image = preview_image,
    preview_message = preview_message)

def projects_page():
    return render_template('projects.html',
    title = prefix + "Projects",
    projects = projects,
    preview_title = preview_title,
    preview_image = preview_image,
    preview_message = preview_message)

def about_page():
    return render_template('about.html',
    title = prefix + "Ashwin, Who?",
    preview_title = preview_title,
    preview_image = preview_image,
    preview_message = preview_message)

def get_project_page(project_name):
    return render_template('project_page.html',
    title = prefix + project_name.upper(),
    # code below from https://stackoverflow.com/a/64013749
    project = [x for x in projects if x["id"]==project_name],
    preview_title = preview_title,
    preview_image = preview_image,
    preview_message = preview_message)
    