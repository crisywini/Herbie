import wolframalpha

client = wolframalpha.Client('9KTT9J-YK3PYT4WL4')
def get_results(query):
    result = client.query('Temperature in Armenia-Quindío')
    return next(result.results).text
