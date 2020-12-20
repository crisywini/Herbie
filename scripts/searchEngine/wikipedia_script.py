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
