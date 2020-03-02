from config import bot, find_location, telebot, publicKey, provider_token
import battle_game
from keyboard import *
from data import *
import time
import random
import json
from datetime import datetime, timedelta
from pprint import pprint
import threading
import requests
from telebot.types import LabeledPrice, ShippingOption
import logging



ADMIN = 765333440
PATH = find_location()
menu = 0
barracks = 0
global lvlrudnic

logging.basicConfig(filename='app.txt',  format='%(name)s - %(levelname)s - [%(asctime)s] %(message)s', level = logging.INFO)

def save(key):
    global maps, users, log, comb
    if key == "all":

        with open(PATH + "tmp/" + 'maps.json', 'w', encoding="utf-16") as f:
            json.dump(maps, f)
        with open(PATH + "tmp/" + 'maps.json', 'rb') as f:
            maps = json.load(f)

        with open(PATH + "tmp/" + 'users.json', 'w', encoding="utf-16") as f:
            json.dump(users, f)
        with open(PATH + "tmp/" + 'users.json', 'rb') as f:
            users = json.load(f)
    elif key == "maps":

        with open(PATH + "tmp/" + 'maps.json', 'w', encoding="utf-16") as f:
            json.dump(maps, f)
        with open(PATH + "tmp/" + 'maps.json', 'rb') as f:
            maps = json.load(f)
    elif key == "users":

        with open(PATH + "tmp/" + 'users.json', 'w', encoding="utf-16") as f:
            json.dump(users, f)
        with open(PATH + "tmp/" + 'users.json', 'rb') as f:
            users = json.load(f)

    elif key == "combat":

        with open(PATH + "tmp/" + 'comb.json', 'w', encoding="utf-16") as f:
            json.dump(comb, f)
        with open(PATH + "tmp/" + 'comb.json', 'rb') as f:
            comb = json.load(f)


    elif key == "log":
        file_log = open(PATH + "tmp/" + 'log.txt', "w")
        file_log.write(log)
        file_log.close()


def start_open():
    logging.info("Запуск игры")

    global maps, users, comb

    maps = {}
    try:
        with open(PATH + "tmp/" + 'maps.json', 'rb') as f:
            maps = json.load(f)
        logging.info('Чтение файла с картой')
    except:
        with open(PATH + "tmp/" + 'maps.json', 'w', encoding="utf-16") as f:
            json.dump(maps, f)
        with open(PATH + "tmp/" + 'maps.json', 'rb') as f:
            maps = json.load(f)

    users = {}
    try:
        with open(PATH + "tmp/" + 'users.json', 'rb') as f:
            users = json.load(f)
        logging.info('Чтение файла с пользователями')
    except:
        logging.info('файл с юзерами не доступен')
        pprint("файл с юзерами не доступен")
    #        with open(PATH + "tmp/" + 'users.json', 'w', encoding="utf-16") as f:
    #            json.dump(users, f)
    #        with open(PATH + "tmp/" + 'users.json', 'rb') as f:
    #            users = json.load(f)

    comb = {}
    try:
        with open(PATH + "tmp/" + 'comb.json', 'rb') as f:
            comb = json.load(f)
    except:
        with open(PATH + "tmp/" + 'comb.json', 'w', encoding="utf-16") as f:
            json.dump(comb, f)
        with open(PATH + "tmp/" + 'comb.json', 'rb') as f:
            comb = json.load(f)

def start_user_default():
    global users

    for key, value in users.items():
        value["healts_used"] = value["healts"]
        value["step_used"] = value["step"]
        value["energy_used"] = value["energy"]
    logging.info('Здоровье, шаги, энергия восстановлены')
    save("users")


def start_user(message):
    logging.info(str(message.chat.id) + ' Команда /start')
    global maps, users, log
    try:
        ref = str(message.text.split(" ")[1])
        logging.info(str(message.chat.id) + ' Вход по реф ссылке '+ ref)
    except:
        ref = "0"
    date_t = date("all")
    if str(message.chat.id) in users:
        logging.info(str(message.chat.id) +  'Пользователь уже есть')

        bot.send_message(message.chat.id, "Пользователь есть", reply_markup=keyboard_main_menu())
    else:

        #            message.chat.id = users[str(message.chat.id)]
        #            log = log + date("fulltime") + " Зарегистрирован новый пользователь " + str(message.chat.id) + "\n"
        users[str(message.chat.id)] = {"id": message.chat.id,
                                       "username": message.from_user.first_name,
                                       "date": str(date_t),
                                       "energy": 0,  # Энергия
                                       "energy_used": 0,  # Энергия истраченная
                                       "step": 0,  # Ходов
                                       "step_used": 0,  # Ходов истрачено
                                       "lvlstep": 1,
                                       "wolk_used": 0,  # Надо пройти
                                       "wolk": 0,  # Пройдено
                                       "lvlheroes": 1,
                                       "healts": 0,
                                       "healts_used": 0,
                                       "wood": 0,
                                       "stone": 0,
                                       "food": 0,
                                       "gold": 0,
                                       "diamond": 0,
                                       "experience": 0,  # Энергия
                                       "experience_used": 0,  # Энергия истрачено
                                       "hit": 20,
                                       "ref": ref,
                                       "weapons": {"arm": 0,
                                                   },
                                       "building":{}
                                       }
        s = random.randint(1, len(maps))

        maps[str(s)] = {"id": str(message.chat.id)}
        pprint(s)
        pprint(maps[str(s)])
        bot.send_message(chat_id=765333440,
                         text=date("fulltime") + " Зарегистрирован новый пользователь " + str(message.chat.id))
        logging.info(str(message.chat.id) + ' Новый пользователь')

    bot.send_message(message.chat.id, text = start_text, reply_markup=keyboard_start())

    save("all")
    #        save("log")


def date(key="all"):
    if key == "fulltime":
        time = datetime.today().strftime("%H:%M:%S %d/%m/%Y")
    elif key == "buytimedown":
        time = datetime.utcnow()
        time += timedelta(hours=3)
        time = time.strftime("%Y-%m-%dT%H:%M")
    elif key == "buytimeup":
        time = datetime.utcnow()
        time += timedelta(hours=4)
        time = time.strftime("%Y-%m-%dT%H:%M")
    elif key == "buyqiwi":
        time = datetime.utcnow()
        time += timedelta(hours=4)
        time = time.strftime("%Y-%m-%dT%H%M")
    elif key == "utctime":
        time = datetime.utcnow()
        time += timedelta(hours=3)
        time = time.strftime("%Y-%m-%dT%H:%M")
    else:
        time = datetime.today().strftime("%d/%m/%Y")

    return (time)


def please(message):
    if message.text == "Нет" or message.text == "нет":
        bot.send_message(message.chat.id, "Отмена", reply_markup=keyboard_main_menu())
    else:
        pprint("test")
        bot.send_message(765333440, "mess @" + str(message.from_user.username) + " " + str(
            message.from_user.first_name) + " " + message.text)
        pprint("test")


def buy(message):
    str = message.text
    try:
        pprint(int(str))
        if int(str) <= 0:
            bot.send_message(text="Повторите ввод. Минимальная покупка 1 💎", chat_id=message.chat.id)
            bot.register_next_step_handler(message, buy)
#            bot.send_message(text="Повторите ввод. Число не корректно", chat_id=message.chat.id, reply_markup=key_buy)
        else:
            bot.send_message(text="Оплата", chat_id=message.chat.id, reply_markup=keyboard_buy())
            Buy(message).buy_qiwi()
    except ValueError:

        bot.send_message(text="Повторите ввод. Число не корректно", chat_id=message.chat.id)
        bot.register_next_step_handler(message, buy)


start_open()
start_user_default()



class Maps():

    def __init__(self, message, call=""):
        global maps, menu, status, attak
        try:
            self.message_call = call.data
            self.id_call = call.id

        except:
            pass
        #        self.user_bot = User(message)
        self.id = message.chat.id
        self.text = message.text
        self.message_id = message.message_id
        self.user_bot = User(message)
        self.user = users[str(self.id)]
