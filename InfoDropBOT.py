import os
from flask import Flask, request
import telebot

TOKEN = "1310851601:AAHAbO1LKPZkaV0a6m_rVV2ZkvOAUsfHJmY"
bot = telebot.TeleBot(token=TOKEN)
server = Flask(__name__)

def findat(msg):
    for i in msg:
        if '@' in i:
            return i

@bot.message_handler(commands=['start']) 
def send_welcome(message):
    bot.reply_to(message, 'Hi!There Welcome To Department Of ISE-BOT \n  Lets get started \n Select the study material you need \n /Lab_Manuals \n /Question_Banks \n /Notes')


@bot.message_handler(commands=['Lab_Manuals'])
def send_lab(message)
    bot.reply_to(message, 'Select the seminster \n /3rd_lab \n /4th_lab \n /5th_lab \n /6th_lab \n /7th_lab')

@bot.message_handler(commands=['3rd_lab'])
def send_3rd_lab(message)
    bot.reply_to(message, 'https://cloud.ewitise.org.in/index.php/s/9cWNXqQSCLFZcSm?path=%2FLab%20Manuals%2F3rd%20Sem')

@bot.message_handler(commands=['help']) 
def send_help(message):
    bot.reply_to(message, "Type The Name Of The Of The Subject for example[*@DBMS*]")

@bot.message_handler(func=lambda msg: msg.text is not None and '@' in msg.text)
def at_converter(message):
    texts = message.text.split()
    at_text = findat(texts)
    if at_text == '@': 
        pass
    else:
        drive_link = "https://patient-union-0c47.kilroy1969.workers.dev/0:search?q={}".format(at_text[1:])
        bot.reply_to(message, drive_link)

@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://infodrop007.herokuapp.com/' + TOKEN)
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))