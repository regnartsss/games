from config import bot
from data import lvlrudnic,step,heroes,enemy,weapons,weapons_data,fight_text_all,fight_trans,buildings,training
import telebot
import time
import random
import json
from datetime import datetime, timedelta
from pprint import pprint
import threading
import buy
#from buy import buy_amount, buy_tranzzo, succefull_tranzzo
import schedule
import tower_battle
import logging
import texting
from importlib import reload
import keyboard
import timeit
import map
import config
import os

ADMIN = 7653334401
global fight_text, combat, st
global maps, users, resource, warrior, build, hero, comb, field
menu = 0
barracks = 0
fight_text, combat = {}, {}

logging.basicConfig(filename='app.txt', format='%(name)s - %(levelname)s - [%(asctime)s] %(message)s',
                    level=logging.INFO)


def find_location():
    return os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))).replace('\\', '/') + '/'


PATH = find_location()


def benchmark(func):
    global st

    def wrapper(*args, **kwargs):
        t = time.time()
        res = func(*args, **kwargs)
        print(func.__name__, time.time() - t)
        return res

    return wrapper


# new
def save(key):
    global maps, users, resource, warrior, build, hero, comb, tower, tower_end, field
    if key == "all":
        with open(PATH + "tmp/" + 'maps.json', 'w', encoding="utf-16") as f:
            json.dump(maps, f)
        with open(PATH + "tmp/" + 'maps.json', 'rb') as f:
            maps = json.load(f)
        with open(PATH + "tmp/" + 'users.json', 'w', encoding="utf-16") as f:
            json.dump(users, f)
        with open(PATH + "tmp/" + 'users.json', 'rb') as f:
            users = json.load(f)
        with open(PATH + "tmp/" + 'warrior.json', 'w', encoding="utf-16") as f:
            json.dump(warrior, f)
        with open(PATH + "tmp/" + 'warrior.json', 'rb') as f:
            warrior = json.load(f)
        with open(PATH + "tmp/" + 'build.json', 'w', encoding="utf-16") as f:
            json.dump(build, f)
        with open(PATH + "tmp/" + 'build.json', 'rb') as f:
            build = json.load(f)
        with open(PATH + "tmp/" + 'hero.json', 'w', encoding="utf-16") as f:
            json.dump(hero, f)
        with open(PATH + "tmp/" + 'hero.json', 'rb') as f:
            hero = json.load(f)

        with open(PATH + "tmp/" + 'resource.json', 'w', encoding="utf-16") as f:
            json.dump(resource, f)
        with open(PATH + "tmp/" + 'resource.json', 'rb') as f:
            resource = json.load(f)
        with open(PATH + "tmp/" + 'field.json', 'w', encoding="utf-16") as f:
            json.dump(field, f)
        with open(PATH + "tmp/" + 'field.json', 'rb') as f:
            field = json.load(f)

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
    elif key == "tower":
        with open(PATH + "tmp/" + 'tower.json', 'w', encoding="utf-16") as f:
            json.dump(tower, f)
        with open(PATH + "tmp/" + 'tower.json', 'rb') as f:
            tower = json.load(f)
    elif key == "tower_end":
        with open(PATH + "tmp/" + 'tower_end.json', 'w', encoding="utf-16") as f:
            json.dump(tower_end, f)
        with open(PATH + "tmp/" + 'tower_end.json', 'rb') as f:
            tower_end = json.load(f)

        with open(PATH + "tmp/" + 'tower.json', 'rb') as f:
            tower = json.load(f)
    elif key == "resource":
        with open(PATH + "tmp/" + 'resource.json', 'w', encoding="utf-16") as f:
            json.dump(resource, f)
        with open(PATH + "tmp/" + 'resource.json', 'rb') as f:
            resource = json.load(f)
    elif key == "hero":
        with open(PATH + "tmp/" + 'hero.json', 'w', encoding="utf-16") as f:
            json.dump(hero, f)
        with open(PATH + "tmp/" + 'hero.json', 'rb') as f:
            hero = json.load(f)
    elif key == "st":
        with open(PATH + "tmp/" + 'st.txt', 'w', encoding="utf-16") as f:
            json.dump(st, f)
    elif key == "warrior":
        with open(PATH + "tmp/" + 'warrior.json', 'w', encoding="utf-16") as f:
            json.dump(warrior, f)
        with open(PATH + "tmp/" + 'warrior.json', 'rb') as f:
            warrior = json.load(f)
    elif key == "field":
        with open(PATH + "tmp/" + 'field.json', 'w', encoding="utf-16") as f:
            json.dump(field, f)
        with open(PATH + "tmp/" + 'field.json', 'rb') as f:
            field = json.load(f)


def open_tower_end():
    global tower_old
    with open(PATH + "tmp/" + 'tower_old.json', 'rb') as f:
        tower_old = json.load(f)


# new
def start_open():
    logging.info("Запуск игры")
    global maps, users, resource, warrior, build, hero, comb, field
    with open(PATH + "tmp/" + 'maps.json', 'rb') as f:
        maps = json.load(f)
    with open(PATH + "tmp/" + 'users.json', 'rb') as f:
        users = json.load(f)
    with open(PATH + "tmp/" + 'maps.json', 'rb') as f:
        maps = json.load(f)
    with open(PATH + "tmp/" + 'warrior.json', 'rb') as f:
        warrior = json.load(f)
    with open(PATH + "tmp/" + 'build.json', 'rb') as f:
        build = json.load(f)
    with open(PATH + "tmp/" + 'hero.json', 'rb') as f:
        hero = json.load(f)
    with open(PATH + "tmp/" + 'resource.json', 'rb') as f:
        resource = json.load(f)
    with open(PATH + "tmp/" + 'comb.json', 'rb') as f:
        comb = json.load(f)
    with open(PATH + "tmp/" + 'tower.json', 'rb') as f:
        tower = json.load(f)
    with open(PATH + "tmp/" + 'field.json', 'rb') as f:
        field = json.load(f)
    bot.send_message(chat_id=765333440, text="Бот запущен")
    start_user_default()


# new
def start_user(message):
    try:
        ref = str(message.text.split(" ")[1])
        bot.send_message(chat_id=int(ref), text=texting.text_ref_new)
    #        logging.info(str(message.chat.id) + ' Вход по реф ссылке ' + ref)
    except IndexError:
        ref = "0"
    if str(message.chat.id) in users:
        bot.send_message(chat_id=message.chat.id, text=texting.text_user_is, reply_markup=keyboard.keyboard_main_menu())
    else:
        users[message.chat.id] = {
            "energy_used": 0,  # Энергия истраченная
            "step": 0,  # Ходов
            "step_used": 0,  # Ходов истрачено
            "lvlstep": 1,
            "wolk_used": 0,  # Надо пройти
            "wolk": 0,  # Пройдено
            "lvlheroes": 1,
            "health_used": 0,
            "experience_used": 0}  # Энергия истрачено
        warrior[message.chat.id] = {"shooting": {1: 0, 2: 0, 3: 0, 4: 0, 5: 0},
                                    "barracks": {1: 0, 2: 0, 3: 0, 4: 0, 5: 0},
                                    "stable": {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}}
        build[message.chat.id] = {"wall": 0, "castle": 1, "storage": 0, "farm": 0, "barracks": 0, "shooting": 0,
                                  "stable": 0}
        hero[message.chat.id] = {"data": str(datetime.today().strftime("%d/%m/%Y")),
                                 "avatar": "\ud83d\udc76",
                                 "nik_name": "player_%i" % (random.randint(1, 9999999)),
                                 "ref": ref,
                                 "free_name": 0}
        resource[str(message.chat.id)] = {"farm_time": datetime.now().strftime("%Y:%m:%d:%H:%M:%S"),
                                          "food": 0,
                                          "wood": 0,
                                          "stone": 0,
                                          "iron": 0,
                                          "gold": 0,
                                          "diamond": 0,
                                          "production": 0,
                                          "mining": {}
                                          }
        s = random.randint(1, len(maps))
        maps[str(s)] = {"id": str(message.chat.id)}
        bot.send_message(chat_id=765333440,
                         text=date("full_time") + texting.text_user_new + str(message.chat.id))
        logging.info(str(message.chat.id) + texting.text_user_new)

        try:
            bot.send_message(message.chat.id, text=texting.text_start, reply_markup=keyboard.keyboard_start())
        except:
            pass
    save("all")


# new
def start_user_name_close(message):
    hero[str(message.chat.id)]["nik_name"] = str(message.text)
    save("hero")
    bot.send_message(chat_id=message.chat.id, text=texting.text_main_menu % (hero[str(message.chat.id)]["nik_name"]),
                     reply_markup=keyboard.keyboard_main_menu())


# new Запрос стартового имени
def start_user_name(message):
    if not message.from_user.username:
        button = "player_%i" % (random.randint(1, 9999999))
    else:
        button = message.from_user.username
    bot.send_message(chat_id=message.chat.id, text=texting.text_user_name,
                     reply_markup=telebot.types.ReplyKeyboardMarkup(True, False).row(button))
    bot.register_next_step_handler(message, start_user_name_close)


# new Восстанавливаемые ресурсы
def start_user_default():
    for key, value in users.items():
        lvl_heroes = value["lvlheroes"]
        value["health_used"] = heroes[lvl_heroes]["health"]
        value["energy_used"] = heroes[lvl_heroes]["energy"]
        value["step_used"] = step[value["lvlstep"]]["step"]
    logging.info('Здоровье, шаги, энергия восстановлены')
    save("users")


# new Вывод инфы о герое
def info_heroes(message, key="heroes"):
    avatar = hero[str(message.chat.id)]["avatar"]
    id = str(message.chat.id)
    nikname = hero[str(message.chat.id)]["nik_name"]
    level = users[str(message.chat.id)]["lvlheroes"]
    energy_used = users[str(message.chat.id)]["energy_used"]
    energy = heroes[level]["energy"]
    experience_used = users[str(message.chat.id)]["experience_used"]
    experience = heroes[level]["experience"]
    health_used = users[str(message.chat.id)]["health_used"]
    health = heroes[level]["health"]
    hit = heroes[level]["hit"]
    lvlstep = users[str(message.chat.id)]["lvlstep"]
    wolk_used = users[str(message.chat.id)]["wolk_used"]
    wolk = step[lvlstep]["wolk"]
    step_used = users[str(message.chat.id)]["step_used"]
    stepin = step[lvlstep]["step"]
    gold = resource[str(message.chat.id)]["gold"]
    diamond = resource[str(message.chat.id)]["diamond"]

    food = resource[str(message.chat.id)]["food"]
    wood = resource[str(message.chat.id)]["wood"]
    stone = resource[str(message.chat.id)]["stone"]
    iron = resource[str(message.chat.id)]["iron"]

    info_hero = texting.text_info_heroes % \
                (avatar, id, nikname, level, energy_used, energy, experience_used, experience, health_used, health,
                 hit, lvlstep, wolk_used, wolk, step_used, stepin, gold, diamond)
    stat = texting.text_info_storage % (stone, wood, iron, food, gold)

    if key == "heroes":
        return info_hero
    elif key == "build":
        return stat


start_open()


# new Создание ячейки
def cell():
    n = random.randint(1, 10000)
    if maps[str(n)]["resource"] == "null":
        maps[str(n)] = map.resource_start(n)
    else:
        cell()


def date(key="all"):
    if key == "full_time":
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
        bot.send_message(message.chat.id, "Отмена", reply_markup=keyboard.keyboard_main_menu())
    else:
        pprint("test")
        bot.send_message(765333440, "mess @" + str(message.from_user.username) + " " + str(
            message.from_user.first_name) + " " + message.text)
        pprint("test")


