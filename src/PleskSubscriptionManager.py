from PleskApiClient import PleskApiClientDummy
from PleskRequestPacket import PleskRequestPacket
from PleskResponsePacket import PleskResponsePacket

class PleskSubscriptionManager():        
    """
        Example Manager Class for the Webspace module of the PLESK XML API\n         
        Args:
            plesk (PleskApiClient, optional): The PleskApiClient Object to run requests Defaults to PleskApiClientDummy().  
        
        TODO \n
        Fix methods        
    """
    def __init__(self,   plesk = PleskApiClientDummy()) -> None:       
          self.plesk = plesk

    def add_subscription(self, owner_id, domain, hostip, package, **data) -> PleskResponsePacket:
        """ Add a subscription

        Args:
            owner_id (int): customers id
            domain (str): a valid domain name e.g. example.org
            hostip (str): the target vhosts ip in plesk
            package (str): the plan name in plesk

        Returns:
            PleskResponsePacket: Response from Plesk

         Generated Request:
            Adds a subscription the user with the id given as 'owner_id', 
            the domain name string and the internal name of the users package
            and returns the subscriptions id

            the request looks like this:

            <webspace>
                <add>
                    <gen_setup>
                        <name>example.com</name>
                        <owner-id>1234</owner-id>
                        <htype>vrt_hst</htype>
                        <ip_address>192.0.2.123</ip_address>
                        <status>0</status>
                    </gen_setup>
                    <hosting>
                        <vrt_hst>
                            <property>
                                <name>ssl</name>
                                <value>false</value>
                            </property>              
                            <ip_address>10.58.103.100</ip_address>
                        </vrt_hst>
                    </hosting>
                    <plan-name>base_template</plan-name>
                </add>
            </webspace>

        """        
        request = PleskRequestPacket("webspace", "add", gen_setup={
            'name':domain,
            'owner-id':owner_id,
            'htype':'vrt_hst',
            'ip_address':hostip,
            'status':0,            
            }, hosting={
                'vrt_hst':{'property':{'name':'ssl', 'value':'true'},
                'ip_address':hostip},
                }, plan_name=package )   
        print(request.to_string())                 
        return self._do_REQUEST(request)
    
    def get_subscription(self, owner:str, dataset:str="gen_info") -> PleskResponsePacket:     
        """ Get subscription info 

        Args:
            owner (str): customers login name\n
                        
            dataset (str): use if you want to retrieve a specific dataset like "gen_info"\n

        Returns:
            PleskResponsePacket: Plesk API Response
        """         
        request =  PleskRequestPacket("webspace", "get", filter={'owner': owner})          
        request.add_data_to_node(request.operation,  dataset={dataset:''}) # the second arguments value will create <dataset><[dataset] /> </dataset>
        return self._do_REQUEST((request))

    
    def update_subscription(self, id, dataset) -> PleskResponsePacket:    
        """ TODO Implement a flexible update function """   
        pass

    def delete_subscription(self, login)  -> PleskResponsePacket:   
        """Delete a subscription

        Args:
            login (str): customers login name

        Returns:
            PleskResponsePacket: Response from Plesk
        """        
        request = PleskRequestPacket("webspace","del", filter = { 'login': login })
        return self._do_REQUEST(request)
        

    def _do_REQUEST(self, request) -> PleskResponsePacket:              
        return PleskResponsePacket(self.plesk.request(request.to_string()))

  


