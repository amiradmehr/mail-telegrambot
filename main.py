from time import sleep, time
from datetime import date

import requests
from gmail import Gmail
from gsheet import Gsheet
from templates import Templates
import os
from dotenv import load_dotenv
import telebot
load_dotenv()


TOKEN = os.getenv('TOKEN')

EMAIL_ADDRESS = os.getenv('EMAIL')
EMAIL_PASSWORD = os.getenv('PASSWORD')

CREDENTIALS = os.getenv('CREDENTIALS')
SHEET_NAME = os.getenv('SHEET_NAME')
WORKBOOK_NAME = os.getenv('WORKBOOK_NAME')
CV = os.getenv('CV')

def main():
    while True:
        state = input("What do you want me to do?")

        if state == 'send now':
            pass
        else:
            print('command not recognized')


def compose(ws_name, num = 20):
    mysheet = Gsheet(CREDENTIALS, SHEET_NAME, ws_name)
    mygmail = Gmail(EMAIL_ADDRESS, EMAIL_PASSWORD)

    mysheet.save_sheet()
    mysheet.fill_duplicates()
    mysheet.update()

    recievers = mysheet.get_rows(num)

    today = date.today().strftime("%d-%b")

    for i in range(recievers.shape[0]):

        to = recievers.iloc[i]['Email']
        professor = recievers.iloc[i]['Name']
        topic = recievers.iloc[i]['Topic']
        paper = recievers.iloc[i]['Paper']
        subject = 'Looking for position'
        template_number = int(recievers.iloc[i]['Template'])

        text = Templates(template_number).get(prof=professor,topic=topic,paper=paper)

        sent_to = mygmail.send_email(to,EMAIL_ADDRESS,subject,text, file=CV)

        recievers.at[i,'Log'] = 'sent'
        recievers.at[i,'Date'] = f'{today}'

        mysheet.update_df(recievers)
        mysheet.update()
        sleep(.2)

    mygmail.close_gmail() 
    print(f"Done emailing for {today}")
    print("-----------\n")

def email_num_request(message):
    request = message.text.split()
    if len(request) < 3 or request[0].lower() not in "send":
        return False
    else:
        return True
        # send US 3

def telegrambot():

    bot = telebot.TeleBot(TOKEN)
    print('Robot is intialized')



    @bot.message_handler(commands=['help'])
    def send_welcome(message):
        help_txt = 'this is mail bot'
        bot.send_message(message.chat.id, help_txt)

    @bot.message_handler(func=email_num_request)
    def composer(message):

        bot.send_message(message.chat.id, "Connecting to server ...")
        num = int(message.text.split()[2])
        ws_name = message.text.split()[1]
        mysheet = Gsheet(CREDENTIALS, SHEET_NAME, ws_name)
        mygmail = Gmail(EMAIL_ADDRESS, EMAIL_PASSWORD)


        bot.send_message(message.chat.id, "connected to servers successfully")

        mysheet.save_sheet()
        mysheet.fill_duplicates()
        mysheet.update()

        recievers = mysheet.get_rows(num)

        today = date.today().strftime("%d-%b")

        for i in range(recievers.shape[0]):

            to = recievers.iloc[i]['Email']
            professor = recievers.iloc[i]['Name']
            topic = recievers.iloc[i]['Topic']
            paper = recievers.iloc[i]['Paper']
            subject = 'Looking for position'
            template_number = int(recievers.iloc[i]['Template'])

            text = Templates(template_number).get(prof=professor,topic=topic,paper=paper)

            sent_to = mygmail.send_email(to,EMAIL_ADDRESS,subject,text, file=CV)
            bot.send_message(message.chat.id, sent_to)
            recievers.at[i,'Log'] = 'sent'
            recievers.at[i,'Date'] = f'{today}'

            mysheet.update_df(recievers)
            mysheet.update()
            sleep(.2)

        mygmail.close_gmail() 
        bot.send_message(message.chat.id,f"Done emailing for {today}")




    bot.polling()


if __name__ == '__main__':
    telegrambot()