from server import server
from flask import Flask
import webbrowser
from threading import Timer
from flask import render_template
from werkzeug.serving import run_simple

import os

if __name__=='__main__':
    backend = server()

    Timer(1, lambda: webbrowser.open_new('index.html')).start();
    backend.run(host='localhost', port=80,use_debugger=True, use_evalex=True)
    