from scripts.speaker import speaker
from scripts.searchEngine.search_engine import SearchEngine

def main():
    searchEngine = SearchEngine('Python')
    result_wiki = searchEngine.get_results_by_wiki()
    if(result_wiki == 'toomany'):
        print(result_wiki + ' now searching on wolframalpha')
        result_wolf = searchEngine.get_results_by_wolf()
        print(result_wolf)
    else:
        print(result_wiki)
if __name__ == '__main__':
    main()
