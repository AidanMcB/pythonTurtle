from flask import Flask 

app=Flask(__name__)

@app.route('/')
def hi():
    return "Hello World"

@app.route('/second-route')
def second():
    return "Second Function"

print(hi())
print(second()) 