# adding flask boilerplate for REST APIs
from flask import Flask, render_template, request
from datetime import datetime
import os
import sys

# define a variable to hold your app
app = Flask(__name__)

# define your resource endpoints
@app.route('/')
def index_page():
    return render_template('index.html',os_type = sys.platform,os_name = os.name)

@app.route('/time')
def get_time():
    return str(datetime.datetime.now())

# serve the app when this file is run
if __name__=='__main__':
    app.run(use_reloader=True)
    print('server running')