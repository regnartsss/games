from config import *
from keyboard import *
from data import *
from battle import *
import time
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove
import random
import json
import datetime
from pprint import pprint
from threading import Thread
import sys

PATH = find_location()
menu = 0
global lvlrudnic

def save(key):
    global maps, users, log
    if key == "all":

        with open(PATH + "tmp/" + 'maps.json', 'w', encoding="utf-16") as f:
            json.dump(maps, f)
        with open(PATH + "tmp/" + 'maps.json', 'rb') as f:
            maps = json.load(f)

        with open(PATH + "tmp/" + 'users.json', 'w', encoding="utf-16") as f:
            json.dump(users, f)
        with open(PATH + "tmp/" + 'users.json', 'rb') as f:
            users = json.load(f)
    elif key == "log":
        file_log = open(PATH + "tmp/" + 'log.txt', "w")
        file_log.write(log)
        file_log.close()


def start_open():
    global maps, users, log
    maps = {}
    try:
        with open(PATH + "tmp/" + 'maps.json', 'rb') as f:
            maps = json.load(f)
    except:
        with open(PATH + "tmp/" + 'maps.json', 'w', encoding="utf-16") as f:
            json.dump(maps, f)
        with open(PATH + "tmp/" + 'maps.json', 'rb') as f:
            maps = json.load(f)

    users = {}
    try:
        with open(PATH + "tmp/" + 'users.json', 'rb') as f:
            users = json.load(f)
    except:
        with open(PATH + "tmp/" + 'users.json', 'w', encoding="utf-16") as f:
            json.dump(users, f)
        with open(PATH + "tmp/" + 'users.json', 'rb') as f:
            users = json.load(f)

    log = ""
    try:
        log = open(PATH + "tmp/" + 'log.txt', "r+").read()
    except:
        log = ""


def date(key="all"):
    if key == "fulltime":
        time = datetime.datetime.today().strftime("%H:%M:%S %d/%m/%Y")
    else:
        time = datetime.datetime.today().strftime("%d/%m/%Y")
    return (time)


start_open()


