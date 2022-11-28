PleskApiClient
 
    PleskApiClient - compatibility class to support legacy apps 

    It is recommended to use PyPleskiApiClient instead. If you need the request method to return a string instead of an PleskResponsePacket use this legacy adapter.
    
PleskApiClient._access_token()
None
PleskApiClient._create_connection()
 Create a Connection to the PLESK Server                  

        Returns:
            http.client.HTTPSConnection or http.client.HTTPConnection: Returns a Connection Object
        
PleskApiClient._credentials()
None
PleskApiClient._header()
 Prepares the header for the Request        

        Returns:
            dict: A dictionary containing the headers for use with the http.client's request method
        
PleskApiClient.request()
 Send a Request to the set PLESK Server

        Args:
            request (str | PleskRequestPacket): The Request to the PLESK API as XML String or PleskRequestPacket Object

        Returns:
            str: The Response as XML string
        
PleskApiClient.set_access_token()
Set an access token to use instead of your credentials

        Args:
            token (str): Your PLESK access token        
        
PleskApiClient.set_credentials()
Set the credentials for PLESK

        Args:
            user (str): Your PLESK username
            pswd (str): Your PLESK password
        
PleskApiClientDummy
 PleskApiClientDummy     

        This class acts as placeholder for testing

    
PleskApiClientDummy._access_token()
None
PleskApiClientDummy._create_connection()
 Create a Connection to the PLESK Server                  

        Returns:
            http.client.HTTPSConnection or http.client.HTTPConnection: Returns a Connection Object
        
PleskApiClientDummy._credentials()
None
PleskApiClientDummy._header()
 Prepares the header for the Request        

        Returns:
            dict: A dictionary containing the headers for use with the http.client's request method
        
PleskApiClientDummy.request()
 simulates a request and returns a positive add user operation or an webspace error

        Args:
            request (_type_): the Request XML When using the dummy this does nothing.
            error (bool, optional): If you need an error set to True. Defaults to False.

        Returns:
            str: An XML Response String        
        
        
PleskApiClientDummy.set_access_token()
Set an access token to use instead of your credentials

        Args:
            token (str): Your PLESK access token        
        
PleskApiClientDummy.set_credentials()
Set the credentials for PLESK

        Args:
            user (str): Your PLESK username
            pswd (str): Your PLESK password
        
PleskRequestPacket
 PleskRequestPacket Class provides an easy way to create PLESK XML API requests
        
        Use examples:

        packet = PleskRequestPacket("webspace", "get", filter={"owner-id":5}, dataset={})

        PleskApiClient.request(packet.to_string())

        packet2 = PleskRequestPacket("webspace", "add", webhosting = {"gen_setup":{'d':'d'}, "hosting": {'d':'d'}})    

        PleskApiClient.request(packet2.to_string())


        More practical example for use in a custom function :  

        def add_customer(self, cname, pname, login, passwd) -> PleskResponsePacket:

            request = PleskRequestPacket("customer","add", gen_info = { 
                'cname': cname, 
                'pname': pname,
                'login': login,
                'passwd': passwd,
                'status': 0,
                'phone': '',
                'fax': '',
                'email': '',
                'address': '',
                'city':'',
                'state':'',
                'pcode':'',
                'country':''
                })


        Or preparing a Statement in a variable: 
            customer_del = PleskRequestPacket("customer","del", filter = { 'login': 'login'})
    
PleskRequestPacket._setup()
 _setup function - Checks if there if the operation tag implies the use of a filter and adds it if needed 
        before adding the provided data to the operation node
            Should only be Called by __init__ 
            
        
PleskRequestPacket.add_data_to_node()
 add_data_to_node function - Adds all data sets to the given parent Element 
            
            TODO 
                -check if we can make private some manager classes access it directly 
                 this should no longer be necessary as the dataset will now be taken together with filter in the constructor of
                 PleskRequestPackage
        
        
PleskRequestPacket.add_filter()
add_filter function - Adds a filter for a single get, set or del request
        
        Args:
            filter (dict): The filter to add                

        
PleskRequestPacket.set_packet_version()
Sets the packet version for the request

        Args:
            version (str, optional): Defaults to "1.6.7.0".
        
PleskRequestPacket.to_string()
to_string function - returns the packet XML as a string
        Args:
            encoding (string): Set string encoding - defaults to: UTF-8
        Returns:
            str: The Plesk Response XML as string
        
        
PleskResponsePacket
 PleskResponsePacket Class provides an easy way to read responses Packets from the PLESK XML API    

    Args:
        response_xml (string): Takes the response string from PleskClient.request()
        
    
    Use examples:

        request_packet = PleskRequestPacket("webspace", "add", webhosting = {"gen_setup":{'...':'...'}, "hosting": {'...':'...'}})  

        response = PleskApiClient.request(request_packet.to_string())


        response_packet = PleskResponsePacket(response)

        response_json = response_packet.to_JSON()

        response_dict = response_packet.to_dict()

        response_list = response_packet.to_list()
        
    
PleskResponsePacket._is_error()
bool(x) -> bool

Returns True when the argument x is true, False otherwise.
The builtins True and False are the only two instances of the class bool.
The class bool is a subclass of the class int, and cannot be subclassed.
PleskResponsePacket.as_xml_etree_element()

        Returns:
            xml.etree.ElementTree.Element: The response as xml.etree.ElementTree.Element object
        
PleskResponsePacket.is_error()

        Returns:
            bool: True if response contains an error
        
PleskResponsePacket.to_JSON()
 
        Returns:
            str: Response as JSON string
        
PleskResponsePacket.to_dict()
 
        Returns:
            dict: Response as dict
        
PleskResponsePacket.to_list()
 
        Returns:
            list: Response as string list
        
PleskResponsePacket.to_string()
 
        Returns:
            str: Response as XML string
        
