import speech_recognition as sr

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
    return recognizer.recognize_google(audio)
