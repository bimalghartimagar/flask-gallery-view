import os
from datetime import datetime
from configparser import ConfigParser

from flask import Flask, render_template, request, Response, stream_with_context
from flask.helpers import send_from_directory

import conf

app = Flask(__name__)

config = ConfigParser()
config.read_dict(conf.cfg)
  
app.config['gallery_path'] = config.get('gallery_view', 'original_path')

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
  return send_from_directory(app.config['gallery_path'] , path)
