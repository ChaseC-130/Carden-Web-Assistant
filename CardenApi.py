import flask 
from Commands import *
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True



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
def process_text():
    text = request.args['text'].lower()
    response = {
        'response': 'X',
        'action': 'Y'  
    }

    if 'play' in text:
        song = text.split('play', 1)[1]
        response['response'] = 'I will now play{} on YouTube.'.format(song)
        response['action'] = get_song(song)

    if 'weather' in text:
        try:
            response['response'] = get_weather(request.remote_addr)
        except KeyError:
            response['response'] = 'I was unable to find the weather based on your IP Address.'
        
    if 'hi' in text:
        response['response'] = "Hello."

    if 'how are you' in text:
        response['response'] = (" I am doing good. How are you?")

    return response


app.run()