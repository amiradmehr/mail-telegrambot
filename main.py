from time import sleep, time
from datetime import date
from gmail import Gmail
from gsheet import Gsheet
from templates import Templates
import os
from dotenv import load_dotenv
import telebot
from telebot import types
from bot_helper import Markups, sheet_request, send_request 
load_dotenv()


TOKEN = os.getenv('TOKEN')

EMAIL_ADDRESS = os.getenv('EMAIL')
EMAIL_PASSWORD = os.getenv('PASSWORD')

CREDENTIALS = os.getenv('CREDENTIALS')
SHEET_NAME = os.getenv('SHEET_NAME')
CV = os.getenv('CV')


'''
things that can go wrong:
    user doesnt send the credentials
    credential name is not correct
    user havent paid the fee
    user hasnt created the columns correctly




'''


def telegrambot():

    bot = telebot.TeleBot(token=TOKEN)
    print('Robot is intialized')
    markups = Markups()





# handle help and start command
    @bot.message_handler(commands=['help', 'start'])
    def send_welcome(message):
        help_txt = '''
        This is telemail
        you need to create a google sheet with columns names:
        Name
        
        '''
        bot.send_message(message.chat.id, help_txt, reply_markup=markups.start())




# handle composer
    @bot.message_handler(func=send_request)
    def composer(message):

        bot.send_message(message.chat.id, "Connecting to server ...")
        # bot.send_message(message.chat.id, f"{message}")

        # split command line
        num = int(message.text.split()[2])
        ws_name = message.text.split()[1]

        mysheet = Gsheet(CREDENTIALS, SHEET_NAME, ws_name)
        mygmail = Gmail(EMAIL_ADDRESS, EMAIL_PASSWORD)

        
        if mysheet.connection and mygmail.connection:
            bot.send_message(message.chat.id, "connected to Google successfully")

            mysheet.save_sheet()
            mysheet.fill_duplicates()
            mysheet.update()

            recievers = mysheet.get_rows(num)

            today = date.today().strftime("%d-%b")

            for i in range(recievers.shape[0]):


                # extract column values
                to = recievers.iloc[i]['Email']
                professor = recievers.iloc[i]['Name']
                topic = recievers.iloc[i]['Topic']
                paper = recievers.iloc[i]['Paper']
                if ws_name == 'US':
                    subject = 'Prospective graduate student interested in ' + recievers.iloc[i]['Subject']
                elif ws_name == 'CA':
                    subject = 'Prospective master student interested in ' + recievers.iloc[i]['Subject']
                else:
                    subject = ''
                template_number = int(recievers.iloc[i]['Template'])
                cv_num = int(recievers.iloc[i]['CV'])
                
                cv = f'CV/CV{cv_num}/CV.pdf'
                text = Templates(template_number).get(prof=professor,topic=topic,paper=paper)

                send_success_failure_message, send_flag = mygmail.send_email(to,EMAIL_ADDRESS,subject,text, file=cv)
                bot.send_message(message.chat.id, send_success_failure_message)
                if send_flag:
                    recievers.iloc[i,recievers.columns.get_loc('Log')] = 'sent'
                    recievers.iloc[i,recievers.columns.get_loc('Date')] = f'{today}'


                mysheet.update_df(recievers)
                mysheet.update()
                sleep(.2)

            mygmail.close_gmail() 
            bot.send_message(message.chat.id,f"Done emailing for {today}")
        else:
            mygmail.close_gmail()
            bot.send_message(message.chat.id, "failed to connect")
    
    @bot.message_handler(func=sheet_request)
    def get_sheet(message):
        ws_name = message.text.split()[1]
        mysheet = Gsheet(CREDENTIALS, SHEET_NAME, ws_name)
        if mysheet.connection:
            try:
                bot.send_message(message.chat.id, f"{mysheet.res[['Name','Log','Date']]}")
            except:
                bot.send_message(message.chat.id, "There is something wrong with sheet indexing")
        else:
            bot.send_message(message.chat.id, f"Connection Failed or sheet named \"{ws_name}\" is not available")


    bot.infinity_polling()


if __name__ == '__main__':
    telegrambot()