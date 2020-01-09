from subprocess import Popen
import os
import sys

def load_jupyter_server_extension(nbapp):
    """serve the streamlit app"""
    os.chdir('rhyme-with-ai/app/')
    sys.path.insert(0, "rhyme-with-ai/src/rhyme_with_ai")
    Popen(["streamlit", "run", "app.py", "--browser.serverAddress=0.0.0.0", "--server.enableCORS=False"])
