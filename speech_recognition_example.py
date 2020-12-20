import speech_recognition as sr

recognizer = sr.Recognizer()
recognizer.energy_threshold = 300

mic = sr.Microphone(device_index= 6)

print(mic)
with mic as source:
    print('Say a number')
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)

output = recognizer.recognize_google(audio,language='es-CO')
print("What you said was: ")
print(output)

if 'dos' in output:
    output = 2

if int(output) %2 == 0:
    print('the number: '+str(output) +" is even")
else:
    print('the number: '+output +" is odd")
