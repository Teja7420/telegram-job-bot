from email_service import send_email
from template import email_template

send_email(
    "your_other_email@gmail.com",
    email_template()
)

print("Email Sent Successfully")