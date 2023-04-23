from twilio.rest import Client

def whatsapp():
    account_sid = 'ACef81c59d5968db38890a98f8855825a2'
    auth_token = 'eba6c5095c04c1e3e2e410c8a118c849'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
    body='This is a message from vigilence squad, Something mischievous is happening🤔 at the location you specified to us.',
    from_='whatsapp:+14155238886',
    to='whatsapp:+918923194616'
    )

    print(message.sid)