from pathlib import Path


PROJECTS = Path('./projects')
# CONFIG = Path('config.json')

def read_md(file):
    file_path = PROJECTS/file
    f = open(str(file_path), 'r')
    return f.read().strip()

def create_md(file):
    file_path = PROJECTS/file
    f = open(str(file_path), 'w')
    return f.write(f'# {file}')

def update_md(file, text):
    file_path = PROJECTS/file
    f = open(str(file_path), 'w')
    return f.write(text)

def delete_md():
    pass
