from server import server
import webbrowser
from threading import Timer

import os

if __name__=='__main__':
    backend = server()

    Timer(1, lambda: webbrowser.open_new('index.html')).start();
    backend.run(host='localhost', port=80,use_debugger=True, use_evalex=True)
    