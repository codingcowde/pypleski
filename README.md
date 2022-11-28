# pypleski - python-plesk-reseller-interface
Easy to use interface for the Plesk XML API -  Create and manage customers, subscriptions and add service addons 

<b> Simplified use of the PLESK Obsidian XML RPC API  with pypleski</b>

pypleski provides some easy to use classes and functions for common tasks an admin or reseller would like to automate. 

PleskResponsePacket -  provides an easy way to read PLESK XML API responses <br>
PleskRequestPacket - provides an easy way to prepare and modify PLESK XML API requests <br>

# TODO
PleskCustomerManager - A simple Customer Manager - <b> review code and improve performance </b> <br>
PleskSubscriptionManager - A simple Subcsription Manager - <b> implement add_subscription </b><br>
PleskClient - A simple PleskAPIClient - <b>check for secure and fast solution</b><br>

# Requirements
pypleski needs Python 3.6 or higher.

dependencies: xmltodict 

# Notes 
What is different to 
Ordered Dictionaries are not needed anymore as with Python 3.6 the dict class now preserves the order of keys. 


# Look into creating django apps to provide api endpoints in django projects (get operations only) 
Django app.pypleski.user for authentication
Django app.pypleski.subscription for booking and managing 



