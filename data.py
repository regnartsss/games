start_text = "Добро пожаловать в фантазийную игру. Управляя героем, находи клады и выполняй миссии, чтобы заработать денег. Увеличивай свою армию. Пошаговое ведение боя.\n Движение по карте осуществляется с помощью кнопочек ➡️⬇️⬆️⬅️. На карте распологаются различные ресурсы: ⛏камень, 🌲дерево, 🔨 еда и монстры, которых вы можете атаковать"
start_text_mining = "Вы начали добычу ресурса.\n Это может занять некоторое время ⏱.\n После окончания добычи, Вам придет уведомление ⏰. \n Для ОТМЕНЫ, нажмите Вернуться на карту 🗺"
lvlrudnic = {1: 3, 2: 6, 3: 12, 4: 24, 5: 48}
lvlexperience = {1: 15, 2: 25, 3: 50, 4: 100, 5: 200, 6: 400, 7: 800, 8: 1600}
lvlstep = {1: 5, 2: 6, 3: 7, 4: 8, 5: 9, 6: 10, 7: 11, 8: 12, 9: 13, 10: 14}
lvlwolk = {1: 10, 2: 30, 3: 60, 4: 100, 5: 200, 6: 400, 7: 500, 8: 1000}
lvlenergy = {1: 5, 2: 7, 3: 9, 4: 11, 5: 12, 6: 13, 7: 14, 8: 15, 9: 16, 10: 17}
lvlhealth = {1: 50, 2: 100, 3: 150, 4: 200, 5: 250, 6: 300, 7: 350, 8: 400}
lvlhit = {1: 5, 2: 10, 3: 20, 4: 30, 5: 40, 6: 140, 7: 150, 8: 170}
def textattaka(lvl):
    text = "Вы напали на странное существо " + lvl + " 🏅  уровня. Что будете делать:\n ⚔️Атаковать или 🏃‍♂️Отступить?"
    return text
archer = {"1": {"wood": 156, "stone": 124, "food": 124}}
texthelp = "Приветствую Вас с моем боте.\n В планах: \n Добавить строительство города \n Добавить поле боя для существ \n Добавить атаку других игроков"
textsell = "Покупкой алмазов считаются добровольные пожертвования в пользу сервера, направленные на покрытие расходов проекта на различные нужды: оплата хостинга, серверов, доменных имен, рекламных услуг и так далее. Пожертвования не подлежат вовзрату ни при каких обстоятельствах.\n"
textbuy = "Сколько вы хотите купить? (1 💎 = 10 руб)"
text_help = "Раздел помощи. Если у вас есть вопросы, предложения по игре - сообщите в раздел '⚙ Настройки -> Обратная связь. "
#storage = {"1": {"wood", "stone", "food"}}
def text_mining(res, lvl, kol, timer):
    if res == "wood":
        text = "🌲 Шахта с деревом \n🎖 Уровень шахты " + str(lvl) + "\n🌑 Количество ресурса: " + str(kol)
    elif res == "iron":
        text = "🔨 Шахта с железом \n🎖 Уровень шахты " + str(lvl) + "\n🌑 Количество ресурса: " + str(kol)
    elif res == "stone":
        text = "⛏ Шахта с камнем \n🎖 Уровень шахты " + str(lvl) + "\n🌑 Количество ресурса: " + str(kol)
    text = text + "\n⚙️ Добыча " + str(lvlrudnic[lvl]) + "шт/cек \n⏱ Собрать ресурс за " + str(timer)

    return (text)
weapons = {"1": {"name": "arm_1", "random": 1},
           "2": {"name": "arm_2", "random": 1},
           "3": {"name": "arm_3", "random": 1},
           "4": {"name": "arm_4", "random": 1}}
weapons_data = {"arm_1": {"name": "Меч новичка", "hit": "30"}}

fight_text_all = {"null":" ", "heroes_head": "👨",
              "heroes_handleft": "🤛",
              "heroes_handright": "🤜",
            "heroes_breast":"👕",
                  "heroes_legs": "👖",
                "heroes_foot":"👞",

              "enemy_head": "👨",
              "enemy_handleft": "🤛",
              "enemy_handright": "🤜",
                  "enemy_breast": "👕",
                  "enemy_legs": "👖",
                  "enemy_foot": "👞",
                  }
fight_trans = {"heroes_head": " Голова героя",
         "heroes_handleft": "Левая рука героя",
              "heroes_handright": "Правая рука героя",
            "heroes_breast":"Тело героя",
                  "heroes_legs": "Ноги героя",
                "heroes_foot":"Обувь героя",

              "enemy_head": "Голова врага",
              "enemy_handleft": "Левая рука врага",
              "enemy_handright": "Правая рука врага",
                  "enemy_breast": "Тело врага",
                  "enemy_legs": "Ноги врага",
                  "enemy_foot": "Обувь врага",
                  }

