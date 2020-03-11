import schedule
import time
from threading import Thread
import os
import json
import random

def find_location():
    return os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))).replace('\\', '/') + '/'
PATH = find_location()



null = 0
def save_battle():
    global allbattle
    with open(PATH + "tmp/" + 'allbattle.json', 'w', encoding="utf-16") as f:
        json.dump(allbattle, f)
    with open(PATH + "tmp/" + 'allbattle.json', 'rb') as f:
        allbattle = json.load(f)

def open_start():
    global allbattle
    with open(PATH + "tmp/" + 'allbattle.json', 'rb') as f:
        allbattle = json.load(f)

def job(data=""):
    global users, allbattle, lvl, kol, ran, max
    open_start()

    lvl = {}
    kol = 0
    ran = []
    i = 1
    for key, value in allbattle.items():
        null=0
        for key_old, value_old in value.items():
            if (key_old == "archer" and value_old > 0) or (key_old == "warrior" and value_old > 0) or (
                    key_old == "cavalry" and value_old > 0):
                pass
#                print("Воины есть")
            else:
                null += 1
#                print("нет воинов")
#        print(null)
        if null < 3:
            ran.append(i)
            lvl[i] = {"name":key, "data":value}
            i += 1

#    print(lvl)
    max = len(lvl)
    if max % 2 == 0:
        battle()
    else:
        lvl[i] = {"name": 123456789, "data": {"archer": 500, "warrior": 500, "cavalry": 500}}
        ran.append(i)
        battle()

  #  randi()
def koll(example, old):

    return allbattle[example][old]


def battle():
    global lvl, allbattle, kol, ran, max, null
#    print(ran)
    if len(ran) > 0:
        numberheroes = random.choice(ran)
        selectionher = rand()
        numberarmyher = lvl[numberheroes]["data"][selectionher]
        heroes = str(lvl[numberheroes]["name"])
        if numberarmyher >= 0:
            if lvl[numberheroes]["data"]["archer"] > 0:
                selectionher = "archer"
                numberarmyher = lvl[numberheroes]["data"]["archer"]
            elif lvl[numberheroes]["data"]["warrior"] > 0:
                selectionher = "warrior"
                numberarmyher = lvl[numberheroes]["data"]["warrior"]
            elif lvl[numberheroes]["data"]["cavalry"] > 0:
                selectionher = "cavalry"
                numberarmyher = lvl[numberheroes]["data"]["cavalry"]
            else:
                print("У игрока нет войск "+ str(numberheroes))
        lvl.pop(numberheroes)
        ran.remove(numberheroes)
    #    print(ran)
        numberenemy = random.choice(ran)
        selection = rand()
        numberarmy = lvl[numberenemy]["data"][selection]
        enemy = str(lvl[numberenemy]["name"])
        if numberarmy >= 0:
            if lvl[numberenemy]["data"]["archer"] > 0:
                selection = "archer"
                numberarmy = lvl[numberenemy]["data"]["archer"]
            elif lvl[numberenemy]["data"]["warrior"] > 0:
                selection = "warrior"
                numberarmy = lvl[numberenemy]["data"]["warrior"]
            elif lvl[numberenemy]["data"]["cavalry"] > 0:
                selection = "cavalry"
                numberarmy = lvl[numberenemy]["data"]["cavalry"]
            else:
                print("У игрока нет войск " + str(numberenemy))
        lvl.pop(numberenemy)
        ran.remove(numberenemy)
    #    print(ran)
        print("Нападает "+heroes+ " войска "+selectionher+" колличество "+str(numberarmyher))
        print("Защищает " + enemy + " войска " + selection + " колличество " + str(numberarmy))

        koef = numberarmyher / numberarmy
        print(koef)
        if koef > 1:
            print(">1")
            itog = int((numberarmyher - numberarmy) / koef)
            itog = numberarmyher - itog
            print("Вернулось " + str(itog))
            try:
                allbattle[heroes][selectionher] = itog
            except: pass
            try:
                allbattle[enemy][selection] = 0
            except: pass
        elif 1 > koef >= 0:
            print("1>koef>0")
            itog = int((numberarmy - numberarmyher)*koef)
            print(itog)
            print("Вы убили "+str(itog) + " вернулось 0")
            try:
                allbattle[heroes][selectionher] = 0
            except:pass
            try:
                allbattle[enemy][selection] -= itog
            except:pass
        elif koef == 1:
            itog = int(numberarmyher - numberarmy * 0.75)
            if heroes == '123456789':
                allbattle[enemy][selection] = itog
            elif enemy == '123456789':
                allbattle[heroes][selectionher] = itog
            else:
                allbattle[heroes][selectionher] = itog
                allbattle[enemy][selection] = itog
        save_battle()
        battle()
    else:
        print("Всё закончено")
    #    null += 1
    #        while null < 1:
    #            job(data="old")


def rand():
    r = random.randint(1, 3)
    if r == 1:
        key = "archer"
    elif r == 2:
        key = "warrior"
    elif r == 3:
        key = "cavalry"
    return key

def shed():
#    schedule.every(10).minutes.do(job)
    schedule.every().day.at("22:22").do(job)
    schedule.every().day.at("22:23").do(job)
    schedule.every().day.at("22:24").do(job)
    schedule.every().day.at("22:25").do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)

#start()
#job()
#Thread(target=shed(), args=()).start()


