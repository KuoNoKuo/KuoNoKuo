from flask import *
app = Flask(__name__)
@app.route('/')
def page1():
    return 'Hello World!'
if __name__=='__main__':
    app.run()
