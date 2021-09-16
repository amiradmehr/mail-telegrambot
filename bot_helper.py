from telebot import types


def send_request(message):
    request = message.text.split()
    if len(request) < 3 or request[0].lower() not in "send":
        return False
    else:
        return True





def sheet_request(message):
    request = message.text.split()
    if len(request) < 2 or request[0].lower() not in "sheet":
        return False
    else:
        return True




class Markups:

    def __init__(self):
        pass

    def start(self):
        markup = types.ReplyKeyboardMarkup(row_width=2)
        itembtn1 = types.KeyboardButton('send US 1')
        itembtn2 = types.KeyboardButton('send CA 1')
        itembtn3 = types.KeyboardButton('send US 10')
        itembtn4 = types.KeyboardButton('send CA 10')
        itembtn5 = types.KeyboardButton('sheet US')
        itembtn6 = types.KeyboardButton('sheet CA')
        markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6)

        return markup