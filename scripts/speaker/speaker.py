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
def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('voice', 'english')
    engine.say(text)
    engine.runAndWait()
