from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def landing():
    return render_template('landing.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 5000))
