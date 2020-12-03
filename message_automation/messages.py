#created on 02.12.2020 by dafr

#pip install twilio
#pip install schedule

from twilio.rest import Client 
import schedule, random, time

morning_texts = [
    "Guten Morgen Schatz",
    "Hey wie hast du geschlafen",
    "Ich vermisse dich!"
]

def send_message(quotes_list=morning_texts):

    account_sid = 'ACed2eb879e7f4b57d958ca1ad7db5dd0c' 
    auth_token = '5cc414b635bb531888a9636b5ebbb725' 
    client = Client(account_sid, auth_token)
    quote = quotes_list[random.randint(0, len(morning_texts)-1)]


    message = client.messages.create( 
                                from_='whatsapp:+14155238886',  
                                body=quote,      
                                to='whatsapp:+4915738348731' 
                            ) 
 
    print(message.sid)


schedule.every().day.at("20.05").do(send_message, morning_texts[0])

while True:
    schedule.run_pending
    time.sleep(2)