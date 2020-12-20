import speech_recognition as sr
from scripts.speaker import speaker
recognizer = sr.Recognizer()
recognizer.energy_threshold = 300

mic = sr.Microphone(device_index= 6)

def listen():
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    return audio

def understand():
    audio = listen();
    #return recognizer.recognize_google(audio,language='es-CO')
    understanding = ''
    try:
        understanding = recognizer.recognize_google(audio)
    except sr.UnknownValueError as e:
        speaker.speak('I did not understand what you said')
    return understanding
