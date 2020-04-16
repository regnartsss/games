import os
import json
import random
import config

def find_location():
    return os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))).replace('\\', '/') + '/'


PATH = find_location()



def open_users():
    global users
    with open(PATH + "tmp/" + 'users.json', 'rb') as f:
        users = json.load(f)

def open_maps():
    global maps
    with open(PATH + "tmp/" + 'maps.json', 'rb') as f:
        maps = json.load(f)

def save_maps():
    with open(PATH + "tmp/" + 'maps.json', 'w', encoding="utf-16") as f:
        json.dump(maps, f)
    with open(PATH + "tmp/" + 'users.json', 'w', encoding="utf-16") as f:
        json.dump(users, f)


def new_maps():  # Прочитать файл
    global maps
    open_users()
    pole, n, maps = 100, 0, {}
    all_cell = pole * pole
    for key, value in users.items():
        r = random.randint(1, pole * pole)
        try:
            maps[str(r)]["id"]
        except KeyError:
            maps[str(r)] = {"id": str(key)}
        users[str(key)]["cell"] = r

    while n < all_cell:
        n += 1
        try:
            maps[str(n)]["id"]
        except KeyError:
            maps[str(n)] = resource_start(n)
#            resource_start(n)
    save_maps()


def resource_start(n):
    r = random.randint(1, 20)
    if r == 1:
        return resource_res(old_res="wood", n=n)
    elif r == 2:
        return resource_res(old_res="stone", n=n)
    elif r == 3:
        return resource_res(old_res="iron", n=n)
    elif r == 4:
        return {"resource": "enemy"}
    elif r >= 5:
        return {"resource": "null"}


def resource_res(old_res, n):
    r = random.randint(1, 15)
    if r == 1 or r == 2 or r == 3 or r == 4 or r == 5:
        return {"resource": old_res, "lvl": 1, "number": random.randint(3000, 5000)}
    elif r == 6 or r == 7 or r == 8 or r == 9:
        return {"resource": old_res, "lvl": 2, "number": random.randint(5001, 15000)}
    elif r == 10 or r == 11 or r == 12:
        return {"resource": old_res, "lvl": 3, "number": random.randint(15001, 30000)}
    elif r == 13 or r == 14:
        return {"resource": old_res, "lvl": 4, "number": random.randint(30001, 60000)}
    elif r == 15:
        return {"resource": old_res, "lvl": 5, "number": random.randint(60001, 120000)}


def statistics(message):
    open_maps()
    w, s, i, u, n, w1, w2, w3, w4, w5, s1, s2, s3, s4, s5, i1, i2, i3, i4, i5, e = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    for key, value in maps.items():
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
    text = "дерево " + str(w) + " \nlvl 1: " + str(w1) + " \nlvl 2: " + str(w2) + " \nlvl 3: " + str(
        w3) + " \nlvl 4: " + str(w4) + " \nlvl 5: " + str(w5) \
           + "\nжелезо " + str(i) + " \nlvl 1: " + str(i1) + " \nlvl 2: " + str(i2) + " \nlvl 3: " + str(
        i3) + " \nlvl 4: " + str(i4) + " \nlvl 5: " + str(i5) \
           + "\nкамень " + str(s) + " \nlvl 1: " + str(s1) + " \nlvl 2: " + str(s2) + " \nlvl 3: " + str(
        s3) + " \nlvl 4: " + str(s4) + " \nlvl 5: " + str(s5) \
           + "\nигроков " + str(u) + "\nПустых ячеек " + str(n) + "\nВрагов " + str(e)
    config.bot.send_message(chat_id=message.chat.id, text=text)
