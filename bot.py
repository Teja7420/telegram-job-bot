from telegram import Update

from telegram.ext import Application
from telegram.ext import MessageHandler
from telegram.ext import filters
from telegram.ext import ContextTypes

from config import BOT_TOKEN

from validator import validate_email

from template import email_template

from email_service import send_email


async def receive(update: Update, context: ContextTypes.DEFAULT_TYPE):

    hr_email = update.message.text.strip()

    if not validate_email(hr_email):

        await update.message.reply_text("❌ Invalid Email Address")

        return

    body = email_template()

    try:

        send_email(hr_email, body)

        await update.message.reply_text(
            "✅ Application Sent Successfully"
        )

    except Exception as e:

        await update.message.reply_text(str(e))


app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(

    MessageHandler(filters.TEXT, receive)

)

print("Bot Started...")

app.run_polling()