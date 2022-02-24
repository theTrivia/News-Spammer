from decouple import config
import smtplib,ssl

from MailFormat import MailFormat


class MailSender:
    SENDER = config('SENDER')
    PASSWORD = config('PASSWORD')
    RECEIVER = config('RECEIVER')

    subject = 'Your Daily Headlines :)'

    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls


    def __init__(self):
        self.mailFormatter = MailFormat()
        self.content = self.mailFormatter.mailFormatter()
        self.context = ssl.create_default_context()

    def sendMail(self):
        try:
            server = smtplib.SMTP(self.smtp_server, self.port)
            server.starttls(context=self.context)  # Secure the connection
            server.login(self.SENDER, self.PASSWORD)
            server.sendmail(self.SENDER, self.RECEIVER, self.content)
        except Exception as e:
            print(e)
        finally:
            server.quit()