#        self.battle_bot = Battle(message)

    def new_maps(self):  # Прочитать файл
        global maps
        pole = 100
        n = 1
        maps = {}
        all_cell = pole * pole
        for key, value in users.items():
            r = random.randint(1, pole * pole)
            try:
                if not pprint(maps[str(r)]):
                    n += 1
            except:
                maps[str(r)] = {"id": str(key)}

        while n <= all_cell:
            try:
                if not pprint(maps[str(n)]):
                    n += 1
            except:
                self.resource(n)
                n += 1
        save("maps")

    def resource(self, n):
        r = random.randint(1, 15)
        if r == 1:
            self.resource_res(old_res="wood", n=n)
        elif r == 2:
            self.resource_res(old_res="stone", n=n)
        elif r == 3:
            self.resource_res(old_res="food", n=n)
        elif r == 4:
            maps[str(n)] = {"resource": "enemy"}
        elif r >= 5:
            maps[str(n)] = {"resource": "null"}

    def resource_res(self, old_res, n):
        r = random.randint(1, 15)
        if r == 1 or r == 2 or r == 3 or r == 4 or r == 5:
            maps[str(n)] = {"resource": old_res, "lvl": 1, "number": random.randint(3000, 5000)}
        elif r == 6 or r == 7 or r == 8 or r == 9:
            maps[str(n)] = {"resource": old_res, "lvl": 2, "number": random.randint(5001, 15000)}
        elif r == 10 or r == 11 or r == 12:
            maps[str(n)] = {"resource": old_res, "lvl": 3, "number": random.randint(15001, 30000)}
        elif r == 13 or r == 14:
            maps[str(n)] = {"resource": old_res, "lvl": 4, "number": random.randint(30001, 60000)}
        elif r == 15:
            maps[str(n)] = {"resource": old_res, "lvl": 5, "number": random.randint(60001, 120000)}

    def statistika(self):
        global maps
        w, s, i, u, n, w1, w2, w3, w4, w5, s1, s2, s3, s4, s5, i1, i2, i3, i4, i5, e = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        for key, value in maps.items():
            pprint(key)
            try:

                if maps[str(key)]["resource"] == "wood":
                    if maps[str(key)]["lvl"] == 1:
                        w1 = w1 + 1
                    elif maps[str(key)]["lvl"] == 2:
                        w2 = w2 + 1
                    elif maps[str(key)]["lvl"] == 3:
                        w3 = w3 + 1
                    elif maps[str(key)]["lvl"] == 4:
                        w4 = w4 + 1
                    elif maps[str(key)]["lvl"] == 5:
                        w5 = w5 + 1
                    w = w + 1
                elif maps[str(key)]["resource"] == "stone":
                    if maps[str(key)]["lvl"] == 1:
                        s1 = s1 + 1
                    elif maps[str(key)]["lvl"] == 2:
                        s2 = s2 + 1
                    elif maps[str(key)]["lvl"] == 3:
                        s3 = s3 + 1
                    elif maps[str(key)]["lvl"] == 4:
                        s4 = s4 + 1
                    elif maps[str(key)]["lvl"] == 5:
                        s5 = s5 + 1
                    s = s + 1
                elif maps[str(key)]["resource"] == "food":
                    if maps[str(key)]["lvl"] == 1:
                        i1 = i1 + 1
                    elif maps[str(key)]["lvl"] == 2:
                        i2 = i2 + 1
                    elif maps[str(key)]["lvl"] == 3:
                        i3 = i3 + 1
                    elif maps[str(key)]["lvl"] == 4:
                        i4 = i4 + 1
                    elif maps[str(key)]["lvl"] == 5:
                        i5 = i5 + 1
                    i = i + 1
                elif maps[str(key)]["resource"] == "null":
                    n = n + 1
                elif maps[str(key)]["resource"] == "enemy":
                    e = e + 1
            except:
                u = u + 1
        pprint("www")
        text = "дерево " + str(w) + " \nlvl 1: " + str(w1) + " \nlvl 2: " + str(w2) + " \nlvl 3: " + str(
            w3) + " \nlvl 4: " + str(w4) + " \nlvl 5: " + str(w5) \
               + "\nеда " + str(i) + " \nlvl 1: " + str(i1) + " \nlvl 2: " + str(i2) + " \nlvl 3: " + str(
            i3) + " \nlvl 4: " + str(i4) + " \nlvl 5: " + str(i5) \
               + "\nкамень " + str(s) + " \nlvl 1: " + str(s1) + " \nlvl 2: " + str(s2) + " \nlvl 3: " + str(
            s3) + " \nlvl 4: " + str(s4) + " \nlvl 5: " + str(s5) \
               + "\nигроков " + str(u) + "\nПустых ячеек " + str(n) + "\nВрагов " + str(e)
        pprint(text)
        bot.send_message(chat_id=self.id, text=text)

    #        pprint("дерево "+str(w)+"\nеда "+str(i)+"\nкамень "+str(s)+"\nигроков "+str(u)+"\nПустых ячеек "+str(n))

    def output_map(self):
        try:
            global pole
            keyboard = telebot.types.InlineKeyboardMarkup()
            x, y, cell_user, n, pole = 1, 0, "", 0, 100
            for key, value in maps.items():
                try:
                    if maps[str(key)]["id"] == str(self.id):
                        cell_user = key
                        break
                except:
                    continue

            if (int(cell_user) % pole) == 3:
                pos = [pole * 3 + 2, pole * 2 + 2, pole + 2, 2, (pole - 2) * -1, (pole * 2 - 2) * -1,
                       (pole * 3 - 2) * -1]
            elif int(cell_user) % pole == 2:
                pos = [pole * 3 + 1, pole * 2 + 1, pole + 1, 1, (pole - 1) * -1, (pole * 2 - 1) * -1,
                       (pole * 3 - 1) * -1]
            elif int(cell_user) % pole == 1:
                pos = [pole * 3, pole * 2, pole, 0, pole * -1, pole * -2, pole * -3]
            else:
                pos = [pole * 3 + 3, pole * 2 + 3, pole + 3, 3, (pole - 3) * -1, (pole * 2 - 3) * -1,
                       (pole * 3 - 3) * -1]
            for x in pos:
                start_field = int(cell_user) - x
                #            pprint(start_field)
                if start_field >= pole * pole:
                    break
                elif start_field < 0:

                    pprint("null")
                    continue

                tab = []
                y = 0
                if (start_field + 7) % pole == 1 or (start_field + 7) % pole == 2 or (start_field + 7) % pole == 3:
                    start_field = start_field - (start_field + 6) % pole

                while y < 7:

                    try:
                        cell = maps[str(start_field)]["resource"]
                    except Exception:
                        cell = maps[str(start_field)]["id"]
                    if start_field % pole == 0 or start_field % pole == 100:
                        y = 7
                        tab.append(telebot.types.InlineKeyboardButton(" ", callback_data=str(start_field)))
                    else:
#                        pprint(str(start_field))
                        if cell == "food":
                            tab.append(telebot.types.InlineKeyboardButton("🍞", callback_data=str(start_field)))
                        elif cell == "wood":
                            tab.append(telebot.types.InlineKeyboardButton("🌲", callback_data=str(start_field)))
                        elif cell == "stone":
                            tab.append(telebot.types.InlineKeyboardButton("⛏", callback_data=str(start_field)))
                        elif cell == "enemy":
#                            if random.randint(1,2) == 1:
                                tab.append(telebot.types.InlineKeyboardButton("👻", callback_data=str(start_field)))
