from service.finders import finders
from service.xmlrpc import xmlrpc
import optparse

class WPFinder:

    Message = """
__        ______  _____ _           _           
\ \      / /  _ \|  ___(_)_ __   __| | ___ _ __ 
 \ \ /\ / /| |_) | |_  | | '_ \ / _` |/ _ \ '__|
  \ V  V / |  __/|  _| | | | | | (_| |  __/ |   
   \_/\_/  |_|   |_|   |_|_| |_|\__,_|\___|_|   
                                                
        Created by - Invelsec 
         \ github.com/invelsec
    """
    
    Info = """
        This tool extracting 'Admin' usernames and Checking XMLRPC Features on wordpress based sites.
        Please don't use this tool for illegal activities.
    """
    
    def __init__(self) -> None:
        opt = optparse.OptionParser(description=self.Info)
        opt.add_option("-u",dest="url",help="Wordpress Site Url.")
        opt.add_option("-x",dest="xmlrpc",help="Testing XMLRPC PingBack.")
        (optInput,_)= opt.parse_args()

        print(self.Message + "\n" + self.Info)

        if optInput.url != None:
            finders().searchAdminUser(optInput.url)
            print("Admin Enumeration Finished. Now Checking XMLRPC!\n")
            xmlrpc().createAndSendRequest(optInput.url)
            if optInput.xmlrpc != None:
                print("\nXmlRpc Pingback Testing!")
                xmlrpc().testXMLRPCPingback(optInput.url,optInput.xmlrpc)
        else:
            print("Please give any wordpress site url!")
            exit

WPFinder()
