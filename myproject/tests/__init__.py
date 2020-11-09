from flask import Flask
from wsgiref.simple_server import make_server
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/api/v1/hello-world-19')
def start():
    return 'Hello, World 19!'

# if __name__ == '__main__':
#     app.run()

with make_server('', 5000, app) as server:
    print("That is working!!!")

    server.serve_forever()