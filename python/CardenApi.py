import flask 
from Commands import *
from flask import request, jsonify, Flask

app = Flask(__name__)

# Route that returns youtube music video link 
@app.route('/api/v1/music', methods=['GET'])
def music_api():
    if 'song' in request.args:
        link = get_song(request.args['song'])
    else:
        return "Please provide a proper request"

    return link

# Process Text
@app.route('/api/v1/process', methods=['GET'])
def receive():
    return process_text(request)

if __name__ == '__main__':
    app.run()