import xml.etree.ElementTree as ET



### get, set, del operations all have the same pattern:
#        packet/ module / operation / filter 

### other operations are less predictable - refer to the Plesk XML Documentation for more information



class PleskRequestPacket():        
    """ PleskRequestPacket Class provides an easy way to create PLESK XML API requests
        
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
    """

    def __init__(self, module:str ="webspace", operation:str = "get", **data) -> None:                                
        self.packet = ET.Element('packet') # The Packet (Root) Node          
        self.module = ET.SubElement(self.packet,module) # The Module Node
        self.operation = ET.SubElement(self.module,operation) # The Operation Node        
        self.filter = None # The Filter Node               
        self.set_packet_version()
        self._setup(**data)



    def _setup(self, **data):
        """ _setup function - Checks if there if the operation tag implies the use of a filter and adds it if needed 
        before adding the provided data to the operation node
            Should only be Called by __init__ 
            
        """
        if self.operation.tag in ["get", "set", "del"] and "filter" in data:   # possibly redundant condition 
            self.add_filter(**data["filter"]) 
            del data["filter"]                   
        self.add_data_to_node(self.operation, **data)         


    def set_packet_version(self, version:str="1.6.7.0") -> None:
        """Sets the packet version for the request

        Args:
            version (str, optional): Defaults to "1.6.7.0".
        """
        
        self.packet.set("version", version)


    def add_data_to_node(self,parent, **data) -> None:    
        """ add_data_to_node function - Adds all data sets to the given parent Element 
            
            TODO 
                -check if we can make private some manager classes access it directly 
                 this should no longer be necessary as the dataset will now be taken together with filter in the constructor of
                 PleskRequestPackage
        
        """
        if self.operation.tag in ["get","set","del"] and self.filter is None:
            print(f" Cant add Data {data} when craftin a {self.operation.tag} request when no filter is set. Use add_filter() to add a filter first.")
            return   
        for key, value in data.items(): 
            ## Python doesn't allow var names to have dashs 
            # if key contains substring "_id" replace it with "-id"  same for "_name"          
            key = key.replace("_id","-id")                                            
            key = key.replace("_name","-name")
            e = ET.SubElement(parent, key)            
            if type(value) == dict:
                self.add_data_to_node(e,**value) #recursion if we have another dict
            else:
                e.text = f"{value}"       


    def add_filter(self, **filter) -> None:
        
        """add_filter function - Adds a filter for a single get, set or del request
        
        Args:
            filter (dict): The filter to add                

        """

        if self.operation.tag not in ["get","set","del"]:
            print(f" Cant add Filter {filter} when craftin a {self.operation.tag} request. Use add_data_to_node() instead.")
            return
        elif self.filter is None: ### make sure filter is set when needed
            self.filter = ET.SubElement(self.operation,'filter')
        for key, value in filter.items():            
            ## Python doesn't allow the names to have dashs ???
            # if key contains substring "_id" replace it with "-id"            
            key = key.replace("_id","-id")    
            key = key.replace("_name","-name")                               
            e =ET.SubElement(self.filter, key)
            e.text = f"{value}"


    def to_string(self, encoding="UTF-8") -> str:
        """to_string function - returns the packet XML as a string
        Args:
            encoding (string): Set string encoding - defaults to: UTF-8
        Returns:
            str: The Plesk Response XML as string
        
        """
        return ET.tostring(self.packet,encoding=encoding)
    
