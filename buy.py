from config import bot, provider_token
import requests
from telebot.types import LabeledPrice
from data import textbuy
from keyboard import keyboard_main_menu
import os
global amount, user
import json

"""
def buy_qiwi(self):
        global amount
        pprint("asdasdasdasdasd")
        markup_buy = telebot.types.InlineKeyboardMarkup()
        markup_check = telebot.types.InlineKeyboardMarkup()
        comment = str(self.id)
        try:
            pprint(users[str(self.id)]["but_qiwi_date"])
        except:
            self.user["but_qiwi_date"] = "0"
            self.user["but_qiwi_date_down"] = "0"
        try:
            pprint(self.user["buy_qiwi_check"])
        except:
            self.user["buy_qiwi_check"] = 1
        pprint(self.user["buy_qiwi_check"])
        pprint(users[str(self.id)]["but_qiwi_date"])

        if self.user["buy_qiwi_check"] == 0 and date("utctime") < users[str(self.id)]["but_qiwi_date"]:
            markup_check.add(telebot.types.InlineKeyboardButton(text='Проверить платеж', callback_data="buy_qiwi"))
            text = "Проверить платеж"
            bot.send_message(self.id, text, reply_markup=markup_check)

        elif self.user["but_qiwi_date_down"] > date("utctime"):
            bot.send_message(self.id,
                             text="Вы уже создали счет на оплату, оплатите его или повторите попытку через час")
            markup_check.add(telebot.types.InlineKeyboardButton(text='Проверить платеж', callback_data="buy_qiwi"))
            text = "Проверить платеж"
            bot.send_message(self.id, text, reply_markup=markup_check)
        else:
            pprint("bnbnbnnb")
            markup_buy.add(telebot.types.InlineKeyboardButton(text='Оплатить',
                                                              url="https://oplata.qiwi.com/create?publicKey=" + publicKey +
                                                                  "&amount=" + str(
                                                                  int(
                                                                      self.text) * 1) + "&comment=" + comment + "&customFields[themeCode]=Konstantyn-PbboM7ch_P&successUrl=https%3A%2F%2Ft.me%2FHeroesLifeBot&lifetime=" + date(
                                                                  'buyqiwi')))
            self.user["buy_qiwi_tranzaction"] = 0
            self.user["buy_qiwi_comment"] = comment
            self.user["buy_qiwi_amount"] = int(self.text)
            self.user["but_qiwi_date_down"] = date('buytimedown')
            self.user["but_qiwi_date_up"] = date('buytimeup')
            self.user["buy_qiwi_check"] = 0
            pprint("asdasd")
            text = "Для покупки " + str(int(self.text)) + " 💎 нажмите на кнопку ниже \nПокупка на сумму " + str(
                int(self.text) * 10) + " руб."
            pprint("zxczxc")
            bot.send_message(self.id, text, reply_markup=markup_buy)
            markup_check.add(telebot.types.InlineKeyboardButton(text='Проверить платеж', callback_data="buy_qiwi"))
            text = "Проверить платеж"
            bot.send_message(self.id, text, reply_markup=markup_check)
        save("users")

def buy_check_qiwi(self):
        api_access_token = '9f5335d8b6e7d3bfdc336db48a160a17'
        mylogin = '79233044552'

        comment = str(self.id)
        lastPayments = self.payment_history_last(mylogin, api_access_token, '3', '', '', comment)
        #        pprint(lastPayments)
        #        pprint(lastPayments)

        for i in range(len(lastPayments['data'])):
            comment = lastPayments['data'][i]['comment']
            status = lastPayments['data'][i]['status']
            txnId = lastPayments['data'][i]['txnId']
            amount = lastPayments['data'][i]['sum']['amount']
            date = lastPayments['data'][i]['date']

            if comment == str(self.id) and status == 'SUCCESS':
                if users[str(self.id)]["but_qiwi_date_down"] < date < users[str(self.id)]["but_qiwi_date_up"]:
                    if self.user["buy_qiwi_check"] == 0:
                        pprint("Платеж прошел успешно")
                        bot.send_message(self.id, "Счет " + str(txnId) + " на сумму " + str(
                            amount) + " руб " + date + ". Оплачен",
                                         reply_markup=keyboard_info())
                        users[str(self.id)]["but_qiwi_date"] = "0"
                        self.user["buy_qiwi_check"] = 1
                        buy_gold = int(amount)
                        users[str(self.id)]["diamond"] = users[str(self.id)]["diamond"] + buy_gold
                    else:
                        bot.send_message(self.id, "Начисление уже было произведено")
                        break
            #       else:
            #            bot.send_message(self.id, "Счет не был оплачен во время")
            else:
                bot.send_message(self.id, "Счет на сумму " + str(amount) + " руб " + date + ". Не оплачен",
                                 reply_markup=keyboard_main_menu())

        #                pprint("Чужой счет " + str(txnId) + " на сумму " + str(amount) + " руб. Оплачен")
        #            pprint(lastPayments['data'][i]['txnId'])
        #            pprint(lastPayments['data'][i]['comment'])
        #            pprint(lastPayments['data'][i]['sum']['amount'])
        #            pprint(lastPayments['data'][i]['date'])

        st = lastPayments['data'][0]['status']
        txnId = lastPayments['data'][0]['txnId']
        s = lastPayments['data'][0]['sum']['amount']
        commentId = lastPayments['data'][0]['comment']
        comment = users[str(self.id)]["buy_qiwi_comment"]
        save("all")

   
        if users[str(self.id)]["buy_qiwi_tranzaction"] == txnId:
            bot.send_message(self.id, 'Нет выставленных счетов на оплату')

        elif st == 'SUCCESS' and comment == commentId:
            bot.send_message(self.id, 'Ура! Спасибо за оплату! Заказ на сумму '+str(s)+' руб.')
            buy_gold = int(s)
            users[str(self.id)]["gold"] = users[str(self.id)]["gold"] + buy_gold
            users[str(self.id)]["buy_qiwi_tranzaction"] = txnId
            save("all")

        else:
            bot.send_message(self.id, "Платеж не прошел, оплатите счет")

        pprint(st)
    """
