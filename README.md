 omdb.py It's a python script file
uerying a favorite movie info through OMDB_API over network. Prerequisites: You need to obtain your personal API key from the OMDb API website in order to be able to use the tool. Once you have it, you can either pass it via --apikey argument, or if you don't wish to pass it every time, you can set it as an environment variable OMDB_API_KEY through ENV in Dockerfile. Building an Image: First Build a image for our program by Dockerfile(we have a dockerfile in our repo). Edit the dockerfile and replace the movie name in CMD with your Movie name by "-t" tag and --tomatoes for . Then execute the folowing command to build an image. 
