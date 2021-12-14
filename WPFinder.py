from service.finders import finders
from service.xmlrpc import xmlrpc
import optparse

class WPFinder:

    Message = """
        Welcome to WPFinder!
        Creator -> Burak Ayvaz
        github.com/invelsec
    """
    
    Info = """
        This tool extracting 'Admin' usernames on wordpress based sites.
        Please don't use this tool for illegal activities.
    """
    
    def __init__(self) -> None:
        opt = optparse.OptionParser(description=self.Info)
        opt.add_option("-u",dest="url",help="Wordpress Site Url.")
        (optInput,_)= opt.parse_args()

        print(self.Message + "\n")

        if optInput.url != None:
            finders().searchAdminUser(optInput.url)
            print("Admin Enumeration Finished. Now Checking XMLRPC!")
            xmlrpc().createAndSendRequest(optInput.url)
        else:
            print("Please give any wordpress site url!")
            exit

WPFinder()
