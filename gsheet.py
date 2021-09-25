import gspread
import pandas as pd
from helper import progressBar
from time import sleep
from copy import deepcopy

class Gsheet:

    def __init__(self, creds, sh_name, ws_name):

        try:
            gc = gspread.service_account(filename=creds)
            self.sh = gc.open(sh_name)
            self.ws = self.sh.worksheet(ws_name)
            self.res = self.ws.get_all_records()
            self.res = pd.DataFrame(self.res)
            del self.res['Link']
            print("Connected to GOOGLE SHEET successfully")
            self.connection = True
        except:
            self.connection = False
            print("\nCan't connect to GOOGLE SHEET")
        
    def updatechanges(self):
        self.res = self.ws.get_all_records()
        self.res = pd.DataFrame(self.res)

    def save_sheet(self):
        self.res.to_excel("apply.xlsx")
        return self.res

    
    def update(self):
        self.ws.update([self.res.columns.values.tolist()] + self.res.values.tolist())
        return True

    
    def fill_duplicates(self):
        emails = self.res['Email']
        duplicates = emails.duplicated(keep='first')
        self.res.at[list(duplicates),'Log'] = 'sent'


    def get_rows(self, num):

        df = deepcopy(self.res)

        index_names = df[df[ 'Subject I'] == '' ].index
        df.drop(index_names, inplace = True)

        rows = df.loc[df['Log']!='sent']
        n_rows = rows.shape[0]

        if n_rows > num:
            rows = rows.iloc[range(num)]
        
        return rows

    def update_df(self, rows):
        self.res.update(rows)


