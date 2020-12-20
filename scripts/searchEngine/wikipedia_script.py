import wikipedia


def get_summary(query):
    result = 'none'
    try:
        result = wikipedia.summary(query, sentences=2)
    except wikipedia.exceptions.PageError:
        result = 'noresults'
    except wikipedia.exceptions.DisambiguationError:
        result = 'toomany'
    return result

def get_page(title):
    result = 'none'
    try:
        result = wikipedia.page(title)
    except wikipedia.exceptions.PageError:
        result = 'nonresults'
    except wikipedia.exceptions.DisambiguationError:
        result = 'toomany'
    return result

def get_geosearch_result(latitude, longitude):
    result = wikipedia.geosearch(latitude, longitude)
    return result
