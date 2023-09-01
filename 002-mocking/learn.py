import asyncio
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from unittest.mock import AsyncMock


async def side_effect_func(*args, **kwargs):
    print(f"Called with args: {args}, kwargs: {kwargs}")


class Mailer:
    def __init__(self, _from):
        self._from = _from

    async def send_mail(self, message: str, to: str) -> None:
        msg = MIMEMultipart("alternative")
        msg["Subject"] = "An example email"
        msg["From"] = self._from
        msg["To"] = to
        msg.attach(MIMEText(f"Mail sent with message: {message}"))
        s = smtplib.SMTP("localhost", port=0)
        s.send_message(msg)
        s.quit()


async def main(mailer: Mailer):
    await mailer.send_mail(message="Something", to="sender@gmail.com")


real_obj = Mailer("admin@gmail.com")

mock = AsyncMock(spec=Mailer)
mock.send_mail.side_effect = side_effect_func

asyncio.run(main(mock))
