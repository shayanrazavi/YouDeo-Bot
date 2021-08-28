from telegram.ext import *

api_key="1777223953:AAHR0WuIhxYRV6ZbJmOAd_2H8648jtxeG_E"
print("bot started")

def start_command(update,context):
    update.message.reply_text("type:")

def help_command(update,context):
    update.message.reply_text("help!!!")

def sample_response(text_input):
    user_message = str(text_input).lower()
    #HI-->hi
    if user_message in ("hi","hello"):
        return ("how are you")
    return "I dont understand you"

def handle_message(update,context):
    text=str(update.message.text)    
    response_text=sample_response(text)
    update.message.reply_text(response_text)

updater=Updater(api_key,use_context=True)
dp=updater.dispatcher

dp.add_handler(CommandHandler("start",start_command))
dp.add_handler(CommandHandler("help",help_command))    
dp.add_handler(MessageHandler(Filters.text,handle_message))

updater.start_polling()
updater.idle()
