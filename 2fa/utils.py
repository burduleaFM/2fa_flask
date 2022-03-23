import random, string
from app import app
from flask_mail import Mail, Message


mail= Mail(app)

# get a random code of 6 chars
def id_generator(size= 6, chars= string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

# the route for send a mail
def send_mail(email):
    code_random = id_generator()
    msg = Message('Confirm code', sender = 'derrrrcaci@mail.com', recipients = [email])
    msg.body = f"Your confirm code is {code_random}, this code is valid only 60 sec"
    mail.send(msg)
    return code_random