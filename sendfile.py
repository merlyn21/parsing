#!/usr/bin/env python
# coding: utf-8

import smtplib
import os
import sys
import subprocess
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate


def send2mail(address, subj, mess, file_to_attach="none"):
    msg = MIMEMultipart()

    address2 = 'm@gmail.com'

    msg['From'] = 'r@us.ru'
    msg['To'] = address
    msg['Subject'] = subj
    message = mess
    msg.attach(MIMEText(message))

    if file_to_attach != "none":
        ind = file_to_attach.rfind("/")
        name_file_to_attach = file_to_attach[ind+1:len(file_to_attach)]
        header = 'Content-Disposition', 'attachment; filename="%s"' % name_file_to_attach

    attachment = MIMEBase('application', "octet-stream")

    if file_to_attach != "none":
        try:
            with open(file_to_attach, "rb") as fh:
                data = fh.read()

            attachment.set_payload( data )
            encoders.encode_base64(attachment)
            attachment.add_header(*header)
            msg.attach(attachment)
        except IOError:
            msg = "Error opening attachment file %s" % file_to_attach
            print(msg)
            sys.exit(1)

    #mailserver.login('robot@ustandart.ru', 'Pr_333151abc')

    try:
        mailserver = smtplib.SMTP_SSL('smtp.yandex.ru:465')
        mailserver.login('r@us.ru', 'Pr')
        mailserver.sendmail('r@us.ru', address, msg.as_string())
        mailserver.sendmail('r@us.ru', address2, msg.as_string())
    except Exception as e:
        print(e)
    finally:
        mailserver.quit()
