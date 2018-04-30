import sys
import requests

class WebFetch():
    def __init__(self):
        self.fetch()

    def readUrl(self):
        print("Please add a website name: ")
        self.url = raw_input()
        return self.url

    def fetch(self):
        try:
            r = requests.get(self.readUrl())
            if(r.status_code == 200):
                print("Request Sucesfully!")
                self.exportHTML("C:\Users", "\index.html",r.content)
            else:
                print("Bad Request! Please add a valid url") 
        except:
            print("Bad input")
            pass   

    def exportHTML(self,path,name,content):
        try:
            filename = path + name
            f = open(filename, 'w') 
            f.write(content)
        except:
            print("Bad path name!")
            pass

    
wb = WebFetch()      