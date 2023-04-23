from twilio.rest import Client

def sms():
    account_sid = 'ACf59e77619358d46632aaaba2ac27344f'
    auth_token = '18f68663a3e5de7634bb27f49f5a5d3c'
    twilio_number = +16812068240
    target_number = +918923194616
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body = "This is a message from vigilence squad, Something mischievous is happening🤔 at the location you specified to us.",
        from_ = twilio_number,
        to = target_number
    )

    print(message.body)