from flask import *
app = Flask(__name__)
@app.route('/')
def page1():
    return 'hello world'

app.run()