data = {"1": 1}

def static_buildings(text, lvl):
    wood = buildings[text][lvl]["wood"]
    stone = buildings[text][lvl]["stone"]
    iron = buildings[text][lvl]["iron"]
    food = buildings[text][lvl]["food"]
    return wood, stone, iron, food


buildings = {"wall": {"name": "🧱 Стена 🧱", 1: {"wood": 700, "stone": 400, "iron": 600, "food": 200, "diamond": 1},
                      2: {"wood": 900, "stone": 500, "iron": 750, "food": 250, "diamond": 4},
                      3: {"wood": 1150, "stone": 650, "iron": 1000, "food": 350, "diamond": 9}},
             "castle": {"name": "🏤 Замок", 1: {"wood": 700, "stone": 400, "iron": 600, "food": 200, "diamond": 1},
                        2: {"wood": 900, "stone": 500, "iron": 750, "food": 250, "diamond": 4},
                        3: {"wood": 1150, "stone": 650, "iron": 1000, "food": 350, "diamond": 9},
                        4: {"wood": 1450, "stone": 850, "iron": 1250, "food": 400, "diamond": 16},
                        5: {"wood": 1900, "stone": 1050, "iron": 1600, "food": 550, "diamond": 25},
                        6: {"wood": 2400, "stone": 1350, "iron": 2050, "food": 700, "diamond": 36},
                        7: {"wood": 3100, "stone": 1750, "iron": 2650, "food": 900, "diamond": 49},
                        8: {"wood": 3950, "stone": 2250, "iron": 3400, "food": 1150, "diamond": 64},
                        9: {"wood": 5050, "stone": 2900, "iron": 4300, "food": 1450, "diamond": 81},
                        10: {"wood": 6450, "stone": 3700, "iron": 5550, "food": 1850, "diamond": 100},
                        11: {"wood": 8250, "stone": 4700, "iron": 7100, "food": 2350, "diamond": 121},
                        12: {"wood": 10600, "stone": 6050, "iron": 9050, "food": 3000, "diamond": 144},
                        13: {"wood": 13550, "stone": 7750, "iron": 11600, "food": 3850, "diamond": 169},
                        14: {"wood": 17350, "stone": 9900, "iron": 14850, "food": 4950, "diamond": 196},
                        15: {"wood": 22200, "stone": 12700, "iron": 19000, "food": 6350, "diamond": 225},
                        16: {"wood": 28400, "stone": 16250, "iron": 24350, "food": 8100, "diamond": 256},
                        17: {"wood": 36350, "stone": 20750, "iron": 31150, "food": 10400, "diamond": 289},
                        18: {"wood": 46500, "stone": 26600, "iron": 39900, "food": 13300, "diamond": 324},
                        19: {"wood": 59550, "stone": 34050, "iron": 51050, "food": 17000, "diamond": 361},
                        20: {"wood": 76200, "stone": 43550, "iron": 65350, "food": 21800, "diamond": 400}},
             "storage": {"name": "🏚 Склад", 0:{"wood":0, "stone":0, "iron":0, "food":0, "diamond":0, "capacity":5000},
                         1:{"wood":1300, "stone":1600, "iron":900, "food":400, "diamond":1, "capacity":12000},
2:{"wood":1650, "stone":2050, "iron":1150, "food":500, "diamond":4, "capacity":17000},
3:{"wood":2150, "stone":2600, "iron":1450, "food":650, "diamond":9, "capacity":23000},
4:{"wood":2750, "stone":3350, "iron":1900, "food":850, "diamond":16, "capacity":31000},
5:{"wood":3500, "stone":4300, "iron":2400, "food":1050, "diamond":25, "capacity":40000},
6:{"wood":4450, "stone":5500, "iron":3100, "food":1350, "diamond":36, "capacity":50000},
7:{"wood":5700, "stone":7050, "iron":3950, "food":1750, "diamond":49, "capacity":63000},
8:{"wood":7300, "stone":9000, "iron":5050, "food":2250, "diamond":64, "capacity":78000},
9:{"wood":9350, "stone":11550, "iron":6500, "food":2900, "diamond":81, "capacity":96000},
10:{"wood":12000, "stone":14750, "iron":8300, "food":3700, "diamond":100, "capacity":118000},
11:{"wood":15350, "stone":18900, "iron":10650, "food":4700, "diamond":121, "capacity":144000},
12:{"wood":19650, "stone":24200, "iron":13600, "food":6050, "diamond":144, "capacity":176000},
13:{"wood":25150, "stone":30950, "iron":17400, "food":7750, "diamond":169, "capacity":214000},
14:{"wood":32200, "stone":39600, "iron":22300, "food":9900, "diamond":196, "capacity":259000},
15:{"wood":41200, "stone":50700, "iron":28500, "food":12700, "diamond":225, "capacity":313000},
16:{"wood":52750, "stone":64900, "iron":36500, "food":16250, "diamond":256, "capacity":379000},
17:{"wood":67500, "stone":83100, "iron":46750, "food":20750, "diamond":289, "capacity":457000},
18:{"wood":86400, "stone":106350, "iron":59800, "food":26600, "diamond":324, "capacity":551000},
19:{"wood":110600, "stone":136100, "iron":76550, "food":34050, "diamond":361, "capacity":664000},
20:{"wood":141550, "stone":174200, "iron":98000, "food":43550, "diamond":400, "capacity":800000}},
             "farm": {"name": "🌾 Ферма", 0:{"wood":0, "stone":0, "iron":0, "food":0, "diamond":0, "production":3},
1:{"wood":700, "stone":900, "iron":700, "food":200, "diamond":1, "production":7},
2:{"wood":1150, "stone":1500, "iron":1150, "food":350, "diamond":4, "production":13},
3:{"wood":1950, "stone":2500, "iron":1950, "food":550, "diamond":9, "production":21},
4:{"wood":3250, "stone":4200, "iron":3250, "food":950, "diamond":16, "production":31},
5:{"wood":5450, "stone":7000, "iron":5450, "food":1550, "diamond":25, "production":46},
6:{"wood":9100, "stone":11700, "iron":9100, "food":2600, "diamond":36, "production":70},
7:{"wood":15200, "stone":19500, "iron":15200, "food":4350, "diamond":49, "production":98},
8:{"wood":25350, "stone":32600, "iron":25350, "food":7250, "diamond":64, "production":140},
9:{"wood":42350, "stone":54450, "iron":42350, "food":12100, "diamond":81, "production":203},
10:{"wood":70700, "stone":90950, "iron":70700, "food":20200, "diamond":100, "production":280},
11:{"wood":118100, "stone":151850, "iron":118100, "food":33750, "diamond":121, "production":392},
12:{"wood":197250, "stone":253600, "iron":197250, "food":56350, "diamond":144, "production":525},
13:{"wood":329400, "stone":423500, "iron":329400, "food":94100, "diamond":169, "production":693},
14:{"wood":550050, "stone":707200, "iron":550050, "food":157150, "diamond":196, "production":889},
15:{"wood":918600, "stone":1181050, "iron":918600, "food":262450, "diamond":225, "production":1120},
16:{"wood":1534050, "stone":1972400, "iron":1534050, "food":438300, "diamond":256, "production":1400},
17:{"wood":2561900, "stone":3293850, "iron":2561900, "food":731950, "diamond":289, "production":1820},
18:{"wood":4278350, "stone":5500750, "iron":4278350, "food":1222400, "diamond":324, "production":2240},
19:{"wood":7144850, "stone":9186250, "iron":7144850, "food":2041400, "diamond":361, "production":2800},
20:{"wood":11931950, "stone":15341050, "iron":11931950, "food":3409150, "diamond":400, "production":3430}},
             "barracks": {"name": "⚔️Казарма", 1:{"wood":2100, "stone":1400, "iron":2600, "food":1200, "diamond":1},
2:{"wood":2700, "stone":1800, "iron":3350, "food":1550, "diamond":4},
3:{"wood":3450, "stone":2300, "iron":4250, "food":1950, "diamond":9},
4:{"wood":4400, "stone":2950, "iron":5450, "food":2500, "diamond":16},
5:{"wood":5650, "stone":3750, "iron":7000, "food":3200, "diamond":25},
6:{"wood":7200, "stone":4800, "iron":8950, "food":4100, "diamond":36},
7:{"wood":9250, "stone":6150, "iron":11450, "food":5300, "diamond":49},
8:{"wood":11800, "stone":7900, "iron":14650, "food":6750, "diamond":64},
9:{"wood":15150, "stone":10100, "iron":18750, "food":8650, "diamond":81},
10:{"wood":19350, "stone":12900, "iron":24000, "food":11050, "diamond":100},
11:{"wood":24800, "stone":16550, "iron":30700, "food":14150, "diamond":121},
12:{"wood":31750, "stone":21150, "iron":39300, "food":18150, "diamond":144},
13:{"wood":40600, "stone":27100, "iron":50300, "food":23200, "diamond":169},
14:{"wood":52000, "stone":34650, "iron":64350, "food":29700, "diamond":196},
15:{"wood":66550, "stone":44350, "iron":82400, "food":38050, "diamond":225},
16:{"wood":85200, "stone":56800, "iron":105450, "food":48700, "diamond":256},
17:{"wood":109050, "stone":72700, "iron":135000, "food":62300, "diamond":289},
18:{"wood":139550, "stone":93050, "iron":172800, "food":79750, "diamond":324},
19:{"wood":178650, "stone":119100, "iron":221200, "food":102100, "diamond":361},
20:{"wood":228650, "stone":152450, "iron":283100, "food":130650, "diamond":400}},
             "shooting ": {"name": "🏹 Стрельба",
                           1: {"wood": 2100, "stone": 1400, "iron": 2600, "food": 1200, "diamond": 1},
                           2: {"wood": 2700, "stone": 1800, "iron": 3350, "food": 1550, "diamond": 4},
                           3: {"wood": 3450, "stone": 2300, "iron": 4250, "food": 1950, "diamond": 9},
                           4: {"wood": 4400, "stone": 2950, "iron": 5450, "food": 2500, "diamond": 16},
                           5: {"wood": 5650, "stone": 3750, "iron": 7000, "food": 3200, "diamond": 25},
                           6: {"wood": 7200, "stone": 4800, "iron": 8950, "food": 4100, "diamond": 36},
                           7: {"wood": 9250, "stone": 6150, "iron": 11450, "food": 5300, "diamond": 49},
                           8: {"wood": 11800, "stone": 7900, "iron": 14650, "food": 6750, "diamond": 64},
                           9: {"wood": 15150, "stone": 10100, "iron": 18750, "food": 8650, "diamond": 81},
                           10: {"wood": 19350, "stone": 12900, "iron": 24000, "food": 11050, "diamond": 100},
                           11: {"wood": 24800, "stone": 16550, "iron": 30700, "food": 14150, "diamond": 121},
                           12: {"wood": 31750, "stone": 21150, "iron": 39300, "food": 18150, "diamond": 144},
                           13: {"wood": 40600, "stone": 27100, "iron": 50300, "food": 23200, "diamond": 169},
                           14: {"wood": 52000, "stone": 34650, "iron": 64350, "food": 29700, "diamond": 196},
                           15: {"wood": 66550, "stone": 44350, "iron": 82400, "food": 38050, "diamond": 225},
                           16: {"wood": 85200, "stone": 56800, "iron": 105450, "food": 48700, "diamond": 256},
                           17: {"wood": 109050, "stone": 72700, "iron": 135000, "food": 62300, "diamond": 289},
                           18: {"wood": 139550, "stone": 93050, "iron": 172800, "food": 79750, "diamond": 324},
                           19: {"wood": 178650, "stone": 119100, "iron": 221200, "food": 102100, "diamond": 361},
                           20: {"wood": 228650, "stone": 152450, "iron": 283100, "food": 130650, "diamond": 400}},
             "stable": {"name": "🐴 Конюшня", 1:{"wood":2600, "stone":1400, "iron":2200, "food":1000, "diamond":1},
2:{"wood":3350, "stone":1800, "iron":2800, "food":1300, "diamond":4},
3:{"wood":4250, "stone":2300, "iron":3600, "food":1650, "diamond":9},
4:{"wood":5450, "stone":2950, "iron":4600, "food":2100, "diamond":16},
5:{"wood":7000, "stone":3750, "iron":5900, "food":2700, "diamond":25},
6:{"wood":8950, "stone":4800, "iron":7550, "food":3450, "diamond":36},
7:{"wood":11450, "stone":6150, "iron":9700, "food":4400, "diamond":49},
8:{"wood":14650, "stone":7900, "iron":12400, "food":5650, "diamond":64},
9:{"wood":18750, "stone":10100, "iron":15850, "food":7200, "diamond":81},
10:{"wood":24000, "stone":12900, "iron":20300, "food":9200, "diamond":100},
11:{"wood":30700, "stone":16550, "iron":25950, "food":11800, "diamond":121},
12:{"wood":39300, "stone":21150, "iron":33250, "food":15100, "diamond":144},
13:{"wood":50300, "stone":27100, "iron":42550, "food":19350, "diamond":169},
14:{"wood":64350, "stone":34650, "iron":54450, "food":24750, "diamond":196},
15:{"wood":82400, "stone":44350, "iron":69700, "food":31700, "diamond":225},
16:{"wood":105450, "stone":56800, "iron":89250, "food":40550, "diamond":256},
17:{"wood":135000, "stone":72700, "iron":114250, "food":51900, "diamond":289},
18:{"wood":172800, "stone":93050, "iron":146200, "food":66450, "diamond":324},
19:{"wood":221200, "stone":119100, "iron":187150, "food":85050, "diamond":361},
20:{"wood":283100, "stone":152450, "iron":239550, "food":108900, "diamond":400}}}
