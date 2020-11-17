import os
from datetime import datetime
from flask import Flask, render_template, request
from flask.helpers import send_from_directory

app = Flask(__name__)

f = open("ip_log.txt", "a")

@app.route('/')
def home():
  f.write(f"HOME: {request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)} \t {str(datetime.now())} \n")
  folders = os.listdir(f'{os.getcwd()}{os.sep}thumbnails')
  return render_template('home.html', folders = folders)

@app.route('/<path:folder>')
def folder(folder):
  f.write(f"PATH: {folder} \t {request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)} \t {str(datetime.now())} \n")
  if 'favicon' in str(folder):
    return ('', 204)
  files = os.listdir(f'{os.getcwd()}{os.sep}thumbnails{os.sep}{folder}')
  return render_template('images.html', folder = folder, files = files)

@app.route('/thumbnails/<path:path>')
def thumbnails(path):
  return send_from_directory('thumbnails', path)

@app.route('/download/<path:path>')
def download(path):
  f.write(f"DOWNLOAD: {path} \t {request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)} \t {str(datetime.now())} \n")
  gallery_path = ""
  return send_from_directory(gallery_path, path)