class Maps():

    def __init__(self, message, call=""):
        global maps, menu, status
        try:
            self.message_call = call.data
            self.id_call = call.id
        except:
            print("нет данных")

        self.id = message.chat.id
        self.text = message.text
        self.message_id = message.message_id

    def new_maps(self):  # Прочитать файл
        global maps, pole, user
        pole = 100
        n = 1
        maps = {}
        all_cell = pole*pole
        for key, value in users.items():
            r = random.randint(1, pole*pole)
            try:
                if not pprint(maps[str(r)]):
                    pprint(str(r))
                    n += 1
            except:
                maps[str(r)] = {"id": str(key)}

        while n <= all_cell:
            try:
                if not pprint(maps[str(n)]):
                    pprint(str(n))
                    n += 1
            except:
                self.resource(n)
                n += 1
        with open(PATH + "tmp/" + 'maps.json', 'w', encoding="utf-16") as f:
            json.dump(maps, f)
        with open(PATH + "tmp/" + 'maps.json', 'rb') as f:
            maps = json.load(f)

    def resource(self, n):
        r = random.randint(1, 15)
        # Дерево
        if r == 1:  # дерево
            r = random.randint(1, 15)
            if r == 1 or r == 2 or r == 3 or r == 4 or r == 5:
                maps[str(n)] = {"resource": "wood", "lvl": "1", "number": str(random.randint(3000, 5000))}
            elif r == 6 or r == 7 or r == 8 or r == 9:
                maps[str(n)] = {"resource": "wood", "lvl": "2", "number": str(random.randint(5001, 15000))}
            elif r == 10 or r == 11 or r == 12:
                maps[str(n)] = {"resource": "wood", "lvl": "3", "number": str(random.randint(15001, 30000))}
            elif r == 13 or r == 14:
                maps[str(n)] = {"resource": "wood", "lvl": "4", "number": str(random.randint(30001, 60000))}
            elif r == 15:
                maps[str(n)] = {"resource": "wood", "lvl": "5", "number": str(random.randint(60001, 120000))}

        # Камень
        elif r == 2:
            r = random.randint(1, 15)
            if r == 1 or r == 2 or r == 3 or r == 4 or r == 5:
                maps[str(n)] = {"resource": "stone", "lvl": "1", "number": str(random.randint(3000, 5000))}
            elif r == 6 or r == 7 or r == 8 or r == 9:
                maps[str(n)] = {"resource": "stone", "lvl": "2", "number": str(random.randint(5001, 15000))}
            elif r == 10 or r == 11 or r == 12:
                maps[str(n)] = {"resource": "stone", "lvl": "3", "number": str(random.randint(15001, 30000))}
            elif r == 13 or r == 14:
                maps[str(n)] = {"resource": "stone", "lvl": "4", "number": str(random.randint(30001, 60000))}
            elif r == 15:
                maps[str(n)] = {"resource": "stone", "lvl": "5", "number": str(random.randint(60001, 120000))}
        # Железо
        elif r == 3:
            r = random.randint(1, 15)
            if r == 1 or r == 2 or r == 3 or r == 4 or r == 5:
                maps[str(n)] = {"resource": "iron", "lvl": "1", "number": str(random.randint(3000, 5000))}
            elif r == 6 or r == 7 or r == 8 or r == 9:
                maps[str(n)] = {"resource": "iron", "lvl": "2", "number": str(random.randint(5001, 15000))}
            elif r == 10 or r == 11 or r == 12:
                maps[str(n)] = {"resource": "iron", "lvl": "3", "number": str(random.randint(15001, 30000))}
            elif r == 13 or r == 14:
                maps[str(n)] = {"resource": "iron", "lvl": "4", "number": str(random.randint(30001, 60000))}
            elif r == 15:
                maps[str(n)] = {"resource": "iron", "lvl": "5", "number": str(random.randint(60001, 120000))}

        elif r == 4:
            maps[str(n)] = {"resource": "enemy"}

        elif r >= 5:
            maps[str(n)] = {"resource": "null"}


    def statistika(self):
        global maps
        w, s, i, u, n, w1,w2,w3,w4,w5,s1,s2,s3,s4,s5,i1,i2,i3,i4,i5,e = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
        for key, value in maps.items():
            pprint(key)
            try:

                if maps[str(key)]["resource"] == "wood":
                    if maps[str(key)]["lvl"] == "1":
                        w1 = w1+ 1
                    elif maps[str(key)]["lvl"] == "2":
                        w2 = w2 + 1
                    elif maps[str(key)]["lvl"] == "3":
                        w3 = w3 + 1
                    elif maps[str(key)]["lvl"] == "4":
                        w4 = w4 + 1
                    elif maps[str(key)]["lvl"] == "5":
                        w5 = w5 + 1
                    w = w +1
                elif maps[str(key)]["resource"] == "stone":
                    if maps[str(key)]["lvl"] == "1":
                        s1 = s1+ 1
                    elif maps[str(key)]["lvl"] == "2":
                        s2 = s2 + 1
                    elif maps[str(key)]["lvl"] == "3":
                        s3 = s3 + 1
                    elif maps[str(key)]["lvl"] == "4":
                        s4 = s4 + 1
                    elif maps[str(key)]["lvl"] == "5":
                        s5 = s5 + 1
                    s = s +1
                elif maps[str(key)]["resource"] == "iron":
                    if maps[str(key)]["lvl"] == "1":
                        i1 = i1+ 1
                    elif maps[str(key)]["lvl"] == "2":
                        i2 = i2 + 1
                    elif maps[str(key)]["lvl"] == "3":
                        i3 = i3 + 1
                    elif maps[str(key)]["lvl"] == "4":
                        i4 = i4 + 1
                    elif maps[str(key)]["lvl"] == "5":
                        i5 = i5 + 1
                    i = i +1
                elif maps[str(key)]["resource"] == "null":
                    n  =n+1
                elif maps[str(key)]["resource"] == "enemy":
                    e = e+1
            except:
                u = u+1
        pprint("www")
        text =    "дерево "+str(w)+" \nlvl 1: "+str(w1)+" \nlvl 2: "+str(w2)+" \nlvl 3: "+str(w3)+" \nlvl 4: "+str(w4)+" \nlvl 5: "+str(w5)\
               +"\nжелезо "+str(i)+" \nlvl 1: "+str(i1)+" \nlvl 2: "+str(i2)+" \nlvl 3: "+str(i3)+" \nlvl 4: "+str(i4)+" \nlvl 5: "+str(i5)\
               +"\nкамень "+str(s)+" \nlvl 1: "+str(s1)+" \nlvl 2: "+str(s2)+" \nlvl 3: "+str(s3)+" \nlvl 4: "+str(s4)+" \nlvl 5: "+str(s5)\
               +"\nигроков "+str(u)+"\nПустых ячеек "+str(n)+"\nВрагов "+str(e)
        pprint(text)
        bot.send_message(chat_id=self.id, text=text)
