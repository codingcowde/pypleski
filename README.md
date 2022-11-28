# What is pypleski?

Pypleski (Pythonic Plesk Interface) is a collection of functions and classes that aim to ease the use of the Plesk XML API. The most important classes being PleskRequestPacket and PleskResponsePacket which are designed to represent the Request and Response Packets defined by Plesk.

For more information on Request and Response Packets, refer to the definition as described in the Plesk XML API Documentation.
https://docs.plesk.com/en-US/obsidian/api-rpc/about-xml-api/xml-api-packets.50168/

The PleskRequestPacket class takes the work of writing complete XML requests thus reducing the amount of written code for each request significantly.


# What pypleski is not
Pypleski is not a security tool. Sanitation of input and error handling should be implemented by app developers. 

Pypleski is not a full fledged API wrapper yet. However, we keep working towards implementing more and more manager classes, to cover as many modules as possible.

# Getting started 
You can install pypleski using pip by running the following command:

pip install pypleski

