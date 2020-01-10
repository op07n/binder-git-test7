from subprocess import Popen
import os

def load_jupyter_server_extension(nbapp):
    """serve the streamlit app"""
    os.chdir('rhyme-with-ai/app/')
    Popen(["PYTHONPATH=$PYTHONPATH:/home/jovyan/rhyme-with-ai/src/rhyme_with_ai/\ streamlit", "run", "app.py", "--browser.serverAddress=0.0.0.0", "--server.enableCORS=False"])
