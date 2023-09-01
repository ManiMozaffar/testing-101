import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import requests


class DataProcessor:
    def process_and_mail_data(self, url: str, to: str, _from: str) -> None:
        # Sending request
        response_data = requests.get(url).text

        # Processing data
        processed_data = response_data.upper()

        # Sending mail
        msg = MIMEMultipart("alternative")
        msg["Subject"] = "An example email"
        msg["From"] = _from
        msg["To"] = to
        msg.attach(MIMEText(f"Mail sent with message: {processed_data}"))
        s = smtplib.SMTP("localhost", port=0)
        s.send_message(msg)
        s.quit()


processor = DataProcessor()
processor.process_and_mail_data(
    url="http://example.com",
    to="dorcci@gmail.com",
    _from="ma_inja_darim_zahmat_mikeshim@gmail.com",
)
