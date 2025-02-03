import os
import telebot
from flask import Flask

# API_KEY = '6239324931:AAGt2JngWrgwxZWGB-dC_7EdZqX4x4HYp0g'
# bot = telebot.TeleBot(API_KEY)
from yallasrvc_bot import bot

# Your Telegram bot handlers here...

# Flask app to serve HTTP traffic, required for Render
app = Flask(__name__)

@app.route('/')
def index():
    return 'Bot is running!'

def start_bot():
    try:
        bot.polling()
    except:
        print(f"Error occurred!")
        bot.polling()

if __name__ == '__main__':
    from threading import Thread
    # Run bot in a separate thread
    bot_thread = Thread(target=start_bot)
    bot_thread.start()
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080))) 
