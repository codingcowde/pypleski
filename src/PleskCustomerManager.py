from PleskRequestPacket import PleskRequestPacket
from PleskResponsePacket import PleskResponsePacket
from PleskApiClient import PleskApiClient, PleskApiClientDummy 


class PleskCustomerManager():        
    """
        Example Manager Class for the Customer module of the PLESK XML API\n         
        Args:
            plesk (PleskApiClient, optional): The PleskApiClient Object to run requests Defaults to PleskApiClientDummy().
       
        Test Scenarios succeeded:\n
            manager = PleskCustomerManager()\n
            manager.add_customer("cname","pname","login","passwd")\n
            manager.delete_customer("login")            

        The PleskApiClientDummy is kept for ease of testing
    """
    def __init__(self,   plesk:PleskApiClient or PleskApiClientDummy = PleskApiClientDummy()) -> None:       
          self.plesk = plesk

    def add_customer(self, cname, pname, login, passwd, **data) -> PleskResponsePacket:
        """ Add a customer 

        Args:
            cname (str): company name
            pname (str): full name
            login (str): login name
            passwd (str): login passwd - has to match the password policy of your plesk server\n
            **data (dict): other user data as key:value pairs             

        Returns:
            PleskResponsePacket: Plesk APIs response PleskResponsePacket object
        """
        request = PleskRequestPacket("customer", "add", gen_info={'cname': cname, 'pname': pname, 'login': login, 'passwd': passwd, 'status': 0, 'phone': data["phone"] if 'phone' in data else '', 'fax': data["fax"] if 'fax' in data else '', 'email': data["email"] if 'email' in data else '', 'address': data["address"] if 'address' in data else '', 'city': data["city"] if 'city' in data else '', 'state': data["state"] if 'state' in data else '', 'pcode': data["pcode"] if 'pcode' in data else '', 'country': data["country"] if 'country' in data else '', 'external-id': data["external-id"] if 'external-id' in data else '', 'phone': data["description"] if 'description' in data else ''})

        return self._do_REQUEST(request)
    
    def get_customer_info(self, login:str, dataset:str="gen_info") -> PleskResponsePacket:     
        """ Get customer info by login name

        Args:
            login (str): customers login name\n
                        
            dataset (str): use if you want to retrieve a specific dataset like "gen_info"\n

        Returns:
            PleskResponsePacket: Plesk API Response
        """         
        request =  PleskRequestPacket("customer", "get", filter={'login': login})          
        request.add_data_to_node(request.operation,  dataset={dataset:''}) # the second arguments value will create <dataset><[dataset] /> </dataset>
        return self._do_REQUEST((request))

    
    def update_customer_info(self, login, dataset) -> PleskResponsePacket:       
        pass

    def delete_customer(self, login)  -> PleskResponsePacket:   
        """Delete a customer by their login name

        Args:
            login (str): customers login name

        Returns:
            PleskResponsePacket: Response from Plesk
        """        
        request = PleskRequestPacket("customer","del", filter = { 'login': login })
        return self._do_REQUEST(request)
        

    def _do_REQUEST(self, request:PleskResponsePacket) -> PleskResponsePacket:              
        return PleskResponsePacket(self.plesk.request(request.to_string()))

  

