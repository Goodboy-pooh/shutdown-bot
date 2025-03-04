import os
import logging
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler

# Load environment variables
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    print("Error: BOT_TOKEN not found. Check your .env file.")
    exit(1)

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

async def start(update: Update, _context):
    await update.message.reply_text("Hello! I can control your system remotely. Use /shutdown, /restart, or /cancel.")

async def shutdown(update: Update, _context):
    await update.message.reply_text("Shutting down the system in 30 seconds. Use /cancel to abort.")
    os.system("shutdown /s /t 30")

async def restart(update: Update, _context):
    await update.message.reply_text("Restarting the system in 30 seconds. Use /cancel to abort.")
    os.system("shutdown /r /t 30")

async def cancel(update: Update, _context):
    await update.message.reply_text("Shutdown/Restart canceled.")
    os.system("shutdown /a")

def main():
    print("Bot is starting...")

    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("shutdown", shutdown))
    application.add_handler(CommandHandler("restart", restart))
    application.add_handler(CommandHandler("cancel", cancel))

    print("Bot is running...")
    application.run_polling()

if __name__ == "__main__":
    main()
