'''
FACEBOOK MESSENGER PRANK BY ANSHUMALI
FOLLOW ME ON:-
Facebook :- https://www.facebook.com/konol123
Instgram :- https://www.instagram.com/anshumali_karna
Linkedin :- https://www.linkedin.com/in/AnshumaliKarna

For Enquiries Email Me on 
anshumali.karna99@gmail.com
'''

import fbchat
from fbchat import Client
from getpass import getpass
import pandas as pd

username = "YOUR_USERNAME_HERE"
client = fbchat.Client(username, getpass())
no_of_friends  = int(input("Number of friends: "))
data = pd.read_csv("list.csv")

for i in range(no_of_friends):
    name = str(input("Name: "))
    friends = client.searchForUsers(name)
    friend = friends[0]
    for i in range(0,449):
        i += 1
        msg = str(data.iat[i,0])
        sent = client.send(fbchat.models.Message(msg), friend.uid)
        if sent:
            print("Success")
            
        