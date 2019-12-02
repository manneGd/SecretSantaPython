from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import config
import smtplib, ssl


def send_email(individual):
    sender = config.email_user
    password = config.email_password
    receiver = individual.email

    body = MIMEMultipart("alternative")
    body["Subject"] = "OMG !!! You\'ve just receive a super Secret message"
    body["From"] = sender
    body["To"] = receiver

    plain_text = """\
            This is the plain text version.
            ------------------------------------------------
            Christmas is coming! So it's time to do some shopping!!!!
            ==> This year, {sender}, you have to give a gift to {chosen} <==
            ------------------------------------------------

            !!! Merry Christmas !!!
    
    
            -- 
            XOXO
            Santa
            
            """.format(sender=individual.name, chosen=individual.chosen)

    html_text = """\
    <html>
        <head>
        </head>
    <body>
        <div class="es-wrapper-color">
            <table class="es-wrapper" width="100%" cellspacing="0" cellpadding="0">
                <tbody>
                    <tr>
                        <td class="esd-email-paddings" valign="top">
                            <table class="es-content es-preheader esd-header-popover" cellspacing="0" cellpadding="0" align="center">
                                <tbody>
                                    <tr>
                                        <td class="es-adaptive esd-stripe" esd-custom-block-id="3839" align="center">
                                            <table class="es-content-body" style="background-color: transparent;" width="600" cellspacing="0" cellpadding="0" align="center">
                                                <tbody>
                                                    <tr>
                                                        <td class="esd-structure es-p10" align="left">
                                                            <table cellspacing="0" cellpadding="0" width="100%">
                                                                <tbody>
                                                                    <tr>
                                                                        <td class="esd-container-frame" width="580" align="left">
                                                                            <table width="100%" cellspacing="0" cellpadding="0">
                                                                                <tbody>
                                                                                    <tr>
                                                                                        <td class="es-infoblock esd-block-text" align="left">
                                                                                            <p style="line-height: 14.4px; text-align: center;">Merry Christmas and happy new year!</p>
                                                                                        </td>
                                                                                    </tr>
                                                                                </tbody>
                                                                            </table>
                                                                        </td>
                                                                    </tr>
                                                                </tbody>
                                                            </table>
                                                        </td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                            <table class="es-content" cellspacing="0" cellpadding="0" align="center">
                                <tbody>
                                    <tr></tr>
                                    <tr>
                                        <td class="esd-stripe" esd-custom-block-id="3802" align="center">
                                            <table class="es-content-body" style="background-color: rgb(255, 255, 255);" width="600" cellspacing="0" cellpadding="0" bgcolor="#ffffff" align="center">
                                                <tbody>
                                                    <tr>
                                                        <td class="esd-structure es-p20t es-p20b es-p20r es-p20l esd-checked" align="left" style="background-image:url(https://eornuu.stripocdn.email/content/guids/CABINET_6fb83e22902d396e5d3c21413ca00855/images/10431575242741109.png);background-position: center top; background-repeat: no-repeat;" background="https://eornuu.stripocdn.email/content/guids/CABINET_6fb83e22902d396e5d3c21413ca00855/images/10431575242741109.png">
                                                            <table cellpadding="0" cellspacing="0" width="100%">
                                                                <tbody>
                                                                    <tr>
                                                                        <td width="560" class="esd-container-frame" align="center" valign="top">
                                                                            <table cellpadding="0" cellspacing="0" width="100%">
                                                                                <tbody>
                                                                                    <tr>
                                                                                        <td align="left" class="esd-block-text">
                                                                                            <p><br></p>
                                                                                            <p><br></p>
                                                                                            <p><br></p>
                                                                                            <p><br></p>
                                                                                            <p><br></p>
                                                                                            <p><br></p>
                                                                                            <p><br></p>
                                                                                            <p><br></p>
                                                                                            <p><br></p>
                                                                                            <p><br></p>
                                                                                            <p><br></p>
                                                                                            <p><br></p>
                                                                                            <p><br></p>
                                                                                            <p><br></p>
                                                                                            <p style="text-align: center;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<strong><span style="font-size:22px;"> {chosen} </span></strong></p>
                                                                                            <p><br></p>
                                                                                            <p><br></p>
                                                                                            <p><br></p>
                                                                                            <p><br></p>
                                                                                            <p><br></p>
                                                                                            <p><br></p>
                                                                                            <p><br></p>
                                                                                            <p><br></p>
                                                                                            <p><br></p>
                                                                                            <p><br></p>
                                                                                        </td>
                                                                                    </tr>
                                                                                </tbody>
                                                                            </table>
                                                                        </td>
                                                                    </tr>
                                                                </tbody>
                                                            </table>
                                                        </td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                            <table class="es-footer esd-footer-popover" cellspacing="0" cellpadding="0" align="center">
                                <tbody>
                                    <tr>
                                        <td class="esd-stripe" esd-custom-block-id="3851" align="center">
                                            <table class="es-footer-body" width="600" cellspacing="0" cellpadding="0" align="center">
                                                <tbody>
                                                    <tr>
                                                        <td class="esd-structure es-p10t es-p20r es-p20l" esd-general-paddings-checked="true" align="left">
                                                            <table width="100%" cellspacing="0" cellpadding="0">
                                                                <tbody>
                                                                    <tr>
                                                                        <td class="esd-container-frame" width="560" valign="top" align="center">
                                                                            <table width="100%" cellspacing="0" cellpadding="0">
                                                                                <tbody>
                                                                                    <tr>
                                                                                        <td class="esd-block-text" align="center">
                                                                                            <p style="font-size: 12px; line-height: 150%;">This is an automatic email, please do not reply to this email.</p>
                                                                                            <p style="font-size: 12px; line-height: 150%;">If you have any reclamation about the chosen person or want to make suggestions, please feel free to send an email to: manne.grand@gmail.com<br></p>
                                                                                        </td>
                                                                                    </tr>
                                                                                </tbody>
                                                                            </table>
                                                                        </td>
                                                                    </tr>
                                                                </tbody>
                                                            </table>
                                                        </td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
        <div class="banner-toolbar"></div>
    </body>
</html> """.format(chosen=individual.chosen)

    part1 = MIMEText(plain_text, "plain")
    part2 = MIMEText(html_text, "html")

    body.attach(part1)
    body.attach(part2)

    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(config.smtp, config.port_smtp, context=context) as server:
            server.login(sender, password)
            server.sendmail(sender, receiver, body.as_string())
            server.close()

        print('Email sent!')
    except:
        print('Something went wrong...')
