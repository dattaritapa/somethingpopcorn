import json,requests

class caramelPopcorn:
    def __init__(self):
        self.findmovieurl = "https://imdb8.p.rapidapi.com/title/find"
        self.findgenreurl = "https://imdb8.p.rapidapi.com/title/get-genres"
        self.getpopmovieurl = "https://imdb8.p.rapidapi.com/title/get-most-popular-movies"
        self.getgenremovurl = "https://imdb8.p.rapidapi.com/title/get-popular-movies-by-genre"
        self.getmorelikeurl = "https://imdb8.p.rapidapi.com/title/get-more-like-this"
        self.getdetailurl = "https://imdb8.p.rapidapi.com/title/get-details"
        self.movid=""
        self.genres=[]

        self.headers = {
            'x-rapidapi-key': "390eb3d922msh2c82861713f4c28p1ee060jsnd27953c51187",
            'x-rapidapi-host': "imdb8.p.rapidapi.com"
            }

    def retreivedata(self,name):
        
        self.querystring = {"q":name}

       

        self.response = requests.request("GET", self.findmovieurl, headers=self.headers, params=self.querystring)

        # python_dictionary_values = json.loads(response.text)

        # print(response.text)
        self.details=self.response.json()
        #print(type(self.details))
        #print(self.details['results'])
        print("_"*150)
        print(self.details['results'][0]['id'])
        print(self.details['results'][0]['id'].split('/')[2])
        print(self.details['results'][0]['image']['url'])
        print(self.details['results'][0]['runningTimeInMinutes'])
        print(self.details['results'][0]['title'])
        print(self.details['results'][0]['year'])
        
        self.movid+=self.details['results'][0]['id'].split('/')[2]

        self.response.close()
        return self.movid

    
    def getgenre(self,name):

        self.id = self.retreivedata(name)
        self.querystring = {"tconst" :self.id}

        self.details =  (requests.request("GET", self.findgenreurl, headers=self.headers, params=self.querystring).json())
        print (self.details)
        #self.details = self.response.json()
        if len(self.details) <= 1:
            self.genres=self.details    
        else :
            self.genres=self.details[:2]
    
        print (self.genres)



    
tub=caramelPopcorn()
name=input("Enter Movie Name: ")
tub.getgenre(name)
