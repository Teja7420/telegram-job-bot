import smtplib

from email.message import EmailMessage

from config import EMAIL
from config import APP_PASSWORD
from config import SUBJECT
from config import RESUME_PATH


def send_email(receiver_email, body):

    msg = EmailMessage()

    msg["Subject"] = SUBJECT

    msg["From"] = EMAIL

    msg["To"] = receiver_email

    msg.set_content(body)

    with open(RESUME_PATH, "rb") as file:

        msg.add_attachment(
            file.read(),
            maintype="application",
            subtype="pdf",
            filename="Teja_Resume.pdf"
        )

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:

        smtp.starttls()

        smtp.login(EMAIL, APP_PASSWORD)

        smtp.send_message(msg)