from scripts.speaker import speaker
from scripts.searchEngine.Exceptions.Wiki_Exception import PageFoundException, GeoFoundException
from scripts.listener import speech_recognition_example as listener
from tkinter import Tk, simpledialog,  messagebox
from scripts.comands import comands

def loadCanvas ():
    root = Tk()
    root.withdraw()

def process_query(query):

    if 'data files' in query:
        comands.search_files_in_data()
    elif 'create file' in query:
        speaker.speak('I need the file name')
        fileName = listener.understand()
        speaker.speak('I need the extension for '+fileName+' file')
        extension = listener.understand()
        comands.create_file(fileName+'.'+extension)
    elif 'delete file' in query:
        speaker.speak('I need the file name')
        fileName = listener.understand()
        speaker.speak('I need the extension for '+fileName+' file')
        extension = listener.understand()
        comands.delete_file(fileName+'.'+extension)
    elif 'search' in query:
        speaker.speak('I need the search engine, Wikipedi or Wolfram')
        search_engine = listener.understand()
        if 'wiki' in search_engine or 'Wiki' in search_engine:
            #Ask for a complete wikiPage
            speaker.speak('Do you want a complete Wikipedia Page?')
            page_answer = listener.understand()
            if 'yes' in page_answer:
                 page = True
                 speaker.speak('What page do you want to search')
                 title = listener.understand()
                 comands.search_by_wiki(title, page=page)
            else:
                speaker.speak('Do you want a geo search?')
                geo_answer = listener.understand()
                if 'yes' in geo_answer:
                    geo = True
                    speaker.speak('What latitude?')
                    latitude_str = listener.understand()
                    try:
                        latitude = float(latitude_str)
                        speaker.speak('What longitude?')
                        longitude_str = listener.understand()
                        longitude = float(longitude_str)
                    except:
                        speaker.speak('I need numbers to the latitude and the longitude')
                else:
                    speaker.speak('What do you want to know')
                    title = listener.listen()
                    comands.search_by_wiki(title)
        elif 'wolf' in search_engine or 'Wolf' in search_engine or 'Wolfram' in search_engine:
            speaker.speak('What do you want to know on wolframalpha engine?')
            title = listener.understand()
            comands.search_by_wolf(title)


def main():
    query = listener.understand()
    process_query(query)

if __name__ == '__main__':
    main()
