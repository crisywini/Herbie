from scripts.searchEngine import wikipedia_script as wiki
from scripts.searchEngine import wolframalpha_script as wolf
from scripts.searchEngine.Exceptions.Wiki_Exception import PageFoundException, GeoFoundException

class SearchEngine:

    def __init__(self, query=''):
        '''
        Init function for SearchEngine
        '''
        super().__init__()
        self.query = query
    def get_results_by_wiki(self, page=False, geo=False, latitude=0, longitude=0):
        '''
        This functions allows to get the results by a query using wikipedia API
        version 1.0 only get the summary
        '''
        if page:
            result = wiki.get_page(self.query)
            if result != 'none' and result != 'nonresults':
                raise PageFoundException(result)
        elif geo:
            result = wiki.get_geosearch_result(latitude, longitude)
            raise GeoFoundException(result)
        else:
            result = wiki.get_summary(self.query)
        return result
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
