from flask import Flask
app=Flask(__name__)
@app.route('/')
def route():
    return 'cicd endterm!'
app.run(host='0.0.0.0',port=5000)  