# new Запись врага
def enemy_write(message, cell):
    r = random.randint(users[str(message)]["lvlheroes"] - 1, users[str(message)]["lvlheroes"])
    if r <= 0:
        r = 1
    users[str(message)]["enemy_lvl"] = r
    users[str(message)]["enemy_health"] = enemy[r]["health"]
    users[str(message)]["enemy_exr"] = 5 * r
    users[str(message)]["enemy_cell"] = cell
    users[str(message)]["enemy_hit"] = enemy[r]["hit"]
    reload(texting)
    bot.send_message(text=texting.text_ataka_enemy %
                          (enemy[r]["name"], r, enemy[r]["health"]), chat_id=message,
                     reply_markup=keyboard.keyboard_battle())


def time_str(timer):
    if timer > 3600:
        return time.strftime('%H:%M:%S', time.gmtime(timer))
    else:
        return time.strftime('%M:%S', time.gmtime(timer))


# new
def mining(message):
    threading.Thread(target=timer_mining, args=(message,)).start()


# new
def timer_mining(message):
    global maps, users
    ss, sum, text = 1, 0, ""
    user_mining = resource[str(message.chat.id)]["mining"]
    res = user_mining["resource"]
    kol_timer = user_mining["number"]
    lvl_timer = lvlrudnic[user_mining["lvl"]]
    timer_all = int(user_mining["number"]) // lvlrudnic[user_mining["lvl"]]
    for i in range(timer_all + 2, 0, -1):
        pprint(str(message.chat.id) + " " + str(user_mining["cell"]) + " " + str(ss * lvl_timer))
        if resource[str(message.chat.id)]["start"] == 0:
            break
        elif sum >= kol_timer:
            break
        ss += 1
        sum = ss * lvl_timer
        time.sleep(1)

    cell_res = str(user_mining["cell"])
    if int(maps[cell_res]["number"]) - int(sum) <= 0:
        resource[str(message.chat.id)][res] += maps[str(user_mining["cell"])]["number"]
        try:
            resource[str(message.chat.id)]["production"] += maps[str(user_mining["cell"])]["number"]
        except:
            resource[str(message.chat.id)]["production"] = maps[str(user_mining["cell"])]["number"]
        text = "⚡️Вы завершили добычу ⚡️\nСобрано " + str(maps[str(user_mining["cell"])]["number"])
        maps[str(user_mining["cell"])]["resource"] = "null"
        maps[str(user_mining["cell"])].pop("lvl")
        maps[str(user_mining["cell"])].pop("number")
        cell()
    elif int(maps[cell_res]["number"]) - int(sum) >= 0:
        maps[str(user_mining["cell"])]["number"] -= sum
        resource[str(message.chat.id)][res] += sum
        try:
            resource[str(message.chat.id)]["production"] += sum
        except:
            resource[str(message.chat.id)]["production"] = sum
        text = "⚡️Вы вышли и собрали " + str(sum) + " ⚡ "

    else:
        pprint("ошибка")
    lvl_storage = build[str(message.chat.id)]["storage"]
    if resource[str(message.chat.id)][res] > buildings["storage"][lvl_storage]["capacity"]:
        resource[str(message.chat.id)][res] = buildings["storage"][lvl_storage]["capacity"]
        text = "⚡️Вы завершили добычу ⚡ \nСобрано " + str(sum) + "\nСклад полон"

    resource[str(message.chat.id)]["start"] = 0
    resource[str(message.chat.id)]["mining"] = {}
    save("maps")
    save("resource")

    bot.send_message(text=text, chat_id=message.chat.id, reply_markup=keyboard.keyboardmap())
    Maps(message=message).goto()

def mining_ataka(message):
        global users
        user_mining = resource[str(message.chat.id)]["mining"]
        field[str(message.chat.id)] = {}
        lvl = user_mining["lvl"]
        print(222)
        k = [4, 2.5, 2, 1.75, 1.6]
        k_k = int(k[lvl - 1] * lvl)
        i = 1
        print(k_k * k_k)
        #    a = np.ones(k_k*k_k, 'int')
        a = [1 for i in range(0, k_k * k_k)]
        #    print("Размер поля %s" %k_k)
        k = 0
        next = random.randint(k, k_k)
        #    print("Начальная ячейка %s" % next)
        a[next] = 2
        d = [0, k_k]
        stop, r_min, r_max = 10, 1, 10
        while 1 < stop:
            #        print(r_min, r_max)
            r = random.randint(r_min, r_max)
            #        print("Следующий ход %s" % r)
            #        print("%s --- %s" % (d[0], d[1]))
            if r == 2 or r == 3 or r == 4:
                #            print("%s ход на %s" % (d[0],next - 1))
                if d[0] <= next - 1:
                    a[next - 1] = 0
                    #                print("Перешли с %s на ячейку %s" % (next, next - 1))
                    next = next - 1
                    r_min, r_max = 1, 4
                else:
                    r_min, r_max = 5, 6
                    pass
            elif r == 5 or r == 6:
                try:
                    a[next + k_k] = 0
                except:
                    print("Error_123")
                    stop = 1
                #            print("Перешли с %s на ячейку %s" % (next, next+k_k))
                next = next + k_k
                d[0] += k_k
                d[1] += k_k
                r_min, r_max = 1, 10

            elif r == 7 or r == 8 or r == 9:
                if d[1] > next + 1:
                    a[next + 1] = 0
                    #                print("Перешли с %s на ячейку %s" % (next, next + 1))
                    next = next + 1
                    r_min, r_max = 7, 10
                else:
                    r_min, r_max = 5, 6
                    pass
        #   print(a)

        r = int(a.count(0) / lvl - 1)

        x = 1
        s = 0
        r_r = r
        n = 0
        while n <= len(a) - 1:
            if a[n] == 0:
                if s == r_r:
                    a[n] = 3

                    r_r += r
                s += 1
            n += 1
        r_num = a.count(3)
        resource[str(message.chat.id)]["mining"]["enem_num"] = r_num
   #     resource[str(message.chat.id)]["mining"]["enem"] = r_num
        resource[str(message.chat.id)]["mining"]["enem_num_resource"] = int(resource[str(message.chat.id)]["mining"]["number"]/r_num)
        data_resource = {"wood": "🌲", "stone": "🧱", "iron": "⛓"}
        res = resource[str(message.chat.id)]["mining"]["resource"]
        resource[str(message.chat.id)]["mining"]["avatar"] = data_resource[res]
        field[str(message.chat.id)] = a
        print("err1223")
        save("field")
        print("err122errr3")
        print(field)
        Fight(message=message).field_goto()


# new Обновление шагов, опыта
def update_statistic(message, data):
    if data == "step":
        if users[str(message.chat.id)]["wolk_used"] >= step[users[str(message.chat.id)]["lvlstep"]]["wolk"]:
            users[str(message.chat.id)]["lvlstep"] += 1
            users[str(message.chat.id)]["wolk_used"] = 0
        else:
            pass

    elif data == "experience":
        if users[str(message.chat.id)]["experience_used"] >= heroes[users[str(message.chat.id)]["lvlheroes"]][
            "experience"]:
            users[str(message.chat.id)]["lvlheroes"] += 1
            users[str(message.chat.id)]["experience_used"] = 0
            users[str(message.chat.id)]["health_used"] = heroes[users[str(message.chat.id)]["lvlheroes"]]["health"]
            users[str(message.chat.id)]["energy_used"] = heroes[users[str(message.chat.id)]["lvlheroes"]]["energy"]
            chat = int(hero[str(message.chat.id)]["ref"])
            if chat != "0":
                bot.send_message(chat_id=chat, text=texting.text_ref_up % users[str(message.chat.id)]["lvlheroes"])
                resource[str(chat)]["diamond"] += users[str(message.chat.id)]["lvlheroes"]
        else:
            pass
    save("users")


# new Восстановление энергии
def energy_timer(message):
    while users[str(message.chat.id)]["energy_used"] < heroes[users[str(message.chat.id)]["lvlheroes"]]["energy"]:
        time.sleep(1500)  # in seconds
        users[str(message.chat.id)]["energy_used"] += 1
    #        save("user")
    bot.send_message(chat_id=message.chat.id, text=texting.text_energy_timer)


# new Подсчет энергии
def energy(message):
    lvl_hero = users[str(message.chat.id)]["lvlheroes"]
    if users[str(message.chat.id)]["energy_used"] == heroes[lvl_hero]["energy"]:
        users[str(message.chat.id)]["energy_used"] -= 1
        threading.Thread(target=energy_timer, args=(message,)).start()
    elif users[str(message.chat.id)]["energy_used"] == 0:
        bot.send_message(chat_id=message.chat.id, text="У вас кончилась энергия")
    elif users[str(message.chat.id)]["energy_used"] < heroes[lvl_hero]["energy"]:
        users[str(message.chat.id)]["energy_used"] -= 1


# new Восстановлени шагов
def timer_step(message):
    while users[str(message.chat.id)]["step_used"] < step[users[str(message.chat.id)]["lvlstep"]]["step"]:
        time.sleep(60)  # in seconds
        users[str(message.chat.id)]["step_used"] += 1


# new Подсчет шагов
def move(message):
    print(message.chat.id)
    lvl_step = users[str(message.chat.id)]["lvlstep"]
    if users[str(message.chat.id)]["step_used"] == step[lvl_step]["step"]:
        users[str(message.chat.id)]["step_used"] -= 1
        users[str(message.chat.id)]["wolk_used"] += 1
        threading.Thread(target=timer_step, args=(message,)).start()
    elif users[str(message.chat.id)]["step_used"] == 0:
        bot.send_message(chat_id=message.chat.id, text="У вас кончились ходы")
    elif users[str(message.chat.id)]["step_used"] < step[lvl_step]["step"]:
        users[str(message.chat.id)]["step_used"] -= 1
        users[str(message.chat.id)]["wolk_used"] += 1

    update_statistic(message, data="step")
#    save("maps")
#    save("users")


def help(message, call=""):
    keyboard = telebot.types.InlineKeyboardMarkup()
    maps = telebot.types.InlineKeyboardButton(text="Карта", callback_data="help_maps")
    battle = telebot.types.InlineKeyboardButton(text="Бой", callback_data="help_battle")
    if message.text == texting.button_help:
        text = texting.text_help
        keyboard.add(maps, battle)
        bot.send_message(chat_id=message.chat.id, text=text, reply_markup=keyboard)

    else:
        if call.data == "help_maps":
            text = "На карте вы можете добывать ресурсы и воевать против монстров.\n На карте распологаются ресурсы: еда, камень, дерево. Они вам понадобятся для постройки у улучшения вашего города."
        elif call.data == "help_battle":
            text = "Бой с соперником проходит в пошаговом режиме.\n На каждом ходе у вас есть два очка защиты и два очка нападения.\n "
        keyboard.add(maps, battle)
        bot.edit_message_text(chat_id=message.chat.id, text=text, message_id=message.message_id,
                              reply_markup=keyboard.keyboard)


def timer_health(message):
    while users[str(message.chat.id)]["health_used"] < heroes[users[str(message.chat.id)]["lvlheroes"]]["health"]:
        time.sleep(20)  # in seconds
        users[str(message.chat.id)]["health_used"] = heroes[users[str(message.chat.id)]["lvlheroes"]]["health"]
        save("user")
    if users[str(message.chat.id)]["health_used"] == heroes[users[str(message.chat.id)]["lvlheroes"]]["health"]:
        bot.send_message(chat_id=message.chat.id, text="Здоровье восстановлено ")


