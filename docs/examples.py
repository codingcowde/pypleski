# Core Classes

"""
    PleskRequestPackage
"""
from pypleski.core import PleskRequestPacket

request = PleskRequestPacket("webspace", "get", filter={"owner-id":5})
request.set_packet_version("1.6.3.2")

print(request.to_string())
"""
Output: b'<packet version="1.6.3.2"><webspace><get><filter><owner-id>5</owner-id></filter></get></webspace></packet>'
"""


# Helper Functions

""" 
 get_plesk_session_token()
 Below, you can see a simple example for how to use the obtain_plesk_session_token function
 You will have to provide tht url, credentials and the clients ip.
 If succsesfull, the funciton returns a valid session token. Otherwise an empty string is returned
"""
from pypleski.core import obtain_plesk_session_token

def sign_in_to_plesk(plesk_url, user, pwd, client_ip):
     token = obtain_plesk_session_token(plesk_url,user,pwd,client_ip)
     if token:     
        print(f"Your Session Token for user {user}@{plesk_url} is {token}.")  

sign_in_to_plesk("https://localhost","user2","S4f3p4ssw0rd","127.0.0.1") # edit to match your credentials


