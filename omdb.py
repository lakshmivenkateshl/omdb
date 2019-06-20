import omdb
omdb.set_default('apikey', API_KEY)
client = omdb.OMDBClient(apikey=API_KEY)
omdb.get(title='True Grit', year=1969, fullplot=True, tomatoes=True)
omdb.get(title='True Grit', year=1969, fullplot=True, tomatoes=True, timeout=5)
omdb.search('True Grit') 
omdb.search('True Grit', timeout=5) 
omdb.search('true', page=2)


