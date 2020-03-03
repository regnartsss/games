import schedule
import time
from threading import Thread
import os
import json
import random

def find_location():
    return os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))).replace('\\', '/') + '/'
PATH = find_location()

with open(PATH + "tmp/" + 'users.json', 'rb') as f:
    users = json.load(f)
#print(users)
allbattle = {}
null = 0
def job(data=""):
    global users, allbattle, lvl, kol, ran, max

    lvl = {}
    kol = 0
    ran = []
    i = 1
#    print(users)
    if data == "old":
        for key, value in users.items():
            if value['allbattle'] == 1:
                print(str(key) + " Игрок участвует")
                lvl[i] = key
                ran.append(i)
#                allbattle[key] = {"archer": value["archer"], "warrior": value["warrior"], "cavalry": value["cavalry"]}
                #            allbattle[key]['battle'] = 0
                i += 1
            else:
                pass
    else:
        for key, value in users.items():
            if value['allbattle'] == 1:
                print(str(key) + " Игрок участвует")
                lvl[i] = key
                ran.append(i)
                allbattle[key] = {"archer": value["archer"], "warrior": value["warrior"], "cavalry": value["cavalry"]}
    #            allbattle[key]['battle'] = 0
                i += 1
            else:
                pass
            #print(str(key) + " Игрок не участвует")


    max = len(lvl)
    if max % 2 == 0:
        battle()
    else:
        ran.append(i)
        allbattle[123456789] = {"archer": 1, "warrior": 1, "cavalry": 1}
        allbattle[123456789]['battle'] = 0
        lvl[i] = 123456789
        battle()

  #  randi()
def koll(example, old):

    return allbattle[example][old]


def battle():
    global lvl, allbattle, kol, ran, max, null

    if kol != max and len(ran)>0:
            heroes = random.choice(ran)
            her = lvl[heroes]
 #       if allbattle[her]['battle'] == 0:
            keyher = rand()
            kolher = koll(her, keyher)
            if kolher == 0:
                kolher = koll(her, keyher)
#            allbattle[her]['battle'] = 1
            lvl.pop(heroes)
            ran.remove(heroes)
            print("Игрок " +str(her)+" Участвует " +keyher+ " в колличестве "+ str(allbattle[her][keyher]))

            enemy = random.choice(ran)
 #           if heroes != enemy:
            keyenem = rand()
            enem = lvl[enemy]
            kolenem = koll(enem, keyenem)
#            allbattle[enem]['battle'] = 1
            if kolenem == 0:
                kolenem = koll(enem, keyenem)
            lvl.pop(enemy)
            ran.remove(enemy)
            print("Враг " +str(enem)+" Участвует " + keyenem + " в колличестве " + str(allbattle[enem][keyenem]))
            koef = kolher / kolenem
            print(koef)
            if  koef > 1:
                    itog = int((kolher - kolenem)/koef)
                    itog = kolher - itog
                    print("Вернулось "+ str(itog))
                    allbattle[her][keyher] = itog
                    allbattle[enem][keyenem] = 0
            elif 1 > koef >= 0:
                    itog = int((kolenem - kolher)*koef)
                    print(itog)
        #            itog = kolenem - itog
                    print("Вы убили "+str(itog) + " вернулось 0")
                    allbattle[her][keyher] = 0
                    allbattle[enem][keyenem] = allbattle[enem][keyenem] - itog
            elif koef == 1:
                    itog = int(kolher - kolher*0.75)
                    print("Вернулось "+ str(itog))
                    allbattle[her][keyher] = itog
                    allbattle[enem][keyenem] = itog
            kol += 1
            battle()
      #  else:
      #      print("Игрок участвовал")
      #      battle()
    else:
        print("Всё закончено")
        null += 1
#        while null < 1:
#            job(data="old")
    print(allbattle)

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
    schedule.every().day.at("14:42").do(job)
    schedule.every().day.at("14:43").do(job)
    schedule.every().day.at("14:44").do(job)
    schedule.every().day.at("15:00").do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)

#start()
#job()
#Thread(target=shed(), args=()).start()


