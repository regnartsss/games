from config import *
import battle_game
from keyboard import *
from data import *
import time
import random
import json
from datetime import datetime, timedelta
from pprint import pprint
import threading
from buy import buy_amount, buy_tranzzo, succefull_tranzzo

import logging
from battle_timer import shed
import timeit

ADMIN = 7653334401

menu = 0
barracks = 0

global lvlrudnic

logging.basicConfig(filename='app.txt', format='%(name)s - %(levelname)s - [%(asctime)s] %(message)s',
                    level=logging.INFO)


def find_location():
    return os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))).replace('\\', '/') + '/'


PATH = find_location()


def save(key):
    global maps, users, log, comb, allbattle
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
    elif key == "allbattle":
        with open(PATH + "tmp/" + 'allbattle.json', 'w', encoding="utf-16") as f:
            json.dump(allbattle, f)
        with open(PATH + "tmp/" + 'allbattle.json', 'rb') as f:
            allbattle = json.load(f)


def start_open():
    logging.info("Запуск игры")

    global maps, users, comb, allbattle

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

    allbattle = {}
    try:
        with open(PATH + "tmp/" + 'allbattle.json', 'rb') as f:
            allbattle = json.load(f)
    except:
        with open(PATH + "tmp/" + 'allbattle.json', 'w', encoding="utf-16") as f:
            json.dump(allbattle, f)
        with open(PATH + "tmp/" + 'allbattle.json', 'rb') as f:
            allbattle = json.load(f)


def start_user_default():
    global users

    for key, value in users.items():
        value["health_used"] = value["health"]
        value["step_used"] = value["step"]
        value["energy_used"] = value["energy"]
    logging.info('Здоровье, шаги, энергия восстановлены')
    save("users")


def check_users():
    global users
    for key, value in users.items():
        #         users[key]["avatar"]= "👶"
        #         users[key]["nik_name"]= "player"
        #         users[key]["free_name"]= 0
        users[key]["building"]["castle"] = 1
        #        try:
        #       print(str(key)+" " + str(value))
        """   
        print(value["id"])
        print(value["username"])
        print(value["date"])
        print(value["avatar"])
        print(value["nik_name"])
        print(value["free_name"])
        print(value["energy"])
        print(value["energy_used"])
        print(value["step"])
        print(value["step_used"])
        print(value["lvlstep"])
        print(value["wolk_used"])
        print(value["wolk"])
        print(value["lvlheroes"])
        print(value["health"])
        print(value["health_used"])
        print(value["wood"])
        print(value["stone"])
        print(value["iron"])
        print(value["food"])
        print(value["gold"])
        print(value["diamond"])
        print(value["experience"])
        print(value["experience_used"])
        print(value["hit"])
        print(value["ref"])
        print(value["weapons"])
        print(value["building"])

       except Exception as n:
           k = str(n)[1:-1]
           pprint(k)
           users[key][k] = ""
#            print(users[key])
           check_users()
           continue
       """
    save("users")


def start_user(message):
    logging.info(str(message.chat.id) + ' Команда /start')
    global maps, users, log
    try:
        ref = str(message.text.split(" ")[1])
        logging.info(str(message.chat.id) + ' Вход по реф ссылке ' + ref)
    except:
        ref = "0"
    date_t = date("all")
    if str(message.chat.id) in users:
        logging.info(str(message.chat.id) + 'Пользователь уже есть')

        bot.send_message(message.chat.id, "Пользователь есть", reply_markup=keyboard_main_menu())
    else:

        #            message.chat.id = users[str(message.chat.id)]
        #            log = log + date("fulltime") + " Зарегистрирован новый пользователь " + str(message.chat.id) + "\n"
        users[str(message.chat.id)] = {"id": message.chat.id,
                                       "username": message.from_user.first_name,
                                       "date": str(date_t),
                                       "avatar": "👶",
                                       "nik_name": "player",
                                       "free_name": 0,
                                       "energy": 0,  # Энергия
                                       "energy_used": 0,  # Энергия истраченная
                                       "step": 0,  # Ходов
                                       "step_used": 0,  # Ходов истрачено
                                       "lvlstep": 1,
                                       "wolk_used": 0,  # Надо пройти
                                       "wolk": 0,  # Пройдено
                                       "lvlheroes": 1,
                                       "health": 0,
                                       "health_used": 0,
                                       "wood": 0,
                                       "stone": 0,
                                       "iron": 0,
                                       "food": 0,
                                       "gold": 0,
                                       "diamond": 0,
                                       "experience": 0,  # Энергия
                                       "experience_used": 0,  # Энергия истрачено
                                       "hit": 20,
                                       "ref": ref,
                                       "weapons": {"arm": ""},
                                       "building": {},
                                       "farm_time": datetime.now().strftime("%Y:%m:%d:%H:%M:%S")
                                       }

        s = random.randint(1, len(maps))

        maps[str(s)] = {"id": str(message.chat.id)}
        pprint(s)
        pprint(maps[str(s)])
        bot.send_message(chat_id=765333440,
                         text=date("fulltime") + " Зарегистрирован новый пользователь " + str(message.chat.id))
        logging.info(str(message.chat.id) + ' Новый пользователь')

    bot.send_message(message.chat.id, text=start_text, reply_markup=keyboard_start())

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


def all_battle():
    threading.Thread(target=shed).start()


start_open()
start_user_default()


# all_battle()
# check_users()


