import logging

from telegram import Update
from telegram.ext import (
    Application,
    MessageHandler,
    CommandHandler,
    ContextTypes,
    filters,
)

from config import BOT_TOKEN
from validator import validate_email
from template import email_template
from email_service import send_email

# Logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome!\n\n"
        "Send me an HR email address.\n\n"
        "Example:\n"
        "hr@company.com"
    )


async def receive(update: Update, context: ContextTypes.DEFAULT_TYPE):
    hr_email = update.message.text.strip()

    if not validate_email(hr_email):
        await update.message.reply_text("❌ Invalid Email Address")
        return

    body = email_template()

    try:
        send_email(hr_email, body)

        await update.message.reply_text(
            f"✅ Application Sent Successfully\n\n📧 {hr_email}"
        )

        logger.info(f"Email sent to {hr_email}")

    except Exception as e:
        logger.exception("Email sending failed")

        await update.message.reply_text(
            f"❌ Failed to send email.\n\n{e}"
        )


def main():
    logger.info("🤖 Bot Started...")

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, receive))

    app.run_polling()


if __name__ == "__main__":
    main()