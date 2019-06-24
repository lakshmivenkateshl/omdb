import sys
import json
#To access the OMDB API, we can create an ''OMDBClient'' instance
from omdb import OMDBClient
#must use OMDB API Parameters
client = OMDBClient(apikey=API_KEY)
print("Success, API is connected")

# Default for Rotten Tomato rating
omdb.set_default('tomatoes', True) 

cmd_Argument = sys.argv[1].strip()
print ("The command line argument is : %s" %(cmd_argument))
#user Input
#movie_name = str(input("please enter movie name : "))
#movie_year = input("enter year as well :")
resl = client.request(t= cmd_argument,  plot='full', tomatoes='true', timeout=5)
xml_content = resl.content

my_json = xml_content.decode('utf8')
print('*' * 30)

#load the json  to a python  list & dump it back out as format
data = json.loads(my_json)
tomato_rat = data["ratings"][1]["value"]
print("rotten Tomato ratings is : ", tomato_rat)
print(' & ' * 30)
print(' & ' * 30)

# all the information about particular movie name 
s = json. dumps(data, indent=4, sort_keys=True)
print(s)
  
   

   

