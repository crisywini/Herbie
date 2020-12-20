from scripts.speaker import speaker
from scripts.searchEngine.search_engine import SearchEngine
from scripts.searchEngine.Exceptions.Wiki_Exception import PageFoundException, GeoFoundException
from scripts.listener import speech_recognition_example as listener

import os
from tkinter import Tk, simpledialog,  messagebox

search_Engine = SearchEngine()


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

def delete_file(name):
    exists = os.path.exists('././data/'+name)
    if exists:
        os.remove('././data/'+name)
        speaker.speak('The file: '+name+' has been removed')
    else:
        speaker.speak('The file: '+name+' does not exists')

def search_by_wiki(query,page=False, geo = False, latitude=0, longitude=0):
    result = ''
    search_Engine.set_query(query)
    try:
        result = search_Engine.get_results_by_wiki(page=page, geo=geo, latitude=latitude, longitude=longitude)
        if not page and not geo:
            speaker.speak(result)
    except PageFoundException as page_e:
        #Preguntar por que coso necesita de la pagona
        speaker.speak('What do you want me to read of the page')
        #Listen the answer
        query = listener.understand()
        if 'categories' in query:
            for category in page_e.wikiPage.categories:
                speaker.speak(category)
        elif 'references' in query:
            for reference in page_e.wikiPage.references:
                speaker.speak(reference)
        else:
            speaker.speak(page_e.wikiPage.summary)
    except GeoFoundException as geo_e:
        list_geo = geo_e.list_geo
        if len(list_geo) == 0:
            speaker.speak('The search did not find something')
        else:
            for location in list_geo:
                speaker.speak(location)

def search_by_wolf(query):
    search_Engine.set_query(query)
    results = search_Engine.get_results_by_wolf()
    if type(results) is str:
        speaker.speak(results)
    else:
        for element in results:
            speaker.speak(element)