def congratulation(message, data):
    if data == "heroes":
        users[str(message.chat.id)]["experience_used"] += 5
        r_gold = random.randint(1, 50)
        resource[str(message.chat.id)]["gold"] += r_gold
        maps[users[str(message.chat.id)]["enemy_cell"]]["resource"] = "null"
        update_statistic(message, data="experience")
        threading.Thread(target=timer_health, args=(message,)).start()
        energy(message)
        #            bot.send_message(text="Бой окончен: ", chat_id=message.chat.id, reply_markup=keyboard.keyboardmap())
        bot.send_message(text=texting.text_ataka_win % r_gold,
                         chat_id=message.chat.id,
                         reply_markup=keyboard.keyboardmap())
        time.sleep(2)
        Maps(message=message).goto()
    elif data == "field":
        users[str(message.chat.id)]["experience_used"] += 3
        r_gold = random.randint(1, 50)
        resource[str(message.chat.id)]["gold"] += r_gold
        update_statistic(message, data="experience")
        threading.Thread(target=timer_health, args=(message,)).start()
        energy(message)


    elif data == "enemy":
        print(22)
        threading.Thread(target=timer_health, args=(message,)).start()
        energy(message)
        #            bot.send_message(text="Бой окончен: ", chat_id=message.chat.id, reply_markup=keyboard.keyboardmap())
        bot.send_message(text=texting.text_ataka_lose, chat_id=message.chat.id,
                         reply_markup=keyboard.keyboard_main_menu())
        time.sleep(2)


#        Maps(message=message).goto()


