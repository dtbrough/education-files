from twilio.rest import TwilioRestClient

account_sid = "AC2b8836f7057fd3c198dc406971288d06"
auth_token = "fa49c7a7a263c2128e4be841a16d4c85"
client = TwilioRestClient(account_sid, auth_token)

message = client.sms.message.create(
    body="Hello"
    to="+447979636254")
print message.sid
