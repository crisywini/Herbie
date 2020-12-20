import pyttsx3

'''
voices = engine.getProperty('voices')
for voice in voices:
    print('Voice:')
    print(f" - ID: %s" % voice.id)
    print(f" - Name: %s" % voice.name)
    print(" - Languages: ",voice.languages)
    print(f" - Gender: %s" % voice.gender)
    print(f" - Age: %s" % voice.age)
'''
engine = pyttsx3.init()
def speak(text):
    engine.setProperty('voice', 'english')
    engine.say(text)
    engine.runAndWait()

def greet():
    speak('Hi sir, how r u?')
