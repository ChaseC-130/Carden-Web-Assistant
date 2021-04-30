import flask 
from Commands import *
from flask import request, jsonify
from flask_cors import CORS, cross_origin

app = flask.Flask(__name__)



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
    response = process_text(request)
    response.headers.add('Content-Type', 'application/json')
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Methods', 'PUT, GET, POST, DELETE, OPTIONS')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Expose-Headers', 'Content-Type,Content-Length,Authorization,X-Pagination')
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)