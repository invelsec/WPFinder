import requests as rq
import random,json,os

class finders:

    def getRandomUserAgent(self) -> str :
        agents = json.load(open(f"{os.getcwd()}/service/useragents.json"))
        return "".join(agents[random.randint(1,43)])

    def searchAdminUser(self,url):
        if url[-1] == "/":
            request_url = url + "?author=1"
        else:
            request_url = url + "/?author=1"
        
        header = {
            "User-Agent":"".join(self.getRandomUserAgent())
        }
        
        response = rq.get(request_url,headers=header)
        if response.url != request_url and response.url != url:
            if "/Author/" in response.url or "author" in response.url:
                data = response.url.split("/")
                print(f"Admin User Found ! -> {data[-2]}")
        else:
            print("Method Failed. Trying to Another Method..")
            self.ApiAdminUser(url)
    
    def ApiAdminUser(self,url):
        if url[-1] == "/":
            request_url = url + "wp-json/wp/v2/users/1"
        else:
            request_url = url + "/wp-json/wp/v2/users/1"

        header = {
            "User-Agent":"".join(self.getRandomUserAgent())
        }
        response = rq.get(request_url,headers=header)
        if response.status_code == 200 and response.json():
            resJSON = response.json()
            print(f"User Founded! -> ID:{resJSON['id']} Username: {resJSON['name']}")
        else:
            print("Can't Find Any User. Failed! \nExiting.")
            exit
