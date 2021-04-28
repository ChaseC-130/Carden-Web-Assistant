import speech_recognition as sr
import subprocess, sys, time
import threading
from Commands import *



def google_speech(recognizer, microphone) -> dict:
    # adjust the recognizer sensitivity to ambient noise and record audio from the microphone
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source, duration = 0.5)
        recognizer.energy_threshold = 150
        audio = recognizer.listen(source)

    # try recognizing the speech in the recording if a RequestError or UnknownValueError exception is caught, update the response object accordingly
    try:
        response = recognizer.recognize_google(audio)
    except UnknownValueError:
        response = "I didn't get that."

    return response


# phrases used to initiliaze Carden's listening
my_name = ['carl', 'carlin', 'garden', 'carden', 'car then', 'car den', 'carmen', 'carlin', 'pardon', 'cotton', 'are they', 'foreign']
recognizer = sr.Recognizer()
microphone = sr.Microphone()

phrases = {'hello': 'Hi Human',
            'weather': get_weather()}



def wait():
    # Listening for google speech
    print("Listening for google")
    response = google_speech(recognizer, microphone)
    pattern = response
    
    if (pattern in phrases):
        say = phrases.get(pattern)
    else:
        say = pattern


    if (say[0:4] == 'play'):
        song = say[5:]
        play_song(song)
    else:
        if (say in dir()):
            say = eval(say)
        get_response(say)
        play_file()
        if (say == "I didn't get that."):
            wait()


    
