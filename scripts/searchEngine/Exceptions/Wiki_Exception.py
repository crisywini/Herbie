class PageFoundException(Exception):
    def __init__(self, wikiPage, message = 'Found a WikipediaPage'):
        self.wikiPage = wikiPage
        self.message = message
        super().__init__(message)
class GeoFoundException(Exception):
    def __init__(self, listGeo, message='Found the location'):
        self.listGeo = listGeo
        self.message = message
        super().__init__(message)
