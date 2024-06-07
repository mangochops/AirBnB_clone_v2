import os
import shutil
import uuid
from flask import Flask, render_template

@app.route('/1-hbnb/')
def display_hbnb():
    cache_id = uuid.uuid4()
    return render_template('1-hbnb.html', cache_id=cache_id)

# Directories and file paths
src_static = 'web_flask/static'
src_html = 'web_flask/templates/100-hbnb.html'
src_init = 'web_flask/__init__.py'
src_py = 'web_flask/100-hbnb.py'

dst_static = 'web_dynamic/static'
dst_html = 'web_dynamic/templates/0-hbnb.html'
dst_init = 'web_dynamic/__init__.py'
dst_py = 'web_dynamic/0-hbnb.py'

# Ensure destination directories exist
os.makedirs(os.path.dirname(dst_static), exist_ok=True)
os.makedirs(os.path.dirname(dst_html), exist_ok=True)
os.makedirs(os.path.dirname(dst_py), exist_ok=True)

# Copy files
shutil.copytree(src_static, dst_static, dirs_exist_ok=True)
shutil.copy(src_init, dst_init)

# Use 8-hbnb.html if 100-hbnb.html is not present
if not os.path.isfile(src_html):
    src_html = 'web_flask/templates/8-hbnb.html'

shutil.copy(src_html, dst_html)
shutil.copy(src_py, dst_py)

# Flask application
app = Flask(__name__)

@app.route('/0-hbnb/')
def display_hbnb():
    cache_id = uuid.uuid4()
    return render_template('0-hbnb.html', cache_id=cache_id)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

