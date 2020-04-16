import os
import json
import random

def find_location():
    return os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))).replace('\\', '/') + '/'


PATH = find_location()

def farm_open():
    global users, warrior, build, weapons, hero
    with open(PATH + "tmp/" + 'users.json', 'rb') as f:
        users = json.load(f)
    warrior = {}
    build = {}
    weapons = {}
    hero = {}

def farm_save():
    with open(PATH + "tmp/" + 'users.json', 'w', encoding="utf-16") as f:
        json.dump(users, f)
    with open(PATH + "tmp/" + 'warrior.json', 'w', encoding="utf-16") as f:
        json.dump(warrior, f)
    with open(PATH + "tmp/" + 'build.json', 'w', encoding="utf-16") as f:
            json.dump(build, f)
    with open(PATH + "tmp/" + 'weapons.json', 'w', encoding="utf-16") as f:
                json.dump(weapons, f)
    with open(PATH + "tmp/" + 'hero.json', 'w', encoding="utf-16") as f:
                json.dump(hero, f)

def rename_nik():
    for k, v in users.items():
        users[str(k)]["nik_name"] = "player_%i" % (random.randint(1, 9999999))
        try:
            warrior[str(k)] = {'barracks': users[str(k)]['barracks'],
                           'stable' :users[str(k)]['stable'],
                           'shooting':users[str(k)]['shooting ']}
        except:
            warrior[str(k)] = {"shooting": {1: 0, 2: 0, 3: 0, 4: 0, 5: 0},
                                       "barracks": {1: 0, 2: 0, 3: 0, 4: 0, 5: 0},
                                       "stable": {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}}
        try:
            build[str(k)] = users[str(k)]['building']
        except:
            build[str(k)] = {"wall": 0, "castle": 1, "storage": 0, "farm": 0, "barracks": 0,
                     "shooting": 0, "stable": 0}
        weapons[str(k)] = {"arm":0}
        try:
            hero[k] = {"date":users[str(k)]['date'],
                     "first_name":users[str(k)]['username']}
        except:
            pass
        try:
            hero[k] = {"avatar": users[str(k)]['avatar'],
                         "nik_name": users[str(k)]['nik_name'],
                         "ref": users[str(k)]['ref'],
                         "free_name":users[str(k)]['free_name']
                         }
        except:
            pass
        try:
            users[str(k)].pop("avatar")

            users[str(k)].pop("ref")
            users[str(k)].pop("free_name")
        except:
            pass
        try:
            users[str(k)].pop("nik_name")
        except:
            pass

        try:
            users[str(k)].pop("id")
            users[str(k)].pop("date")
            users[str(k)].pop("username")

        except:
            pass
        try:
            users[str(k)].pop("archer")
        except:
            pass
        try:
            users[str(k)].pop("warrior")
        except:
            pass
        try:
            users[str(k)].pop("cavalry")
        except:
            pass
        try:
            users[str(k)].pop("health")
        except:
            pass
        try:
            users[str(k)].pop("hit")
        except:
            pass
        try:
            users[str(k)].pop("experience")
        except:
            pass
        try:
            users[str(k)].pop("enemy_exr")
        except:
            pass
        try:
            users[str(k)].pop("enemy_lvl")
        except:
            pass
        try:
            users[str(k)].pop("enemy_cell")
        except:
            pass
        try:
            users[str(k)].pop("enemy_hit")
        except:
            pass
        try:
            users[str(k)].pop("enemy_hit")
        except:
            pass
        try:
            users[str(k)].pop("enemy_health")

        except:
            pass
        try:
            users[str(k)].pop("enemy_dodge")

        except:
            pass
        try:
            users[str(k)].pop("energy")
        except:
            pass
        try:
            users[str(k)].pop("stable")
        except:
            pass
        try:
            users[str(k)].pop("shooting ")
        except:
            pass
        try:
            users[str(k)].pop("barracks")
        except:
            pass
        try:
            users[str(k)].pop("allbattle")
        except:
            pass
        try:
            users[str(k)].pop("building")
        except:
            pass
        try:
            users[str(k)].pop("weapons")
        except:
            pass
        print(users[str(k)])
farm_open()
rename_nik()
farm_save()