from twilio.rest import Client

account_sid = 'ACda3906ef32e2cd5dd892fa4f3d1797f3'
auth_token = 'c47f4e0c84edf9cbd9a0d528968327cc'
client = Client(account_sid, auth_token)

message = client.messages.create(
    body='Hello,Something mischievous is happening🤔.Take a look😎',
    from_='whatsapp:+14155238886',
    to='whatsapp:+918923194616'
)

print(message.sid)