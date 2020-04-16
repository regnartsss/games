import schedule
import time
from threading import Thread
import os
import json
import random
from data import training
import logging
from config import bot
def find_location():
    return os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))).replace('\\', '/') + '/'


PATH = find_location()

null = 0
logging.basicConfig(filename='app_old.txt', format='%(name)s - %(levelname)s - [%(asctime)s] %(message)s',
                    level=logging.INFO)

def save_old(tower_old):
    with open(PATH + "tmp/" + 'tower_old.json', 'w', encoding="utf-16") as f:
        json.dump(tower_old, f)

def save(tower):
    with open(PATH + "tmp/" + 'tower.json', 'w', encoding="utf-16") as f:
        json.dump(tower, f)

def save_stat():
    with open(PATH + "tmp/" + 'statistics.json', 'w', encoding="utf-16") as f:
        json.dump(statistics, f)

#def save_battle():
#    global self.tower
#    with open(PATH + "tmp/" + 'self.tower.json', 'w', encoding="utf-16") as f:
#        json.dump(self.tower, f)
#    with open(PATH + "tmp/" + 'self.tower.json', 'rb') as f:
#        self.tower = json.load(f)

def open_start():
    global tower, statistics
    with open(PATH + "tmp/" + 'tower.json', 'rb') as f:
        tower = json.load(f)
    with open(PATH + "tmp/" + 'statistics.json', 'rb') as f:
                statistics = json.load(f)

def open_tower_old():
    global tower_old
    with open(PATH + "tmp/" + 'tower_old.json', 'rb') as f:
        tower_old = json.load(f)

#    with open(PATH + "tmp/" + 'self.tower.json', 'rb') as f:
#        self.tower_old = json.load(f)
#    with open(PATH + "tmp/" + 'users.json', 'rb') as f:
#            users = json.load(f)

#    statistics = {}
#    try:
    with open(PATH + "tmp/" + 'statistics.json', 'rb') as f:
            statistics = json.load(f)
#    except:
#        with open(PATH + "tmp/" + 'statistics.json', 'w', encoding="utf-16") as f:
#            json.dump(statistics, f)
#        with open(PATH + "tmp/" + 'statistics.json', 'rb') as f:
#            statistics = json.load(f)
def tower_comparison():
        global tower_old, tower
        open_tower_old()
        open_start()
        text = ""
        for k, v in tower_old.items():
                    text += "Игрок " +str(k)+"\n"
                    for key, value in tower_old[k].items():
                        t = 1
                        for key_old, value_old in value.items():
                            if value_old > 0:

                                text += "Осталось " +training[key]["name"]+" "+str(key_old)+" лвл "+str(value_old)+"\n"
                            else:
                                if t == 5:
                                    text += "Все "+training[key]["name"]+" погибли\n"
                                t += 1
        bot.send_message(chat_id="@HeroesLifeStat", text=text)

class Battletower():
    global tower, statistics
    def __init__(self):
        open_start()
        self.key = ""
        self.key_old = ""
        self.tower = tower

    def count_user(self):
        if self.tower == {}:
            print("Никто не зареган на башнюю")
            tower_old = {}
            save_old(tower_old)
        else:
            barracks = {}
            shooting = {}
            stable = {}
            k = 0.2
            logging.info('Суммируем воинов')


            for self.key, value in self.tower.items():
                try:
                    statistics[str(self.key)]["dead_one"] = 0
                except KeyError:
                    statistics[str(self.key)] = {"dead_all": 0, "dead_one": 0}
                for self.key_old, value_old in value.items():
                    if self.key_old == "barracks":
                        for key_b in value_old:
                            try:
                                barracks[key_b] += self.tower[self.key][self.key_old][key_b] - int(self.tower[self.key][self.key_old][key_b]*k)  # складываем значения
                            except KeyError:  # если ключа еще нет - создаем
                                barracks[key_b] = self.tower[self.key][self.key_old][key_b]
                    elif self.key_old == "shooting ":
                        for key_b in value_old:
                            try:
                                shooting[key_b] += self.tower[self.key][self.key_old][key_b] - int(self.tower[self.key][self.key_old][key_b]*k)  # складываем значения
                            except KeyError:  # если ключа еще нет - создаем
                                shooting[key_b] = self.tower[self.key][self.key_old][key_b]
                    if self.key_old == "stable":
                        for key_b in value_old:
                            try:
                                stable[key_b] += self.tower[self.key][self.key_old][key_b] - int(self.tower[self.key][self.key_old][key_b]*k)  # складываем значения
                            except KeyError:  # если ключа еще нет - создаем
                                stable[key_b] = self.tower[self.key][self.key_old][key_b]
            self.tow_all = {"barracks": barracks, "shooting ": shooting, "stable": stable}
            logging.info(self.tow_all)
            self.tower_all()
            if self.tow_all == {'barracks': {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0},
                                'shooting ': {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0},
                                'stable': {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0}}:
                pass
            save_old(self.tower)
            save(self.tower)
            save_stat()
    def tower_all(self):
        i = 1

        while i < 5:
            for self.key, value in self.tower.items():  # весь списо
                logging.info("Уровень " + str(i))
                logging.info("Пользователь "+ str(self.key))
                n = 1

                for self.key_old, value_old in value.items():  # какой то юзер
                    logging.info("Войска "+self.key_old)
                    for self.key_olding, self.value_olding in value[self.key_old].items():

                        if self.key_olding == str(i):
                            logging.info("Уровень воинов " + str(self.key_olding))
                            if self.value_olding != 0:
                                if self.key_old == "barracks":
