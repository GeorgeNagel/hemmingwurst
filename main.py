import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/')
def root():
    return render_template('root.html')

if __name__ == "__main__":
    app.run()
