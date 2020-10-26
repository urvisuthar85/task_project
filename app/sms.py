# from twilio.rest import Client

# account_sid = 
# auth_token = ''
# client = Client(account_sid,auth_token)


# message = client.messages \ 
#     .create(
#         body = ""
#         from_ = "+12679154178"
#         to = "+918306308768"
#     )

def send_sms(account_sid,auth_token,body,from_,to_):
    from twilio.rest import Client
    client = Client(account_sid,auth_token)
    message = client.messages.create(
        body = body,
        from_= from_,
        to = to_,
    )

def get_otp():
    import math,random
    digites = '0123456789'
    OTP = ''
    for i in range(6):
        OTP += digites[math.floor(random.random() * 10)]

    return OTP

o = get_otp()
print(o)