#                            else:
#                                tab.append(telebot.types.InlineKeyboardButton("☠️", callback_data=str(start_field)))

                        elif cell == str(self.id):
                            tab.append(telebot.types.InlineKeyboardButton("🧛‍♂", callback_data=str(start_field)))
                        elif cell != "null":
                            tab.append(telebot.types.InlineKeyboardButton("🏰", callback_data=str(start_field)))
                        elif start_field == int(cell_user) - 1:
                            tab.append(telebot.types.InlineKeyboardButton("⬅", callback_data=str(start_field)))
                        elif start_field == int(cell_user) - pole:
                            tab.append(telebot.types.InlineKeyboardButton("⬆", callback_data=str(start_field)))
                        elif start_field == int(cell_user) + 1:
                            tab.append(telebot.types.InlineKeyboardButton("➡", callback_data=str(start_field)))
                        elif start_field == int(cell_user) + pole:
                            tab.append(telebot.types.InlineKeyboardButton("⬇", callback_data=str(start_field)))
                        elif cell == "null":
                            tab.append(telebot.types.InlineKeyboardButton(" ", callback_data=str(start_field)))

                        y += 1
                        start_field += 1

                keyboard.row(*tab)
            step = telebot.types.InlineKeyboardButton(text="🚶‍♂️Ходов: " + str(users[str(self.id)]["step_used"]),
                                              callback_data=" ")
            energy = telebot.types.InlineKeyboardButton(text="🔋 ️Энергии: " + str(users[str(self.id)]["energy_used"]),
                                                callback_data=" ")
            arena = telebot.types.InlineKeyboardButton(text="Отправиться на поле боя", callback_data="goto_battle")
            keyboard.row(step, energy)
            keyboard.row(arena)
            #        keyboard.row(types.InlineKeyboardButton("Вернуться в город", callback_data="Вернуться в город"))

            save("all")
            return keyboard
        except Exception as s:
            pprint(s)

    def goto(self):
        global maps, pole, attak
        pole = 100
        cell_user = 0

        for key, value in maps.items():
            try:
                if maps[str(key)]["id"] == str(self.id):
                    cell_user = key
                    break
            except:
                continue
        try:
            value_call = maps[str(self.message_call)]["resource"]
        except:
            try:
                value_call = self.message_call.split("_")[1]
            except:
                value_call = "null"
        if users[str(self.id)]["step_used"] == 0:
            bot.send_message(text="У вас нет ходов", chat_id=self.id)
        elif users[str(self.id)]["healts_used"] <= 0:
            bot.send_message(text="Вы мертвы", chat_id=self.id)

        elif self.message_call == cell_user:
            bot.answer_callback_query(self.id_call, 'Это вы')

        elif int(self.message_call) == int(cell_user) - 1:
            if value_call == "food" or value_call == "wood" or value_call == "stone":
                bot.delete_message(self.id, message_id=self.message_id)
                self.rudnic(cell_user)
            elif value_call == "enemy":

                if users[str(self.id)]["energy_used"] == 0:
                    bot.send_message(text="У вас нет энергии", chat_id=self.id)
                else:
                    logging.info(str(self.id) + ' Атака монстра')
                    bot.delete_message(self.id, message_id=self.message_id)
                    self.enemy_write(cell_user)
            elif value_call == "olduser":
                pprint("test")
                bot.send_message(text="Аттака другого игрока на стадии разработки", chat_id=self.id)
            else:
                self.goto_cell(cell_user, position_user=-1)

        elif int(self.message_call) == int(cell_user) + 1:
            if value_call == "food" or value_call == "wood" or value_call == "stone":
                bot.delete_message(self.id, message_id=self.message_id)
                self.rudnic(cell_user)
            elif value_call == "enemy":
                if users[str(self.id)]["energy_used"] == 0:
                    bot.send_message(text="У вас нет энергии", chat_id=self.id)
                else:
                    logging.info(str(self.id) + ' Атака монстра')
                    bot.delete_message(self.id, message_id=self.message_id)
                    self.enemy_write(cell_user)
            elif value_call == "olduser":
                bot.send_message(text="Аттака другого игрока на стадии разработки", chat_id=self.id)
            else:
                self.goto_cell(cell_user, position_user=1)

        elif int(self.message_call) == int(cell_user) - pole:
            if value_call == "food" or value_call == "wood" or value_call == "stone":
                bot.delete_message(self.id, message_id=self.message_id)
                self.rudnic(cell_user)
            elif value_call == "enemy":
                if users[str(self.id)]["energy_used"] == 0:
                    bot.send_message(text="У вас нет энергии", chat_id=self.id)
                else:
                    logging.info(str(self.id) + ' Атака монстра')
                    bot.delete_message(self.id, message_id=self.message_id)
                    self.enemy_write(cell_user)
            elif value_call == "olduser":
                bot.send_message(text="Аттака другого игрока на стадии разработки", chat_id=self.id)
            else:
                self.goto_cell(cell_user, position_user=- pole)

        elif int(self.message_call) == int(cell_user) + pole:
            if value_call == "food" or value_call == "wood" or value_call == "stone":
                bot.delete_message(self.id, message_id=self.message_id)
                self.rudnic(cell_user)
            elif value_call == "enemy":
                if users[str(self.id)]["energy_used"] == 0:
                    bot.send_message(text="У вас нет энергии", chat_id=self.id)
                else:
                    logging.info(str(self.id) + ' Атака монстра')
                    bot.delete_message(self.id, message_id=self.message_id)
                    self.enemy_write(cell_user)
            elif value_call == "olduser":
                bot.send_message(text="Аттака другого игрока на стадии разработки", chat_id=self.id)
            else:
                self.goto_cell(cell_user, position_user=pole)

        elif value_call == "null":
            bot.answer_callback_query(callback_query_id=self.id_call, text='Поле не активно')
        elif value_call == "food":
            bot.answer_callback_query(callback_query_id=self.id_call, text='Шахта с едам')
        elif value_call == "wood":
            bot.answer_callback_query(callback_query_id=self.id_call, text='Шахта с деревом')
        elif value_call == "stone":
            bot.answer_callback_query(callback_query_id=self.id_call, text='Шахта с камнем')
        elif value_call == "enemy":
            bot.answer_callback_query(callback_query_id=self.id_call, text='Страшный монстр')
        elif value_call == "olduser":
            bot.answer_callback_query(callback_query_id=self.id_call, text='Город соперника')

    def goto_cell(self, cell_user, position_user):
        maps[str(cell_user)] = {"resource": "null"}
        maps[str(int(cell_user) + position_user)] = {"id": str(self.id)}
        self.user_bot.move()
        bot.edit_message_text(text="Ходите", chat_id=self.id, message_id=self.message_id,
                              reply_markup=self.output_map())

    def enemy_write(self, cell_user):
        r = random.randint(self.user["lvlheroes"]-1, self.user["lvlheroes"])
        if r <= 0:
            r = 1
        logging.info(str(self.id) + ' Атака монстра, уровень монстра'+str(r))
        self.user["enemy_lvl"] = str(r)
        self.user["enemy_healts"] = 50 * r
        self.user["enemy_exr"] = 5 * r
        self.user["enemy_cell"] = str(self.message_call)
        self.user["enemy_hit"] = 10 * r
#        self.user["enemy_dodge"] = lvlenemy[str(r)]["dodge"]

        bot.send_message(text=textattaka(str(r)), chat_id=self.id, reply_markup=keyboard_battle())

