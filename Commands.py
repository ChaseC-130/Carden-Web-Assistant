import geocoder, requests, json, random
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

    if 'weather in' in text:
        try:
            response['response'] = get_weather(text.split('weather in', 1)[1])
        except KeyError:
            response['response'] = 'I was unable to find the weather.'

    if 'shuffle' in text:
        song = text.split('shuffle', 1)[1]
        response['reponse'] = 'I will shuffle 10 results regarding {}'.format(song)
        response['action'] = shuffle(song)

#    if 'hi' in text:
 #       response['response'] = "Hello."

    if 'how are you' in text:
        response['response'] = "I am doing good. How are you?"

    if "what's your name" in text or "who are you" in text:
        response['response'] = "My name is Cardena"

    if response['response'] == 'X':
        response['response'] = "Searching google for {}".format(text)
        response['action'] = requests.get("https://www.google.com/search?q=" + text).url

    return response



def get_song(song):
    result = VideosSearch(song, limit = 100).result()
    #print(result)
    #return result
    try:
        url = result['result'][0]['id']
    except IndexError:
        return "Error"
    return "https://www.youtube.com/embed/" + url + "?autoplay=1"

def get_weather(location):
    g = geocoder.osm(location)
    lat = g.lat
    long = g.lng
    url = requests.get(f'https://api.weather.gov/points/{lat},{long}').json()["properties"]["forecast"]
    return requests.get(url).json()["properties"]["periods"][0]["detailedForecast"]
    

def shuffle(song):
    result = VideosSearch(song, limit = 100).result()
    #print(result)
    #return result
    url = "https://www.youtube.com/watch_videos?video_ids="
    count = 0
    nums = random.sample(range(10), 10)
    try:
        while(count < 10):
            url += result['result'][nums[count]]['id'] + ','
            count += 1
    except IndexError:
        return "Error"
    return requests.get(url).url.replace("watch", "embed")



def get_response(text):
    if 'hi' in text:
        response = "Hello. How are you?"