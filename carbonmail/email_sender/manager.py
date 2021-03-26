import os
import smtplib
import ssl

from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

from os import path
from decouple import AutoConfig
import threading

import PySimpleGUI as sg

from carbonmail.list_editor.manager import get_list_contacts
from carbonmail.utils import string_null_or_empty, root_folder
from carbonmail.carbon.manager import download_image


def validate_email_sending(window, code_path, title, content, list_name):
    contacts = get_list_contacts(list_name)

    if not path.isfile(code_path):
        return -2

    if string_null_or_empty(title) or string_null_or_empty(content):
        return -1

    if not contacts or len(contacts) == 0:
        return 0

    threading.Thread(
        target=send_mass_email,
        args=(window, contacts, title, content, code_path),
    ).start()


def send_mass_email(window, contacts, title, content, code_path):
    image_path = download_image(code_path)

    for contact in contacts:
        send_email(contact, title, content, image_path)

    window.write_event_value("-Thread-", "Done")


def send_email(contact, title, content, image_path):
    config = AutoConfig(search_path=root_folder())

    SMTP_USER = config("SMTP_USER")
    SMTP_PASSWORD = config("SMTP_PASSWORD")
    SMTP_SERVER = config("SMTP_SERVER")
    SMTP_PORT = config("SMTP_PORT")

    image_data = open(image_path, "rb").read()

    message = MIMEMultipart()
    message["Subject"] = title
    message["From"] = SMTP_USER
    message["To"] = f"{contact[0]} <{contact[1]}>"

    body = MIMEText(content)
    message.attach(body)

    image = MIMEImage(image_data, name=os.path.basename(image_path))
    message.attach(image)

    context = ssl.create_default_context()
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls(context=context)
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.sendmail(SMTP_USER, contact, message.as_string())

    print(f"Enviou e-mail para: {contact[0]} <{contact[1]}>")


def initialize():
    from carbonmail.email_sender import Email_Sender

    ms = Email_Sender()
    ms.enable_window()
