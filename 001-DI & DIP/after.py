import smtplib
from abc import ABC, abstractmethod
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import requests


class RequestClientAbc(ABC):
    @abstractmethod
    def send_request(self, url: str) -> str:
        pass


class MailClientAbc(ABC):
    @abstractmethod
    def send_mail(self, message: str) -> None:
        pass


class HttpSender(RequestClientAbc):
    def send_request(self, url: str) -> str:
        return requests.get(url).text


class SmtpLibMailClient(MailClientAbc):
    def __init__(self, to, _from):
        self.to = to
        self._from = _from

    def send_mail(self, message: str) -> None:
        msg = MIMEMultipart("alternative")
        msg["Subject"] = "An example email"
        msg["From"] = self._from
        msg["To"] = self.to
        msg.attach(MIMEText(f"Mail sent with message: {message}"))
        s = smtplib.SMTP("localhost", port=0)
        s.send_message(msg)
        s.quit()


class DataProcessor:
    def __init__(self, mailer: MailClientAbc, request_sender: RequestClientAbc) -> None:
        self.mailer = mailer
        self.request_sender = request_sender

    def process_and_mail_data(self, url: str) -> None:
        response_data = self.request_sender.send_request(url)
        processed_data = response_data.upper()  # Simple data processing
        self.mailer.send_mail(f"Processed Data: {processed_data}")


processor = DataProcessor(
    # Performed DI HERE!
    mailer=SmtpLibMailClient(
        to="dorcci@gmail.com",
        _from="ma_inja_darim_zahmat_mikeshim@gmail.com",
    ),
    request_sender=HttpSender(),
    # ---
)
processor.process_and_mail_data("http://example.com")
