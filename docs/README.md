# pypleski 0.0.6

## About this package
Pypleski (Pythonic Plesk Interface) is a collection of functions and classes that aim to ease the use of the Plesk XML API. The most important classes being PleskRequestPacket and PleskResponsePacket which are designed to represent the Request and Response Packets defined by Plesk.


## Changes:

* merging PyPleskiApiClient and PleskApiClient into PleskApiClient class to improve naming consistency
* the managers module is deprecated
* new modules where introduced and provide functions to forge requests
* add_filter() method and filter variable where removed PleskRequestPacket
* add_data_to_node() method in PleskRequestPacket now makes sure the right symbol(_/-) is used in tag names

### Bugfixes:

* PleskRequestPacket.to_string() no longer returns a bytestring (b'')


### Added Modules
* customer
* database
* db_server
* dns
* extension
* ftp_user
* git
* ip
* locales
* log_rotation
* mail
* nodejs
* php_handlers
* session

#  Managers module deprecated.

The managers module was removed with version 0.0.5.

Use the PleskApiClient Class's request method to retrieve in conjunction with the several plypleski modules functions.

We moved away from building ManagerClasses and instead provide a functions based approach

this allows usage like this and makes managers obsolete
```
from pypleski.core import PleskApiClient
from pypleski.datbase import get_database

#create client object
client = PleskApiClient("localhost") 

#add your token or use set_credentials method
client.set_access_token("IamAValidTokenLOL") 

#make your request
datbase_info = client.request(get_database("webspace-name", "domain.name"))

#print out the response
print(database_info)
```


# Core Classes in short

## PleskApiClient
 
A simple Plesk XML Api Client. 

      
* ### PleskApiClient.request(request:str | PleskRequestPacket)
   Send a Request to the set PLESK Server
   ```
   Args:
      request (str | PleskRequestPacket): The Request to send to the PLESK API as XML String or PleskRequestPacket Object

   Returns:
      str: The Response as XML string
   ```

* ### PleskApiClient.set_access_token()
   Sets an access token to use instead of your credentials
   ```
   Args:
      token (str): Your PLESK access token        
   ```

* ### PleskApiClient.set_credentials()
   Set the credentials for PLESK
   ```
   Args:
         user (str): Your PLESK username
         pswd (str): Your PLESK password
   ```


## PleskApiClientDummy

 This class acts as placeholder for testing

    
* ### PleskApiClientDummy.request()
   Simulates a request and returns a positive add user operation or an webspace error.
   ```
   Args:
      request (_type_): the Request XML When using the dummy this does nothing.
      error (bool, optional): If you need an error set to True. Defaults to False.

   Returns:
      str: An XML Response String        
   ```
        
* ### PleskApiClientDummy.set_access_token()
   Set an access token to use instead of your credentials
   ```
   Args:
      token (str): Your PLESK access token        
   ```        
* ### PleskApiClientDummy.set_credentials()
   Set the credentials for PLESK
   ```
      Args:
         user (str): Your PLESK username
         pswd (str): Your PLESK password
   ```

## PleskRequestPacket
PleskRequestPacket Class provides an easy way to create PLESK XML API requests
        
Use examples:
```
packet = PleskRequestPacket("webspace", "get", filter={"owner-id":5}, dataset={})

PleskApiClient.request(packet.to_string())

packet2 = PleskRequestPacket("webspace", "add", webhosting = {"gen_setup":{'d':'d'}, "hosting": {'d':'d'}})    

PleskApiClient.request(packet2.to_string())

```
More practical example for use in a custom function :  
```
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
```

Or preparing a Statement in a variable: 
```
   customer_del = PleskRequestPacket("customer","del", filter = { 'login': 'user_342'})
```
            
        
* ### PleskRequestPacket.add_data_to_node(**data)
   Adds **data to the given parent Element.
            
        
* ### PleskRequestPacket.set_packet_version()
   Sets the packet version for the request
   ```
   Args:
      version (str, optional): Defaults to "1.6.7.0".
   ```

* ### PleskRequestPacket.to_string()
   Returns the packet XML as a string
   ```
   Args:
      encoding (string): Set string encoding - defaults to: UTF-8
   Returns:
      str: The Plesk Response XML as string
   ```
        
## PleskResponsePacket
PleskResponsePacket Class provides an easy way to read responses Packets from the PLESK XML API     
    
Use examples:
   ```
   request_packet = PleskRequestPacket("webspace", "add", webhosting = {"gen_setup":{'...':'...'}, "hosting": {'...':'...'}})  

   response = PleskApiClient.request(request_packet.to_string())


   response_packet = PleskResponsePacket(response)

   response_json = response_packet.to_JSON()

   response_dict = response_packet.to_dict()

   response_list = response_packet.to_list()
   ```

* ### PleskResponsePacket.as_xml_etree_element()
   ```
   Returns:
      xml.etree.ElementTree.Element: The response as xml.etree.ElementTree.Element object
   ```
* ### PleskResponsePacket.is_error()
   ```
   Returns:
      bool: True if response contains an error
   ```
* ### PleskResponsePacket.to_JSON()
   ```
   Returns:
      str: Response as JSON string
   ```
* ### PleskResponsePacket.to_dict()
   ```
   Returns:
      dict: Response as dict
   ```

* ### PleskResponsePacket.to_list()
   ```
   Returns:
      list: Response as string list
   ```
* ### PleskResponsePacket.to_string()
   ```
   Returns:
      str: Response as XML string
   ```
