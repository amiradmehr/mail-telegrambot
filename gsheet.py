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
        df = deepcopy(self.res.loc[:,self.res.columns != 'Counter'])
        df = deepcopy(df.loc[:,df.columns != 'Reply'])
        df = deepcopy(df.loc[:,df.columns != 'Conclusion'])

        self.ws.update([df.columns.values.tolist()] + df.values.tolist())
        return True

    
    def fill_duplicates(self):
        df = deepcopy(self.res)

        index_names = df[df['Email'] == '' ].index
        df.drop(index_names, inplace = True)

        # emails = self.res['Email']
        emails = df['Email']
        duplicates = emails.duplicated(keep='first')
        df.at[list(duplicates),'Log'] = 'sent'
        # self.res.at[list(duplicates),'Log'] = 'sent'
        self.res.update(df)


    def get_rows(self, num):

        df = deepcopy(self.res)

        index_names = df[df['CV'] == '' ].index
        df.drop(index_names, inplace = True)

        rows = df.loc[df['Log']!='sent']
        n_rows = rows.shape[0]

        if n_rows > num:
            rows = rows.iloc[range(num)]
        
        return rows

    def update_df(self, rows):
        self.res.update(rows)


