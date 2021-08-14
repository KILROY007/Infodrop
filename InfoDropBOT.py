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
    bot.reply_to(message, 'Hi!There Welcome To Department Of ISE-BOT \n\n Lets get started \n Select the study material you need \n\n /Lab_Manuals \n\n /Question_Banks\n\n /Notes')

@bot.message_handler(commands=['Lab_Manuals'])
def send_lab_manuals(message):
    bot.reply_to(message, 'Select the semister \n\n /3rd_lab \n\n /4th_lab \n\n /5th_lab \n\n /6th_lab \n\n /7th_lab\n\n /Go_Back')

@bot.message_handler(commands=['Go_Back'])
def go_back(message):
    bot.reply_to(message, 'Hi!There Welcome To Department Of ISE-BOT \n\n Lets get started \n Select the study material you need \n\n /Lab_Manuals \n\n /Question_Banks\n\n /Notes')

@bot.message_handler(commands=['3rd_lab'])
def send_3rd_lab(message):
    bot.reply_to(message, 'https://cloud.ewitise.org.in/index.php/s/9cWNXqQSCLFZcSm?path=%2FLab%20Manuals%2F3rd%20Sem')
    
@bot.message_handler(commands=['4th_lab'])
def send_4th_lab(message):
    bot.reply_to(message, 'https://cloud.ewitise.org.in/index.php/s/9cWNXqQSCLFZcSm?path=%2FLab%20Manuals%2F4th%20sem')

@bot.message_handler(commands=['5th_lab'])
def send_5th_lab(message):
    bot.reply_to(message, 'https://cloud.ewitise.org.in/index.php/s/9cWNXqQSCLFZcSm?path=%2FLab%20Manuals%2F5th%20Sem')

@bot.message_handler(commands=['6th_lab'])
def send_6th_lab(message):
    bot.reply_to(message, 'https://cloud.ewitise.org.in/index.php/s/9cWNXqQSCLFZcSm?path=%2FLab%20Manuals%2F6th%20Sem')

@bot.message_handler(commands=['7th_lab'])
def send_7th_lab(message):
    bot.reply_to(message, 'https://cloud.ewitise.org.in/index.php/s/9cWNXqQSCLFZcSm?path=%2FLab%20Manuals%2F7th%20Sem')

@bot.message_handler(commands=['Question_Banks'])
def send_question_banks(message):
    bot.reply_to(message,'https://cloud.ewitise.org.in/index.php/s/9cWNXqQSCLFZcSm?path=%2FQuestion%20Banks')

@bot.message_handler(commands=['Notes'])
def send_notes(message):
    bot.reply_to(message,'Select the semister \n\n /3rd \n\n /4th \n\n /5th \n\n /6th \n\n /7th \n\n /8th /Go_Back')

@bot.message_handler(commands=['3rd'])
def send_3rd(message):
    bot.reply_to(message,'https://cloud.ewitise.org.in/index.php/s/9cWNXqQSCLFZcSm?path=%2FStudy%20Materials%2F3rd%20Semester')

@bot.message_handler(commands=['4th'])
def send_4th(message):
    bot.reply_to(message,'Will be updated soon..')

@bot.message_handler(commands=['5th'])
def send_5th(message):
    bot.reply_to(message,'https://cloud.ewitise.org.in/index.php/s/9cWNXqQSCLFZcSm?path=%2FStudy%20Materials%2F5th%20Semester')

@bot.message_handler(commands=['6th'])
def send_6th(message):
    bot.send_message(message,'Will be updated soon..')

@bot.message_handler(commands=['7th'])
def send_7th(message):
    bot.send_message(message,'https://cloud.ewitise.org.in/index.php/s/9cWNXqQSCLFZcSm?path=%2FStudy%20Materials%2F7th%20Semester')

@bot.message_handler(commands=['8th'])
def send_8th(message):
    bot.send_message(message,'Will be updated soon..')
    

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