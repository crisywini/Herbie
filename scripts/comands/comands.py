from scripts.speaker import speaker
import os
from tkinter import Tk, simpledialog,  messagebox

def answer_greeting(greet):
    if 'you' in greet:
        speaker.speak('I am doing a good job Sir, thanks for asking')
        speaker.speak('What would you like to know')
    elif 'good' in greet:
        speaker.speak('That is really great Sir, I hope you have a good day')
        speaker.speak('What do u need right now?')
    elif 'bad' in greet or 'ok' in greet:
        speaker.speak('I hope everything is great Sir')
        speaker.speak('What do u need right now?')
    elif not greet:
        speaker.speak('Sorry that I have to ask you again, but I did not hear you')

def search_files_in_data():
    files = os.listdir('././data')
    if len(files) == 0:
        speaker.speak('There are no files Sir')
    for file in files:
        speaker.speak(file)
    else:
        speaker.speak('There are no more files sir')

def create_file(name):
    file = open('././data/'+name, 'w+')
    file.close()
    speaker.speak('File '+name+' created in the data directory')
