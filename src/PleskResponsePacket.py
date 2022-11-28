import xml.etree.ElementTree as ET
import json
import xmltodict


class PleskResponsePacket():
    """ PleskResponsePacket Class provides an easy way to read responses Packets from the PLESK XML API    

    Args:
        response_xml (string): Takes the response string from PleskClient.request()
        
    
    Use examples:

        request_packet = PleskRequestPacket("webspace", "add", webhosting = {"gen_setup":{'...':'...'}, "hosting": {'...':'...'}})  

        response = PleskApiClient.request(request_packet.to_string())


        response_packet = PleskResponsePacket(response)

        response_json = response_packet.to_JSON()

        response_dict = response_packet.to_dict()

        response_list = response_packet.to_list()
        
    """
    _is_error = True

    def __init__(self, response_xml):
       
        self.packet = ET.fromstring(response_xml)                      
        err = self.packet.find(".//errcode")        
        if err is None:                             
            self._is_error = False            


    def to_JSON(self) -> str:    ### easy to use with a JSON string        
        """ 
        Returns:
            str: Response as JSON string
        """
        return json.dumps(self.to_dict())

    def to_dict(self) -> dict:    ### easy to use as dictionary
        """ 
        Returns:
            dict: Response as dict
        """
        return xmltodict.parse(self.to_string())

    def to_list(self) -> list :    ### only usefull for few responses due to its structure
        """ 
        Returns:
            list: Response as string list
        """
        return ET.tostringlist(self.packet, encoding="UTF-8")

    def to_string(self) -> str:    ### get the plain XML String
        """ 
        Returns:
            str: Response as XML string
        """
        return ET.tostring(self.packet, encoding="UTF-8")

    def as_xml_etree_element(self) -> ET.Element:
        """
        Returns:
            xml.etree.ElementTree.Element: The response as xml.etree.ElementTree.Element object
        """
        return self.packet
        
    def is_error(self) -> bool:   ### see if it is an error before parsing any output
        """
        Returns:
            bool: True if response contains an error
        """
        return self._is_error