def find_location():
    return os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))).replace('\\', '/') + '/'
PATH = find_location()

def save_buy():
    global users
    with open(PATH + "tmp/" + 'users.json', 'w', encoding="utf-16") as f:
        json.dump(users, f)
def open_buy():
    global users
    with open(PATH + "tmp/" + 'users.json', 'rb') as f:
            users = json.load(f)

def buy_amount(message):
    if message.text == "Tranzzo":
        bot.send_message(text=textbuy, chat_id=message.chat.id)
        bot.register_next_step_handler(message, buy_amount)
    else:
        str = message.text
        try:
            print(int(str))
            if int(str) <= 0:
                bot.send_message(text="Повторите ввод. Минимальная покупка 1 💎", chat_id=message.chat.id)
                bot.register_next_step_handler(message, buy_amount)
            else:
                bot.send_message(text="Оплата", chat_id=message.chat.id)
                buy_tranzzo(message)
 #               bot.register_next_step_handler(message, buy_tranzzo)
        except ValueError:
            bot.send_message(text="Повторите ввод. Число не корректно", chat_id=message.chat.id)
            bot.register_next_step_handler(message, buy_amount)


def buy_tranzzo(message):

        amount = message.text
        #        prices = [LabeledPrice(label='Working Time Machine', amount=5750)]
        #        pprint(self.text)
        #        print(self.is_int(self.text))

        prices = [LabeledPrice(label='Heroes Life', amount=int(amount) * 1000)]

        #    bot.send_message(message.chat.id, "Нажмите для оплаты /buy")
        bot.send_invoice(message.chat.id, title='Покупка золота в Heroes Life',
                         description='Для оплаты нажмите на кнопку ниже.',
                         provider_token=provider_token,
                         currency='rub',
                         #                     photo_url='http://erkelzaar.tsudao.com/models/perrotta/TIME_MACHINE.jpg',
                         #                     photo_height=512,  # !=0/None or picture won't be shown
                         ##                     photo_width=512,
                         #                    photo_size=512,
                         is_flexible=False,  # True If you need to set up Shipping Fee
                         prices=prices,
                         start_parameter='time-machine-example',
                         invoice_payload='Heroes Life'
                         )

def succefull_tranzzo(message):
    global users
    open_buy()
    users[str(message.chat.id)]["diamond"] += int(message.successful_payment.total_amount / 1000)
    save_buy()
    bot.send_message(message.chat.id,
                     'Ура! Спасибо за оплату! Мы выполним ваш заказ на сумму `{} {}` как можно быстрее! '
                     'Оставайтесь на связи. '.format(
                         message.successful_payment.total_amount / 100, message.successful_payment.currency),
                     parse_mode='Markdown', reply_markup=keyboard_main_menu())




"""
        
def buy_user(self, message):
        global users
        buy_gold = message.successful_payment.total_amount / 1000
        buy_gold = (str(buy_gold)).split(".")[0]
        users[str(self.id)]["diamond"] = users[str(self.id)]["diamond"] + int(buy_gold)
        save("all")

def payment_history_last(self, my_login, api_access_token, rows_num, next_TxnId, next_TxnDate, txnID):
        s = requests.Session()
        s.headers['authorization'] = 'Bearer ' + api_access_token
        parameters = {'rows': rows_num, 'nextTxnId': next_TxnId, 'nextTxnDate': next_TxnDate, 'txnID': txnID}
        h = s.get('https://edge.qiwi.com/payment-history/v2/persons/' + my_login + '/payments', params=parameters)
        return h.json()
"""