#        pprint("дерево "+str(w)+"\nжелезо "+str(i)+"\nкамень "+str(s)+"\nигроков "+str(u)+"\nПустых ячеек "+str(n))


    def output_map(self):
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
        pprint(str(cell_user) +" temp")
        pprint(int(cell_user) % pole)

        if (int(cell_user) % pole) == 3:
            pos = [pole * 3 + 2, pole * 2 + 2, pole + 2, 2, (pole - 2) * -1, (pole * 2 - 2) * -1, (pole * 3 - 2) * -1]
        elif int(cell_user) % pole == 2:
            pos = [pole * 3 + 1, pole * 2 + 1, pole + 1, 1, (pole - 1) * -1, (pole * 2 - 1) * -1, (pole * 3 - 1) * -1]
        elif int(cell_user) % pole == 1:
            pos = [pole * 3, pole * 2, pole, 0, pole * -1, pole * -2, pole * -3]
        else:
            pos = [pole * 3 + 3, pole * 2 + 3, pole + 3, 3, (pole - 3) * -1, (pole * 2 - 3) * -1, (pole * 3 - 3) * -1]

        for x in pos:
            start_field = int(cell_user) - x
            pprint(start_field)
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
                        tab.append(types.InlineKeyboardButton(" ", callback_data=str(start_field)))
                else:
                    if cell == "iron":
                        tab.append(types.InlineKeyboardButton(u'\U0001F528', callback_data=str(start_field)))
                    elif cell == "wood":
                        tab.append(types.InlineKeyboardButton("🌲", callback_data=str(start_field)))
                    elif cell == "stone":
                        tab.append(types.InlineKeyboardButton("⛏", callback_data=str(start_field)))
                    elif cell == "enemy":
                        tab.append(types.InlineKeyboardButton("🙉", callback_data=str(start_field)))
                    elif cell == str(self.id):
                        tab.append(types.InlineKeyboardButton("🛑", callback_data=str(start_field)))
                    elif start_field == int(cell_user) - 1:
                        tab.append(types.InlineKeyboardButton("⬅", callback_data=str(start_field)))
                    elif start_field == int(cell_user) - pole:
                        tab.append(types.InlineKeyboardButton("⬆", callback_data=str(start_field)))
                    elif start_field == int(cell_user) + 1:
                        tab.append(types.InlineKeyboardButton("➡", callback_data=str(start_field)))
                    elif start_field == int(cell_user) + pole:
                        tab.append(types.InlineKeyboardButton("⬇", callback_data=str(start_field)))
                    elif cell == "null":
                        tab.append(types.InlineKeyboardButton(" ", callback_data=str(start_field)))
                    else:
                        tab.append(types.InlineKeyboardButton("❌", callback_data=str(start_field) + "_olduser"))

                    y += 1
                    start_field += 1
            keyboard.row(*tab)

        save("all")
        return keyboard

    def goto(self):
        global maps, pole
        #        pprint(self.message_call)
        #        pprint(self.id)
        #        pprint(self.text) ###
        #        pprint(self.message_id)
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
            value_call = "null"
        pprint(cell_user)
        pprint(value_call)
        if self.message_call == cell_user:
            bot.answer_callback_query(self.id_call, 'Это вы')

        elif value_call == "enemy":

            bot.delete_message(self.id, message_id=self.message_id)
            bot.send_message(text=textattaka, chat_id=self.id, reply_markup=keyattaka())

        elif int(self.message_call) == int(cell_user) - 1:
            if value_call == "iron" or value_call == "wood" or value_call == "stone":
                bot.delete_message(self.id, message_id=self.message_id)
                self.rudnic(cell_user)
            else:
                maps[str(cell_user)] = {"resource": "null"}
                posuser = int(cell_user) - 1
                maps[str(posuser)] = {"id": str(self.id)}
                bot.edit_message_text(text="Ходите", chat_id=self.id, message_id=self.message_id,
                                      reply_markup=self.output_map())
        elif int(self.message_call) == int(cell_user) + 1:

            if value_call == "iron" or value_call == "wood" or value_call == "stone":
                bot.delete_message(self.id, message_id=self.message_id)
                self.rudnic(cell_user)
            else:
                maps[str(cell_user)] = {"resource": "null"}
                posuser = int(cell_user) + 1
                maps[str(posuser)] = {"id": str(self.id)}
                bot.edit_message_text(text="Ходите", chat_id=self.id, message_id=self.message_id,
                                      reply_markup=self.output_map())
        elif int(self.message_call) == int(cell_user) - pole:

            if value_call == "iron" or value_call == "wood" or value_call == "stone":
                bot.delete_message(self.id, message_id=self.message_id)
                self.rudnic(cell_user)
            else:
                maps[str(cell_user)] = {"resource": "null"}
                posuser = int(cell_user) - pole
                maps[str(posuser)] = {"id": str(self.id)}
                bot.edit_message_text(text="Ходите", chat_id=self.id, message_id=self.message_id,
                                      reply_markup=self.output_map())
        elif int(self.message_call) == int(cell_user) + pole:
            if value_call == "iron" or value_call == "wood" or value_call == "stone":

                bot.delete_message(self.id, message_id=self.message_id)

                self.rudnic(cell_user)
            else:
                maps[str(cell_user)] = {"resource": "null"}
                posuser = int(cell_user) + pole
                maps[str(posuser)] = {"id": str(self.id)}
                bot.edit_message_text(text="Ходите", chat_id=self.id, message_id=self.message_id,
                                      reply_markup=self.output_map())
        elif value_call == "null":
            bot.answer_callback_query(callback_query_id=self.id_call, text='Поле не активно')


    def rudnic(self, cell_user):
        global maps, menu, res, kol, map_res, lvl
        map_res = self.message_call
        res = maps[str(self.message_call)]["resource"]
        kol = maps[str(self.message_call)]["number"]
        lvl = maps[str(self.message_call)]["lvl"]
        text = ""

        timer = self.time(int(kol) // lvlrudnic[lvl])

        if res == "wood":
            text = "Шахта с деревом \nУровень шахты "+lvl+"\nКоличество ресурса: " + kol
        elif res == "iron":
            text = "Шахта с железом \nУровень шахты "+lvl+"\nКоличество ресурса: " + kol
        elif res == "stone":
            text = "Шахта с камнем \nУровень шахты "+lvl+"\nКоличество ресурса: " + kol

        text = text + "\n Добыча "+str(lvlrudnic[lvl])+"шт/cек \nВыкопать шахту за " + str(timer)
        menu = "rudnic"
        bot.send_message(text=text, chat_id=self.id, reply_markup=keyrudnic())

    def time(self, timer):
        return time.strftime('%M:%S', time.gmtime(timer))

    def timer(self, timer):
        global maps, users, res, kol, map_res, status
        ss = 0
        for i in range(timer, 0, -1):
            if status == "close":
                break
            print(i)
            ss += 1
            time.sleep(1)

        if status == "close":
            print("close")
            kol = ss * 100

            summa = str(int(kol) + int(users[str(self.id)][res]))
            users[str(self.id)][res] = summa
            maps[str(map_res)]["number"] = str(int(maps[str(map_res)]["number"]) - kol)
            save("all")
            bot.send_message(text="Вы выкопали " + str(kol), chat_id=self.id, reply_markup=self.output_map())

            sys.exit()

        else:
            summa = str(int(kol) + int(users[str(self.id)][res]))
            users[str(self.id)][res] = summa
            maps[str(map_res)]["resource"] = "null"
            save("all")
            self.cell()
            bot.send_message(text="Вы выкопали ", chat_id=self.id, reply_markup=keyboardmap())
            bot.send_message(text="Вы выкопали " + kol, chat_id=self.id, reply_markup=self.output_map())

    def mining(self):
        global maps, users, res, kol, map_res, lvl

        timer = int(kol) // lvlrudnic[lvl]
        Thread(target=self.timer, args=(timer,)).start()

    def cell(self):
        n = random.randint(1, 100)
        try:
            if maps[str(n)]["resource"] == "null":
                self.resource(n)
            pprint(n)
        except:
            pprint("ячейка занята")


class User():

    def __init__(self, message):
        #        self.users = users
        self.id = message.chat.id
        self.text = message.text
        self.first_name = message.from_user.username

    def start_user(self):
        global maps, users, log
        date_t = date()
        if str(self.id) in users:
            log = log + date("fulltime") + " Повторный вход \n"
            bot.send_message(self.id, "Пользователь есть", reply_markup=keyboarddom())
        else:
            log = log + date("fulltime") + " Зарегистрирован новый пользователь " + str(self.id) + "\n"
            users[str(self.id)] = {"id": str(self.id),
                                   "username": self.first_name,
                                   "date": str(date_t),
                                   "level": "1",
                                   "healts": "100",
                                   "wood": "0",
                                   "stone": "0",
                                   "iron": "0"}

            s = random.randint(1, len(maps))
            maps[str(s)] = {"id": str(self.id)}
            bot.send_message(self.id, "Ваша начальная позиция на карте " + str(s), reply_markup=keyboarddom())
        save("all")
        save("log")

    def info_herous(self, key):
        global users
        id = users[str(self.id)]["id"]
        username = users[str(self.id)]["username"]
        date = users[str(self.id)]["date"]
        level = users[str(self.id)]["level"]
        healts = users[str(self.id)]["healts"]
        wood = users[str(self.id)]["wood"]
        stone = users[str(self.id)]["stone"]
        iron = users[str(self.id)]["iron"]
        herous = "Информация о герое\n" + "id: " + str(id) + "\n" + "Имя: " + str(
            username) + "\n" + "Уровень: " + level + "\n" + "Здоровье: " + healts + "\n"
        sklad = "Информация о складе\n" + "Железо: " + iron + "\n" + "Дерево: " + wood + "\n" + "Камень: " + stone + "\n"
        if key == "herous":
            return (herous)
        elif key == "sklad":
            return (sklad)


@bot.message_handler(commands=['start'])
def start_message(message):
    if message.chat.id == ADMIN:
        bot.send_message(text="Админское меню", chat_id=message.chat.id, reply_markup=keyadmin())

    else:
        user_bot = User(message)
        user_bot.start_user()


@bot.message_handler(content_types=['text'])
def send_text(message):
    global menu, status
    #    print(menu)
    user_bot = User(message)
    maps_bot = Maps(message)
    battle_bot = Battle(message)
    if message.chat.id == ADMIN:
        pprint("dd")
        if message.text == "Создать карту":
            maps_bot.new_maps()
        elif message.text == "Кол-во ячеек":
            maps_bot.statistika()

    else:
        if message.text == 'Карта' or message.text == "На карту":
            bot.send_message(text="Вывод карты", chat_id=message.chat.id, reply_markup=keyboardmap())
            bot.send_message(text="Ходите", chat_id=message.chat.id, reply_markup=maps_bot.output_map())

        elif message.text == 'Вернуться в город':
            menu = "dom"
            bot.delete_message(message.chat.id, message_id=message.message_id - 1)
            bot.send_message(text="Домой", chat_id=message.chat.id, reply_markup=keyboarddom())
        elif message.text == 'Назад':
                print(menu)
                if menu == "dom":
                    bot.send_message(text="Назад", chat_id=message.chat.id, reply_markup=keyboardmap())
                    bot.send_message(text="Назад", chat_id=message.chat.id, reply_markup=maps_bot.output_map())
                elif menu == "heroes":
                    menu = "dom"
                    bot.send_message(text="Назад", chat_id=message.chat.id, reply_markup=keyboarddom())
                elif menu == "sklad":
                   menu = "dom"
                   bot.send_message(text="Назад", chat_id=message.chat.id, reply_markup=keyboarddom())
                elif menu == "rudnic":
                    bot.send_message(text="Назад", chat_id=message.chat.id, reply_markup=keyboardmap())
                    bot.send_message(text="Назад", chat_id=message.chat.id, reply_markup=maps_bot.output_map())
                else:
                    bot.send_message(text="Назад", chat_id=message.chat.id, reply_markup=keyboardmenu())

        elif message.text == 'Герой':
            menu = "heroes"
            bot.send_message(text=user_bot.info_herous("herous"), chat_id=message.chat.id, reply_markup=keyboardback())
        elif message.text == 'Склад':
            menu = "sklad"
            bot.send_message(text=user_bot.info_herous("sklad"), chat_id=message.chat.id, reply_markup=keyboardback())
        elif message.text == 'Копать':
            menu = "rudnic"
            status = "open"
            bot.send_message(text="Копаем", chat_id=message.chat.id, reply_markup=keymap())
            maps_bot.mining()

        elif message.text == "Меню игрока":
            bot.send_message(text="Меню игрока", chat_id=message.chat.id, reply_markup=keyboardmenu())
        elif message.text == "Вернуться на карту":
            status = "close"
            bot.send_message(text="Вернуться", chat_id=message.chat.id, reply_markup=keyboardmap())
        elif message.text == "Атаковать":
            pprint("бой")
            bot.send_message(text="Бой", chat_id=message.chat.id, reply_markup=keyboardback())
            battle_bot.battle()
        else:
            pprint(message.text)

"""
    if message.text == 'Карта':
        bot.send_message(message.chat.id, "Вывод карты", reply_markup=keyboardom())
        bot.send_message(text="Ходите", chat_id=message.chat.id, reply_markup=maps_bot.output_map())
    elif message.text == 'Дом':
        menu = 1
        bot.delete_message(message.chat.id, message_id=message.message_id - 1)
        bot.send_message(text="Назад", chat_id=message.chat.id, reply_markup=keydom())
    elif message.text == 'Назад':
        if menu == 1:
            bot.send_message(text="Назад", chat_id=message.chat.id, reply_markup=keyboardmenu())
        elif menu == "rudnic":
            bot.send_message(text="Назад", chat_id=message.chat.id, reply_markup=keyboardom())

            bot.send_message(text="Назад", chat_id=message.chat.id, reply_markup=maps_bot.output_map())
        else:
            bot.send_message(text="Назад", chat_id=message.chat.id, reply_markup=keyboardmenu())
    elif message.text == 'Герой':
        bot.send_message(text=user_bot.info_herous("herous"), chat_id=message.chat.id)
    elif message.text == 'Склад':
        bot.send_message(text=user_bot.info_herous("sklad"), chat_id=message.chat.id)
    elif message.text == 'Копать':
        menu = "rudnic"
        status = "open"
        bot.send_message(text="Копаем", chat_id=message.chat.id, reply_markup=keymap())
        maps_bot.mining()

    elif message.text == "Создать карту":
        print("eee")
        maps_bot.new_maps()
    elif message.text == "Меню игрока":
        bot.send_message(text="Меню игрока", chat_id=message.chat.id, reply_markup=keyboardmenu())
    elif message.text == "Вернуться на карту":
        status = "close"
        bot.send_message(text="Вернуться", chat_id=message.chat.id, reply_markup=keyboardom())
    else: pprint(message.text)
"""


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    maps_bot = Maps(message=call.message, call=call)
    battle_bot = Battle(message=call.message, call=call)
    pprint(call.data)
    if call.data.split("_")[0] == "battle":
        battle_bot.status()
    else:
        maps_bot.goto()


while True:
    try:
#        bot.polling(none_stop=True, timeout=30)
        bot.infinity_polling(True)
    except Exception as e:
        print(e)
