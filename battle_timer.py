import schedule
import time
from threading import Thread
import os
import json
import random
from data import training


def find_location():
    return os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))).replace('\\', '/') + '/'


PATH = find_location()

null = 0


def save():
    global tower_end, tower
    with open(PATH + "tmp/" + 'tower_end.json', 'w', encoding="utf-16") as f:
        json.dump(tower_end, f)
    with open(PATH + "tmp/" + 'tower.json', 'w', encoding="utf-16") as f:
        json.dump(tower, f)
    with open(PATH + "tmp/" + 'statistics.json', 'w', encoding="utf-16") as f:
        json.dump(statistics, f)


def open_start():
    global tower, tower_old, statistics
    with open(PATH + "tmp/" + 'tower.json', 'rb') as f:
        tower = json.load(f)
    with open(PATH + "tmp/" + 'tower.json', 'rb') as f:
        tower_old = json.load(f)
    #    with open(PATH + "tmp/" + 'users.json', 'rb') as f:
    #            users = json.load(f)

    statistics = {}
    try:
        with open(PATH + "tmp/" + 'statistics.json', 'rb') as f:
            statistics = json.load(f)
    except:
        with open(PATH + "tmp/" + 'statistics.json', 'w', encoding="utf-16") as f:
            json.dump(statistics, f)
        with open(PATH + "tmp/" + 'statistics.json', 'rb') as f:
            statistics = json.load(f)


class BattleTower():
    def __init__(self):
        global tower, tower_end
        self.tower = tower

    def count_user(self):
        open_start()
        if self.tower == {}:
            print("Никто не зареган на башнюю")
        else:
            barracks = {}
            shooting = {}
            stable = {}
            k = 0.2
            for key, value in self.tower.items():
                for key_old, value_old in value.items():
                    if key_old == "barracks":
                        for key_b in value_old:
                            try:
                                barracks[key_b] += self.tower[key][key_old][key_b] - int(
                                    self.tower[key][key_old][key_b] * k)  # складываем значения
                            except KeyError:  # если ключа еще нет - создаем
                                barracks[key_b] = self.tower[key][key_old][key_b]
                    elif key_old == "shooting ":
                        for key_b in value_old:
                            try:
                                shooting[key_b] += self.tower[key][key_old][key_b] - int(
                                    self.tower[key][key_old][key_b] * k)  # складываем значения
                            except KeyError:  # если ключа еще нет - создаем
                                shooting[key_b] = self.tower[key][key_old][key_b]
                    if key_old == "stable":
                        for key_b in value_old:
                            try:
                                stable[key_b] += self.tower[key][key_old][key_b] - int(
                                    self.tower[key][key_old][key_b] * k)  # складываем значения
                            except KeyError:  # если ключа еще нет - создаем
                                stable[key_b] = self.tower[key][key_old][key_b]
            self.tow_all = {"barracks": barracks, "shooting ": shooting, "stable": stable}
            print(self.tow_all)
            self.tower_battle()
            self.tower_comparison()
