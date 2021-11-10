from flask import render_template
import json

# Page Content
prefix = "Ashwin Charathsandran — "

# Meta Tags
preview_message = ""
preview_title = ""
preview_image = ""

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

def file_page():
    return render_template('files.html',
    title = prefix + "Files",
    )