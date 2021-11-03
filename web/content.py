from flask import render_template
import json

# Page Content
prefix = "Ashwin Charathsandran — "

# Meta Tags
preview_message = ""
preview_title = ""
preview_image = ""

with open('web/projects.json', 'r') as file:
    projects = json.load(file)

def index_page():
    return render_template('index.html',
    title = prefix + "Welcome!",
    sample_projects = projects[0:2],
    preview_title = preview_title,
    preview_image = preview_image,
    preview_message = preview_message)

def projects_page():
    return render_template('projects.html',
    title = prefix + "Projects",
    items = projects,
    preview_title = preview_title,
    preview_image = preview_image,
    preview_message = preview_message)


def file_page():
    return render_template('files.html',
    title = prefix + "Files",
    )