#            tower = {}
            save()

    def tower_comparison(self):
        global tower_end
        tower_end = {}
        for key, value in tower_old.items():  # весь списо
            for key_old, value_old in value.items():  # какой то юзер
                for key_olding, value_olding in value[key_old].items():
                    if tower_old[key][key_old][key_olding] != self.tower[key][key_old][key_olding]:
                        num = tower_old[key][key_old][key_olding] - self.tower[key][key_old][key_olding]
                        #                        print(tower_old[key])
                        print("Убито " + key_old + " уровня " + str(key_olding) + " в количестве " + str(num))
                        try:
                            tower_end[key][key_old][key_olding] += int(num * 0.2)  # складываем значения
                        except KeyError:  # если ключа еще нет - создаем
                            tower_end[key] = self.tower[key]
                            tower_end[key][key_old][key_olding] += int(num * 0.2)
        save()

    def tower_battle(self):
        global statistics
        i = 1
        for k, v in self.tower.items():
            text = ""
            for key, value in self.tower[k].items():
                for key_old, value_old in value.items():
                    if value_old > 0:
                        text += training[key]["name"] + " " + str(key_old) + " лвл " + str(value_old) + "\n"
            print(str(k) + " \n" + text)

        while i < 3:
            for key, value in self.tower.items():  # весь списо
                try:
                    statistics[str(key)]["dead_one"] = 0
                except KeyError:
                    statistics[str(key)] = {"dead_all": 0, "dead_one": 0}

                for key_old, value_old in value.items():  # какой то юзер
                    for key_olding, value_olding in value[key_old].items():
                        if key_olding == str(i):
                            if value_olding != 0:
                                if key_old == "barracks":
                                    self.tower_battle_boy(key, key_old, value_olding, i)
                                elif key_old == "shooting ":
                                    self.tower_battle_boy(key, key_old, value_olding, i)
                                elif key_old == "stable":
                                    self.tower_battle_boy(key, key_old, value_olding, i)
                            else:
                                pass
                        else:
                            pass
            i += 1

        for k, v in self.tower.items():
            text = ""
            for key, value in self.tower[k].items():
                for key_old, value_old in value.items():
                    if value_old > 0:
                        text += training[key]["name"] + " " + str(key_old) + " лвл " + str(value_old) + "\n"
            print(str(k) + " \n" + text)

    def tower_battle_boy(self, key, key_old, value_olding, i):
        global statistics
        try:
            statistics[str(key)]

        except:
            statistics[str(key)] = {"dead_all": 0, "dead_one": 0}

        if self.tow_all == {'barracks': {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0},
                            'shooting ': {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0},
                            'stable': {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0}}:
            print("Ураа")
            return

        if i == 1:
            s = 1
        elif i == 2:
            s = 1.69
        r = random.randint(1, 3)
        if r == 1:
            if key_old == "shooting ":
                k = 1.25 * s
            elif key_old == "stable":
                k = 0.5 * s
            else:
                k = 1 * s
            #            print(key_old+" "+str(i)+" "  + str(value_olding)+" - barracks "+str(self.tow_all["barracks"][str(i)]))
            k = int(int(value_olding) * k)
            try:
                if self.tow_all["barracks"][str(i)] > 0:
                    if self.tow_all["barracks"][str(i)] - k < 0:
                        statistics[str(key)]["dead_all"] += self.tow_all["barracks"][str(i)]
                        statistics[str(key)]["dead_one"] += self.tow_all["barracks"][str(i)]
                        self.tower[key][key_old][str(i)] -= self.tow_all["barracks"][str(i)]
                        if self.tower[key][key_old][str(i)] < 0:
                            self.tower[key][key_old][str(i)] = 0

                        else:
                            self.tow_all["barracks"][str(i)] = 0
                            value_olding = self.tower[key][key_old][str(i)]
                            self.tower_battle_boy(key, key_old, value_olding, i)
                    else:
                        statistics[str(key)]["dead_all"] += k
                        statistics[str(key)]["dead_one"] += k
                        self.tow_all["barracks"][str(i)] -= k
                        self.tower[key][key_old][str(i)] = 0
                else:
                    self.tower_battle_boy(key, key_old, value_olding, i)
            except:
                print("В башне нет таких войск")
                pass

        elif r == 2:
            #            print("Лучники "+str(i)+" против "+ name)
            if key_old == "barracks":
                k = 0.5 * s
            elif key_old == "stable":
                k = 1.25 * s
            else:
                k = 1 * s
            #            print(key_old+" "+str(i)+" "  + str(value_olding)+" - shooting "+str(self.tow_all["shooting "][str(i)]))
            k = int(int(value_olding) * k)
            try:
                if self.tow_all["shooting "][str(i)] > 0:
                    if self.tow_all["shooting "][str(i)] - k < 0:
                        statistics[str(key)]["dead_all"] += self.tow_all["shooting "][str(i)]
                        statistics[str(key)]["dead_one"] += self.tow_all["shooting "][str(i)]
                        self.tower[key][key_old][str(i)] -= self.tow_all["shooting "][str(i)]
                        if self.tower[key][key_old][str(i)] < 0:
                            self.tower[key][key_old][str(i)] = 0
                        else:
                            self.tow_all["shooting "][str(i)] = 0
                            value_olding = self.tower[key][key_old][str(i)]
                            self.tower_battle_boy(key, key_old, value_olding, i)
                    else:
                        statistics[str(key)]["dead_all"] += k
                        statistics[str(key)]["dead_one"] += k
                        self.tow_all["shooting "][str(i)] -= k
                        self.tower[key][key_old][str(i)] = 0

                else:
                    self.tower_battle_boy(key, key_old, value_olding, i)
            except:
                print("В башне нет таких войск")
                pass
        elif r == 3:
            #            print("Всадники "+str(i)+" против "+name)
            if key_old == "barracks":
                k = 1.25 * s
            elif key_old == "shooting ":
                k = 0.5 * s
            else:
                k = 1 * s
            #            print(key_old+" "+str(i)+" "  + str(value_olding)+" - stable "+str(self.tow_all["stable"][str(i)]))
            k = int(int(value_olding) * k)
            try:
                if self.tow_all["stable"][str(i)] > 0:
                    if self.tow_all["stable"][str(i)] - k < 0:
                        statistics[str(key)]["dead_all"] += self.tow_all["stable"][str(i)]
                        statistics[str(key)]["dead_one"] += self.tow_all["stable"][str(i)]
                        self.tower[key][key_old][str(i)] -= self.tow_all["stable"][str(i)]
                        if self.tower[key][key_old][str(i)] < 0:
                            self.tower[key][key_old][str(i)] = 0
                        else:
                            # self.tower[key][key_old][str(i)] -= self.tow_all["barracks"][str(i)]
                            self.tow_all["stable"][str(i)] = 0
                            value_olding = self.tower[key][key_old][str(i)]
                            self.tower_battle_boy(key, key_old, value_olding, i)
                    else:
                        statistics[str(key)]["dead_all"] += k
                        statistics[str(key)]["dead_one"] += k
                        self.tow_all["stable"][str(i)] -= k
                        self.tower[key][key_old][str(i)] = 0

                else:
                    self.tower_battle_boy(key, key_old, value_olding, i)
            except:
                print("В башне нет таких войск")
                pass


def timer_tower():
    schedule.every().day.at("02:00").do(BattleTower().count_user())
    schedule.every().day.at("12:00").do(BattleTower().count_user())
    schedule.every().day.at("16:00").do(BattleTower().count_user())
    schedule.every().day.at("18:00").do(BattleTower().count_user())
    schedule.every().day.at("22:00").do(BattleTower().count_user())
