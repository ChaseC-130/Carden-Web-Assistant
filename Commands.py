import geocoder, requests, json
from youtubesearchpython import VideosSearch

def process_text(request):
    text = request.args['speech'].lower()
    #print(text)
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
            response['response'] = get_weather(text)
        except KeyError:
            response['response'] = 'I was unable to find the weather.'
        
    if 'hi' in text:
        response['response'] = "Hello."

    if 'how are you' in text:
        response['response'] = (" I am doing good. How are you?")

    return response



def get_song(song):
    result = VideosSearch(song, limit = 1).result()
    #print(result)
    #return result
    try:
        url = result['result'][0]['id']
    except IndexError:
        return "Error"
    return "https://www.youtube.com/embed/" + url + "?autoplay=1"

def get_weather(location): 
    g = geocoder.google(location)
    lat = g.lat
    long = g.lng
    url = requests.get(f'https://api.weather.gov/points/{lat},{long}').json()["properties"]["forecast"]
    return requests.get(url).json()["properties"]["periods"][0]["detailedForecast"]
    

def get_response(text):
    if 'hi' in text:
        response = "Hello. How are you?"