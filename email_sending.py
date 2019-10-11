import config
import smtplib


def send_email(individual):
    user = config.email_user
    password = config.email_password

    sent_from = user
    to = [individual.email]
    subject = 'OMG Super Important Message'
    body = 'Ps: Sorry for the lake of design, I\'ll try to do better next year'

    email_text = """\  
    From: %s  
    To: %s  
    Subject: %s

    ------------------------------------------------
    Only 26 days until Christmas! It's time to do some shopping!!
    ==> This year, %s, you have to give a gift to %s <==
    ------------------------------------------------
    https://www.youtube.com/watch?v=V3EYjVPRClU
    
    !!! Merry Christmas !!!
    
    
    -- 
    xoxo
    Santa

    %s
    """ % (sent_from, ", ".join(to), subject, individual.name, individual.chosen, body)

    try:
        server = smtplib.SMTP_SSL(config.smtp, config.port_smtp)
        server.ehlo()
        server.login(user, password)
        server.sendmail(sent_from, to, email_text)
        server.close()

        print('Email sent!')
    except:
        print('Something went wrong...')
