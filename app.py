from scripts.speaker import speaker
from scripts.searchEngine.search_engine import SearchEngine
from scripts.searchEngine.Exceptions.Wiki_Exception import PageFoundException, GeoFoundException
from scripts.listener import speech_recognition_example as listener
from tkinter import Tk, simpledialog,  messagebox
from scripts.comands import comands
searchEngine = SearchEngine()

def loadCanvas ():
    root = Tk()
    root.withdraw()

def process_query(query):
    searchEngine.set_query(query)
    if 'data files' in query:
        comands.search_files_in_data()
    elif 'create file' in query:
        speaker.speak('I need the file name')
        fileName = listener.understand()
        speaker.speak('I need the extension for '+fileName+' file')
        extension = listener.understand()
        comands.create_file(fileName+'.'+extension)
def main():
    #speaker.greet()
    query = listener.understand()
    #while 'goodbye' not in query:
        #Process query
        #Listen new query
    #    print('')
    process_query(query)

if __name__ == '__main__':
    main()