class Maps():

    def __init__(self, message, call=""):
        global maps, menu, status, attak
        try:
            self.call = call.data
            self.call_id = call.id
            self.call_message_id = call.message.message_id
        except:
            pass
        self.first_name = message.from_user.username
        self.id = message.chat.id
        self.text = message.text
        self.message_id = message.message_id
        self.user = users[str(self.id)]

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
        r = random.randint(1, 20)
        if r == 1:
            self.resource_res(old_res="wood", n=n)
        elif r == 2:
            self.resource_res(old_res="stone", n=n)
        elif r == 3:
            self.resource_res(old_res="iron", n=n)
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
                elif maps[str(key)]["resource"] == "iron":
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
               + "\nжелезо " + str(i) + " \nlvl 1: " + str(i1) + " \nlvl 2: " + str(i2) + " \nlvl 3: " + str(
            i3) + " \nlvl 4: " + str(i4) + " \nlvl 5: " + str(i5) \
               + "\nкамень " + str(s) + " \nlvl 1: " + str(s1) + " \nlvl 2: " + str(s2) + " \nlvl 3: " + str(
            s3) + " \nlvl 4: " + str(s4) + " \nlvl 5: " + str(s5) \
               + "\nигроков " + str(u) + "\nПустых ячеек " + str(n) + "\nВрагов " + str(e)
        pprint(text)
        bot.send_message(chat_id=self.id, text=text)

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
                        if cell == "iron":
                            tab.append(telebot.types.InlineKeyboardButton("⚒", callback_data=str(start_field)))
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
                            tab.append(
                                telebot.types.InlineKeyboardButton(self.user["avatar"], callback_data=str(start_field)))
                        elif cell != "null":
                            tab.append(telebot.types.InlineKeyboardButton(users[str(cell)]["avatar"],
                                                                          callback_data=str(start_field)))
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
            #        arena = telebot.types.InlineKeyboardButton(text="Отправиться на поле боя", callback_data="gotobattle")
            keyboard.row(step, energy)
            #            keyboard.row(arena)
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
            value_call = maps[str(self.call)]["resource"]
        except:
            try:
                value_call = self.call.split("_")[1]
            except:
                value_call = "null"
        if users[str(self.id)]["step_used"] == 0:
            bot.send_message(text="У вас нет ходов", chat_id=self.id)
        elif users[str(self.id)]["health_used"] <= 0:
            bot.send_message(text="Вы мертвы", chat_id=self.id)

        elif self.call == cell_user:
            bot.answer_callback_query(self.call_id, 'Это вы')

        elif int(self.call) == int(cell_user) - 1:
            if value_call == "iron" or value_call == "wood" or value_call == "stone":
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

        elif int(self.call) == int(cell_user) + 1:
            if value_call == "iron" or value_call == "wood" or value_call == "stone":
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

        elif int(self.call) == int(cell_user) - pole:
            if value_call == "iron" or value_call == "wood" or value_call == "stone":
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

        elif int(self.call) == int(cell_user) + pole:
            if value_call == "iron" or value_call == "wood" or value_call == "stone":
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
            bot.answer_callback_query(callback_query_id=self.call_id, text='Поле не активно')
        elif value_call == "iron":
            bot.answer_callback_query(callback_query_id=self.call_id, text='Шахта с едам')
        elif value_call == "wood":
            bot.answer_callback_query(callback_query_id=self.call_id, text='Шахта с деревом')
        elif value_call == "stone":
            bot.answer_callback_query(callback_query_id=self.call_id, text='Шахта с камнем')
        elif value_call == "enemy":
            bot.answer_callback_query(callback_query_id=self.call_id, text='Страшный монстр')
        elif value_call == "olduser":
            bot.answer_callback_query(callback_query_id=self.call_id, text='Город соперника')

    def goto_cell(self, cell_user, position_user):
        maps[str(cell_user)] = {"resource": "null"}
        maps[str(int(cell_user) + position_user)] = {"id": str(self.id)}
        self.move()
        bot.edit_message_text(text="Ходите", chat_id=self.id, message_id=self.message_id,
                              reply_markup=self.output_map())

    def enemy_write(self, cell_user):
        r = random.randint(self.user["lvlheroes"] - 1, self.user["lvlheroes"])
        if r <= 0:
            r = 1
        logging.info(str(self.id) + ' Атака монстра, уровень монстра' + str(r))
        self.user["enemy_lvl"] = str(r)
        self.user["enemy_health"] = 50 * r
        self.user["enemy_exr"] = 5 * r
        self.user["enemy_cell"] = str(self.call)
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
        map_res = self.call
        res = maps[str(self.call)]["resource"]
        kol = maps[str(self.call)]["number"]
        lvl = maps[str(self.call)]["lvl"]
        timer = self.time(kol // lvlrudnic[lvl])
        menu = "rudnic"
        bot.send_message(text=text_mining(res, lvl, kol, timer), chat_id=self.id, reply_markup=keyrudnic())

    def time(self, timer):
        return time.strftime('%M:%S', time.gmtime(timer))

    def timer(self):
        global maps, users, res, kol, map_res, status, lvl
        timer = int(kol) // lvlrudnic[lvl]
        ss = 1
        sum, text = 0, ""
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
            text = "⚡️Вы завершили добычу ⚡️\nСобрано " + str(sum)
        elif int(maps[str(sell)]["number"]) - int(sum) >= 0:
            maps[str(sell)]["number"] = maps[str(sell)]["number"] - sum
            summa = sum + users[str(self.id)][res]
            users[str(self.id)][res] = summa
            text = "⚡️Вы завершили добычу ⚡️\nСобрано " + str(sum)
        else:
            pprint("ошибка")
        print(users[str(self.id)][res])
        print(buildings["storage"][self.user["building"]["storage"]]["capacity"])

        if self.user[res] > buildings["storage"][self.user["building"]["storage"]]["capacity"]:
            self.user[res] = buildings["storage"][self.user["building"]["storage"]]["capacity"]
            text = "⚡️Вы завершили добычу ⚡ \nСклад полон"
        save("all")
        bot.send_message(text=text, chat_id=self.id,
                         reply_markup=keyboardmap())
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

    # class User():

    #    def __init__(self, message, call=""):
    #        try:
    #            self.call= call.data
    #            self.call_id = call.id
    #            self.call_id = call.message.message_id
    #            pprint(self.call_id)
    #        except:
    #            pass

    #        self.id = message.chat.id
    #        self.text = message.text
    #        self.first_name = message.from_user.username
    #        self.user = users[str(self.id)]
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
            if self.call == "help_maps":
                text = "На карте вы можете добывать ресурсы и воевать против монстров.\n На карте распологаются ресурсы: еда, камень, дерево. Они вам понадобятся для постройки у улучшения вашего города."
            elif self.call == "help_battle":
                text = "Бой с соперником проходит в пошаговом режиме.\n На каждом ходе у вас есть два очка защиты и два очка нападения.\n "
            keyboard.add(maps, battle)
            bot.edit_message_text(chat_id=self.id, text=text, message_id=self.message_id, reply_markup=keyboard)

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
        self.user["health"] = lvlhealth[self.user["lvlheroes"]]
        self.user["health_used"] = lvlhealth[self.user["lvlheroes"]]
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
                self.user["health"] = lvlhealth[self.user["lvlheroes"]]
                self.user["health_used"] = self.user["health"]
                self.user["energy"] = lvlenergy[self.user["lvlheroes"]]
        save("users")

    def info_heroes(self, key):
        id = self.user["id"]
        username = self.user["username"]
        #        date = self.user["date"]
        level = self.user["lvlheroes"]
        health = self.user["health"]
        health_used = self.user["health_used"]
        experience = self.user["experience"]
        wood = self.user["wood"]
        stone = self.user["stone"]
        iron = self.user["iron"]
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
        food = self.start_farm()
        #       print(self.user)
        heroes = "Информация о герое\n" + "id: " + str(id) + "\n" + \
                 "👤 Имя: " + str(username) + "\n" + \
                 "🏅 Уровень: " + str(level) + "\n" + \
                 "🔋 Энергия: " + str(energy_used) + '/' + str(energy) + "\n" + \
                 "🌟 Опыт: " + str(experience_used) + "/" + str(experience) + "\n" + \
                 "❤ Здоровье: " + str(health_used) + "/" + str(health) + "\n" + "\n" + \
                 "Урон: " + str(hit) + "\n" + "\n" + \
                 "🚶‍♂️Ур. ходьбы: " + str(lvlstep) + " (" + str(wolk_used) + '/' + str(wolk) + ")" + "\n" + \
                 "🚶‍♂️Ходов по карте: " + str(step_used) + '/' + str(step) + "\n" + "\n" + \
                 "💰 Золото: " + str(gold) + "\n" + \
                 "💎 Алмазы: " + str(iamond) + "\n"

        sklad = "Информация о складе\n" + "Железо: " + str(iron) + "\n" + "Дерево: " + str(
            wood) + "\n" + "Камень: " + str(stone)
        stat = "⚒: " + str(iron) + " 🌲: " + str(wood) + " ⛏: " + str(stone) + " 🌽: " + str(food) + " 💰: " + str(gold)
        #       print("rer")
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

    #        if users[str(self.id)]["energy_used"] == users[str(self.id)]["energy"]:
    #            bot.send_message(chat_id=self.id, text="Энергия восстановилась " + str(users[str(self.id)]["energy_used"]))

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
            save("user")

    #        if users[str(self.id)]["step_used"] == users[str(self.id)]["step"]:
    #            bot.send_message(chat_id=self.id, text="Ходы восстановились " + str(users[str(self.id)]["step_used"]))

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

    def start_farm(self):
        global users
        farm_time_old = datetime.now().strftime("%Y:%m:%d:%H:%M:%S")
        a = farm_time_old.split(':')
        aa = datetime(int(a[0]), int(a[1]), int(a[2]), int(a[3]), int(a[4]), int(a[5]))
        farm_time = self.user["farm_time"]
        b = farm_time.split(':')
        bb = datetime(int(b[0]), int(b[1]), int(b[2]), int(b[3]), int(b[4]), int(b[5]))
        ss = (aa - bb).seconds
        lvl_farm = self.user["building"]["farm"]
        num_farm = buildings["farm"][lvl_farm]["production"]
        num_farm = num_farm * ss
        lvl_storage = self.user["building"]["storage"]
        num_storage = buildings["storage"][lvl_storage]["capacity"]
        #    print(num_storage)
        #    print(num_farm)
        self.user["food"] += num_farm
        if self.user["food"] > num_storage:
            #            print("Склад полон")
            self.user["food"] = num_storage
        else:
            self.user["food"] += num_farm
        self.user["farm_time"] = farm_time_old
        save("users")
        return self.user["food"]

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
            iron = archer["1"]["iron"]
            pprint("test")
            text = "Обучить за " + str(wood) + " " + str(stone) + " " + str(iron)
            bot.send_message(text=text, chat_id=self.id, reply_markup=keyboaryesno())
        elif barr == "yes":
            users[str(self.id)]["wood"] = str(int(users[str(self.id)]["wood"]) - archer["1"]["wood"])
            users[str(self.id)]["stone"] = str(int(users[str(self.id)]["stone"]) - archer["1"]["stone"])
            users[str(self.id)]["iron"] = str(int(users[str(self.id)]["iron"]) - archer["1"]["iron"])
            users[str(self.id)]["archer"] = arc + 1
            bot.send_message(text="Вы обучили лучника \n Общее кол-во " + str(users[str(self.id)]["archer"]),
                             chat_id=self.id, reply_markup=keyboaryesno())
            save("all")

    def build(self, data):
        keyboard = telebot.types.InlineKeyboardMarkup()
        if data == "back":
            #            bot.delete_message(chat_id=self.id, message_id=self.message_id)
            self.building()
        elif data == "update":
            build = self.call.split("_")[2]
            text_stone, text_wood, text_iron, text_food = self.building_update(build)
            if text_stone == "✅" and text_wood == "✅" and text_iron == "✅" and text_food == "✅":
                if build == "storage" and self.user["building"]["castle"] <= self.user["building"]["storage"]:
                    bot.answer_callback_query(callback_query_id=self.call_id, text="Увеличьте уровень 🏤 замка")
                    self.user["building"]["temp"] = "storage"
                    self.build(data="castle")
                elif build == "farm" and self.user["building"]["storage"] <= self.user["building"]["farm"]:
                    bot.answer_callback_query(callback_query_id=self.call_id, text="Увеличьте уровень 🏚склада")
                    self.user["building"]["temp"] = "farm"
                    self.build(data="storage")
                elif build == "barracks" and self.user["building"]["farm"] <= self.user["building"]["barracks"]:
                    bot.answer_callback_query(callback_query_id=self.call_id, text="Увеличте уровень фермы")
                    self.user["building"]["temp"] = "barracks"
                    self.build(data="farm")
                elif build == "shooting " and self.user["building"]["barracks"] <= self.user["building"]["shooting "]:
                    bot.answer_callback_query(callback_query_id=self.call_id, text="Увеличте уровень казармы")
                    self.user["building"]["temp"] = "shooting "
                    self.build(data="barracks")
                elif build == "stable" and self.user["building"]["shooting "] <= self.user["building"]["stable"]:
                    bot.answer_callback_query(callback_query_id=self.call_id, text="Увеличте уровень стрельбы")
                    self.user["building"]["temp"] = "stable"
                    self.build(data="shooting ")
                elif build == "wall" and self.user["building"]["stable"] <= self.user["building"]["wall"]:
                    bot.answer_callback_query(callback_query_id=self.call_id, text="Увеличте уровень конюшны")
                    self.user["building"]["temp"] = "wall"
                    self.build(data="stable")
                elif build == "castle" and self.user["building"]["wall"] < self.user["building"]["castle"]:
                    bot.answer_callback_query(callback_query_id=self.call_id, text="Увеличте уровень 🧱 стены")
                    self.user["building"]["temp"] = "castle"
                    self.build(data="wall")
                else:

                    print("все ресурсы есть")
                    self.user["building"][build] += 1
                    new_lvl = self.user["building"][build]
                    pprint(new_lvl)
                    num_stone, num_wood, num_iron, num_food = static_buildings(build, new_lvl)
                    #                        print(num_stone)
                    self.user["wood"] -= num_wood
                    self.user["stone"] -= num_stone
                    self.user["iron"] -= num_iron
                    self.user["food"] -= num_food
                    try:
                        buil = self.user["building"]["temp"]
                        if build == "":
                            self.build(data=build)
                        else:
                            self.user["building"].pop("temp")
                            self.build(data=buil)
                    except:
                        self.build(data=build)

                    #                save
                    #    print(data_old)

                    #    if data_old != "":
                    #        self.build(data=data_old)
                    #    else:


            else:
                #                print("не хватает ресуров")
                bot.answer_callback_query(callback_query_id=self.call_id, text="Не хватает ресуров")

        #        elif data == "market" or data == "wall" or data == "shooting " or data == "stable" or data == "barracks" or data == "castle":
        #            bot.answer_callback_query(callback_query_id=self.call_id, text='Не активно, ожидайте обновление')

        else:

            name = buildings[data]["name"]
            lvl = self.user["building"][data]
            new_lvl = lvl + 1
            num_stone, num_wood, num_iron, num_food = static_buildings(data, new_lvl)
            text_stone, text_wood, text_iron, text_food = self.building_update(data)
            stone = str(num_stone) + text_stone
            wood = str(num_wood) + text_wood
            iron = str(num_iron) + text_iron
            food = str(num_food) + text_food
            text = "Строение " + name + " " + str(lvl) + " уровня\n Улучшить " + name + " до " + str(
                new_lvl) + " уровня за: \n Камень: " + stone + "\n Дерево: " + wood + "\n Железо: " + iron + "\n Еда: " + food
            keyboard.row(telebot.types.InlineKeyboardButton(text="Улучшить",
                                                            callback_data="build_update_" + data))
            keyboard.row(telebot.types.InlineKeyboardButton(text="Назад", callback_data="build_back"))
            if data == "storage":
                text += "\nВместимость ресурсов: " + str(buildings[data][lvl]["capacity"])
            elif data == "farm":
                text += "\nПроизводство ресурсов: " + str(buildings[data][lvl]["production"]) + " шт\с"

        bot.edit_message_text(text=text, chat_id=self.id, message_id=self.message_id, reply_markup=keyboard)

    def building_update(self, data):
        pprint("building update")
        lvl = self.user["building"][data]
        new_lvl = lvl + 1
        stone_player = self.user["stone"]
        wood_player = self.user["wood"]
        iron_player = self.user["iron"]
        food_player = self.user["food"]
        stone = static_buildings(data, new_lvl)[0]
        wood = static_buildings(data, new_lvl)[1]
        iron = static_buildings(data, new_lvl)[2]
        food = static_buildings(data, new_lvl)[3]
        text_stone, text_wood, text_iron, text_food = "✅", "✅", "✅", "✅"
        if stone_player < stone:
            text_stone = "⛔️"
        #           pprint("Не хватает камня")
        if wood_player < wood:
            text_wood = "⛔️ "
        #          pprint("Не хватает дерева")
        if iron_player < iron:
            text_iron = "⛔️"
        #           pprint("Не хватает железа")
        if food_player < food:
            text_food = "⛔️"
        #           pprint("Не хватает еды")
        return text_stone, text_wood, text_iron, text_food

    def translator(self):
        if self.text == "Склад":
            bul = "storadge"
        elif self.text == "Казарма":
            bul = "barracks"
        return bul

    def building(self):
        if self.user["building"] == {}:
            bul = {}

            for key, value in buildings.items():
                bul.update({key: 0})
            self.user["building"] = bul
            self.user["building"]["castle"] = 1
            save("users")
        elif self.text == "Строения":
            bot.send_message(text="Здесь вы можете улучшить ваши постройки", chat_id=self.id,
                             reply_markup=self.print_building())

        else:
            bot.edit_message_text(text="Здесь вы можете улучшить ваши постройки", chat_id=self.id,
                                  message_id=self.message_id, reply_markup=self.print_building())

    def print_building(self):
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.row(telebot.types.InlineKeyboardButton(text=self.info_heroes(key="stat"), callback_data=" "))
        i = 1
        tab = []
        for key, value in self.user["building"].items():
            lvl = self.user["building"][key]
            tab.append(telebot.types.InlineKeyboardButton(text=buildings[key]["name"] + " " + str(lvl),
                                                          callback_data="build_" + key))
            if i == 1 or i == 4 or i == 7:
                keyboard.row(*tab)
                tab = []
            i += 1
        keyboard.row(*tab)
        keyboard.row(telebot.types.InlineKeyboardButton(text="🎪 Рынок", callback_data="build_market"))
        return keyboard

    def timer_health(self):
        while users[str(self.id)]["health_used"] < users[str(self.id)]["health"]:
            time.sleep(60)  # in seconds
            users[str(self.id)]["health_used"] = users[str(self.id)]["health"]

            save("user")
        if users[str(self.id)]["health_used"] == users[str(self.id)]["health"]:
            bot.send_message(chat_id=self.id, text="Здоровье восстановлено ")

    def congratulation(self, data):
        if data == "heroes":
            self.user["experience_used"] += 5
            r_gold = random.randint(1, 50)
            self.user["gold"] += r_gold
            maps[self.user["enemy_cell"]]["resource"] = "null"
            self.update_statistic(data="experiens")
            self.energy()

            bot.send_message(text="Бой окончен: ", chat_id=self.id, reply_markup=keyboardmap())
            bot.send_message(text="Вы победили и получили 5 опыта.\n Вам выпало " + str(r_gold) + " золота",
                             chat_id=self.id,
                             reply_markup=self.output_map())
        elif data == "enemy":
            threading.Thread(target=self.timer_health, daemon=True).start()
            self.energy()
            bot.send_message(text="Бой окончен: ", chat_id=self.id, reply_markup=keyboardmap())
            bot.send_message(text="Вы проиграли. Здоровье восстановится через 60 сек.", chat_id=self.id,
                             reply_markup=self.output_map())

    def attak(self):
        global users, maps, attak
        #        pprint(attak)
        r = random.randrange(1, 3)

        pprint(r)
        if r == 1:
            #                self.user["energy_used"] -= 1
            self.energy()
            bot.send_message(text="Бой окончен: ", chat_id=self.id, reply_markup=keyboardmap())
            bot.send_message(text="Вы проиграли", chat_id=self.id, reply_markup=self.output_map())
        else:
            self.user["experience_used"] += 5
            #               self.user["energy_used"] -= 1
            maps[self.user["enemy_cell"]]["resource"] = "null"
            self.update_statistic(data="experiens")
            self.energy()
            #            pprint("test")
            #            wea = self.weapons_random()
            #            weapons = weapons_data[wea]["name"]
            #            pprint(weapons)
            #            weapons = ""
            #            if weapons == "":
            bot.send_message(text="Бой окончен: ", chat_id=self.id, reply_markup=keyboardmap())
            bot.send_message(text="Вы победили и получили 5 опыта", chat_id=self.id,
                             reply_markup=self.output_map())
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
                text = self.text + " \n⚔️Враг увернулся. Осталось " + str(self.user["enemy_health"] + "здоовья")
            else:
                self.user["enemy_health"] -= self.user["hit"]
                text = self.text + " \n⚔️Вы аттаковали врага и нанесли " + str(
                    self.user["hit"]) + " урона. Осталось " + str(self.user["enemy_health"]) + " здоовья"

            if self.user["enemy_health"] <= 0:
                bot.send_message(text="⏱ Вывод карты ⏱", chat_id=self.id, reply_markup=keyboardmap())
                stop = 1
                text = self.text + "\nВы одержали победу 💥 "
                time.sleep(2)
                self.user["experience_used"] += 5
                self.user["health_used"] = self.user["health"]
                maps[self.user["enemy_cell"]]["resource"] = "null"
                self.update_statistic(data="experiens")
                self.energy()
                bot.send_message(text="Вы победили и получили 5 🌕 опыта", chat_id=self.id,
                                 reply_markup=self.output_map())
        elif self.call == "battle_defence":
            text = self.text + "\n🛡 Вы защищаетесь от врага и восстанавливаете здоровье"
            self.user["health_used"] += 10
        else:
            if maps[cell]["resource"] == "enemy":
                bot.edit_message_text(text="Выберите дальнейшее действие", chat_id=self.id, message_id=self.message_id,
                                      reply_markup=self.keyboard_attak_new())

        bot.edit_message_text(text=text, chat_id=self.id, message_id=self.message_id,
                              reply_markup=self.keyboard_attak_new())
        #        time.sleep(1)
        r = random.randint(1, 2)
        if r == 1 and stop == 0:
            self.user["health_used"] -= self.user["enemy_hit"]
            text = text + " \n⚔️Враг аттаковал вас и нанес " + str(self.user["enemy_hit"]) + " урона. Осталось " + str(
                self.user["health_used"]) + " здоовья"
            bot.edit_message_text(text=text, chat_id=self.id, message_id=self.message_id,
                                  reply_markup=self.keyboard_attak_new())
        elif r == 2 and stop == 0:
            text = text + "\n🛡 Враг защищается и восстанавливает здоровье"
            #            self.user["enemy_health"] += self.user["enemy_dodge"]
            bot.edit_message_text(text=text, chat_id=self.id, message_id=self.message_id,
                                  reply_markup=self.keyboard_attak_new())
        if self.user["health_used"] <= 0:
            self.update_statistic(data="experiens")
            self.user["health_used"] = self.user["health"]
            pprint(self.user["health_used"])
            save("users")
            bot.send_message(text="⏱ Вывод карты ⏱", chat_id=self.id, reply_markup=keyboardmap())
            bot.send_message(text="Вы умерли.", chat_id=self.id,
                             reply_markup=self.output_map())

    def weapons_random(self):
        r = random.randint(1, 1)
        pprint(r)
        pprint(weapons[str(self.user["lvlheroes"])]["random"])
        r_r = weapons[str(self.user["lvlheroes"])]["random"]
        pprint(r_r)
        if r == 1:  # arm
            r_a = random.randint(1, r_r)
            if r_a == 1:
                return weapons[str(r_r)]["name"]
        else:
            return ""

    def attaka_new(self):
        keyboard = telebot.types.InlineKeyboardMarkup()
        null = telebot.types.InlineKeyboardButton(text="➖➖", callback_data="null")
        heroes_head = telebot.types.InlineKeyboardButton(text=fight_text["heroes_head"],
                                                         callback_data="fight_heroes_head")
        heroes_left = telebot.types.InlineKeyboardButton(text=fight_text["heroes_handleft"],
                                                         callback_data="fight_heroes_handleft")
        heroes_right = telebot.types.InlineKeyboardButton(text=fight_text["heroes_handright"],
                                                          callback_data="fight_heroes_handright")
        heroes_breast = telebot.types.InlineKeyboardButton(text=fight_text["heroes_breast"],
                                                           callback_data="fight_heroes_breast")
        heroes_legs = telebot.types.InlineKeyboardButton(text=fight_text["heroes_legs"],
                                                         callback_data="fight_heroes_legs")
        heroes_foot = telebot.types.InlineKeyboardButton(text=fight_text["heroes_foot"],
                                                         callback_data="fight_heroes_foot")

        enemy_head = telebot.types.InlineKeyboardButton(text=fight_text["enemy_head"], callback_data="fight_enemy_head")
        enemy_left = telebot.types.InlineKeyboardButton(text=fight_text["enemy_handleft"],
                                                        callback_data="fight_enemy_handleft")
        enemy_right = telebot.types.InlineKeyboardButton(text=fight_text["enemy_handright"],
                                                         callback_data="fight_enemy_handright")
        enemy_brest = telebot.types.InlineKeyboardButton(text=fight_text["enemy_breast"],
                                                         callback_data="fight_enemy_breast")
        enemy_legs = telebot.types.InlineKeyboardButton(text=fight_text["enemy_legs"], callback_data="fight_enemy_legs")
        enemy_foot = telebot.types.InlineKeyboardButton(text=fight_text["enemy_foot"], callback_data="fight_enemy_foot")

        text_pole = telebot.types.InlineKeyboardButton(text=fight_text["null"], callback_data="1")
        health_used = telebot.types.InlineKeyboardButton(text=self.user["health_used"], callback_data="1")
        enemy_health = telebot.types.InlineKeyboardButton(text=self.user["enemy_health"], callback_data="1")
        keyboard.row(text_pole)
        keyboard.row(heroes_head, null, enemy_head, )
        keyboard.row(heroes_left, heroes_right, null, null, enemy_left, enemy_right)
        #        keyboard.row(heroes_left, heroes_breast, heroes_right, enemy_left, enemy_brest,enemy_right)
        keyboard.row(heroes_breast, null, enemy_brest)
        keyboard.row(heroes_legs, null, enemy_legs)
        keyboard.row(heroes_foot, null, enemy_foot)
        #        keyboard.row(text_pole)
        keyboard.row(health_used, enemy_health)
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
            bot.send_message(text="Вы аттаковали врага. Выберите какую часть тела защитить и атакуйте врага",
                             chat_id=self.id, reply_markup=self.attaka_new())

        else:
            pprint(self.call)
            pprint(self.message_id)
            data = self.call.split("_")[1]
            data_old = self.call.split("_")[2]
            d = data + "_" + data_old
            if data == "heroes":
                if 0 < self.user["defence"] <= 2:
                    if data_old == "head":
                        fight_text[d] += " 🛡"
                        combat[d] = 1
                        pprint("test")
                        comb[d] += 1
                        pprint("test2")
                    elif data_old == "handleft":
                        fight_text[d] += " 🛡"
                        combat[d] = 1
                        comb[d] += 1
                    elif data_old == "handright":
                        fight_text[d] += " 🛡"
                        combat[d] = 1
                        comb[d] += 1
                    elif data_old == "breast":
                        fight_text[d] += " 🛡"
                        combat[d] = 1
                        comb[d] += 1
                    elif data_old == "legs":
                        fight_text[d] += " 🛡"
                        combat[d] = 1
                        comb[d] += 1
                    elif data_old == "foot":
                        fight_text[d] += " 🛡"
                        combat[d] = 1
                        comb[d] += 1
                    self.user["defence"] -= 1

                    bot.answer_callback_query(callback_query_id=self.call_id, text='Защитились')
                else:
                    bot.answer_callback_query(callback_query_id=self.call_id, text='Очки защиты законились')
                    return
            #   elif self.user["defence"] >2:
            elif data == "enemy":
                if 0 < self.user["attaka"] <= 2:
                    if data_old == "head":
                        fight_text[d] += " ⚔️"
                        combat[d] = 1
                        comb[d] += 1
                    elif data_old == "handleft":
                        fight_text[d] += " ⚔️"
                        combat[d] = 1
                        comb[d] += 1
                    elif data_old == "handright":
                        fight_text[d] += " ⚔️"
                        combat[d] = 1
                        comb[d] += 1
                    elif data_old == "breast":
                        fight_text[d] += " ⚔️"
                        combat[d] = 1
                        comb[d] += 1
                    elif data_old == "legs":
                        fight_text[d] += " ⚔️"
                        combat[d] = 1
                        comb[d] += 1
                    elif data_old == "foot":
                        fight_text[d] += " ⚔️"
                        combat[d] = 1
                        comb[d] += 1
                    self.user["attaka"] -= 1

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
                bot.edit_message_text(text=text_attaka, chat_id=self.id, message_id=self.message_id,
                                      reply_markup=self.attaka_new())
                text_old = self.combat_battle()
                raund += 1
                text_attaka += "\n/----/ Раунд " + str(raund) + " /----/" + text_old + "\n"
                time.sleep(3)
                fight_text = fight_text_all.copy()
                text = "Защита 2 очка. Аттака 2 очка"
                fight_text["null"] = text
                if self.user["health_used"] <= 0:
                    bot.delete_message(self.id, message_id=self.message_id)
                    bot.send_message(self.id, text=text_attaka)
                    self.congratulation("enemy")
                    print("Герой проиграл")
                elif self.user["enemy_health"] <= 0:
                    bot.delete_message(self.id, message_id=self.message_id)
                    bot.send_message(self.id, text=text_attaka)
                    self.congratulation("heroes")
                    print("Враг проиграл")
                else:
                    bot.edit_message_text(text=text_attaka, chat_id=self.id, message_id=self.message_id,
                                          reply_markup=self.attaka_new())

            else:
                defence = self.user["defence"]
                attaka = self.user["attaka"]

                #                    text = "Выберите часть тела для защиты и для аттаки"
                text = "Защита " + str(defence) + " очка. Аттака " + str(attaka) + " очка"
                fight_text["null"] = text

                bot.edit_message_text(text=text_attaka, chat_id=self.id, message_id=self.message_id,
                                      reply_markup=self.attaka_new())

    def combat_battle(self):
        global combat, comb, her, ene
        #        pprint(combat)
        text, h_a, h_a_s, d_e, d_e_s = "", 0, 0, 0, 0
        her, ene = {}, {}
        for key, value in comb.items():
            if key.split("_")[0] == "heroes":
                her[key] = value
            elif key.split("_")[0] == "enemy":
                ene[key] = value
        max_value_her = min(her.values())
        for k, v in her.items():
            if v == max_value_her:
                her[k] = 9999999
                h_a = k
                break
        max_value_her = min(her.values())
        for k, v in her.items():
            if v == max_value_her:
                h_a_s = k
        max_value_ene = max(ene.values())
        for k, v in ene.items():
            if v == max_value_ene:
                ene[k] = 0
                d_e = k
        max_value_ene = max(ene.values())
        for k, v in ene.items():
            if v == max_value_ene:
                d_e_s = k

        for key, value in combat.items():
            if h_a == key:
                text += "\n 🛡 Вы отразили аттаку врага в " + fight_trans[h_a]
            elif h_a_s == key:
                text += "\n 🛡 Вы отразили аттаку врага в " + fight_trans[h_a_s]
            elif d_e == key:
                text += "\n 🛡 Враг отразил вашу аттаку в " + fight_trans[d_e]
            elif d_e_s == key:
                text += "\n 🛡 Враг отразил вашу аттаку в " + fight_trans[d_e_s]
            elif key.split("_")[0] == "heroes":
                text += "\n ⚔️Враг нанес вам удар -" + str(self.user["enemy_hit"]) + " ♥️"
                self.user["health_used"] -= self.user["enemy_hit"]
            elif key.split("_")[0] == "enemy":
                text += "\n ⚔️Вы нанесли удар противнику - " + str(self.user["hit"]) + " ♥️"
                self.user["enemy_health"] -= self.user["hit"]

        combat = {}
        return text

    def keyboard_all_battle(self):
        keyboard = telebot.types.InlineKeyboardMarkup()
        archer_50 = telebot.types.InlineKeyboardButton(text="50 🏹", callback_data="gotobattle_archer_50")
        archer_100 = telebot.types.InlineKeyboardButton(text="100 🏹", callback_data="gotobattle_archer_100")
        archer_500 = telebot.types.InlineKeyboardButton(text="500 🏹", callback_data="gotobattle_archer_500")
        archer_all = telebot.types.InlineKeyboardButton(text="Всех 🏹", callback_data="gotobattle_archer_all")
        warrior_50 = telebot.types.InlineKeyboardButton(text="50 ⚔️", callback_data="gotobattle_warrior_50")
        warrior_100 = telebot.types.InlineKeyboardButton(text="100 ⚔️", callback_data="gotobattle_warrior_100")
        warrior_500 = telebot.types.InlineKeyboardButton(text="500 ⚔️", callback_data="gotobattle_warrior_500")
        warrior_all = telebot.types.InlineKeyboardButton(text="Всех ⚔️", callback_data="gotobattle_warrior_all")
        cavalry_50 = telebot.types.InlineKeyboardButton(text="50 🐴", callback_data="gotobattle_cavalry_50")
        cavalry_100 = telebot.types.InlineKeyboardButton(text="100 🐴", callback_data="gotobattle_cavalry_100")
        cavalry_500 = telebot.types.InlineKeyboardButton(text="500 🐴", callback_data="gotobattle_cavalry_500")
        cavalry_all = telebot.types.InlineKeyboardButton(text="Всех 🐴", callback_data="gotobattle_cavalry_all")
        goto = telebot.types.InlineKeyboardButton(text="Отправить", callback_data="gotobattle_goto")
        keyboard.row(archer_50, warrior_50, cavalry_50)
        keyboard.row(archer_100, warrior_100, cavalry_100)
        keyboard.row(archer_500, warrior_500, cavalry_500)
        keyboard.row(archer_all, warrior_all, cavalry_all)
        keyboard.row(goto)
        return keyboard

    def number_warrior(self, data=""):
        global allbattle
        archer = str(self.user["archer"])
        warrior = str(self.user["warrior"])
        cavalry = str(self.user["cavalry"])
        archer_allbattle = str(allbattle[self.id]["archer"])
        warrior_allbattle = str(allbattle[self.id]["warrior"])
        cavalry_allbattle = str(allbattle[self.id]["cavalry"])
        if data == "":
            text = "У вас в городе\n лучников🏹: " + archer + " воинов⚔: " + warrior + " кавалерии🐴:" + cavalry + \
                   "\n На поле боя\n лучников🏹: " + archer_allbattle + " воинов⚔: " + warrior_allbattle + " кавалерии🐴:" + cavalry_allbattle
        elif data == "battle":
            text = "На поле боя:\n лучников🏹: " + archer_allbattle + " воинов⚔: " + warrior_allbattle + " кавалерии🐴:" + cavalry_allbattle + "\n🗡🔥⚡️Ожидайте сражения ⚡🔥🗡"

        return text

    def all_battle(self):
        global allbattle
        if self.call == "gotobattle":
            text_all = "Вы отправились на поле боя. \n Сражения проводятся в 10:00, 14:00, 18:00\n" \
                       " Выберите кол-во воинов для отправки на войну\n "
            bot.send_message(text=text_all, chat_id=self.id, reply_markup=keyboard_battle_back())

            allbattle[self.id] = {"archer": 0, "warrior": 0, "cavalry": 0}
            #            save("users")
            bot.delete_message(chat_id=self.id, message_id=self.call_message_id)
            bot.send_message(chat_id=self.id, text=self.number_warrior(), reply_markup=self.keyboard_all_battle())
        elif self.call.split("_")[1] == "archer":
            text_koll = self.warrior_schet(data="archer")
        elif self.call.split("_")[1] == "warrior":
            text_koll = self.warrior_schet(data="warrior")
        elif self.call.split("_")[1] == "cavalry":
            text_koll = self.warrior_schet(data="cavalry")
        elif self.call.split("_")[1] == "goto":
            allbattle[self.id] = {"archer": allbattle[self.id]["archer"], "warrior": allbattle[self.id]["warrior"],
                                  "cavalry": allbattle[self.id]["cavalry"]}
            #            self.user["archer"] -= allbattle[self.id]["archer"]
            #            self.user["warrior"] -= allbattle[self.id]["warrior"]
            #            self.user["cavalry"] -= allbattle[self.id]["cavalry"]
            text_koll = self.number_warrior(data="battle")
            bot.delete_message(self.id, message_id=self.message_id)
            bot.send_message(self.id, text_koll)
            save("allbattle")
            save("users")

        try:
            bot.edit_message_text(text=text_koll, chat_id=self.id, message_id=self.message_id,
                                  reply_markup=self.keyboard_all_battle())
        except:
            pass

    def warrior_schet(self, data):
        number = self.call.split("_")[2]
        pprint(number)
        text_koll = self.number_warrior()
        if self.user[data] <= 0:
            bot.answer_callback_query(callback_query_id=self.call_id, text='У вас нет ' + data)
            return
        #          text_koll = self.number_warrior()
        elif number == "all":
            allbattle[self.id][data] = self.user[data]
            self.user[data] = 0
            text_koll = self.number_warrior()
        else:
            if self.user[data] - int(number) < 0:
                bot.answer_callback_query(callback_query_id=self.call_id, text='У вас нет столько воинов ' + data)
                return
            #            text_koll = self.number_warrior()
            else:
                pprint("qwe")
                allbattle[self.id][data] += int(number)
                self.user[data] -= int(number)
                text_koll = self.number_warrior()
        return text_koll

    def troop_return(self):
        try:

            self.user["archer"] += allbattle[str(self.id)]["archer"]
            self.user["warrior"] += allbattle[str(self.id)]["warrior"]
            self.user["cavalry"] += allbattle[str(self.id)]["cavalry"]
            allbattle.pop(str(self.id))
            save("users")
            save("allbattle")
        except:
            print("Ошибка")

        bot.send_message(text="Вернуться", chat_id=self.id, reply_markup=keyboardmap())
        bot.send_message(text="Делайте ход по игровому полю", chat_id=self.id,
                         reply_markup=self.output_map())

    def keyboard_shop(self):
        keyboard = telebot.types.InlineKeyboardMarkup()
        rename = telebot.types.InlineKeyboardButton(text="Изменить имя", callback_data="shop_rename")
        changeavatar = telebot.types.InlineKeyboardButton(text="Изменить аватар", callback_data="shop_avatar")
        keyboard.add(rename)
        keyboard.add(changeavatar)
        return keyboard

    def shop(self):
        print("ff")
        if self.text == "/shop" or self.text == "Магазин":
            bot.send_message(chat_id=self.id, text="Магазин. Для подробной информации о товаре, нажмите на него",
                             reply_markup=self.keyboard_shop())


@bot.message_handler(commands=['start', 'shop'])
def start_message(message):
    print("command")
    if message.chat.id == ADMIN:
        bot.send_message(text="Админское меню", chat_id=message.chat.id, reply_markup=keyadmin())
    elif message.text == "/start":
        start_user(message)
    elif message.text == "/shop":
        #        maps_bot = Maps(message)
        Maps(message).shop()


@bot.message_handler(content_types=['successful_payment'])
def got_payment(message):
    global users
    succefull_tranzzo(message)
    with open(PATH + "tmp/" + 'users.json', 'rb') as f:
        users = json.load(f)


@bot.message_handler(content_types=['text'])
def send_text(message):
    global menu, status, barracks, allbattle
    maps_bot = Maps(message)
    if message.chat.id == ADMIN:
        if message.text == "Создать карту":
            maps_bot.new_maps()
        elif message.text == "Кол-во ячеек":
            maps_bot.statistika()
        #        elif message.text == "Новая атака":
        #            maps_bot.new_attaka()
        elif message.text == "Бой":
            users[str(message.chat.id)]["defence"] = 2
            users[str(message.chat.id)]["attaka"] = 2
            maps_bot.fight()
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

            bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 1)
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
            #           elif menu == "QIWI":
            #               menu = "feedback"
            #               bot.send_message(text="Назад", chat_id=message.chat.id, reply_markup=keyboard_buy())
            else:
                bot.send_message(text="Назад", chat_id=message.chat.id, reply_markup=keyboardmenu())
        elif message.text == 'Герой':
            menu = "heroes"
            bot.send_message(text=maps_bot.info_heroes("heroes"), chat_id=message.chat.id)
        elif message.text == 'Склад':
            menu = "sklad"
            maps_bot.build()
            bot.send_message(text=maps_bot.info_heroes("sklad"), chat_id=message.chat.id, reply_markup=keyboardback())
        elif message.text == "Меню игрока":
            bot.send_message(text="Меню игрока", chat_id=message.chat.id, reply_markup=keyboardmenu())
        elif message.text == "Вернуться на карту 🗺":
            status = "close" + str(message.chat.id)
            bot.send_message(text="Вернуться", chat_id=message.chat.id, reply_markup=keyboardmap())
        elif message.text == "Покинуть поле боя":
            maps_bot.troop_return()
        elif message.text == "Атаковать":
            users[str(message.chat.id)]["defence"] = 2
            users[str(message.chat.id)]["attaka"] = 2
            maps_bot.fight()
        elif message.text == "Отступить":
            bot.send_message(text="⏱ Вывод карты ⏱", chat_id=message.chat.id, reply_markup=keyboardmap())
            time.sleep(2)
            bot.send_message(text="Делайте ход по игровому полю", chat_id=message.chat.id,
                             reply_markup=maps_bot.output_map())
        elif message.text == "Казарма":
            barracks = 1
            menu = "barracks"
            maps_bot.build()
            maps_bot.barracks("all")
        elif barracks == 1:
            if message.text == "Обучить лучника":
                maps_bot.barracks("archer")
            elif message.text == "Да":
                maps_bot.barracks("yes")
            elif message.text == "Нет":
                save("all")
                barracks = 0
                bot.send_message(text="Казарма", chat_id=message.chat.id, reply_markup=keyboardbarracks())
        elif message.text == "Строения":  # Cтроения
            menu = "building"
            #            bot.send_message(text="Будет добавлено в следующем обновлении", chat_id=message.chat.id)
            maps_bot.building()
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
            bot.send_message(text=textsell + "Выберите платежную систему", chat_id=message.chat.id,
                             reply_markup=keyboard_buy())
        #       elif message.text == "QIWI":
        #           menu = "QIWI"
        #           bot.send_message(text=textbuy, chat_id=message.chat.id, reply_markup=keyboarddel())
        #           bot.register_next_step_handler(message, buy)
        #
        #       elif message.text == "Оплата QIWI":
        #           buy_bot.buy_qiwi()
        #           bot.send_message(text=textbuy, chat_id=message.chat.id, reply_markup=keyboard_info())
        elif message.text == "Tranzzo":
            menu = "Tranzzo"
            buy_amount(message)
        elif message.text == "Всё понятно":
            maps_bot.new_game()
        elif message.text == "Чат":
            bot.send_message(message.chat.id,
                             "Чат предназначен для общения, предложения идей и выявления багов @heroeslifeg")
        elif message.text == "Пригласить":
            bot.send_message(message.chat.id,
                             "Для приглашения друга отправть ему ссылку ниже. И получи 10 💎 за каждый взятый им уровень")
            bot.send_message(message.chat.id, "https://telegram.me/heroeslifebot?start=" + str(message.chat.id))
        elif message.text == "Помощь":
            maps_bot.help()
        else:
            pprint(message.text)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    print(call.data)
    maps_bot = Maps(message=call.message, call=call)
    #   buy_bot = Buy(message=call.message, call=call)
    if call.data.split("_")[0] == "battle":
        maps_bot.attak()
    elif call.data.split("_")[0] == "build":
        maps_bot.build(data=call.data.split("_")[1])
    elif call.data.split("_")[0] == "fight":
        maps_bot.fight()
    #   elif call.data == "buy_qiwi":
    #       buy_bot.buy_check_qiwi()
    elif call.data == "null":
        bot.answer_callback_query(callback_query_id=call.id, text='Не активное поле')
    elif call.data.split("_")[0] == "help":
        maps_bot.help()
    elif call.data.split("_")[0] == "gotobattle":
        maps_bot.all_battle()
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
