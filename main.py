import logging
from dotenv import load_dotenv
load_dotenv()
import os
from gsheet import Gsheet



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

def test():
    mysheet = Gsheet(CREDENTIALS, SHEET_NAME, 'US')

    while True:

        a = input('press')
        if a =='s':
            mysheet.updatechanges()
            print(mysheet.res)
            

        else:
            pass


if __name__ == '__main__':
    test()