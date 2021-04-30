import flask 
from Commands import *
from flask import request, jsonify
from flask_cors import CORS, cross_origin

app = flask.Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app, resources={r"/*": {"origins": "*"}})

# Route that returns weather for passed IP address
@app.route('/api/v1/weather', methods=['GET'])
def weather_api():
    if 'ip' in request.args:
        weather = get_weather(request.args['ip'])
    else:
        return "Please provide a proper request"

    return weather


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
    app.run(host='0.0.0.0', port=8000)