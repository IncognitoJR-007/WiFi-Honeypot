from flask import Flask, render_template
from database import fetch_logs

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/logs')
def logs():
    logs = fetch_logs()
    return render_template('logs.html', logs=logs)

if __name__ == '__main__':
    app.run(debug=True)
