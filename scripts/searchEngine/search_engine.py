from scripts.searchEngine import wikipedia_script as wiki
from scripts.searchEngine import wolframalpha_script as wolf

class SearchEngine:

    def __init__(self, query=''):
        '''
        Init function for SearchEngine
        '''
        super().__init__()
        self.query = query
    def get_results_by_wiki(self):
        '''
        This functions allows to get the results by a query using wikipedia API
        version 1.0 only get the summary
        '''
        return wiki.get_summary(self.query)
    def get_results_by_wolf(self):
        '''
        This functions allows to get the results by a query using wolframalpha API
        version 1.0 get the results
        '''
        return wolf.get_results(self.query)
    def set_query(self, query):
        '''
        This function allows to set the new query
        '''
        self.query = query
    def get_query():
        return self.query