#                                    print(str(self.key)+" "+self.key_old+" "+str(self.value_olding)+" "+str(i))
                                    self.tower_battle_boy(i)
                                elif self.key_old == "shooting ":
#                                    print(str(self.key)+" "+self.key_old+" "+str(self.value_olding)+" "+str(i))
                                    self.tower_battle_boy(i)
                                elif self.key_old == "stable":
#                                    print(str(self.key)+" "+self.key_old+" "+str(self.value_olding)+" "+str(i))
                                    self.tower_battle_boy(i)
                            else:
                                logging.info("Воинов уровня "+ str(self.key_olding)+ " нет")

                        else:
                            pass
            i += 1
  #      print(self.tower)
  #      save()
    def tower_battle_boy(self, i):
            r = random.randint(1, 3)
            logging.info("Рандом " + str(r))
            if r == 1:
                dat = "Воин"
                dat_old = "barracks"
                if self.key_old == "shooting ":
                    k = 1.25
                elif self.key_old == "stable":
                    k = 0.5
                else:
                    k = 1
                self.tower_battle_boy_all(k, i, dat, dat_old)
            elif r == 2:
                dat = "Лучник"
                dat_old = "shooting "
                if self.key_old == "barracks":
                    k = 0.5
                elif self.key_old == "stable":
                    k = 1.25
                else:
                    k = 1
                self.tower_battle_boy_all( k, i, dat, dat_old)
            elif r == 3:
                dat = "Всадник"
                dat_old = "stable "
                if self.key_old == "barracks":
                    k = 1.25
                elif self.key_old == "shooting ":
                    k = 0.5
                else:
                    k = 1
                self.tower_battle_boy_all( k, i, dat, dat_old)

    def tower_battle_boy_all(self,  k, i, dat, dat_old):
        k = int(int(self.value_olding) * k)
        try:
            if self.tow_all[dat_old][str(i)] > 0:
                if self.tow_all[dat_old][str(i)] - k <= 0:
                    print(self.tow_all[dat_old][str(i)])
                    statistics[str(self.key)]["dead_all"] += self.tow_all[dat_old][str(i)]*i
                    statistics[str(self.key)]["dead_one"] += self.tow_all[dat_old][str(i)]*i

                    if self.tower[self.key][self.key_old][str(i)] - self.tow_all[dat_old][str(i)] <= 0:
                        self.tower[self.key][self.key_old][str(i)] = 0

                    else:
                        self.tower[self.key][self.key_old][str(i)] -= self.tow_all[dat_old][str(i)]
                        self.tow_all[dat_old][str(i)] = 0
                        self.value_olding = self.tower[self.key][self.key_old][str(i)]
                else:
                    print(k)
                    statistics[str(self.key)]["dead_all"] += k*i
                    statistics[str(self.key)]["dead_one"] += k*i
                    self.tow_all[dat_old][str(i)] -= k
                    self.tower[self.key][self.key_old][str(i)] = 0
            else:
                pass
        except:
            pass
