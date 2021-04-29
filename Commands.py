import geocoder, requests, json
from youtube_search import YoutubeSearch


def get_song(song):
    result = json.loads(YoutubeSearch(song, max_results=1).to_json())
    url = 'https://www.youtube.com' + result['videos'][0]['url_suffix']
    return url


def get_weather(ip): 
    g = geocoder.ip(ip)
    lat = g.lat
    long = g.lng
    url = requests.get(f'https://api.weather.gov/points/{lat},{long}').json()["properties"]["forecast"]
    return requests.get(url).json()["properties"]["periods"][0]["detailedForecast"]
    

def get_response(text):
    if 'hi' in text:
        response = "Hello. How are you?"