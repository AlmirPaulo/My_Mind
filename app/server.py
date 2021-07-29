from flask import render_template, Flask, request, redirect, url_for
from .crud import read_md, create_md, update_md, Path, delete_md
import logging, json, requests

app = Flask(__name__)

url = "https://api.github.com/markdown"

#Routes
@app.route('/project/<string:project>', methods=['GET', 'POST'])
def project(project):
    if request.method == 'POST':
        text = request.form.get('editor')
        update_md(project, text)
            
    title = project
    dict_data =  {"text":read_md(project)}
    json_data = json.dumps(dict_data)
    req = requests.post(url, data=json_data)
    output = req.content.decode('utf-8')
    if output.strip() == '':
        delete_md(project)
        return render_template('error.html', title=title , warn='This Project was deleted!')
    return render_template('project.html', title=title, html=output, md=read_md(project))

@app.route('/find')
def find():
    search = request.url   
    parse = search.split('=')
    if parse[1] == '':
        err = '<h1>You should  type  something...</h1>'
        return err
    elif Path(f'./projects/{parse[1]}').is_file() == False:
        create_md(parse[1])
        return redirect(url_for('project', project=parse[1]))

@app.route('/')
def home():
    files = Path('./projects')
    output = []
    for file in files.glob('*'):
        output.append(file.name)
        if file.name == 'default':
            output.pop()
    return render_template('welcome.html', projects=output)

@app.route('/guide')
def guide():
    dict_data =  {"text":read_md('default/guide.md')}
    json_data = json.dumps(dict_data)
    req = requests.post(url, data=json_data)
    output = req.content.decode('utf-8')

    return render_template('guide.html', guide=output)

@app.route('/settings')
def settings():
    pass

@app.route('/share')
def share():
    pass

