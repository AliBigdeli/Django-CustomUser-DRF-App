from django.core.mail import EmailMessage
import threading
from templated_mail.mail import BaseEmailMessage
class EmailThread(threading.Thread):

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()
class TemplateEmailThread(threading.Thread):

    def __init__(self, email_obj,email):
        self.email_obj = email_obj
        self.email = [email]
        threading.Thread.__init__(self)

    def run(self):
        self.email_obj.send(self.email)
class Util:
    @staticmethod
    def send_email(data):
        email = EmailMessage(
            subject=data['email_subject'], body=data['email_body'], to=[data['to_email']])
        EmailThread(email).start()

    @staticmethod
    def send_templated_email(template_path,data):
        email = BaseEmailMessage(template_name=template_path,context = data)
        TemplateEmailThread(email,data["email"]).start()

