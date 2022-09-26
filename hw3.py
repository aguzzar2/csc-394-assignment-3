from flask import Flask,render_template

app= Flask(__name__)
@app.route('/hw3')

def main():
    return render_template('index.html')