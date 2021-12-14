import requests as rq
import random,json,os

class xmlrpc:

    def getRandomUserAgent(self) -> str:
        agents = json.load(open(f"{os.getcwd()}/service/useragents.json"))
        return "".join(agents[random.randint(1,43)])

    def createAndSendRequest(self,url) -> str:
        xmlData = """
        <?xml version="1.0" encoding="utf-8"?> 
        <methodCall> 
        <methodName>system.listMethods</methodName> 
        <params></params> 
        </methodCall>
        """

        header = {
            "User-Agent":"".join(self.getRandomUserAgent())
        }
        
        if url[-1] == "/":
            request_url = url + "xmlrpc.php"
        else:
            request_url = url + "/xmlrpc.php"
            
        xmlrpc_lookup = rq.get(request_url,headers=header).text
        if xmlrpc_lookup == "XML-RPC server accepts POST requests only.":
            print("Boom!.. XmlRpc Enabled on Wordpress.\n")
            ##Looking XMLRpc Methods
            xmlrpc_methods_checks = rq.post(request_url,headers=header,data=xmlData).text
            print(f"XmlRPC Methods Check Complete - All Methods Listed \n {xmlrpc_methods_checks}")
            print("Hint: You can try out the XMLRpc ping back feature.")
        else:
            print("Sad Story :( - XmlRPC Failed")
