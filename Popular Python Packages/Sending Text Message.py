from twilio.rest import client

account_sid = " put here your twilio ACCOUNT SID"
auth_token = "put here your AUTH TOKEN"
client = client(account_sid, auth_token)

client.messages.create(
    to="...",
    from_="...",
    body="Message"
    
)