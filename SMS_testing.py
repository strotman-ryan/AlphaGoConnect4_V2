



#fun with sms
from twilio.rest import Client


client = Client("AC9c71e8bf50be8e734ed0d3c3ab855eb9", "62309c663d49dbc94a25d034ec176b5e")

client.messages.create(to="+15136384300", 
                       from_="+13345106249", 
                       body="Hello from Python!")