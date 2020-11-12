import os

from flask import Flask, render_template

app = Flask(__name__)

import os

@app.route('/')
def home():
  folders = os.listdir(f'{os.getcwd()}{os.sep}thumbnails')
  return render_template('home.html', folders = folders)