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
        markup = types.ReplyKeyboardMarkup(row_width=1)
        itembtn1 = types.KeyboardButton('send US 1')
        itembtn2 = types.KeyboardButton('send US 10')
        itembtn3 = types.KeyboardButton('sheet US')
        markup.add(itembtn1, itembtn2, itembtn3)

        return markup