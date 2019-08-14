# Needs To Install (gem install rest-client ) Before
require 'rest-client'
require "json"
api_key = '6e3f4aa4'
print 'Enter Movie Name: '
name = gets.chomp
tomatoes = true
print "Fetching #{name} Movie Information in progress. \n"
# Get Entered Movie Information
response = RestClient.get "http://www.omdbapi.com/?apikey=#{api_key}&t=#{name}&tomatoes=#{tomatoes}"
print "=============================================\n#{name} Movie Details Fetched Successfully. \n=============================================\n"
puts JSON.parse(response)

body = JSON.parse(response)
print 'Enter following Keywords for getting data ["Title", "Year", "Rated", "Released", "Runtime", "Genre", "Director", "Writer", "Actors", "Plot", "Language", "Country", "Awards", "Poster", "Ratings", "Metascore", "imdbRating", "imdbVotes", "imdbID", "Type", "tomatoMeter", "tomatoImage", "tomatoRating", "tomatoReviews", "tomatoFresh", "tomatoRotten", "tomatoConsensus", "tomatoUserMeter", "tomatoUserRating", "tomatoUserReviews", "tomatoURL", "DVD", "BoxOffice", "Production", "Website", "Response"]: '
input_val = gets.chomp
result = body["#{input_val}"]
puts result == nil ? "No information found for the entered Keyword" : result
