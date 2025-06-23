import os
from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_text('¡Hola! Soy un bot en Fly.io')

def main():
    token = os.environ.get('8002085886:AAGvphg93iBGqSc9KiQcueounUUUd3L1kkg')
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()