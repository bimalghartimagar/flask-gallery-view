import os

from flask import Flask, render_template
from flask.helpers import send_from_directory

app = Flask(__name__)

import os

@app.route('/')
def home():
  folders = os.listdir(f'{os.getcwd()}{os.sep}thumbnails')
  return render_template('home.html', folders = folders)

@app.route('/<path:folder>')
def folder(folder):
  files = os.listdir(f'{os.getcwd()}{os.sep}thumbnails{os.sep}{folder}')
  return render_template('images.html', folder = folder, files = files)

@app.route('/thumbnails/<path:path>')
def thumbnails(path):
  return send_from_directory('thumbnails', path)

@app.route('/download/<path:path>')
def download(path):
  gallery_path = ""
  return send_from_directory(gallery_path, path)