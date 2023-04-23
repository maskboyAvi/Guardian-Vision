from twilio.rest import Client
import keys_of_sms_alert

client = Client(keys_of_sms_alert.account_sid, keys_of_sms_alert.auth_token)

message = client.messages.create(
    body = "This is a message from",
    from_ = keys_of_sms_alert.twilio_number,
    to = keys_of_sms_alert.target_number
)

print(message.body)