class Maps():
    def __init__(self, call="", message=""):
        global maps, menu, attak
        try:
            self.text = message.text
            self.message_chat_id = message.chat.id

        except:
            pass
        try:

            self.message = call.message
            self.call = call.data
            self.call_id = call.id
            self.text = "_"
            self.call_message_id = call.message.message_id
            #            print(self.message.chat.id)
            self.message_chat_id = call.message.chat.id

        except:
            pass

    @benchmark
    def output_map(self):

        global pole
        keyboard = telebot.types.InlineKeyboardMarkup()
        x, y, cell_user, n, pole = 1, 0, "", 0, 100
        cell_user = users[str(self.message_chat_id)]["cell"]

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

                    elif cell == str(self.message_chat_id):
                        tab.append(
                            telebot.types.InlineKeyboardButton(hero[str(self.message_chat_id)]["avatar"],
                                                               callback_data=str(start_field)))
                    elif cell != "null":
                        tab.append(telebot.types.InlineKeyboardButton(hero[str(cell)]["avatar"],
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
            step = telebot.types.InlineKeyboardButton(
                text="🚶‍♂️Ходов: " + str(users[str(self.message_chat_id)]["step_used"]),
                callback_data=" ")
            energy = telebot.types.InlineKeyboardButton(
                text="🔋 ️Энергии: " + str(users[str(self.message_chat_id)]["energy_used"]),
                callback_data=" ")
            health = telebot.types.InlineKeyboardButton(
                text="❤ Здоровье: " + str(users[str(self.message_chat_id)]["health_used"]),
                callback_data=" ")
        keyboard.row(step, energy, health)

        return keyboard

    @benchmark
    def goto(self):
        #        global maps, pole, attak
        if self.text == "⏱ Вывод карты ⏱" or self.text == texting.button_maps or \
                self.text == texting.button_mining_map or self.text == texting.button_goto_two or \
                self.text[0:3] == "/--" or self.text == texting.button_mining or self.text == texting.button_goto:
            try:
                bot.send_message(text=texting.text_goto_maps, chat_id=self.message_chat_id,
                                 reply_markup=self.output_map())
            except Exception as n:
                print(n)
        else:
            pole = 100
            cell_user = users[str(self.message_chat_id)]["cell"]
            #            print(self.call)
            #            print(cell_user)
            try:
                value_call = maps[str(self.call)]["resource"]
            except:
                try:
                    value_call = "olduser_" + maps[str(self.call)]["id"]
                except:
                    value_call = "null"

            if users[str(self.message_chat_id)]["step_used"] == 0:
                bot.answer_callback_query(callback_query_id=self.call_id, text='У вас нет ходов')
            elif users[str(self.message_chat_id)]["health_used"] <= 0:
                bot.answer_callback_query(callback_query_id=self.call_id, text='Вы мертвы')
            elif self.call == str(cell_user):
                bot.answer_callback_query(callback_query_id=self.call_id, text='Это вы')
            elif int(self.call) == int(cell_user) - 1:
                self.database(cell_user, value_call, -1)
            elif int(self.call) == int(cell_user) + 1:
                self.database(cell_user, value_call, +1)
            elif int(self.call) == int(cell_user) - pole:
                self.database(cell_user, value_call, - pole)
            elif int(self.call) == int(cell_user) + pole:
                self.database(cell_user, value_call, + pole)
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
            elif value_call.split("_")[0] == "olduser":
                bot.answer_callback_query(callback_query_id=self.call_id, text='Город соперника')

    @benchmark
    def database(self, cell_user, value_call, s):
#rudnic
        if value_call == "iron" or value_call == "wood" or value_call == "stone":
            bot.delete_message(chat_id=self.message_chat_id, message_id=self.call_message_id)
            self.rudnic(int(self.call))
#enemy
        elif value_call == "enemy":
            if users[str(self.message_chat_id)]["energy_used"] == 0:
                bot.send_message(text="У вас нет энергии", chat_id=self.message_chat_id)
            else:
                bot.delete_message(chat_id=self.message_chat_id, message_id=self.call_message_id)
                #                users[str(self.message_chat_id)]["cell"] = users[str(self.message_chat_id)]["cell"] + s
                enemy_write(self.message_chat_id, self.call)
        elif value_call.split("_")[0] == "olduser":
            bot.send_message(text="Аттака другого игрока на стадии разработки", chat_id=self.message_chat_id)
        else:
            users[str(self.message_chat_id)]["cell"] = users[str(self.message_chat_id)]["cell"] + s
            self.goto_cell(cell_user, position_user=s)

    @benchmark
    def goto_cell(self, cell_user, position_user):
        maps[str(cell_user)] = {"resource": "null"}
        maps[str(int(cell_user) + position_user)] = {"id": str(self.message_chat_id)}
        move(self.message)
        bot.edit_message_text(text=texting.text_goto, chat_id=self.message_chat_id, message_id=self.message.message_id,
                              reply_markup=self.output_map())

    @benchmark
    def rudnic(self, cell_user):
        #        reload(texting)
        resource[str(self.message_chat_id)]["mining"] = {}
        user_mining = resource[str(self.message_chat_id)]["mining"]
        user_mining["cell"] = cell_user
        user_mining["resource"] = maps[str(cell_user)]["resource"]
        user_mining["number"] = maps[str(cell_user)]["number"]
        user_mining["lvl"] = maps[str(cell_user)]["lvl"]
        tim = user_mining["number"] // lvlrudnic[user_mining["lvl"]]
        user_mining["timer"] = time_str(tim)
        bot.send_message(text=texting.text_mining(user_mining), chat_id=self.message_chat_id,
                         reply_markup=keyboard.keyboard_keyrudnic())


class Build():

    def __init__(self, call="", message=""):
        global users, combat, fight_text, text_ataka

        try:
            self.message = message
            self.text = message.text
            self.message_chat_id = message.chat.id

        except:
            pass
        try:
            self.message = call.message
            self.call_data = call.data
            self.call_id = call.id
            self.call_message_id = call.message.message_id
            self.message_chat_id = call.message.chat.id
            self.data = self.call_data.split("_")[1]

        except:
            pass
        self.user = users[str(self.message_chat_id)]

        self.user_building = build[str(self.message_chat_id)]

    def build(self, text=""):
        keyboard = telebot.types.InlineKeyboardMarkup()
        #        self_user = str(call.message.chat.id)
        #        self.user_building["temp"] = self.user_building
        #        if data_new != "":
        #           self.data = data_new

        if self.data == "back":
            self.user_building["temp"] = ""
            self.user_building.pop("temp")
            self.building()
        #            bot.answer_callback_query(callback_query_id=self.call_id, text="Назад")
        elif self.data == "update":

            self.data = self.call_data.split("_")[2]

            text_stone, text_wood, text_iron, text_food = self.building_update()
            if text_stone == "✅" and text_wood == "✅" and text_iron == "✅" and text_food == "✅":
                if self.data == "storage" and self.user_building["castle"] <= self.user_building["storage"]:
                    bot.answer_callback_query(callback_query_id=self.call_id, text="Увеличьте уровень 🏤 замка")
                    self.user_building["temp"] = "storage"

                #                    self.build()
                elif self.data == "farm" and self.user_building["storage"] <= self.user_building["farm"]:
                    bot.answer_callback_query(callback_query_id=self.call_id, text="Увеличьте уровень 🏚склада")
                    self.user_building["temp"] = "farm"
                #                    self.build(data_new="storage")
                elif self.data == "barracks" and self.user_building["farm"] <= self.user_building["barracks"]:
                    bot.answer_callback_query(callback_query_id=self.call_id, text="Увеличьте уровень фермы")
                    self.user_building["temp"] = "barracks"
                #                    self.build(data_new="farm")
                elif self.data == "shooting" and self.user_building["barracks"] <= self.user_building["shooting"]:
                    bot.answer_callback_query(callback_query_id=self.call_id, text="Увеличьте уровень казармы")
                    self.user_building["temp"] = "shooting"
                #                    self.build(data_new="barracks")
                elif self.data == "stable" and self.user_building["shooting"] <= self.user_building["stable"]:
                    bot.answer_callback_query(callback_query_id=self.call_id, text="Увеличьте уровень стрельбы")
                    self.user_building["temp"] = "stable"
                #                    self.build(data_new="shooting")
                elif self.data == "wall" and self.user_building["stable"] <= self.user_building["wall"]:
                    bot.answer_callback_query(callback_query_id=self.call_id, text="Увеличьте уровень конюшни")
                    self.user_building["temp"] = "wall"
                #                    self.build(data_new="stable")
                elif self.data == "castle" and self.user_building["wall"] < self.user_building["castle"]:
                    bot.answer_callback_query(callback_query_id=self.call_id, text="Увеличьте уровень 🧱 стены")
                    self.user_building["temp"] = "castle"
                #                    self.build(data_new="wall")
                else:
                    print("все ресурсы есть")
                    self.user_building[self.data] += 1
                    text = texting.text_building_up
                    num_stone, num_wood, num_iron, num_food = self.static_build(self.user_building[self.data])
                    resource[str(self.message_chat_id)]["wood"] -= num_wood
                    resource[str(self.message_chat_id)]["stone"] -= num_stone
                    resource[str(self.message_chat_id)]["iron"] -= num_iron
                    resource[str(self.message_chat_id)]["food"] -= num_food
                    save("users")
                    save("resource")
                    self.build(text)
            #                    try:
            #                        print("123131")
            #                        self.data = self.user_building["temp"]["temp"]
            #                        print(self.data)
            #                        if self.data == "":
            #                            self.build()
            #                        else:
            #                            self.user_building["temp"].pop("temp")
            #                            print("test1")
            #                            time.sleep(3)
            #                            print("test2")
            #                            self.build()
            #                    except:

            #                save
            #    print(data_old)

            #    if data_old != "":
            #        build(data=data_old)
            #    else:
            else:
                bot.answer_callback_query(callback_query_id=self.call_id, text="Не хватает ресуров")
        elif self.data == "market":
            print(111)
            if self.call_data.split("_")[2] == "buy" or self.call_data.split("_")[2] == "sell":
                print(222)
                try:
                    if self.call_data.split("_")[4] == "1000" or self.call_data.split("_")[4] == "10000":
                        self.buysell()
                except:
                    bot.edit_message_text(text=self.market_text(), chat_id=self.message_chat_id,
                                          message_id=self.call_message_id,
                                          reply_markup=self.keyboard_market_buysell())
            else:

                bot.edit_message_text(text=self.market_text(), chat_id=self.message_chat_id,
                                      message_id=self.call_message_id,
                                      reply_markup=self.keyboard_market())
        else:
            name = buildings[self.data]["name"]
            lvl = self.user_building[self.data]
            new_lvl = lvl + 1
            num_stone, num_wood, num_iron, num_food = self.static_build(new_lvl)
            text_stone, text_wood, text_iron, text_food = self.building_update()
            stone = str(num_stone) + text_stone
            wood = str(num_wood) + text_wood
            iron = str(num_iron) + text_iron
            food = str(num_food) + text_food

            text += texting.text_building_resource % (name, lvl, name, new_lvl, stone, wood, iron, food)

            keyboard.row(telebot.types.InlineKeyboardButton(text=texting.button_update,
                                                            callback_data="build_update_" + self.data))
            print(self.data)
            if self.data == "storage":
                text += "\nВместимость ресурсов: " + str(buildings[self.data][lvl]["capacity"])
            elif self.data == "farm":
                text += "\nПроизводство ресурсов: " + str(buildings[self.data][lvl]["production"]) + " шт\с"
            elif self.data == "barracks":
                keyboard.row(
                    telebot.types.InlineKeyboardButton(text=texting.text_building_goto, callback_data="entry_barracks"))
            elif self.data == "shooting":
                keyboard.row(
                    telebot.types.InlineKeyboardButton(text=texting.text_building_goto, callback_data="entry_shooting"))
            elif self.data == "stable":
                keyboard.row(
                    telebot.types.InlineKeyboardButton(text=texting.text_building_goto, callback_data="entry_stable"))

            keyboard.row(telebot.types.InlineKeyboardButton(text=texting.button_back, callback_data="build_back"))
            bot.edit_message_text(text=text, chat_id=self.message_chat_id, message_id=self.call_message_id,
                                  reply_markup=keyboard)

    def static_build(self, new_lvl):
        wood = buildings[self.data][new_lvl]["wood"]
        stone = buildings[self.data][new_lvl]["stone"]
        iron = buildings[self.data][new_lvl]["iron"]
        food = buildings[self.data][new_lvl]["food"]
        return stone, wood, iron, food

    def building_update(self):
        lvl = self.user_building[self.data]
        new_lvl = lvl + 1
        stone_player = resource[str(self.message_chat_id)]["stone"]
        wood_player = resource[str(self.message_chat_id)]["wood"]
        iron_player = resource[str(self.message_chat_id)]["iron"]
        food_player = resource[str(self.message_chat_id)]["food"]
        stone, wood, iron, food = self.static_build(new_lvl)
        #        wood = build[self.data][new_lvl]["wood"]
        #        stone = build[self.data][new_lvl]["stone"]
        #        iron = build[self.data][new_lvl]["iron"]
        #        food = build[self.data][new_lvl]["food"]
        text_stone, text_wood, text_iron, text_food = "✅", "✅", "✅", "✅"
        if stone_player < stone:
            text_stone = "⛔️"
        if wood_player < wood:
            text_wood = "⛔️ "
        if iron_player < iron:
            text_iron = "⛔️"
        if food_player < food:
            text_food = "⛔️"
        return text_stone, text_wood, text_iron, text_food

    def building(self):
        if self.text == texting.button_building:
            bot.send_message(text=texting.text_building_update % (info_heroes(self.message, key="build")),
                             chat_id=self.message_chat_id, reply_markup=self.print_building())

        else:
            bot.edit_message_text(
                text=texting.text_building_update % (info_heroes(self.message, key="build")),
                chat_id=self.message_chat_id,
                message_id=self.call_message_id, reply_markup=self.print_building())


    def print_building(self):
        keyboard = telebot.types.InlineKeyboardMarkup()
        i = 1
        tab = []
        for key, value in self.user_building.items():
            tab.append(
                telebot.types.InlineKeyboardButton(text=buildings[key]["name"] + " " + str(self.user_building[key]),
                                                   callback_data="build_" + key))
            if key == "temp":
                continue
            if i == 1 or i == 4 or i == 7:
                keyboard.row(*tab)
                tab = []
            i += 1

        keyboard.row(*tab)
        keyboard.row(telebot.types.InlineKeyboardButton(text=texting.button_market, callback_data="build_market_null"))
        return keyboard

    def market_text(self):
        stone_player = str(resource[str(self.message_chat_id)]["stone"])
        wood_player = str(resource[str(self.message_chat_id)]["wood"])
        iron_player = str(resource[str(self.message_chat_id)]["iron"])
        food_player = str(resource[str(self.message_chat_id)]["food"])
        gold_player = str(resource[str(self.message_chat_id)]["gold"])
        text = texting.text_building_market % (gold_player, stone_player, wood_player, iron_player, food_player)
        return text

    def keyboard_market(self):
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.add(telebot.types.InlineKeyboardButton(text="💰 Купить", callback_data="build_market_buy"),
                     telebot.types.InlineKeyboardButton(text="💰 Продать", callback_data="build_market_sell"))
        keyboard.row(telebot.types.InlineKeyboardButton(text=texting.button_back, callback_data="build_back"))
        return keyboard

    def keyboard_market_buysell(self):
        keyboard = telebot.types.InlineKeyboardMarkup()
        m = self.call_data.split("_")[2]
        stone1000 = telebot.types.InlineKeyboardButton(text="⛏ Камень 1000",
                                                       callback_data="build_market_" + m + "_stone_1000")
        iron1000 = telebot.types.InlineKeyboardButton(text="⚒ Железо 1000",
                                                      callback_data="build_market_" + m + "_iron_1000")
        wood1000 = telebot.types.InlineKeyboardButton(text="🌲 Дерево 1000",
                                                      callback_data="build_market_" + m + "_wood_1000")
        food1000 = telebot.types.InlineKeyboardButton(text="🌽 Еда 1000",
                                                      callback_data="build_market_" + m + "_food_1000")
        stone10000 = telebot.types.InlineKeyboardButton(text="⛏ Камень 10000",
                                                        callback_data="build_market_" + m + "_stone_10000")
        iron10000 = telebot.types.InlineKeyboardButton(text="⚒ Железо 10000",
                                                       callback_data="build_market_" + m + "_iron_10000")
        wood10000 = telebot.types.InlineKeyboardButton(text="🌲 Дерево 10000",
                                                       callback_data="build_market_" + m + "_wood_10000")
        food10000 = telebot.types.InlineKeyboardButton(text="🌽 Еда 10000",
                                                       callback_data="build_market_" + m + "_food_10000")

        if m == "buy":
            buysell = telebot.types.InlineKeyboardButton(text="Выберите кол-во для покупки", callback_data="nuu")
        elif m == "sell":
            buysell = telebot.types.InlineKeyboardButton(text="Выберите кол-во для продажи", callback_data="nuu")

        keyboard.row(buysell)
        keyboard.row(stone1000, stone10000)
        keyboard.row(wood1000, wood10000)
        keyboard.row(iron1000, iron10000)
        if m == "buy":
            keyboard.row(food1000, food10000)

        keyboard.row(telebot.types.InlineKeyboardButton(text=texting.button_back, callback_data="build_market_null"))
        return keyboard

    def buysell(self):

        m = self.call_data.split("_")[2]
        res = self.call_data.split("_")[3]
        num = int(self.call_data.split("_")[4])
        lvl_storage = build[str(self.message_chat_id)]["storage"]
        #        print(lvl_storage)
        if m == "buy":
            if resource[str(self.message_chat_id)]["gold"] - int(num / 100) < 0:
                bot.answer_callback_query(callback_query_id=self.call_id, text="У вас не хватает золота")
            elif resource[str(self.message_chat_id)][res] + num > buildings["storage"][lvl_storage]["capacity"]:
                bot.answer_callback_query(callback_query_id=self.call_id, text="Нет места на складе")
            else:
                resource[str(self.message_chat_id)]["gold"] -= int(num / 100)
                resource[str(self.message_chat_id)][res] += num
                bot.edit_message_text(text=self.market_text(), chat_id=self.message_chat_id,
                                      message_id=self.call_message_id,
                                      reply_markup=self.keyboard_market_buysell())
        elif m == "sell":
            if resource[str(self.message_chat_id)][res] - num < 0:
                bot.answer_callback_query(callback_query_id=self.call_id, text="У вас не хватает ресурсов")

            else:
                resource[str(self.message_chat_id)]["gold"] += int(num / 100)
                resource[str(self.message_chat_id)][res] -= num
                bot.edit_message_text(text=self.market_text(), chat_id=self.message_chat_id,
                                      message_id=self.call_message_id,
                                      reply_markup=self.keyboard_market_buysell())
        save("resource")


class Fight():
    def __init__(self, call="", message=""):
        global users, combat, fight_text, text_ataka, field
        try:

            self.text = message.text
            self.message_chat_id = message.chat.id
            self.message = message
        except:
            print("fier")
            pass
        try:
            self.message = call.message
            self.call_data = call.data
            self.call_id = call.id
            self.call_message_id = call.message.message_id
            self.message_chat_id = call.message.chat.id
        except:
            print("fier2")
            pass
        try:
            print(self.message_chat_id)
            self.field = field[str(self.message_chat_id)]
        except:
            print("fier3")
            pass
        try:
            text_ataka
        except:
            text_ataka = {}
        try:
            text_ataka[str(self.message_chat_id)]
        except:
            text_ataka[str(self.message_chat_id)] = {}

        print("fier4")
        self.user = users[str(self.message_chat_id)]
        self.lvl_enemy = int(users[str(self.message_chat_id)]["enemy_lvl"])
        self.lvl_heroes = int(users[str(self.message_chat_id)]["lvlheroes"])
        print("fier5")

    def keyboard_attaka(self, user):
        #        print(fight_text[user])
        keyboard = telebot.types.InlineKeyboardMarkup()
        null = telebot.types.InlineKeyboardButton(text="➖➖", callback_data="null")
        heroes_head = telebot.types.InlineKeyboardButton(text=fight_text[user]["heroes_head"],
                                                         callback_data="fight_heroes_head")
        heroes_left = telebot.types.InlineKeyboardButton(text=fight_text[user]["heroes_handleft"],
                                                         callback_data="fight_heroes_handleft")
        heroes_right = telebot.types.InlineKeyboardButton(text=fight_text[user]["heroes_handright"],
                                                          callback_data="fight_heroes_handright")
        heroes_breast = telebot.types.InlineKeyboardButton(text=fight_text[user]["heroes_breast"],
                                                           callback_data="fight_heroes_breast")
        heroes_legs = telebot.types.InlineKeyboardButton(text=fight_text[user]["heroes_legs"],
                                                         callback_data="fight_heroes_legs")
        heroes_foot = telebot.types.InlineKeyboardButton(text=fight_text[user]["heroes_foot"],
                                                         callback_data="fight_heroes_foot")
        enemy_head = telebot.types.InlineKeyboardButton(text=fight_text[user]["enemy_head"],
                                                        callback_data="fight_enemy_head")
        enemy_left = telebot.types.InlineKeyboardButton(text=fight_text[user]["enemy_handleft"],
                                                        callback_data="fight_enemy_handleft")
        enemy_right = telebot.types.InlineKeyboardButton(text=fight_text[user]["enemy_handright"],
                                                         callback_data="fight_enemy_handright")
        enemy_brest = telebot.types.InlineKeyboardButton(text=fight_text[user]["enemy_breast"],
                                                         callback_data="fight_enemy_breast")
        enemy_legs = telebot.types.InlineKeyboardButton(text=fight_text[user]["enemy_legs"],
                                                        callback_data="fight_enemy_legs")
        enemy_foot = telebot.types.InlineKeyboardButton(text=fight_text[user]["enemy_foot"],
                                                        callback_data="fight_enemy_foot")

        text_pole = telebot.types.InlineKeyboardButton(text=text_ataka[user]["null"], callback_data="1")
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
        global round_num
        print("test")
        user = str(self.message_chat_id)
        print("test")
        print(self.text)
        if self.text == texting.button_attack or self.text == "Ходите":
            fight_text[user] = {}
            combat[user] = {}
            round_num = 0
            fight_text[user] = fight_text_all.copy()
            text_ataka[user]["text"] = "/-------------------------/"
            text_ataka[user]["null"] = "Защита 2 очка. Аттака 2 очка"
            bot.send_message(text="Атака", chat_id=self.message_chat_id,
                             reply_markup=keyboard.keyboard_battle_one_back())
            bot.send_message(text="Вы атаковали врага. Выберите какую часть тела защитить и атакуйте врага",
                             chat_id=self.message_chat_id, reply_markup=self.keyboard_attaka(user=user))
        elif self.text == texting.button_goto:
            fight_text[user] = {}
            combat[user] = {}

        else:
            data = self.call_data.split("_")[1]
            data_old = self.call_data.split("_")[2]
            d = data + "_" + data_old
            if data == "heroes":
                if 0 < self.user["defence"] <= 2:
                    if data_old == "head":
                        fight_text[user][d] += " 🛡"
                        combat[user][d] = 1
                        pprint("test")
                        comb[d] += 1
                        pprint("test2")
                    elif data_old == "handleft":
                        fight_text[user][d] += " 🛡"
                        combat[user][d] = 1
                        comb[d] += 1
                    elif data_old == "handright":
                        fight_text[user][d] += " 🛡"
                        combat[user][d] = 1
                        comb[d] += 1
                    elif data_old == "breast":
                        fight_text[user][d] += " 🛡"
                        combat[user][d] = 1
                        comb[d] += 1
                    elif data_old == "legs":
                        fight_text[user][d] += " 🛡"
                        combat[user][d] = 1
                        comb[d] += 1
                    elif data_old == "foot":
                        fight_text[user][d] += " 🛡"
                        combat[user][d] = 1
                        comb[d] += 1
                    self.user["defence"] -= 1

                    bot.answer_callback_query(callback_query_id=self.call_id, text='Защитились')
                else:
                    bot.answer_callback_query(callback_query_id=self.call_id, text='Очки защиты законились')
                    return
            #   elif users[str(message.chat.id)]["defence"] >2:
            elif data == "enemy":
                if 0 < self.user["attaka"] <= 2:
                    if data_old == "head":
                        fight_text[user][d] += " ⚔️"
                        combat[user][d] = 1
                        comb[d] += 1
                    elif data_old == "handleft":
                        fight_text[user][d] += " ⚔️"
                        combat[user][d] = 1
                        comb[d] += 1
                    elif data_old == "handright":
                        fight_text[user][d] += " ⚔️"
                        combat[user][d] = 1
                        comb[d] += 1
                    elif data_old == "breast":
                        fight_text[user][d] += " ⚔️"
                        combat[user][d] = 1
                        comb[d] += 1
                    elif data_old == "legs":
                        fight_text[user][d] += " ⚔️"
                        combat[user][d] = 1
                        comb[d] += 1
                    elif data_old == "foot":
                        fight_text[user][d] += " ⚔️"
                        combat[user][d] = 1
                        comb[d] += 1
                    self.user["attaka"] -= 1
                    bot.answer_callback_query(callback_query_id=self.call_id, text='Атаковали')
                else:
                    bot.answer_callback_query(callback_query_id=self.call_id, text='Очки атаки законились')
                    return
            save("combat")
            if self.user["defence"] == 0 and self.user["attaka"] == 0:
                self.user["attaka"] = 2
                self.user["defence"] = 2
                text_ataka[user]["null"] = "Идет бой, ожидайте"
                bot.edit_message_text(text=text_ataka[user]["text"], chat_id=self.message_chat_id,
                                      message_id=self.call_message_id,
                                      reply_markup=self.keyboard_attaka(user))
                print("Бой прошел")
                round_num += 1
                text_ataka[user]["text"] += "\n/----/ Раунд " + str(round_num) + " /----/" + self.combat_battle(
                    user) + "\n"
                time.sleep(3)
                fight_text[user] = {}
                fight_text[user] = fight_text_all.copy()
                text_ataka[user]["null"] = "Защита 2 очка. Аттака 2 очка"
                if self.user["health_used"] <= 0:
                    bot.delete_message(self.message_chat_id, message_id=self.call_message_id)
                    bot.send_message(self.message_chat_id, text=text_ataka[user]["text"])
                    congratulation(self.message, "enemy")
                    print("Герой проиграл")
                elif self.user["enemy_health"] <= 0:
                    bot.delete_message(self.message_chat_id, message_id=self.call_message_id)
                    bot.send_message(self.message_chat_id, text=text_ataka[user]["text"])

                    print("Враг проиграл")

                    if resource[str(self.message_chat_id)]["f_m"] == 1:
                        congratulation(self.message, "field")
                        self.figth_mining()

                    else:
                        congratulation(self.message, "heroes")

                else:
                    bot.edit_message_text(text=text_ataka[user]["text"], chat_id=self.message_chat_id,
                                          message_id=self.call_message_id,
                                          reply_markup=self.keyboard_attaka(user))

            else:
                defence = self.user["defence"]
                attaka = self.user["attaka"]

                #                    text = "Выберите часть тела для защиты и для аттаки"

                text_ataka[user]["null"] = "Защита " + str(defence) + " очка. Аттака " + str(attaka) + " очка"

                bot.edit_message_text(text=text_ataka[user]["text"], chat_id=self.message_chat_id,
                                      message_id=self.call_message_id,
                                      reply_markup=self.keyboard_attaka(user))

    def figth_mining(self):
        user_mining = resource[str(self.message_chat_id)]["mining"]
        res = user_mining["resource"]
        enem_num_resource= user_mining["enem_num_resource"]
        maps[str(user_mining["cell"])]["number"] -= enem_num_resource
        if maps[str(user_mining["cell"])]["number"] < 10:
            maps[str(user_mining["cell"])]["resource"] = "null"
            maps[str(user_mining["cell"])].pop("lvl")
            maps[str(user_mining["cell"])].pop("number")
            cell()
        resource[str(self.message_chat_id)][res] += enem_num_resource
        lvl_storage = build[str(self.message_chat_id)]["storage"]
        if resource[str(self.message_chat_id)][res] > buildings["storage"][lvl_storage]["capacity"]:
            resource[str(self.message_chat_id)][res] = buildings["storage"][lvl_storage]["capacity"]
        celli = users[str(self.message_chat_id)]["enemy_cell"]
        resource[str(self.message_chat_id)]["f_m"] = 0
        self.field[celli]=0
        self.r_print_r("new")


    def combat_battle(self, user):
        global comb, her, ene
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
        for key, value in combat[user].items():
            if h_a == key:
                text += "\n 🛡 Вы отразили аттаку врага в " + fight_trans[h_a]
            elif h_a_s == key:
                text += "\n 🛡 Вы отразили аттаку врага в " + fight_trans[h_a_s]
            elif d_e == key:
                text += "\n 🛡 Враг отразил вашу аттаку в " + fight_trans[d_e]
            elif d_e_s == key:
                text += "\n 🛡 Враг отразил вашу аттаку в " + fight_trans[d_e_s]
            elif key.split("_")[0] == "heroes":
                text += "\n ⚔️Враг нанес вам удар -" + str(enemy[self.lvl_enemy]["hit"]) + " ♥️"
                self.user["health_used"] -= enemy[self.lvl_enemy]["hit"]
            elif key.split("_")[0] == "enemy":
                text += "\n ⚔️Вы нанесли удар противнику - " + str(heroes[self.lvl_heroes]["hit"]) + " ♥️"
                self.user["enemy_health"] -= heroes[self.lvl_heroes]["hit"]
        combat[user] = {}
        return text



    def r_print_r(self, st=""):
        keyboard = telebot.types.InlineKeyboardMarkup()
        a = self.field
        print(a)
        avatar = resource[str(self.message_chat_id)]["mining"]["avatar"]
        print(avatar)
        dd = {0: " ", 1: avatar, 2: "🕴", 3: "👻"}
        l = len(a)
        k_k = l ** 0.5
        f = []
        x, y, n = 1, 1, 0
        print("er1234r")
        while x <= k_k:
            tab = []
            keyfield = []
            y = 1
            while y <= k_k:
                    tab.append(a[n])
#                    print("error_2")
                    keyfield.append(telebot.types.InlineKeyboardButton(text="%s" % dd[a[n]], callback_data="field_%s_%s" % (a[n], n)))
                    y += 1
                    n += 1
            x += 1
            f.append(tab)
            keyboard.row(*keyfield)
#        pprint(f)
        if st == "new":
            step = telebot.types.InlineKeyboardButton(text="🚶‍♂️Ходов: " + str(users[str(self.message_chat_id)]["step_used"]),
                callback_data=" ")
            energy = telebot.types.InlineKeyboardButton(
                text="🔋 ️Энергии: " + str(users[str(self.message_chat_id)]["energy_used"]),
                callback_data=" ")
            health = telebot.types.InlineKeyboardButton(
                text="❤ Здоровье: " + str(users[str(self.message_chat_id)]["health_used"]),
                callback_data=" ")
            keyboard.row(step, energy,health)
            bot.send_message(text="Ходите", chat_id=self.message_chat_id,reply_markup=keyboard)
        else:
            try:
                step = telebot.types.InlineKeyboardButton(
                    text="🚶‍♂ Ходов: " + str(users[str(self.message_chat_id)]["step_used"]),
                    callback_data=" ")
                energy = telebot.types.InlineKeyboardButton(
                    text="🔋 Энергии: " + str(users[str(self.message_chat_id)]["energy_used"]),
                    callback_data=" ")
                health = telebot.types.InlineKeyboardButton(
                    text="❤ Здоровье: " + str(users[str(self.message_chat_id)]["health_used"]),
                    callback_data=" ")
                keyboard.row(step, energy, health)
                bot.edit_message_text(text="Ходите", chat_id=self.message_chat_id, message_id=self.call_message_id, reply_markup=keyboard)
            except: pass


    def field_goto(self):
        print(self.text)
        if self.text == texting.button_mining_ataka:
            print("errrrr")
            self.r_print_r("new")
        else:
#            print(self.call.data)
            i = 0
            print("her_1")
            a = len(self.field) ** 0.5

            while i <= len(self.field):
#                print(self.field[i])
                if self.field[i] == 2:
                    her = i
                    break
                i +=1
            print("ewrwe")
            cell = int(self.call_data.split("_")[2])
            result = int(self.call_data.split("_")[1])
            print(result)
            print("Игрок %s ходит на %s" %(her, cell))
            if result == 1:
                print("dddd")
                try:
                    bot.answer_callback_query(callback_query_id=self.call_id, text="Ячейка не доступна")
                except:
                    pass
            elif result == 0 or result == 3:
                print("num_2")
                if her - cell == 1 or cell - her == 1 or cell - her == a or her - cell == a:
                    print("rez %s" %result)
                    move(self.message)
                    if result == 3:
                        print(result)
                        print("атака")
                        users[str(self.message_chat_id)]["defence"] = 2
                        users[str(self.message_chat_id)]["attaka"] = 2
                        print("атака")
                        lvl = users[str(self.message_chat_id)]["lvlheroes"] - 1
                        users[str(self.message_chat_id)]["enemy_lvl"] = lvl
                        users[str(self.message_chat_id)]["enemy_health"] = enemy[lvl]["health"]

#                        users[str(self.message_chat_id)]["enemy_exr"] = 5 * lvl
                        users[str(self.message_chat_id)]["enemy_cell"] = cell
                        users[str(self.message_chat_id)]["enemy_hit"] = enemy[lvl]["hit"]
                        resource[str(self.message_chat_id)]["f_m"] = 1
                        print("rrrrrrr")
                        self.fight()
                    else:
                        self.field[her] = 0
                        self.field[cell] = 2
                        self.r_print_r()

                else:
                    print("Ошибка")



class Shop():
    def __init__(self, call="", message=""):
        global users
        try:
            self.message = message
            self.text = message.text
            self.message_chat_id = message.chat.id
        except:
            pass
        try:
            self.message = call.message
            self.call_data = call.data
            self.call_id = call.id
            self.call_message_id = call.message.message_id
            self.message_chat_id = call.message.chat.id
        except:
            pass

    def keyboard_shop(self):
        keyboard = telebot.types.InlineKeyboardMarkup()
        rename = telebot.types.InlineKeyboardButton(text="Изменить имя 5 💎", callback_data="shop_rename")
        changeavatar = telebot.types.InlineKeyboardButton(text="Изменить аватар 5 💎", callback_data="shop_avatar")
        sell = telebot.types.InlineKeyboardButton(text="Купить 💎", callback_data="shop_sell")
        keyboard.add(rename)
        keyboard.add(changeavatar)
        keyboard.add(sell)
        return keyboard

    def shop(self):
        if self.call_data.split("_")[1] == "menu":
            bot.edit_message_text(text="Для подробной информации о товаре, нажмите на него",
                                  chat_id=self.message_chat_id,
                                  message_id=self.call_message_id, reply_markup=self.keyboard_shop())
        elif self.call_data.split("_")[1] == "avatar":
            bot.edit_message_text(text="Выберите аватар\n Стоимость смены аватара 5 💎", chat_id=self.message_chat_id,
                                  message_id=self.call_message_id, reply_markup=self.avatar())

        elif self.call_data.split("_")[1] == "emoji":
            key = self.call_data.split("_")[2]
            keyboard = telebot.types.InlineKeyboardMarkup()
            yes = telebot.types.InlineKeyboardButton(text="Да", callback_data="shop_" + key + "_yes")
            no = telebot.types.InlineKeyboardButton(text="Нет", callback_data="shop_" + key + "_no")
            keyboard.row(yes, no)
            bot.edit_message_text(
                text="Стоимость смены аватара 5 💎.\nВы действительно хотите сменить аватар на " + key + "?",
                chat_id=self.message_chat_id,
                message_id=self.call_message_id, reply_markup=keyboard.keyboard)
        elif self.call_data.split("_")[1] == "sell":
            buy.buy_amount(message=self.message)
        elif self.call_data.split("_")[1] == "rename":
            bot.delete_message(chat_id=self.message_chat_id, message_id=self.call_message_id)
            self.rename_heroes()

        elif self.call_data.split("_")[2] == "yes":
            key = self.call_data.split("_")[1]
            hero[str(self.message_chat_id)]["avatar"] = key
            if resource[str(self.message_chat_id)]["diamond"] - 5 < 0:
                bot.edit_message_text(text="У вас не хватает алмазов", chat_id=self.message_chat_id,
                                      message_id=self.call_message_id, reply_markup=self.keyboard_shop())
            else:
                resource[str(self.message_chat_id)]["diamond"] -= 5
                bot.edit_message_text(text="Вы сменили аватар на " + key + ". Поздавляем", chat_id=self.message_chat_id,
                                      message_id=self.call_message_id, reply_markup=self.keyboard_shop())
        elif self.call_data.split("_")[2] == "no":
            bot.edit_message_text(text="Отмена",
                                  chat_id=self.message_chat_id,
                                  message_id=self.call_message_id, reply_markup=self.avatar())
        save("hero")
        save("resource")

    def avatar(self):
        emoji = ["🥶", "😴", "😈", "👿", "👹", "👺", "💩", "👻", "💀", "☠", "👽", "🤖", "🎃", "😺", "😸"]
        keyboard = telebot.types.InlineKeyboardMarkup()
        i = 1
        tab = []
        for key in emoji:
            tab.append(telebot.types.InlineKeyboardButton(text=key, callback_data="shop_emoji_" + key))
            if i == 5 or i == 10 or i == 15:
                keyboard.row(*tab)
                tab = []
            i += 1
        keyboard.row(*tab)
        keyboard.row(telebot.types.InlineKeyboardButton(text="Назад", callback_data="shop_menu"))
        return keyboard

    def rename_heroes(self):
        print(self.text)
        if self.text[0:3] == "Для":
            bot.send_message(text=texting.text_rename_nik, chat_id=self.message_chat_id)
            users[str(self.message_chat_id)]["rename"] = 1
        elif users[str(self.message_chat_id)]["rename"] == 1:
            if self.text == "11":
                users[str(self.message_chat_id)]["rename"] = 0
                bot.send_message(text=texting.text_shop, chat_id=self.message_chat_id,
                                 reply_markup=self.keyboard_shop())

            #     pass
            else:
                users[str(self.message_chat_id)]["rename"] = 0
                if resource[str(self.message_chat_id)]["diamond"] - 5 <= 0:
                    bot.send_message(text=texting.text_shop_not_diamond, chat_id=self.message_chat_id,
                                     reply_markup=self.keyboard_shop())
                else:
                    resource[str(self.message_chat_id)]["diamond"] -= 5
                    hero[str(self.message_chat_id)]["nik_name"] = self.text

                    bot.send_message(text=texting.text_rename_nik_new % self.text, chat_id=self.message_chat_id,
                                     reply_markup=keyboard.keyboard_main_menu())
        save("hero")


class Training():

    def __init__(self, call="", message=""):
        global users
        try:
            self.message = message
            self.text = message.text
            self.message_chat_id = message.chat.id
        except:
            pass
        try:
            self.message = call.message
            self.call_data = call.data
            self.call_id = call.id
            self.call_message_id = call.message.message_id
            self.message_chat_id = call.message.chat.id
        except:
            pass
        self.user = warrior[str(self.message_chat_id)]

    def entry(self):
        if self.call_data.split("_")[0] == "training":
            self.old = self.call_data.split("_")[1]
            self.lvl = self.call_data.split("_")[2]
            self.status = self.call_data.split("_")[3]
            if self.status == "⛔":
                bot.answer_callback_query(callback_query_id=self.call_id,
                                          text=texting.text_training_uplvl % build[self.old]["name"])
            else:
                text = self.text_training() + texting.text_training_numwar
                print(text)
                try:
                    bot.edit_message_text(text=text, chat_id=self.message_chat_id,
                                          message_id=self.call_message_id,
                                          reply_markup=self.keyboard_training_one())
                except:
                    print("ERROR_1")

        elif self.call_data.split("_")[0] == "entry":
            try:
                self.old = self.call_data.split("_")[1]
                print(self.user[self.old])
            #                self.old = self.user[self.old]
            except:
                self.old = self.call_data.split("_")[1]
                self.user[self.old] = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
                save("warrior")
            text = self.text_training() + "\n Выберите уровень войск"
            try:
                print(text)
                bot.send_message(text=text, chat_id=self.message_chat_id, reply_markup=self.keyboard_training_lvl())
            except:
                print("ERROR_2")

        else:
            print("null")
        save("warrior")

    def training(self):
        print(self.call_data)
        self.old = self.call_data.split("_")[1]
        self.lvl = self.call_data.split("_")[3]
        self.number = int(self.call_data.split("_")[2])
        self.status = self.call_data.split("_")[4]
        if self.status == "✅":

            self.user[self.old][self.lvl] += int(self.number)

            stone = training[self.old][int(self.lvl)]["stone"] * self.number
            wood = training[self.old][int(self.lvl)]["wood"] * self.number
            iron = training[self.old][int(self.lvl)]["iron"] * self.number
            food = training[self.old][int(self.lvl)]["food"] * self.number
            resource[str(self.message_chat_id)]["stone"] -= stone
            resource[str(self.message_chat_id)]["wood"] -= wood
            resource[str(self.message_chat_id)]["iron"] -= iron
            resource[str(self.message_chat_id)]["food"] -= food
            save("users")
            save("resource")
            bot.answer_callback_query(callback_query_id=self.call_id, text="Обучение успешно")
        else:
            bot.answer_callback_query(callback_query_id=self.call_id, text="Не хватает ресурсов")
        try:
            bot.edit_message_text(text=self.text_training(), chat_id=self.message_chat_id,
                                  message_id=self.call_message_id,
                                  reply_markup=self.keyboard_training_one())
        except:
            print("ERROR_3")

    def keyboard_training_one(self):
        print(55555)
        keyboard = telebot.types.InlineKeyboardMarkup()
        number = [5, 10, 25, 50]
        for i in number:
            number_war = users[str(self.message_chat_id)]["lvlheroes"] * i

            stone = training[self.old][int(self.lvl)]["stone"] * number_war
            wood = training[self.old][int(self.lvl)]["wood"] * number_war
            iron = training[self.old][int(self.lvl)]["iron"] * number_war
            food = training[self.old][int(self.lvl)]["food"] * number_war
            cons = training[self.old][int(self.lvl)]["consumption"] * number_war
            stone_player = str(int(stone / 1000))
            wood_player = str(int(wood / 1000))
            iron_player = str(int(iron / 1000))
            food_player = str(int(food / 1000))
            consumption_player = str(cons)

            if resource[str(self.message_chat_id)]["stone"] < stone or \
                    resource[str(self.message_chat_id)]["wood"] < wood or \
                    resource[str(self.message_chat_id)]["iron"] < iron or \
                    resource[str(self.message_chat_id)]["food"] < food:
                status = "⛔"
            else:
                status = "✅"

            text = status + " " + str(number_war) + " " + training[self.old]["name"]
            text += ": ⚒ " + iron_player + "т. 🌲 " + wood_player + "т. ⛏" + stone_player + "т. 🌽" + food_player + "т. / -🌽 " + consumption_player + "/мин."

            keyboard.row(telebot.types.InlineKeyboardButton(text=text, callback_data="train_" + self.old + "_" + str(
                number_war) + "_" + str(self.lvl) + "_" + status))
        keyboard.row(telebot.types.InlineKeyboardButton(text="Назад", callback_data="entry_" + self.old))
        return keyboard

    def keyboard_training_lvl(self):
        keyboard = telebot.types.InlineKeyboardMarkup()
        number = [1, 2, 3, 4, 5]
        for i in number:
            stone_player = str(training[self.old][i]["stone"])
            wood_player = str(training[self.old][i]["wood"])
            iron_player = str(training[self.old][i]["iron"])
            food_player = str(training[self.old][i]["food"])
            if build[str(self.message_chat_id)][self.old] < i * 4:
                status = "⛔"
            else:
                status = "✅"
            consumption_player = str(training[self.old][i]["consumption"])
            text = status + training[self.old]["name"] + " " + str(
                i) + " лвл / ⚒ " + iron_player + " 🌲 " + wood_player + "⛏" + stone_player + "🌽" + food_player + " / -🌽 " + consumption_player

            keyboard.row(telebot.types.InlineKeyboardButton(text=text,
                                                            callback_data="training_" + self.old + "_" + str(
                                                                i) + "_" + status))
        keyboard.row(telebot.types.InlineKeyboardButton(text="Назад", callback_data="build_" + self.old))
        return keyboard

    def text_training(self):
        text = texting.text_training_castle
        for key, value in self.user[self.old].items():
            text += texting.text_training_castle_old \
                    % (training[self.old]["name"], key, value, training[self.old][int(key)]["consumption"] * value)
        return text


class Location():
    def __init__(self, call="", message=""):
        global users, tower
        try:
            self.message = message
            self.text = message.text
            self.message_chat_id = message.chat.id
        except:
            pass
        try:
            self.message = call.message
            self.call_data = call.data
            self.call_id = call.id
            self.call_message_id = call.message.message_id
            self.message_chat_id = call.message.chat.id
        except:
            pass
        try:
            self.user = warrior[str(self.message_chat_id)]
        except:
            pass

    def location(self):
        print(self.text)
        if "1" == "1":
            bot.send_message(chat_id=self.message_chat_id, text="Ждите обновление")
        elif self.time_tower() == "False":
            bot.send_message(chat_id=self.message_chat_id, text="Идет бой, ожидайте окончания")
        else:
            text_tower = self.tower_printer()
            if self.text == "🗼 Осада башни":
                bot.send_message(chat_id=self.message_chat_id,
                                 text=text_tower + "Осада башни. Бой проходит автоматически\n Выберите какие войска отправите на войну",
                                 reply_markup=self.keyboard_location())
            elif self.call_data == "tower_":
                bot.edit_message_text(chat_id=self.message_chat_id, message_id=self.call_message_id,
                                      text=text_tower + " Выберите какие войска отправите на войну",
                                      reply_markup=self.keyboard_location())
            elif self.call_data.split("_")[0] == "tower":
                self.old = self.call_data.split("_")[1]
                self.lvl = self.call_data.split("_")[2]
                if self.user[self.old][self.lvl] <= 0:
                    bot.answer_callback_query(callback_query_id=self.call_id, text="У вас нет этих войск")
                else:
                    bot.edit_message_text(chat_id=self.message_chat_id, message_id=self.call_message_id,
                                          text=text_tower + "Выберите количество воинов",
                                          reply_markup=self.keyboard_location_war())
            elif self.call_data.split("_")[0] == "towerold":
                self.old = self.call_data.split("_")[1]
                self.lvl = self.call_data.split("_")[2]
                self.number = int(self.call_data.split("_")[3])
                self.user[self.old][self.lvl] -= self.number
                self.tower_save()
                print("ccccc")
                #            print(self.tower_printer())
                bot.edit_message_text(chat_id=self.message_chat_id, message_id=self.call_message_id,
                                      text=self.tower_printer() + "Отправлено " + training[self.old][
                                          "name"] + " " + str(self.number), reply_markup=self.keyboard_location())

    def tower_printer(self):
        try:
            print(tower[str(self.message_chat_id)])
        except:
            text = "Нет войск\n "
            return text
        text = "В осаде: \n"
        for key, value in tower[str(self.message_chat_id)].items():
            for key_old, value_old in value.items():
                if value_old > 0:
                    text += training[key]["name"] + " " + str(key_old) + " лвл " + str(value_old) + "\n"
        return text

    def tower_save(self):
        print("qqq")
        try:
            tower[str(self.message_chat_id)]
        except:
            tower[str(self.message_chat_id)] = {}
        try:
            tower[str(self.message_chat_id)][self.old]
        except:
            tower[str(self.message_chat_id)][self.old] = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0}
        tower[str(self.message_chat_id)][self.old][self.lvl] += self.number
        save("users")
        save("tower")

    def keyboard_location_war(self):
        keyboard = telebot.types.InlineKeyboardMarkup()
        #        text_full = "У вас "+training[self.old]["name"] +" "+str(self.user[self.old][self.lvl])

        number_5 = str(int(self.user[self.old][self.lvl] / 5))
        number_3 = str(int(self.user[self.old][self.lvl] / 3))
        number_2 = str(int(self.user[self.old][self.lvl] / 2))
        number_1 = str(self.user[self.old][self.lvl])
        text_5 = training[self.old]["name"] + " " + number_5
        text_3 = training[self.old]["name"] + " " + number_3
        text_2 = training[self.old]["name"] + " " + number_2
        text_1 = training[self.old]["name"] + " " + number_1
        text5 = telebot.types.InlineKeyboardButton(text=text_5, callback_data="towerold_" + self.old + "_" + str(
            self.lvl) + "_" + str(number_5))
        text3 = telebot.types.InlineKeyboardButton(text=text_3, callback_data="towerold_" + self.old + "_" + str(
            self.lvl) + "_" + str(number_3))
        text2 = telebot.types.InlineKeyboardButton(text=text_2, callback_data="towerold_" + self.old + "_" + str(
            self.lvl) + "_" + str(number_2))
        text1 = telebot.types.InlineKeyboardButton(text=text_1, callback_data="towerold_" + self.old + "_" + str(
            self.lvl) + "_" + str(number_1))
        #        keyboard.row(text_full)
        keyboard.row(text5, text3, text2, text1)
        keyboard.row(telebot.types.InlineKeyboardButton(text="Назад", callback_data="tower_"))
        return keyboard

    def keyboard_location(self):
        keyboard = telebot.types.InlineKeyboardMarkup()
        i = 1
        while i <= 5:
            barr = self.user["barracks"][str(i)]
            shoot = self.user["shooting"][str(i)]
            stable = self.user["stable"][str(i)]
            if barr == 0 and shoot == 0 and stable == 0:
                i += 1
                continue
            else:
                barr_avatar = training["barracks"]["name"]
                shoot_avatar = training["shooting"]["name"]
                stable_avatar = training["stable"]["name"]
                barr_text = barr_avatar + " " + str(i) + " лвл " + str(barr)
                shoot_text = shoot_avatar + " " + str(i) + " лвл " + str(shoot)
                stable_text = stable_avatar + " " + str(i) + " лвл " + str(stable)
                barr = telebot.types.InlineKeyboardButton(text=barr_text, callback_data="tower_barracks_" + str(i))
                shoot = telebot.types.InlineKeyboardButton(text=shoot_text, callback_data="tower_shooting_" + str(i))
                stable = telebot.types.InlineKeyboardButton(text=stable_text, callback_data="tower_stable_" + str(i))
                i += 1
                keyboard.row(barr, shoot, stable)
        #        keyboard.row(telebot.types.InlineKeyboardButton(text="Назад", callback_data=""))
        return keyboard

    def keyboard_warrior(self):
        text = texting.text_location_all

        i = 1
        while i <= 5:
            text += "%s %s %s" % (
            training["barracks"]["name"], i, warrior[str(self.message_chat_id)]["barracks"][str(i)])
            text += "%s %s %s" % (
            training["shooting"]["name"], i, warrior[str(self.message_chat_id)]["shooting"][str(i)])
            text += "%s %s %s\n" % (training["stable"]["name"], i, warrior[str(self.message_chat_id)]["stable"][str(i)])

            #                text += training["barracks"]["name"] + " " + str(i) + " уровня: " + str(
            #                    warrior[str(self.message_chat_id)]["barracks"][str(i)]) + "     "
            #                text += training["shooting"]["name"] + " " + str(i) + " уровня: " + str(
            #                    warrior[str(self.message_chat_id)]["shooting"][str(i)]) + "       "
            #                text += training["stable"]["name"] + " " + str(i) + " уровня: " + str(
            #                    warrior[str(self.message_chat_id)]["stable"][str(i)]) + "\n"

            i += 1
        # text += "\n"
        save("users")
        bot.send_message(text=text, chat_id=self.message_chat_id, reply_markup=keyboard.keyboard_locat())

    def time_tower(self):
        time = datetime.utcnow()
        utctime = time.strftime("%H:%M")
        print(utctime)
        # 14:00 +7 - это 21:00

        if "06:00" <= utctime <= "06:10" or "10:00" <= utctime <= "10:10" or "12:00" <= utctime <= "12:10" or "16:00" <= utctime <= "16:10" or "20:00" <= utctime <= "20:10":
            return "False"
        else:
            return "True"

#
# def alert_tower():
#     print(1)
#     bot.send_message(chat_id="@HeroesLifeStat", text="Бой в башне начнется через час")
#     print(2)
#
#
# def alert_tower_start():
#     bot.send_message(chat_id="@HeroesLifeStat", text="Бой в башне начался")
#
#
# def open_start():
#     global tower
#     with open(PATH + "tmp/" + 'tower.json', 'rb') as f:
#         tower = json.load(f)
#
#
# def open_tower_old():
#     global tower_old
#     with open(PATH + "tmp/" + 'tower_old.json', 'rb') as f:
#         tower_old = json.load(f)
#
#
# def save_tower(tower):
#     with open(PATH + "tmp/" + 'tower.json', 'w', encoding="utf-16") as f:
#         json.dump(tower, f)
#
#
# def tower_print_battle():
#     global tower_old, tower
#     open_tower_old()
#     open_start()
#     if tower_old == {}:
#         print("Никто на башню не зареган")
#     else:
#         #        open_tower_old()
#         #        open_start()
#         text = ""
#         tower = {}
#         for k, v in tower_old.items():
#             l = len(v)
#             s = 0
#             num_gold_statis(k)
#             text += "\nИгрок " + users[str(k)]["nik_name"] + "\n"
#             for key, value in tower_old[k].items():
#                 t = 1
#                 for key_old, value_old in value.items():
#                     if value_old > 0:
#                         text += "Осталось " + training[key]["name"] + " " + str(key_old) + " лвл " + str(
#                             value_old) + "\n"
#                         try:
#                             tower[k][key][key_old] = value_old
#                         except:
#                             try:
#                                 tower[k][key] = {key_old: value_old}
#                             except:
#                                 tower[k] = {key: {key_old: value_old}}
#                     else:
#                         try:
#                             tower[k][key][key_old] = 0
#                         except:
#                             try:
#                                 tower[k][key] = {key_old: 0}
#                             except:
#                                 tower[k] = {key: {key_old: 0}}
#                         if t == 5:
#                             text += "Войск " + training[key]["name"] + " нет\n"
#                             s += 1
#                             if s == l:
#                                 tower.pop(k)
#                         t += 1
#         save_tower(tower)
#         bot.send_message(chat_id="@HeroesLifeStat", text=text)
#
#
# def num_gold_statis(key):
#     with open(PATH + "tmp/" + 'statistics.json', 'rb') as f:
#         statistics = json.load(f)
#         num = statistics[str(key)]["dead_one"]
#         r = random.randint(num, int(num * 1.5))
#         print("Вы заработали " + str(r) + " золота")
#         resource[str(key)]["gold"] += r
#         bot.send_message(chat_id=key, text="Вашим воинам удалось вынести " + str(r) + " золота")
#     save("resource")
#
#
# def tower_start_stop():
#     global tower
#     alert_tower()
#     time.sleep(10)
#     print("test1")
#     alert_tower_start()
#     print("test2")
#     time.sleep(60)
#     x = 1
#     while x <= 2:
#         reload(tower_battle)
#         tower_battle.Battletower().count_user()
#         time.sleep(60)
#         bot.send_message(chat_id="@HeroesLifeStat", text="Штурм башни \n//------ " + str(x) + " ------//")
#         tower_print_battle()
#         time.sleep(60)
#         x += 1
#     for k, v in tower.items():
#         for key, value in v.items():
#             print("%i Вернулось %i" % (str(k), str(key)))
#
#     tower = {}
#     save("tower")
#
#
# def timer_tow():
#     threading.Thread(target=tower_start_stop).start()
#
#
# def timer_tower():
#     #    schedule.every().hour.do(job)
#     schedule.every().day.at("11:47").do(timer_tow)
#     schedule.every().day.at("16:00").do(timer_tow)
#     schedule.every().day.at("18:00").do(timer_tow)
#     schedule.every().day.at("22:00").do(timer_tow)
#     #    schedule.every().day.at("15:52").do(timer_tower)
#     #    schedule.every().day.at("17:00").do(tower_start_stop)
#     #    schedule.every().day.at("19:00").do(tower_start_stop)
#     #    schedule.every().day.at("23:00").do(tower_start_stop)
#     #    schedule.every().day.at("15:57").do(pppp)
#
#     #    schedule.every().day.at("22:23").do(tower_print_battle)
#
#     #    schedule.every(10).minutes.do(job)
#     #    schedule.every().hour.do(job)
#     #    schedule.every().day.at("10:30").do(job)
#     #    schedule.every().monday.do(job)
#     #    schedule.every().wednesday.at("13:15").do(job)
#     while True:
#         time.sleep(10)
#         schedule.run_pending()
#
#
# def statisctick(message, data):
#     global users
#     from collections import OrderedDict
#     with open(PATH + "tmp/" + 'statistics.json', 'rb') as f:
#         statistics = json.load(f)
#     if data == "one":
#         statistics_one = (OrderedDict(sorted(statistics.items(), key=lambda k: -k[1]["dead_one"])))
#         i = 1
#         text = "Убийств в башне за последний бой\n"
#         for k, v in statistics_one.items():
#             text += str(i) + ": " + str(users[str(k)]["nik_name"]) + " / " + str(v["dead_one"]) + "\n"
#             i += 1
#         bot.send_message(chat_id=message.chat.id, text=text)
#     if data == "all":
#         statistics_all = (OrderedDict(sorted(statistics.items(), key=lambda k: -k[1]["dead_all"])))
#         i = 1
#         text = "Убийств в башне за всё время\n"
#         for k, v in statistics_all.items():
#             text += str(i) + ": " + str(users[str(k)]["nik_name"]) + " / " + str(v["dead_all"]) + "\n"
#             i += 1
#         bot.send_message(chat_id=message.chat.id, text=text)
#
#
# def test():
#     reload(texting)
#     for k, v in users.items():
#         try:
#             bot.send_message(chat_id=int(k), text=texting.text_mail)
#             print("Отправлено %s" % k)
#         except:
#             print("Не отправлено %s" % k)


#        if v["production"] != 0:
#            print(str(k) + " Добыл " + str(v["production"]))
# new Фарм еды
def sheduler_farm():
    for k, v in resource.items():
        farm_time_old = datetime.now().strftime("%Y:%m:%d:%H:%M:%S")
        a = farm_time_old.split(':')
        aa = datetime(int(a[0]), int(a[1]), int(a[2]), int(a[3]), int(a[4]), int(a[5]))
        farm_time = resource[str(k)]["farm_time"]
        b = farm_time.split(':')
        bb = datetime(int(b[0]), int(b[1]), int(b[2]), int(b[3]), int(b[4]), int(b[5]))
        ss = (aa - bb).seconds
        war_1 = warrior[str(k)]["shooting"]["1"] + warrior[str(k)]["barracks"]["1"] + warrior[str(k)]["stable"]["1"]
        war_2 = warrior[str(k)]["shooting"]["2"] + warrior[str(k)]["barracks"]["2"] + warrior[str(k)]["stable"]["2"]
        war_3 = warrior[str(k)]["shooting"]["3"] + warrior[str(k)]["barracks"]["3"] + warrior[str(k)]["stable"]["3"]
        min = int(ss * war_1 / 60 + ss * war_2 * 3 / 60 + ss * war_3 * 5 / 60)
        lvl_farm = build[str(k)]["farm"]
        num_farm = buildings["farm"][lvl_farm]["production"]
        num_farm = num_farm * ss
        lvl_storage = build[str(k)]["storage"]
        num_storage = int(buildings["storage"][lvl_storage]["capacity"])
        if resource[str(k)]["food"] + num_farm - min > num_storage:
            resource[str(k)]["food"] = num_storage
        elif resource[str(k)]["food"] + num_farm - min < 0:
            resource[str(k)]["food"] = 0
        else:
            resource[str(k)]["food"] += num_farm - min
        resource[str(k)]["farm_time"] = farm_time_old


def sheduler_save():
    save("all")
    print("Данные сохранены")


def farm_timer():
    print("Запуск фарма")
    schedule.every(1).minutes.do(sheduler_farm)
    schedule.every(1).minutes.do(sheduler_save)
    while True:
        schedule.run_pending()
        time.sleep(1)


def all():
    #    threading.Thread(target=timer_tower).start()
    threading.Thread(target=farm_timer).start()


all()


@bot.message_handler(commands=['start', 'shop', 'button'])
def start_message(message):
    try:
        if resource[str(message.chat.id)]["start"] == 1:
            if message.text == texting.button_mining_map:
                resource[str(message.chat.id)]["start"] = 0
            else:
                bot.send_message(text="Вы заняты добычей", chat_id=message.chat.id)
                return
    except:
        pass
    if message.chat.id == ADMIN:
        #        bot.send_message(text="Админское меню", chat_id=message.chat.id, reply_markup=texting.keyadmin())
        pass
    elif message.text.split(" ")[0] == "/start":
        start_user(message)
    elif message.text == "/button":
        resource[str(message.chat.id)]["start"] = 0
        save("resource")
        bot.send_message(text="Кнопки", chat_id=message.chat.id, reply_markup=keyboard.keyboard_main_menu())
    elif message.text == "/shop":
        bot.send_message(chat_id=message.chat.id, text="Для подробной информации о товаре, нажмите на него",
                         reply_markup=Shop(message=message).keyboard_shop())


@bot.message_handler(content_types=['successful_payment'])
def got_payment(message):
    global users
    buy.succefull_tranzzo(message)
    with open(PATH + "tmp/" + 'users.json', 'rb') as f:
        users = json.load(f)


@bot.message_handler(content_types=['text'])
def send_text(message):
    global menu, status_mining, barracks, allbattle, users

    try:
        mess_id = users[str(message.chat.id)]["mess_id"]
        users[str(message.chat.id)].pop("mess_id")
        bot.delete_message(message.chat.id, mess_id)
    except:
        print("ERROR_1")
        pass
    try:
        resource[str(message.chat.id)]["start"]
    except:
        resource[str(message.chat.id)]["start"] = 0

    try:
        if users[str(message.chat.id)]["rename"] == 1:
            Shop(message=message).rename_heroes()
    except:
        pass
    try:
        hero[str(message.chat.id)]["username"]
    except:
        hero[str(message.chat.id)]["username"] = message.from_user.username

    if resource[str(message.chat.id)]["start"] == 1:
            print("Копаю %s" % message.chat.id)
            print(message.text)
            if message.text == texting.button_mining_map:
                print("C,hjc")
                resource[str(message.chat.id)]["start"] = 0
            else:
                bot.send_message(text="Вы заняты добычей", chat_id=message.chat.id)
    elif message.text == '🗺 Карта' or message.text == texting.button_maps or message.text == texting.button_goto_two or message.text == "🗺 Вернуться на карту":
        users[str(message.chat.id)]["mess_id"] = message.message_id + 2
        bot.send_message(text="⏱ Вывод карты ⏱", chat_id=message.chat.id, reply_markup=keyboard.keyboardmap())
        Maps(message=message).goto()
    elif message.text == texting.button_castle:
        bot.send_message(text="🏘 Домой", chat_id=message.chat.id, reply_markup=keyboard.keyboard_main_menu())

# Копать
    elif message.text == texting.button_mining:
        resource[str(message.chat.id)]["start"] = 1
        save("resource")
        bot.send_message(text=texting.text_mining_start, chat_id=message.chat.id, reply_markup=keyboard.keyboard_map())
        mining(message)
#
    elif message.text == texting.button_mining_ataka:
        bot.send_message(text=texting.text_mining_ataka, chat_id=message.chat.id, reply_markup=keyboard.keyboard_map())
        mining_ataka(message)

    # Назад
    elif message.text == texting.button_back:
        bot.send_message(text=texting.button_back, chat_id=message.chat.id, reply_markup=keyboard.keyboard_main_menu())
    # Инфо герой
    elif message.text == texting.button_heroes:
        bot.send_message(text=info_heroes(message), chat_id=message.chat.id)
        bot.send_message(text=info_heroes(message, key="build"), chat_id=message.chat.id)
    elif message.text == texting.button_attack:
        users[str(message.chat.id)]["defence"] = 2
        users[str(message.chat.id)]["attaka"] = 2
        Fight(message=message).fight()
    elif message.text == texting.button_goto:
        bot.send_message(text="⏱ Вывод карты ⏱", chat_id=message.chat.id, reply_markup=keyboard.keyboardmap())
        Fight(message=message).fight()
        Maps(message=message).goto()
    # Cтроения
    elif message.text == texting.button_building:
        menu = "building"
        users[str(message.chat.id)]["mess_id"] = message.message_id + 1
        Build(message=message).building()
    elif message.text == texting.button_setting:
        menu = "info"
        bot.send_message(text=texting.texthelp, chat_id=message.chat.id, reply_markup=keyboard.keyboard_info())
    elif message.text == "Обратная связь":
        menu = "feedback"
        bot.send_message(
            text="Напишите ваши пожелания или найденные ошибки. \n Если нажали случайно, введите 'нет'",
            chat_id=message.chat.id, reply_markup=keyboard.keyboard_info())
        bot.register_next_step_handler(message, please)
    elif message.text == "Помочь проекту":
        menu = "feedback"
        bot.send_message(text=texting.textsell + "Выберите платежную систему", chat_id=message.chat.id,
                         reply_markup=keyboard.keyboard_buy())
    elif message.text == "Tranzzo":
        menu = "Tranzzo"
        buy.buy_amount(message)
    elif message.text == texting.button_start:
        start_user_name(message)
    elif message.text == "💬 Чат":
        bot.send_message(message.chat.id,
                         "Чат предназначен для общения, предложения идей и выявления багов @heroeslifeg")
    elif message.text == "Пригласить":
        bot.send_message(message.chat.id,
                         "Для приглашения друга отправть ему ссылку ниже. И получи 💎 за каждый взятый им уровень")
        bot.send_message(message.chat.id, "https://telegram.me/heroeslifebot?start=" + str(message.chat.id))
    elif message.text == texting.button_help:
        pass
#        help(message)
    elif message.text == texting.button_location:
        menu = "Location"
        Location(message=message).keyboard_warrior()
    elif message.text == "🗼 Осада башни":
        Location(message=message).location()
    elif message.text == texting.button_top:
        bot.send_message(chat_id=message.chat.id, text=texting.button_top, reply_markup=keyboard.keyboard_statisctick())
    # elif message.text == 'Общий рейтинг за башни':
    #     statisctick(message, "all")
    # elif message.text == 'Последний бой за башни':
    #     statisctick(message, "one")
    # elif message.text == "Время":
    #     test()
    elif message.text == texting.button_shop:
        bot.send_message(chat_id=message.chat.id, text="Для подробной информации о товаре, нажмите на него",
                         reply_markup=Shop(message=message).keyboard_shop())
    #            Shop(message=message).shop()
    elif message.text == "Создать карту":
        reload(map)
        map.new_maps()
        start_open()
    elif message.text == "/111":
        users[str(message.chat.id)]["experience_used"] += 5
        update_statistic(message, "experience")
    elif message.text == "222":
        map.statistics(message)
    else:
        pass
        pprint(message.text)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    #   buy_bot = Buy(message=call.message, call=call)
    if call.data.split("_")[0] == "battle":
        attak()
    elif call.data.split("_")[0] == "build":
        Build(message=call.message, call=call).build()

    elif call.data.split("_")[0] == "fight":
        Fight(message=call.message, call=call).fight()
    #        fight(message=call.message, call=call)
    #   elif call.data == "buy_qiwi":
    #       buy_bot.buy_check_qiwi()
    elif call.data == "null":
        bot.answer_callback_query(callback_query_id=call.id, text='Не активное поле')
#    elif call.data.split("_")[0] == "help":
#        help(message=call.message, call=call)
    #    elif call.data.split("_")[0] == "gotobattle":
    #        all_battle()
    elif call.data.split("_")[0] == "entry":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        Training(message=call.message, call=call).entry()
    elif call.data.split("_")[0] == "training":
        Training(message=call.message, call=call).entry()
    elif call.data.split("_")[0] == "train":
        Training(message=call.message, call=call).training()
    elif call.data.split("_")[0] == "tower" or call.data.split("_")[0] == "towerold":
        Location(message=call.message, call=call).location()
    elif call.data.split("_")[0] == "shop":
        Shop(message=call.message, call=call).shop()
    elif call.data.split("_")[0] == "field":
        Fight(message=call.message, call=call).field_goto()

    else:

        Maps(message=call.message, call=call).goto()


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
