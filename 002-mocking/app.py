import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from uuid import uuid4

from fastapi import Body, Depends, FastAPI

app = FastAPI()


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


def get_mailer() -> Mailer:
    return Mailer("admin@gmail.com")


@app.post("/forget-password/")
async def forget_password(
    email: str = Body(),
    mailer: Mailer = Depends(get_mailer),
):
    message = f"Your password link is {uuid4()}"
    await mailer.send_mail(message, email)
