from flask import Flask, render_template, send_file

app=Flask(__name__)

@app.route('/')
def hello_world():
    #return send_file('../1/index.html')
    return render_template('index.html')

app.run(host='localhost', port=5000)