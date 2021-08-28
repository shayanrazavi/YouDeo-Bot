from __future__ import unicode_literals
from telegram.ext import *
from pytube import YouTube
api_key="1999704554:AAGgpjH1X6kLY80jfZdartzShCUouVo8zFE"
print('bot started')

def start_command(update,context):
    update.message.reply_text('Hi . welcome :)You can use this bot to download the videos you want on YouTube :) All you have to do is enter the URL of the video you want.')
def help_command(update,context):
    update.message.reply_text('Im busy right now. Solve the problem yourself.')

def sample_response(text_input):
    user_message=str(text_input).lower()
    yt = YouTube(user_message)
    return ("Title: ",yt.title,"Number of views: ",yt.views,"Length of video: ",yt.length,"Rating of video: ",yt.rating)

def handle_message(update,context):
    text=str(update.message.text)
    response_text=sample_response(text)
    update.message.reply_text(response_text)

updater=Updater(api_key,use_context=True)
dp=updater.dispatcher

dp.add_handler(CommandHandler("start",start_command))
dp.add_handler(CommandHandler("help",help_command))
dp.add_handler(MessageHandler(Filters.text, handle_message))


updater.start_polling()
updater.idle()
