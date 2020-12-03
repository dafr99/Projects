#created on 02.12.2020 by dafr

#pip install apscheduler
#pip install twilio

from twilio.rest import Client 
 
account_sid = 'ACed2eb879e7f4b57d958ca1ad7db5dd0c' 
auth_token = '5cc414b635bb531888a9636b5ebbb725' 
client = Client(account_sid, auth_token) 


def send_love():
    message = client.messages.create( 
                                from_='whatsapp:+14155238886',  
                                body='testtest3',      
                                to='whatsapp:+4915738348731' 
                            ) 
 
    print(message.sid)
