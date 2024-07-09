from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', name='Steve')

@app.route('/<name>')
def named(name):
    return render_template('index.html', name=name)

''' This is the more common notation, but doesn't work in this instance... 
@app.route('<path:name>')
def named(name):
	render_template('index.html', name=name)
'''

if __name__ == '__main__':
    app.run(debug=True)
