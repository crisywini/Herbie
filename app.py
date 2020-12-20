from scripts.speaker import speaker
from scripts.searchEngine.search_engine import SearchEngine
from scripts.searchEngine.Exceptions.Wiki_Exception import PageFoundException, GeoFoundException
def main():
    searchEngine = SearchEngine('Python')
    try:
        result_wiki = searchEngine.get_results_by_wiki(geo=True, latitude=4.570868 , longitude=-74.297333)
        if(result_wiki == 'toomany'):
            print(result_wiki + ' now searching on wolframalpha')
            result_wolf = searchEngine.get_results_by_wolf()
            print(result_wolf)
        else:
            print(result_wiki)
    except PageFoundException as e:
        #Ask for the content of the page that I want to know
        print(e.wikiPage.content)
    except GeoFoundException as e:
        if len(e.listGeo) ==0:
            print('No matching')
        else:
            #Need the speaker
            print(e.listGeo)



if __name__ == '__main__':
    main()
