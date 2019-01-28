from new import New 
from admin import Admin
from client import Client
from message import Message

C = "C"
lol = "l+"
a = Admin(C, C, C, C)
New.news[2] = New(a, lol, lol, lol, lol)
Client.show_news(Message.ME)

if len(New.news):
	print(len(New.news))
else:
	print("no")




New.news[2].delete_new()


