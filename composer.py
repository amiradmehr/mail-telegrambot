from time import sleep
from datetime import date
from gmail import Gmail
from gsheet import Gsheet
from templates import Templates
import os
from dotenv import load_dotenv
import schedule
import getopt, sys
from helper import progressBar
load_dotenv()

EMAIL_ADDRESS = os.getenv('EMAIL')
EMAIL_PASSWORD = os.getenv('PASSWORD')

CREDENTIALS = os.getenv('CREDENTIALS')
SHEET_NAME = os.getenv('SHEET_NAME')
WORKBOOK_NAME = os.getenv('WORKBOOK_NAME')
CV = os.getenv('CV')


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

        mygmail.send_email(to,EMAIL_ADDRESS,subject,text, file=CV)

        recievers.iloc[i]['Log'] = 'sent'
        recievers.iloc[i]['Date'] = today

        mysheet.update_df(recievers)
        mysheet.update()
        sleep(.2)
        
    print(f"Done emailing for {today}")
    print("-----------\n")

def job():
    print("I'm working...")

if __name__ == '__main__':

    argumentList = sys.argv[1:]
    
    options = "c:w:n:t"
    long_options = ["Clock=", "Workbook=", "Num=","Test"]
    
    try:
        arguments, values = getopt.getopt(argumentList, options, long_options)
        
        for currentArgument, currentValue in arguments:
    
            if currentArgument in ("-c", "--Clock"):
                clock = currentValue
                
            elif currentArgument in ("-w", "--Workbook"):
                WORKBOOK_NAME = currentValue
                
            elif currentArgument in ("-n", "--Num"):
                num = int(currentValue)

            elif currentArgument in ("-t", "--Test"):
                print("test mdoe:")
                for i in range(10):
                    sleep(1)
                    progressBar(i,10)

                compose(WORKBOOK_NAME,num)
                
    except getopt.error as err:
        print (str(err))

    try:
        schedule.every().monday.at(clock).do(compose, WORKBOOK_NAME, num)
        schedule.every().tuesday.at(clock).do(compose, WORKBOOK_NAME, num)
        schedule.every().wednesday.at(clock).do(compose, WORKBOOK_NAME, num)
        schedule.every().thursday.at(clock).do(compose, WORKBOOK_NAME, num)
        schedule.every().friday.at(clock).do(compose, WORKBOOK_NAME, num)
        print(f"Scheduled at {clock}")
        while True:
            schedule.run_pending()
            sleep(1)

    except NameError:
        print("Enter all arguments correctly")
    

    
