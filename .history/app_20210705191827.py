from flask import Flask, request

web = Flask(__name__)
web.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@api.route('/')