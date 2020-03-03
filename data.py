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
storage = {"1": {"wood", "stone", "food"}}
def text_mining(res, lvl, kol, timer):
    if res == "wood":
        text = "🌲 Шахта с деревом \n🎖 Уровень шахты " + str(lvl) + "\n🌑 Количество ресурса: " + str(kol)
    elif res == "food":
        text = "🔨 Ферма с едой \n🎖 Уровень фермы " + str(lvl) + "\n🌑 Количество ресурса: " + str(kol)
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

    wood = int(buildings[text]["wood"]* lvl * buildings[text]["konst"])
    stone = int(buildings[text]["stone"] * lvl * buildings[text]["konst"])
    food = int(buildings[text]["food"] * lvl * buildings[text]["konst"])
    return wood, stone, food

buildings = {"castle": {"name": "Замок", "lvl": 1, "wood": 500, "stone": 500, "food": 500, "gold": 1, "konst":1.15},
             "storage": {"name": "Склад", "lvl": 1, "wood": 300, "stone": 300, "food": 300, "gold": 1, "konst":1.15},
             "barracks": {"name": "Казарма", "lvl": 1, "wood": 200, "stone": 200, "food": 200, "gold": 1, "konst":1.15},
             "wood": {"name": "Дерево", "lvl": 1, "wood": 500, "stone": 800, "food": 500, "gold": 1, "konst":1.15},
             "food": {"name": "Еда", "lvl": 1, "wood": 500, "stone": 900, "food": 500, "gold": 1, "konst":1.15},
             "stone": {"name": "еда", "lvl": 1, "wood": 500, "stone": 1000, "food": 500, "gold": 1, "konst":1.15}}