#    def enemy(self, cell_user):
#        keyboard = telebot.types.InlineKeyboardMarkup()
#        attak = types.InlineKeyboardButton(text="Атаковать", callback_data="battle_"+str(cell_user))
#        keyboard.row(attak)
#        bot.edit_message_text(text="Вы напали на существо", chat_id=self.id, message_id=self.message_id,
#                              reply_markup=keyboard)

    def rudnic(self, cell_user):
        global maps, menu, res, kol, map_res, lvl
        map_res = self.message_call
        res = maps[str(self.message_call)]["resource"]
        kol = maps[str(self.message_call)]["number"]
        lvl = maps[str(self.message_call)]["lvl"]
        timer = self.time(kol // lvlrudnic[lvl])
        menu = "rudnic"
        bot.send_message(text=text_mining(res, lvl, kol, timer), chat_id=self.id, reply_markup=keyrudnic())

    def time(self, timer):
        return time.strftime('%M:%S', time.gmtime(timer))

    def timer(self):
        global maps, users, res, kol, map_res, status, lvl
        timer = int(kol) // lvlrudnic[lvl]
        ss = 1
        sum = 0
        lvl_timer = lvlrudnic[lvl]
        kol_timer = kol
        sell = map_res

        for i in range(timer + 2, 0, -1):
            pprint(str(self.id) + " ячейка " + str(sell) + " " + str(ss * lvl_timer))
            if status == "close" + str(self.id):
                pprint("close")
                i = 0
                break
            elif sum >= kol_timer:
                break
            ss += 1
            sum = ss * lvl_timer
            time.sleep(1)

        if int(maps[str(sell)]["number"]) - int(sum) <= 0:
            maps[str(sell)]["resource"] = "null"
            sum = maps[str(sell)]["number"]
            summa = users[str(self.id)][res] + sum
            users[str(self.id)][res] = summa
            self.cell()
        elif int(maps[str(sell)]["number"]) - int(sum) >= 0:
            maps[str(sell)]["number"] = maps[str(sell)]["number"] - sum
            summa = sum + users[str(self.id)][res]
            users[str(self.id)][res] = summa
        else:
            pprint("ошибка")
        save("all")
        bot.send_message(text="⚡️Вы завершили добычу ⚡️\nСобрано " + str(sum), chat_id=self.id, reply_markup=keyboardmap())
        bot.send_message(text="🚶‍♂️Делайте ход по игровому полю", chat_id=self.id, reply_markup=self.output_map())

    def mining(self):
        threading.Thread(target=self.timer).start()

    def cell(self):
        n = random.randint(1, 10000)
        try:
            if maps[str(n)]["resource"] == "null":
                self.resource(n)
            pprint(n)
        except:
            pprint("ячейка занята")

class User():

    def __init__(self, message, call=""):
        try:
            self.message_call = call.data
            self.call_id = call.id
            self.message_call_id = call.message.message_id
#            pprint(self.call_id)
        except:
            pass

        self.id = message.chat.id
        self.text = message.text
        self.first_name = message.from_user.username
        self.user = users[str(self.id)]
#        pprint(self.id)

    def help(self):
        keyboard = telebot.types.InlineKeyboardMarkup()
        maps = telebot.types.InlineKeyboardButton(text="Карта", callback_data="help_maps")
        battle = telebot.types.InlineKeyboardButton(text="Бой", callback_data="help_battle")
        if self.text == "Помощь":
            text = text_help
            keyboard.add(maps, battle)
            bot.send_message(chat_id=self.id, text=text, reply_markup=keyboard)

        else:
            if self.message_call == "help_maps":
                text = "На карте вы можете добывать ресурсы и воевать против монстров.\n На карте распологаются ресурсы: еда, камень, дерево. Они вам понадобятся для постройки у улучшения вашего города."
            elif self.message_call == "help_battle":
                text = "Бой с соперником проходит в пошаговом режиме.\n На каждом ходе у вас есть два очка защиты и два очка нападения.\n "
            keyboard.add(maps, battle)
            bot.edit_message_text(chat_id=self.id, text=text,message_id=self.message_call_id, reply_markup=keyboard)

    def new_game(self):
        pprint("test")
        self.start_user_statistic()
        bot.send_message(self.id, "Начнём", reply_markup=keyboard_main_menu())

    def start_user_statistic(self):
        self.user["step"] = lvlstep[self.user["lvlstep"]]
        self.user["step_used"] = lvlstep[self.user["lvlstep"]]
        self.user["wolk"] = lvlwolk[self.user["lvlstep"]]
        self.user["experience"] = lvlexperience[self.user["lvlheroes"]]
        self.user["energy"] = lvlenergy[self.user["lvlheroes"]]
        self.user["energy_used"] = lvlenergy[self.user["lvlheroes"]]
        self.user["healts"] = lvlhealts[self.user["lvlheroes"]]
        self.user["healts_used"] = lvlhealts[self.user["lvlheroes"]]
        save("users")
        logging.info(str(self.id) + ' Выставлены стартовые параметры')

    def update_statistic(self, data):
        if data == "step":

            if self.user["wolk_used"] >= lvlwolk[self.user["lvlstep"]]:
                logging.info(str(self.id) + ' Новый уровень шагов')
                self.user["lvlstep"] += 1
                self.user["wolk"] = lvlwolk[self.user["lvlstep"]]
                self.user["step"] = lvlstep[self.user["lvlstep"]]

        elif data == "experiens":

            if self.user["experience_used"] >= lvlexperience[self.user["lvlheroes"]]:
                logging.info(str(self.id) + ' Новый уровень героя')
                self.user["lvlheroes"] += 1
                self.user["experience"] = lvlexperience[self.user["lvlheroes"]]
                self.user["healts"] = lvlhealts[self.user["lvlheroes"]]
                self.user["healts_used"] = self.user["healts"]
                self.user["energy"] = lvlenergy[self.user["lvlheroes"]]
        save("users")

    def info_heroes(self, key):
        id = self.user["id"]
        username = self.user["username"]
        #        date = self.user["date"]
        level = self.user["lvlheroes"]
        healts = self.user["healts"]
        healts_used = self.user["healts_used"]
        experience = self.user["experience"]
        wood = self.user["wood"]
        stone = self.user["stone"]
        food = self.user["food"]
        iamond = self.user["diamond"]
        energy = self.user["energy"]
        energy_used = self.user["energy_used"]
        step_used = self.user["step_used"]
        step = self.user["step"]
        lvlstep = self.user["lvlstep"]
        wolk = self.user["wolk"]
        wolk_used = self.user["wolk_used"]
        experience_used = self.user["experience_used"]
        hit = self.user["hit"]
        gold = self.user["gold"]
        print(self.user)
        heroes = "Информация о герое\n" + "id: " + str(id) + "\n" + \
                 "👤 Имя: " + str(username) + "\n" + \
                 "🏅 Уровень: " + str(level) + "\n" + \
                 "🔋 Энергия: " + str(energy_used) + '/' + str(energy) + "\n" + \
                 "🌟 Опыт: " + str(experience_used) + "/" + str(experience) + "\n" + \
                 "❤ Здоровье: " + str(healts_used) + "/" + str(healts) + "\n" + "\n" +\
                 "Урон: " +str(hit)+"\n"+"\n" +\
                 "🚶‍♂️Ур. ходьбы: " + str(lvlstep) +" ("+ str(wolk_used) + '/' + str(wolk)+")" + "\n"  + \
                 "🚶‍♂️Ходов по карте: " + str(step_used) + '/' + str(step) + "\n" +  "\n"+\
                 "💰 Золото: "+str(gold) + "\n"+\
                 "💎 Алмазы: " + str(iamond) + "\n"

        sklad = "Информация о складе\n" + "еда: " + str(food) + "\n" + "Дерево: " + str(
            wood) + "\n" + "Камень: " + str(stone)
        stat = "Ресурсов: Еда: " + str(food)  + " Дерево: " + str(wood)  + " Камень: " + str(stone)
        if key == "heroes":
            return (heroes)
        elif key == "sklad":
            return (sklad)
        elif key == "stat":
            return stat

    def energy_timer(self):
        while users[str(self.id)]["energy_used"] < users[str(self.id)]["energy"]:
            time.sleep(60)  # in seconds
            users[str(self.id)]["energy_used"] += 1
#            bot.send_message(chat_id=self.id, text="У вас появилась энергия " + str(users[str(self.id)]["energy_used"]))
            #            self.maps_bot.goto
            save("user")
        if users[str(self.id)]["energy_used"] == users[str(self.id)]["energy"]:
            bot.send_message(chat_id=self.id, text="Энергия восстановилась " + str(users[str(self.id)]["energy_used"]))

    def energy(self):
        if users[str(self.id)]["energy_used"] == users[str(self.id)]["energy"]:
            users[str(self.id)]["energy_used"] -= 1
            threading.Thread(target=self.energy_timer, daemon=True).start()
        elif users[str(self.id)]["energy_used"] == 0:
            bot.send_message(chat_id=self.id, text="У вас кончилась энергия")
        elif users[str(self.id)]["energy_used"] < users[str(self.id)]['energy']:
            users[str(self.id)]["energy_used"] -= 1

    def move_timer(self):
        while users[str(self.id)]["step_used"] < users[str(self.id)]["step"]:
            time.sleep(30)  # in seconds
            users[str(self.id)]["step_used"] += 1
#            bot.send_message(chat_id=self.id, text="У вас появился ход " + str(users[str(self.id)]["step_used"]))
            #            self.maps_bot.goto
            save("user")
        if users[str(self.id)]["step_used"] == users[str(self.id)]["step"]:
            bot.send_message(chat_id=self.id, text="Ходы восстановились " + str(users[str(self.id)]["step_used"]))

    def move(self):
        if users[str(self.id)]["step_used"] == users[str(self.id)]["step"]:
            users[str(self.id)]["step_used"] -= 1
            self.user["wolk_used"] += 1
            threading.Thread(target=self.move_timer, daemon=True).start()
        elif users[str(self.id)]["step_used"] == 0:
            bot.send_message(chat_id=self.id, text="У вас кончились ходы")
        elif users[str(self.id)]["step_used"] < users[str(self.id)]['step']:
            users[str(self.id)]["step_used"] -= 1
            self.user["wolk_used"] += 1
        #            pprint(users[str(self.id)]["move_used"])
        self.update_statistic(data="step")

    def barracks(self, barr):
        global users
        try:
            arc = users[self.id]["archer"]
        except:
            arc = 0
        if barr == "all":
            text = "У вас имеется: \n Лучников " + str(arc) + "\n Воинов "
            bot.send_message(text=text, chat_id=self.id, reply_markup=keyboardbarracks())

        elif barr == "archer":
            wood = archer["1"]["wood"]
            stone = archer["1"]["stone"]
            food = archer["1"]["food"]
            pprint("test")
            text = "Обучить за " + str(wood) + " " + str(stone) + " " + str(food)
            bot.send_message(text=text, chat_id=self.id, reply_markup=keyboaryesno())
        elif barr == "yes":
            users[str(self.id)]["wood"] = str(int(users[str(self.id)]["wood"]) - archer["1"]["wood"])
            users[str(self.id)]["stone"] = str(int(users[str(self.id)]["stone"]) - archer["1"]["stone"])
            users[str(self.id)]["food"] = str(int(users[str(self.id)]["food"]) - archer["1"]["food"])
            users[str(self.id)]["archer"] = arc + 1
            bot.send_message(text="Вы обучили лучника \n Общее кол-во " + str(users[str(self.id)]["archer"]),
                             chat_id=self.id, reply_markup=keyboaryesno())
            save("all")

    def build(self, data):
        keyboard = telebot.types.InlineKeyboardMarkup()
        pprint("2")
        if data == "back":
            self.building()
        elif data == "update":
            pprint("tests")
            #        elif data == "update":
            data_old = self.message_call.split("_")[2]
            pprint(data_old)
#            if not self.building_update(data_old):
#                text = "Ресурсов не хватает"
#                pprint(self.building_update(data_old))
#             self.build(data=data_old)
#            else:
#                text = "Строение улучшено"
            self.user["building"][data_old] += 1

            save("users")
            self.build(data = data_old)
        else:
            pprint("3")
            name = buildings[data]["name"]
            lvl = self.user["building"][data]
            new_lvl = lvl + 1
            stone = str(static_buildings(data, new_lvl)[0])
            wood = str(static_buildings(data, new_lvl)[1])
            food = str(static_buildings(data, new_lvl)[2])
            pprint("4")
            text = "Строение "+name +" "+ str(lvl)+" уровня\n"
            text += "Улучшить "+name+" до "+ str(new_lvl)+" уровня за: \n Камень: "+ stone+"\n Дерево: "+ wood +"\n еда: "+ food
            pprint("5")
            keyboard.row(telebot.types.InlineKeyboardButton(text="Улучшить", callback_data="build_update_"+data))
            pprint("6")
            keyboard.row(telebot.types.InlineKeyboardButton(text="Назад", callback_data="build_back"))


        bot.edit_message_text(text=text, chat_id=self.id, message_id=self.message_call_id, reply_markup=keyboard)

    def building_update(self, data):
        pprint("building update")
        lvl = self.user["building"][data]
        new_lvl = lvl +1
        stone_player = self.user["stone"]
        wood_player = self.user["wood"]
        food_player = self.user["food"]
        stone = static_buildings(data, new_lvl)[0]
        wood = static_buildings(data, new_lvl)[1]
        food = static_buildings(data, new_lvl)[2]
        text =""

        if stone_player < stone:
            text += "Не хватает камня\n"
            pprint("Не хватает камня")
        if wood_player < wood:
            text += "Не хватает дерева\n"
            pprint("Не хватает дерева")
        if food_player < food:
            text += "Не хватает еды\n"
            pprint("Не хватает еды")
        if not text:
            return
        else:
            return text

    def translator(self):
        if self.text == "Склад":
            bul = "storadge"
        elif self.text == "Казарма":
            bul = "barracks"
        return bul

    def building(self):
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.row(telebot.types.InlineKeyboardButton(text=self.info_heroes(key="stat"), callback_data=" "))
        if self.user["building"] == {}:
            i = 1
            tab = []
            bul = {}

            for key, value in buildings.items():
                bul.update({key : 0})
                tab.append(telebot.types.InlineKeyboardButton(text=buildings[key]["name"] +" 0", callback_data="build_"+key))
                if i == 3 or i == 6:
                    keyboard.row(*tab)
                    tab = []
                i += 1
            keyboard.row(*tab)
            self.user["building"] = bul
            save("users")

        else:
            i = 1
            tab = []

            for key, value in self.user["building"].items():
                lvl = self.user["building"][key]
                tab.append(telebot.types.InlineKeyboardButton(text=buildings[key]["name"] + " "+str(lvl), callback_data="build_"+key))
                if i == 3 or i == 6:
                    keyboard.row(*tab)
                    tab = []
                i += 1
            keyboard.row(*tab)

        bot.send_message(text="Здесь вы можете улучшить ващи постройки", chat_id=self.id, reply_markup=keyboard)

    def timer_healts(self):
        while users[str(self.id)]["healts_used"] < users[str(self.id)]["healts"]:
            time.sleep(60)  # in seconds
            users[str(self.id)]["healts_used"] = users[str(self.id)]["healts"]

            save("user")
        if users[str(self.id)]["healts_used"] == users[str(self.id)]["healts"]:
            bot.send_message(chat_id=self.id, text="Здоровье восстановлено ")


class Buy():
    global amount, user

    def __init__(self, message="", call=""):
        self.id = message.chat.id
        self.text = message.text
        self.first_name = message.from_user.username
        self.user = users[str(self.id)]

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

        if  self.user["buy_qiwi_check"] == 0 and date("utctime") < users[str(self.id)]["but_qiwi_date"]:
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
                                                          int(self.text) * 1) + "&comment=" + comment + "&customFields[themeCode]=Konstantyn-PbboM7ch_P&successUrl=https%3A%2F%2Ft.me%2FHeroesLifeBot&lifetime=" + date('buyqiwi')))
            self.user["buy_qiwi_tranzaction"] = 0
            self.user["buy_qiwi_comment"] = comment
            self.user["buy_qiwi_amount"] = int(self.text)
            self.user["but_qiwi_date_down"] = date('buytimedown')
            self.user["but_qiwi_date_up"] = date('buytimeup')
            self.user["buy_qiwi_check"] = 0
            pprint("asdasd")
            text = "Для покупки "+str(int(self.text))+" 💎 нажмите на кнопку ниже \nПокупка на сумму " + str(int(self.text) * 10) + " руб."
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
                        if  self.user["buy_qiwi_check"] == 0:
                            pprint("Платеж прошел успешно")
                            bot.send_message(self.id, "Счет " + str(txnId) + " на сумму " + str(amount) + " руб "+date+". Оплачен",
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
                bot.send_message(self.id, "Счет на сумму " + str(amount) + " руб "+date+". Не оплачен",
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

    """
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

    def buy_tranzzo(self):
        global prices, amount
        amount =1
#        prices = [LabeledPrice(label='Working Time Machine', amount=5750)]
        #        pprint(self.text)
        #        print(self.is_int(self.text))
        prices = [LabeledPrice(label='Heroes Life', amount=int(amount) * 1000)]
        #    bot.send_message(message.chat.id, "Нажмите для оплаты /buy")
        bot.send_invoice(self.id, title='Покупка золота в Heroes Life',
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


class Battle():
    def __init__(self, message, call=""):

        try:

            self.call = call.data
            self.call_id = call.id
            self.message_call_id = call.message.message_id
#            print(str(self.call))
        except Exception:
            pass

        self.id = message.chat.id
        self.text = message.text
        self.first_name = message.from_user.username
        self.user = users[str(self.id)]
        self.maps = Maps(message)
        self.user_bot = User(message)
        self.message_id = message.message_id
        global text, attak


    def congratulation(self,data):
        if data == "heroes":
            self.user["experience_used"] += 5
            r_gold = random.randint(1,50)
            self.user["gold"] += r_gold
            maps[self.user["enemy_cell"]]["resource"] = "null"
            self.user_bot.update_statistic(data="experiens")
            self.user_bot.energy()

            bot.send_message(text="Бой окончен: ", chat_id=self.id, reply_markup=keyboardmap())
            bot.send_message(text="Вы победили и получили 5 опыта.\n Вам выпало "+str(r_gold)+ " золота", chat_id=self.id,
                             reply_markup=self.maps.output_map())
        elif data =="enemy":
            threading.Thread(target=self.user_bot.timer_healts, daemon=True).start()
            self.user_bot.energy()
            bot.send_message(text="Бой окончен: ", chat_id=self.id, reply_markup=keyboardmap())
            bot.send_message(text="Вы проиграли. Здоровье восстановится через 60 сек.", chat_id=self.id, reply_markup=self.maps.output_map())

    def attak(self):
        global users, maps, attak
#        pprint(attak)
        r = random.randrange(1, 3)

        pprint(r)
        if r == 1:
            #                self.user["energy_used"] -= 1
            self.user_bot.energy()
            bot.send_message(text="Бой окончен: ", chat_id=self.id, reply_markup=keyboardmap())
            bot.send_message(text="Вы проиграли", chat_id=self.id, reply_markup=self.maps.output_map())
        else:
            self.user["experience_used"] += 5
            #               self.user["energy_used"] -= 1
            maps[self.user["enemy_cell"]]["resource"] = "null"
            self.user_bot.update_statistic(data="experiens")
            self.user_bot.energy()
#            pprint("test")
#            wea = self.weapons_random()
#            weapons = weapons_data[wea]["name"]
#            pprint(weapons)
#            weapons = ""
#            if weapons == "":
            bot.send_message(text="Бой окончен: ", chat_id=self.id, reply_markup=keyboardmap())
            bot.send_message(text="Вы победили и получили 5 опыта", chat_id=self.id,
                             reply_markup=self.maps.output_map())
#            else:
#                self.user["weapons"]["arm"] = 1
#                bot.send_message(text="Вы победили и получили 5 опыта\n Вы нашли "+weapons, chat_id=self.id,
#                             reply_markup=self.maps.output_map())
       #                self.resource(attak)

        pprint("всё ок")
        save("users")

    def keyboard_attak_new(self):
        keyboard = telebot.types.InlineKeyboardMarkup()
        attak = telebot.types.InlineKeyboardButton(text="Атака", callback_data="battle_attak")
        defence = telebot.types.InlineKeyboardButton(text="Защита", callback_data="battle_defence")
        keyboard.row(attak, defence)
        return keyboard

    def att(self):
        stop = 0
        cell = self.call.split("_")[1]
        if self.call == "battle_attak":

                    r = random.randint(1, 100)
                    pprint(r)
                    if r < self.user["enemy_dodge"]:
                        text = self.text + " \n⚔️Враг увернулся. Осталось " + str(self.user["enemy_healts"]+ "здоовья")
                    else:
                        self.user["enemy_healts"] -= self.user["hit"]
                        text = self.text + " \n⚔️Вы аттаковали врага и нанесли "+str(self.user["hit"])+" урона. Осталось "+ str(self.user["enemy_healts"]) + " здоовья"

                    if self.user["enemy_healts"] <= 0:
                        bot.send_message(text="⏱ Вывод карты ⏱", chat_id=self.id, reply_markup=keyboardmap())
                        stop = 1
                        text = self.text + "\nВы одержали победу 💥 "
                        time.sleep(2)
                        self.user["experience_used"] += 5
                        self.user["healts_used"] = self.user["healts"]
                        maps[self.user["enemy_cell"]]["resource"] = "null"
                        self.user_bot.update_statistic(data="experiens")
                        self.user_bot.energy()
                        bot.send_message(text="Вы победили и получили 5 🌕 опыта", chat_id=self.id,
                                         reply_markup=self.maps.output_map())
        elif self.call == "battle_defence":
            text = self.text + "\n🛡 Вы защищаетесь от врага и восстанавливаете здоровье"
            self.user["healts_used"] += 10
        else:
            if maps[cell]["resource"] == "enemy":
                bot.edit_message_text(text="Выберите дальнейшее действие", chat_id=self.id, message_id=self.message_id,
                                      reply_markup=self.keyboard_attak_new())

        bot.edit_message_text(text=text, chat_id=self.id, message_id=self.message_id, reply_markup=self.keyboard_attak_new())
#        time.sleep(1)
        r = random.randint(1, 2)
        if r == 1 and stop == 0:
            self.user["healts_used"] -= self.user["enemy_hit"]
            text = text + " \n⚔️Враг аттаковал вас и нанес "+str(self.user["enemy_hit"])+" урона. Осталось "+str(self.user["healts_used"])+ " здоовья"
            bot.edit_message_text(text=text, chat_id=self.id, message_id=self.message_id,
                                  reply_markup=self.keyboard_attak_new())
        elif r == 2 and stop == 0:
            text = text + "\n🛡 Враг защищается и восстанавливает здоровье"
#            self.user["enemy_healts"] += self.user["enemy_dodge"]
            bot.edit_message_text(text=text, chat_id=self.id, message_id=self.message_id,
                                  reply_markup=self.keyboard_attak_new())
        if self.user["healts_used"] <= 0:
            self.user_bot.update_statistic(data="experiens")
            self.user["healts_used"] = self.user["healts"]
            pprint(self.user["healts_used"])
            save("users")
            bot.send_message(text="⏱ Вывод карты ⏱", chat_id=self.id, reply_markup=keyboardmap())
            bot.send_message(text="Вы умерли.", chat_id=self.id,
                             reply_markup=self.maps.output_map())

    def weapons_random(self):
        r = random.randint(1, 1)
        pprint(r)
        pprint(weapons[str(self.user["lvlheroes"])]["random"])
        r_r = weapons[str(self.user["lvlheroes"])]["random"]
        pprint(r_r)
        if r ==1: #arm
            r_a = random.randint(1, r_r)
            if r_a == 1:
                return weapons[str(r_r)]["name"]
        else: return ""

    def attaka_new(self):
        keyboard = telebot.types.InlineKeyboardMarkup()
        null = telebot.types.InlineKeyboardButton(text="➖➖", callback_data="null")
        heroes_head = telebot.types.InlineKeyboardButton(text=fight_text["heroes_head"], callback_data="fight_heroes_head")
        heroes_left = telebot.types.InlineKeyboardButton(text=fight_text["heroes_handleft"], callback_data="fight_heroes_handleft")
        heroes_right = telebot.types.InlineKeyboardButton(text=fight_text["heroes_handright"], callback_data="fight_heroes_handright")
        heroes_breast = telebot.types.InlineKeyboardButton(text=fight_text["heroes_breast"], callback_data="fight_heroes_breast")
        heroes_legs = telebot.types.InlineKeyboardButton(text=fight_text["heroes_legs"], callback_data="fight_heroes_legs")
        heroes_foot = telebot.types.InlineKeyboardButton(text=fight_text["heroes_foot"], callback_data="fight_heroes_foot")

        enemy_head = telebot.types.InlineKeyboardButton(text=fight_text["enemy_head"], callback_data="fight_enemy_head")
        enemy_left = telebot.types.InlineKeyboardButton(text=fight_text["enemy_handleft"], callback_data="fight_enemy_handleft")
        enemy_right = telebot.types.InlineKeyboardButton(text=fight_text["enemy_handright"], callback_data="fight_enemy_handright")
        enemy_brest = telebot.types.InlineKeyboardButton(text=fight_text["enemy_breast"], callback_data="fight_enemy_breast")
        enemy_legs = telebot.types.InlineKeyboardButton(text=fight_text["enemy_legs"], callback_data="fight_enemy_legs")
        enemy_foot = telebot.types.InlineKeyboardButton(text=fight_text["enemy_foot"], callback_data="fight_enemy_foot")


        text_pole = telebot.types.InlineKeyboardButton(text=fight_text["null"], callback_data="1")
        healts_used = telebot.types.InlineKeyboardButton(text=self.user["healts_used"] , callback_data="1")
        enemy_healts = telebot.types.InlineKeyboardButton(text=self.user["enemy_healts"], callback_data="1")
        keyboard.row(text_pole)
        keyboard.row(heroes_head,  null, enemy_head,)
        keyboard.row(heroes_left, heroes_right,null, null,enemy_left, enemy_right)
#        keyboard.row(heroes_left, heroes_breast, heroes_right, enemy_left, enemy_brest,enemy_right)
        keyboard.row(heroes_breast, null, enemy_brest)
        keyboard.row(heroes_legs, null, enemy_legs)
        keyboard.row(heroes_foot, null, enemy_foot)
#        keyboard.row(text_pole)
        keyboard.row(healts_used, enemy_healts)
        return keyboard

    def fight(self):
        global fight_text, combat, comb, text_attaka, raund

        if self.text == "Атаковать":
            fight_text = fight_text_all.copy()
            combat = {}
            raund = 0
            text_attaka = "/-------------------------/"
            fight_text["null"] = "Защита 2 очка. Аттака 2 очка"
            bot.send_message(text="Аттака", chat_id=self.id, reply_markup=keyboard_map())
            bot.send_message(text="Вы аттаковали врага. Выберите какую часть тела защитить и атакуйте врага", chat_id=self.id, reply_markup=self.attaka_new())
  #      elif self.call == "null":
  #
        else:
                pprint(self.call)
                data = self.call.split("_")[1]
                data_old = self.call.split("_")[2]
                d = data +"_"+ data_old
                if data == "heroes":
                    if 0 < self.user["defence"] <= 2:
                        if data_old =="head":
                            fight_text[d] +=   " 🛡"
                            combat[d] = 1
                            pprint("test")
                            comb[d] += 1
                            pprint("test2")
                        elif data_old =="handleft":
                            fight_text[d] +=   " 🛡"
                            combat[d] = 1
                            comb[d] += 1
                        elif data_old =="handright":
                            fight_text[d] +=   " 🛡"
                            combat[d] = 1
                            comb[d] += 1
                        elif data_old == "breast":
                            fight_text[d] += " 🛡"
                            combat[d] = 1
                            comb[d] += 1
                        elif data_old =="legs":
                            fight_text[d] +=   " 🛡"
                            combat[d] = 1
                            comb[d] += 1
                        elif data_old =="foot":
                            fight_text[d] +=   " 🛡"
                            combat[d] = 1
                            comb[d] += 1
                        self.user["defence"] -=1

                        bot.answer_callback_query(callback_query_id=self.call_id, text='Защитились')
                    else:
                        bot.answer_callback_query(callback_query_id=self.call_id, text='Очки защиты законились')
                        return
                 #   elif self.user["defence"] >2:
                elif data == "enemy":
                    if 0 < self.user["attaka"] <= 2:
                        if data_old =="head":
                            fight_text[d] +=   " ⚔️"
                            combat[d] = 1
                            comb[d] += 1
                        elif data_old =="handleft":
                            fight_text[d] +=   " ⚔️"
                            combat[d] = 1
                            comb[d] += 1
                        elif data_old =="handright":
                            fight_text[d] +=   " ⚔️"
                            combat[d] = 1
                            comb[d] += 1
                        elif data_old == "breast":
                            fight_text[d] += " ⚔️"
                            combat[d] = 1
                            comb[d] += 1
                        elif data_old =="legs":
                            fight_text[d] +=   " ⚔️"
                            combat[d] = 1
                            comb[d] += 1
                        elif data_old =="foot":
                            fight_text[d] +=   " ⚔️"
                            combat[d] = 1
                            comb[d] += 1
                        self.user["attaka"] -=1

                        bot.answer_callback_query(callback_query_id=self.call_id, text='Аттаковали')
                    else:
                        bot.answer_callback_query(callback_query_id=self.call_id, text='Очки аттаки законились')
                        return
                save("combat")
                if self.user["defence"] == 0 and self.user["attaka"] == 0:
                    self.user["attaka"] = 2
                    self.user["defence"] = 2

                    text = "Идет бой, ожидайте"
                    fight_text["null"] = text
                    bot.edit_message_text(text=text_attaka, chat_id=self.id, message_id=self.message_call_id,
                                          reply_markup=self.attaka_new())
                    text_old = self.combat_battle()
                    raund += 1
                    text_attaka += "\n/----/ Раунд "+str(raund)+" /----/" + text_old +"\n"
                    time.sleep(3)
                    fight_text = fight_text_all.copy()
                    text = "Защита 2 очка. Аттака 2 очка"
                    fight_text["null"] = text
                    if self.user["healts_used"] <= 0:
                        bot.delete_message(self.id, message_id=self.message_id)
                        bot.send_message(self.id, text=text_attaka)
                        self.congratulation("enemy")
                        print("Герой проиграл")
                    elif self.user["enemy_healts"] <= 0:
                        bot.delete_message(self.id, message_id=self.message_id)
                        bot.send_message(self.id, text=text_attaka)
                        self.congratulation("heroes")
                        print("Враг проиграл")
                    else:
                        bot.edit_message_text(text=text_attaka, chat_id=self.id, message_id=self.message_call_id,
                                          reply_markup=self.attaka_new())

                else:
                    defence = self.user["defence"]
                    attaka = self.user["attaka"]

#                    text = "Выберите часть тела для защиты и для аттаки"
                    text = "Защита "+str(defence)+" очка. Аттака "+str(attaka)+" очка"
                    fight_text["null"] = text

                    bot.edit_message_text(text=text_attaka, chat_id=self.id, message_id=self.message_call_id, reply_markup=self.attaka_new())

    def combat_battle(self):
        global combat, comb , her,ene
#        pprint(combat)
        text = ""
        her,ene = {},{}
        for key, value in comb.items():
            if key.split("_")[0] == "heroes":
                her[key] = value
            elif key.split("_")[0] == "enemy":
                ene[key] = value

        max_value_her = min(her.values())
        for k, v in her.items():
                 if v == max_value_her:
                     her[k] = 9999999
                     heroes_attaka = k
                     break

        max_value_her = min(her.values())
        for k, v in her.items():
                 if v == max_value_her:
                     heroes_attaka_second = k


        max_value_ene = max(ene.values())
        for k, v in ene.items():
                 if v == max_value_ene:
                     ene[k] = 0
                     defence_enemy = k
        max_value_ene = max(ene.values())
        for k, v in ene.items():
                 if v == max_value_ene:
                     defence_enemy_second = k

        for key, value in combat.items():

            if heroes_attaka == key:
                text += "\n 🛡 Вы отразили аттаку врага в "+ fight_trans[heroes_attaka]
            elif heroes_attaka_second == key:
                text += "\n 🛡 Вы отразили аттаку врага в "+ fight_trans[heroes_attaka_second]
            elif defence_enemy == key:
                text += "\n 🛡 Враг отразил вашу аттаку в "+fight_trans[defence_enemy]
            elif defence_enemy_second == key:
                text += "\n 🛡 Враг отразил вашу аттаку в "+fight_trans[defence_enemy_second]
            elif key.split("_")[0] == "heroes":
                text += "\n ⚔️Враг нанес вам удар -"+ str(self.user["enemy_hit"])+" ♥️"
                self.user["healts_used"] -= self.user["enemy_hit"]
            elif key.split("_")[0] == "enemy":
                text += "\n ⚔️Вы нанесли удар противнику - "+str(self.user["hit"])+" ♥️"
                self.user["enemy_healts"] -= self.user["hit"]

        combat = {}
        return text

    def all_battle(self):
        text_all_battle = "Вы отправились на поле боя. Ожидайте сражения\n Сражения проводятся в 10:00, 14:00, 18:00"
        self.user["allbattle"] = 1
        save("users")
        bot.delete_message(chat_id=self.id, message_id=self.message_id)
        bot.send_message(chat_id=self.id, text=text_all_battle, reply_markup=all_battle())

@bot.message_handler(commands=['start'])
def start_message(message):

    if message.chat.id == ADMIN:
        bot.send_message(text="Админское меню", chat_id=message.chat.id, reply_markup=keyadmin())
    else:
        start_user(message)


@bot.message_handler(content_types=['successful_payment'])
def got_payment(message):
    bot.send_message(message.chat.id,
                     'Ура! Спасибо за оплату! Мы выполним ваш заказ как можно быстрее! '
                     'Оставайтесь на связи. '.format(
                         message.successful_payment.total_amount / 1000, message.successful_payment.currency),
                     parse_mode='Markdown', reply_markup=keyboard_main_menu())


@bot.message_handler(content_types=['text'])
def send_text(message):
    global menu, status, barracks
    pprint("test1")
    user_bot = User(message)
    maps_bot = Maps(message)
    buy_bot = Buy(message)
    battle_bot = Battle(message)
    pprint("test2")
    if message.chat.id == ADMIN:
        if message.text == "Создать карту":
            maps_bot.new_maps()
        elif message.text == "Кол-во ячеек":
            maps_bot.statistika()
        elif message.text == "Новая атака":
            battle_bot.new_attaka()
        elif message.text == "Бой":
            users[str(message.chat.id)]["defence"] = 2
            users[str(message.chat.id)]["attaka"] = 2
            battle_bot.fight()


    else:
        if message.text == 'Карта 🗺' or message.text == "На карту 🗺":
            bot.send_message(text="⏱ Вывод карты ⏱", chat_id=message.chat.id, reply_markup=keyboardmap())
            time.sleep(1)
            bot.send_message(text="Делайте ход по игровому полю", chat_id=message.chat.id,
                             reply_markup=maps_bot.output_map())
        elif message.text == "Город":
            menu = "dom"
            bot.send_message(text="Город", chat_id=message.chat.id, reply_markup=keyboard_main_menu())
        elif message.text == 'Вернуться в город':
            menu = "dom"
            bot.send_message(text="Домой", chat_id=message.chat.id, reply_markup=keyboard_main_menu())
        elif message.text == 'Копать':
            menu = "rudnic"
            status = "open"
            bot.send_message(text=start_text_mining, chat_id=message.chat.id, reply_markup=keyboard_map())
#            bot.send_message(text="rjgfnm", chat_id=message.chat.id, reply_markup=keyboard_map())
            maps_bot.mining()
        elif message.text == 'Назад':
            if menu == "dom" or menu == "rudnic":
                bot.send_message(text="Назад", chat_id=message.chat.id, reply_markup=keyboardmap())
                bot.send_message(text="Назад", chat_id=message.chat.id, reply_markup=maps_bot.output_map())
            elif menu == "heroes" or menu == "building" or menu == "info":
                menu = "dom"
                bot.send_message(text="Назад", chat_id=message.chat.id, reply_markup=keyboard_main_menu())
            elif menu == "sklad" or menu == "barracks":
                menu = "building"
                bot.send_message(text="Назад", chat_id=message.chat.id, reply_markup=keyboard_building())
            elif menu == "feedback" or menu == "help":
                menu = "info"
                bot.send_message(text="Назад", chat_id=message.chat.id, reply_markup=keyboard_info())
            elif menu == "QIWI":
                menu = "feedback"
                bot.send_message(text="Назад", chat_id=message.chat.id, reply_markup=keyboard_buy())
            else:
                bot.send_message(text="Назад", chat_id=message.chat.id, reply_markup=keyboardmenu())

        elif message.text == 'Герой':
            menu = "heroes"
            bot.send_message(text=user_bot.info_heroes("heroes"), chat_id=message.chat.id)
        elif message.text == 'Склад':
            menu = "sklad"

            user_bot.build()
            bot.send_message(text=user_bot.info_heroes("sklad"), chat_id=message.chat.id, reply_markup=keyboardback())


        elif message.text == "Меню игрока":
            bot.send_message(text="Меню игрока", chat_id=message.chat.id, reply_markup=keyboardmenu())

        elif message.text == "Вернуться на карту 🗺":
            status = "close" + str(message.chat.id)
            bot.send_message(text="Вернуться", chat_id=message.chat.id, reply_markup=keyboardmap())



        elif message.text == "Покинуть поле боя":
            users[str(message.chat.id)]["allbattle"] = 0
            save("users")
            bot.send_message(text="Вернуться", chat_id=message.chat.id, reply_markup=keyboardmap())
            bot.send_message(text="Делайте ход по игровому полю", chat_id=message.chat.id,
                             reply_markup=maps_bot.output_map())

        elif message.text == "Атаковать":
            users[str(message.chat.id)]["defence"] = 2
            users[str(message.chat.id)]["attaka"] = 2
#            bot.send_message(text="Бой", chat_id=message.chat.id, reply_markup=keyboardback())
            battle_bot.fight()
         #   battle_bot.attak()
            #bot.send_message(text="Выберите действие: Атаковать или Защищаться", chat_id=message.chat.id, reply_markup=battle_bot.keyboard_attak_new())

        elif message.text == "Отступить":
#            bot.send_message(text="Бой", chat_id=message.chat.id, reply_markup=keyboardback())
            bot.send_message(text="⏱ Вывод карты ⏱", chat_id=message.chat.id, reply_markup=keyboardmap())
            time.sleep(2)
            bot.send_message(text="Делайте ход по игровому полю", chat_id=message.chat.id,
                         reply_markup=maps_bot.output_map())


        elif message.text == "Казарма":
            barracks = 1
            menu = "barracks"
            user_bot.build()
            #            bot.send_message(text="Казарма", chat_id=message.chat.id, reply_markup=keyboardbarracks())
            user_bot.barracks("all")

        elif barracks == 1:
            if message.text == "Обучить лучника":
                user_bot.barracks("archer")
            elif message.text == "Да":
                user_bot.barracks("yes")

            elif message.text == "Нет":
                save("all")
                barracks = 0
                bot.send_message(text="Казарма", chat_id=message.chat.id, reply_markup=keyboardbarracks())
        elif message.text == "Строения":
            menu = "building"
            bot.send_message(text="Будет добавлено в следующем обновлении", chat_id=message.chat.id)
            user_bot.building()

        elif message.text == "⚙ Настройки":
            menu = "info"
            bot.send_message(text=texthelp, chat_id=message.chat.id, reply_markup=keyboard_info())

        elif message.text == "Обратная связь":
            menu = "feedback"
            bot.send_message(
                text="Напишите ваши пожелания или найденные ошибки. \n Если нажали случайно, введите 'нет'",
                chat_id=message.chat.id, reply_markup=keyboard_info())
            bot.register_next_step_handler(message, please)

        elif message.text == "Помочь проекту":
            menu = "feedback"
            bot.send_message(text=textsell+"Выберите платежную систему", chat_id=message.chat.id, reply_markup=keyboard_buy())


        elif message.text == "QIWI":
            menu = "QIWI"
            bot.send_message(text=textbuy, chat_id=message.chat.id, reply_markup=keyboarddel())
            bot.register_next_step_handler(message, buy)
#
        elif message.text == "Оплата QIWI":
            buy_bot.buy_qiwi()
            bot.send_message(text=textbuy, chat_id=message.chat.id, reply_markup=keyboard_info())

        elif message.text == "Tranzzo":
            menu = "Tranzzo"
            buy_bot.buy_tranzzo()
        elif message.text == "Всё понятно":
            user_bot.new_game()

        #            bot.send_message(message.chat.id, "Начнем игру", reply_markup=keyboard_main_menu())
        elif message.text == "Чат":
            bot.send_message(message.chat.id, "Чат предназначен для общения, предложения идей и выявления багов @heroeslifeg")
        elif message.text == "Пригласить":
            bot.send_message(message.chat.id,
                             "Для приглашения друга отправть ему ссылку ниже. И получи 10 💎 за каждый взятый им уровень")
            bot.send_message(message.chat.id,  "https://telegram.me/heroeslifebot?start="+str(message.chat.id))

        elif message.text == "Помощь":
#            bot.send_message(chat_id=message.chat.id, text=text_help)
            user_bot.help()
        else:
            pprint(message.text)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    maps_bot = Maps(message=call.message, call=call)
    battle_bot = Battle(message=call.message, call=call)
    buy_bot = Buy(message=call.message, call=call)
    user_bot = User(message=call.message, call=call)

    if call.data.split("_")[0] == "battle":
        battle_bot.attak()
    elif call.data.split("_")[0] == "build":
        user_bot.build(data = call.data.split("_")[1])
    elif call.data.split("_")[0] == "fight":
        battle_bot.fight()
    elif call.data == "buy_qiwi":
        buy_bot.buy_check_qiwi()
    elif call.data == "null":
        bot.answer_callback_query(callback_query_id=call.id, text='Не активное поле')
    elif call.data.split("_")[0] =="help":
        user_bot.help()
    elif call.data == "goto_battle":
        battle_bot.all_battle()
    else:
        maps_bot.goto()


@bot.shipping_query_handler(func=lambda query: True)
def shipping(shipping_query):
    print(shipping_query)
    bot.answer_shipping_query(shipping_query.id, ok=True,
                              error_message='Oh, seems like our Dog couriers are having a lunch right now. Try again later!')


@bot.pre_checkout_query_handler(func=lambda query: True)
def checkout(pre_checkout_query):
    bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True,
                                  error_message="Aliens tried to steal your card's CVV, but we successfully protected your credentials,"
                                                " try to pay again in a few minutes, we need a small rest.")


# while True:
try:
    #        bot.polling(none_stop=True, timeout=30)
    bot.infinity_polling(True)
except Exception as e:
    print(e)
