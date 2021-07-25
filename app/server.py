from flask import render_template, Flask
from pathlib import Path
import logging, json, requests


app = Flask(__name__)

PROJECTS = Path('./projects')
# CONFIG = Path('config.json')

#Functions
def read_md(file):
    file_path = PROJECTS/file
    f = open(str(file_path), 'r')
    return f.read()

def create_md():
    pass

#Routes
@app.route('/<string:project>')
def project(project):
    url = "https://api.github.com/markdown"
    dict_data =  {"text":read_md(project)}
    json_data = json.dumps(dict_data)
    req = requests.post(url, data=json_data)
    output = req.content.decode('utf-8')
    print(type(output))
    return render_template('index.html', html=output, md=read_md(project).strip())


@app.route('/editor')
def edit():
    pass

@app.route('/about')
def about():
    pass

@app.route('/manual')
def manual():
    pass

@app.route('/settings')
def settings():
    pass

@app.route('/share')
def share():
    pass




if __name__ == "__main__":
    app.run(debug=True)
