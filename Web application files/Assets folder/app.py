from flask import Flask, render_template

app = Flask(__name__)

# Define routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sheets')
def sheets():
    return render_template('sheets.html')

@app.route('/dashboards')
def dashboards():
    return render_template('dashboards.html')

@app.route('/stories')
def stories():
    return render_template('stories.html')

if __name__ == '__main__':
    app.run(debug=True)
