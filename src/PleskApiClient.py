import http.client
import ssl
from PleskRequestPacket import PleskRequestPacket
from PleskResponsePacket import PleskResponsePacket
from contextlib import contextmanager


class PyPleskiApiClient:
    """PyPleskApiClient Class - A simple http(s) client that uses http.client and ssl
    
    This classes request(request) method returns a PleskResponsePacket object instead of a String.
    The request argument can be a XML String or a PleskResponsePacket

    
      Args:
            server (_type_): The URL to your PLESK Server
            port (int, optional): The Port PLESK is listening. Defaults to 8443.
            use_ssl (str, optional): Use SSL (https). Defaults to True.
            unverified_ssl (bool, optional): Ignore ssl errors. Defaults to False.            
    """
    _access_token = None # will store the set access token as string
    _credentials = None # will store credentials as tuple("username","password")


    def __init__(self, server:str, port:int=8443, use_ssl:bool = True, unverified_ssl:bool = False):
        """Constructor

        Args:
            server (_type_): The URL to your PLESK Server
            port (int, optional): The Port PLESK is listening. Defaults to 8443.
            use_ssl (str, optional): Use SSL (https). Defaults to True.
            unverified_ssl (bool, optional): Ignore ssl errors. Defaults to False.
        """
        self.server = server
        self.port = port
        self.use_ssl = use_ssl
        self.unverified_ssl = unverified_ssl        
        
    def set_credentials(self, user:str, pswd:str ) -> None:        
        """Set the credentials for PLESK

        Args:
            user (str): Your PLESK username
            pswd (str): Your PLESK password
        """
        self._credentials = (user,pswd)

    def set_access_token(self, token:str) -> None:
        """Set an access token to use instead of your credentials

        Args:
            token (str): Your PLESK access token        
        """
        if not token:
            return
        self._access_token = token
        del self._credentials # No need to keep them in memory as we are using the token
    
    @contextmanager
    def _create_connection(self) -> http.client.HTTPSConnection or http.client.HTTPConnection:
        """ Create a Connection to the PLESK Server                  

        Returns:
            http.client.HTTPSConnection or http.client.HTTPConnection: Returns a Connection Object
        """
        try:
            if not self.use_ssl:
                connection = http.client.HTTPConnection(self.server, self.port) # implement log warning 

            if self.unverified_ssl:
                connection = http.client.HTTPSConnection(self.server, self.port, context=ssl._create_unverified_context())
            else:
                connection = http.client.HTTPSConnection(self.server, self.port)  
            yield connection
        finally: 
            connection.close()

    
    def _header(self) -> dict:
        """ Prepares the header for the Request        

        Returns:
            dict: A dictionary containing the headers for use with the http.client's request method
        """
        header = {"Content-Type": "TEXT/XML", "HTTP_PRETTY_PRINT": "TRUE"}        
        if self._access_token: # use access token     
            header["KEY"] = self._access_token
           
        else: # unpack the credentials from tuple into header dict
            header["HTTP_AUTH_LOGIN"], header["HTTP_AUTH_PASSWD"]  = self._credentials 
        
        return header

    def request(self, request:str or PleskRequestPacket) -> PleskResponsePacket:
        """ Send a Request to the set PLESK Server

        Args:
            request (str | PleskRequestPacket): The Request to the PLESK API as XML String or PleskRequestPacket Object

        Returns:
            PleskResponsePacket: The Response Packet as PleskResponsePacket Object
        """
        try:
            xml = request.to_string()
        except Exception:
            xml = request # set the XML with the request

        with(self._create_connection()) as connection:
            connection.request("POST", "/enterprise/control/agent.php", xml, self._header())
            response = connection.getresponse()
            data = response.read()
            print(data.decode("utf-8"))
            return PleskResponsePacket(data.decode("utf-8"))        
            
class PleskApiClient(PyPleskiApiClient):
    """ 
    PleskApiClient - compatibility class to support legacy apps 

    It is recommended to use PyPleskiApiClient instead. If you need the request method to return a string instead of an PleskResponsePacket use this legacy adapter.
    """

    def request(self, request:str or PleskRequestPacket) -> str:
        """ Send a Request to the set PLESK Server

        Args:
            request (str | PleskRequestPacket): The Request to the PLESK API as XML String or PleskRequestPacket Object

        Returns:
            str: The Response as XML string
        """
        try:
            xml = request.to_string()
        except Exception:
            xml = request # set the XML with the request

        with(self._create_connection()) as connection:
            connection.request("POST", "/enterprise/control/agent.php", xml, self._header())
            response = connection.getresponse()
            data = response.read()            
            return data.decode("utf-8")

class PleskApiClientDummy(PyPleskiApiClient):
    """ PleskApiClientDummy     

        This class acts as placeholder for testing

    """
    ### Just for testing purpose
    # no real connection 

    
    def request(self, request:any, error:bool = False) -> str:
        """ simulates a request and returns a positive add user operation or an webspace error

        Args:
            request (any): the Request XML When using the dummy this does nothing.
            error (bool, optional): If you need an error set to True. Defaults to False.

        Returns:
            str: An XML Response String        
        
        """
        return """<packet>
                        <webspace>
                            <get>
                                <result>
                                    <status>error</status>
                                    <errcode>1013</errcode>
                                    <errtext>Object not found.</errtext>
                                    <id>1234</id>
                                </result>
                            </get>
                        </webspace>
                    </packet>""" if error else """
                        <packet version="1.6.7.0">
                            <customer>
                                <add>
                                    <result>
                                        <status>ok</status>
                                        <id>3</id>
                                        <guid>d7914f79-d089-4db1-b506-4fac617ebd60</guid>
                                    </result>
                                </add>
                            </customer>
                        </packet>"""
