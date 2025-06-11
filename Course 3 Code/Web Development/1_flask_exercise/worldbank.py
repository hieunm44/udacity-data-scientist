from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/project-one')
def project_one():
    return render_template('project_one.html')

# new route
@app.route('/new-route')
def new_route():
    return render_template('new_route.html')

app.run(host='0.0.0.0', port=3000, debug=True)