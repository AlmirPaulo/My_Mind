from flask import render_template, Flask
from pathlib import Path
import logging, requests


app = Flask(__name__)

PROJECTS = Path('projects')
# CONFIG = Path('config.json')

@app.route('/')
def project():
    url = "https://api.github.com/markdown"
    req = requests.post(url, data='') 
    return render_template('index.html', data=req.content)

if __name__ == "__main__":
    app.run(debug=True)
