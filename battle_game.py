#from games import *
#import games
#from games import bot,random,threading,pprint,telebot, time, save
from keyboard import keyboardmap, keyboard_map
from data import weapons,fight_text_all,fight_trans


#from pprint import pprint
#from game import *
"""
class Battle():
    def __init__(self, message, call=""):
        self.id = message.chat.id
        self.text = message.text
        self.first_name = message.from_user.username
        self.user = users[str(self.id)]
        self.maps = Maps(message)
        self.user_bot = User(message)

    def attak(self):
        global users, maps, attak
        pprint(attak)
        r = random.randrange(1, 3)
        pprint(r)
        if r == 1:
            #                self.user["energy_used"] -= 1
            self.user_bot.energy()
            bot.send_message(text="Вы проиграли", chat_id=self.id, reply_markup=self.maps.output_map())
        else:
            self.user["experience_used"] += 5
            #               self.user["energy_used"] -= 1
            maps[attak]["resource"] = "null"
            self.user_bot.update_statistic(data="experiens")
            self.user_bot.energy()
            bot.send_message(text="Вы победили и получили 5 опыта", chat_id=self.id,
                             reply_markup=self.maps.output_map())
        #                self.resource(attak)

        pprint("всё ок")
        save("users")


    
    
    
    def __init__(self, message, call=""):
        global battlemap, st, attak
        self.id = message.chat.id
        self.text = message.text
        self.message_id = message.message_id
        try:
            self.message_call = call.data
            self.id_call = call.id
        except:

            print("нет данных")
        st = 1


    def battle(self):
        global battlemap
#        print(self.id)
#        keyboard = telebot.types.InlineKeyboardMarkup()
        x, s = 1, 1
        battlemap = {}
#        button1 = types.InlineKeyboardButton("Атака1", callback_data=" ")
#        button2 = types.InlineKeyboardButton("Атака2", callback_data=" ")
        r_enemy = random.randrange(1, 7)
        r = random.randrange(0, 6)
        while x < 8:
            y = 1
            while y <= 8:
                        field = str(x)+"-"+str(y)
                        if s == r_enemy * 8:
                            battlemap[field] = 'battle_enemy'
                            y += 1
                            s += 1
                            continue
                        elif s == r * 8 + 1:
                            battlemap[field] = 'battle_player'
                            y += 1
                            s += 1
                            continue
                        else:
                            battlemap[field] = ' '
                            y += 1
                            s += 1
            x += 1
#        self.pole()
#        pprint(battlemap)
        self.print_battle()



    def print_battle(self):
        global battlemap, st

        keyboard = telebot.types.InlineKeyboardMarkup()
        s = 1
        while s < 8:
            tab = []
            for key, value in battlemap.items():
                x = int(key.split("-")[0])
                if x == s:
                    tab.append(types.InlineKeyboardButton(text=self.dat_pos(value), callback_data='battle_'+key))
            s += 1
            keyboard.row(*tab)
        keyboard.row(types.InlineKeyboardButton(text="Ходить", callback_data='battle_go'))
        if st == 0:
            bot.edit_message_text(text="Ходите", chat_id=self.id, message_id=self.message_id,
                                  reply_markup=keyboard)
        else:
            pprint("22")
            bot.send_message(text="Battle", chat_id=self.id, reply_markup=keyboard)


    def dat_pos(self, value):
        if value == " ":
            return " "
        else:
            dat = value.split("_")[1]
            if dat == 'enemy':
                return "🙉"
            elif dat == "player":
                return "😺"
            elif dat == "pole":
                return '◻'
            else:
                return " "


    def pole(self):
        global battlemap
        p = 1
        for k, v in battlemap.items():
            if v == "battle_player":
                x = int(k.split("-")[0])
                y = int(k.split("-")[1])
                battlemap[str(x) + "-" + str(y+p)] = "battle_pole"
#                battlemap[str(x) + "-" + str(y - p)] = "battle_pole"
                battlemap[str(x+p) + "-" + str(y)] = "battle_pole"
                battlemap[str(x-p) + "-" + str(y)] = "battle_pole"


    def status(self):
        global attak
        data = self.message_call.split("_")[0]
        data_old = self.message_call.split("_")[1]

#        pprint(str(attak)+" attaka")
#        pprint(data_old+" ячейка")
        try:
            pprint(attak)
            if data_old == "go" and attak == 0:
                attak = 1
                self.attaka()
            elif data_old == "go" and attak == 1:
                pprint("повторная аттака")
            elif data == "battle" and attak == 1:
                self.go()
                attak = 0
        except:
            attak = 1
            self.attaka()


    def go(self):
        global battlemap, st
        pprint("хожу")
        hod = "dir"
        if hod == "dir":
            p = 1
        elif hod == "diag":
            p, d = 0, 1
        else:
            p, d = 1, 1
        data = self.message_call.split("_")[1]
        x = int(data.split("-")[0])
        y = int(data.split("-")[1])
#
        if self.bat(x, y+p) == "battle_player" and p == 1: # вправо
                battlemap[str(x) + "-" + str(y+p)] = "battle_" + str(x) + "-" + str(y+p)
                battlemap[str(x) + "-" + str(y)] = "battle_player"
                st = 0
        elif self.bat(x+p, y) == "battle_player" and p == 1:
                battlemap[str(x+p) + "-" + str(y)] = "battle_" + str(x+p) + "-" + str(y)
                battlemap[str(x) + "-" + str(y)] = "battle_player"
                st = 0
        elif self.bat(x-p, y) == "battle_player" and p == 1:
                battlemap[str(x - p) + "-" + str(y)] = "battle_" + str(x - p) + "-" + str(y)
                battlemap[str(x) + "-" + str(y)] = "battle_player"
                st = 0
        elif self.bat(x, y-p) == "battle_player" and p == 1:
                battlemap[str(x) + "-" + str(y-p)] = "battle_" + str(x) + "-" + str(y-p)
                battlemap[str(x) + "-" + str(y)] = "battle_player"
                st = 0
        elif battlemap[str(x-d)+"-"+str(y-d)] == "battle_player" and d == 1:
                pprint("test")
                battlemap[str(x-d) + "-" + str(y-d)] = "battle_" + str(x-d) + "-" + str(y-d)
                battlemap[str(x) + "-" + str(y)] = "battle_player"
                st = 0
        elif battlemap[str(x+d)+"-"+str(y-d)] == "battle_player" and d == 1:
                pprint("test")
                battlemap[str(x+d) + "-" + str(y-d)] = "battle_" + str(x+d) + "-" + str(y-d)
                battlemap[str(x) + "-" + str(y)] = "battle_player"
                st = 0
        elif battlemap[str(x - d) + "-" + str(y + d)] == "battle_player" and d == 1:
                pprint("test")
                battlemap[str(x - d) + "-" + str(y + d)] = "battle_" + str(x - d) + "-" + str(y + d)
                battlemap[str(x) + "-" + str(y)] = "battle_player"
                st = 0
        elif battlemap[str(x+d)+"-"+str(y+d)] == "battle_player" and d == 1:
                pprint("test")
                battlemap[str(x+d) + "-" + str(y+d)] = "battle_" + str(x+d) + "-" + str(y+d)
                battlemap[str(x) + "-" + str(y)] = "battle_player"
                st = 0

        for k, v in battlemap.items():
                if v == "battle_pole":
                    battlemap[k] = " "
        self.print_battle()

  #      else:
  #              battlemap[str(x) + "-" + str(y + p)] = "battle_pole"
  #              st = 0

    def attaka(self):
        global battlemap, st
        p, st = 1, 0
        for k, v in battlemap.items():
            if v == "battle_player":
                x = int(k.split("-")[0])
                y = int(k.split("-")[1])
                if y == 1:
                    battlemap[str(x) + "-" + str(y + p)] = "battle_pole"
                #                battlemap[str(x) + "-" + str(y - p)] = "battle_pole"
                    battlemap[str(x + p) + "-" + str(y)] = "battle_pole"
                    battlemap[str(x - p) + "-" + str(y)] = "battle_pole"

                else:
                    battlemap[str(x) + "-" + str(y + p)] = "battle_pole"
                    battlemap[str(x) + "-" + str(y - p)] = "battle_pole"
                    battlemap[str(x + p) + "-" + str(y)] = "battle_pole"
                    battlemap[str(x - p) + "-" + str(y)] = "battle_pole"
        self.print_battle()

    def delete_pole(self):
        global battlemap
        p = 1
        for k, v in battlemap.items():
            if v == "battle_pole":
                battlemap[v] = " "

    def bat(self, x, y):
        if x == 0:
            return battlemap[str(1) + "-" + str(y)]
        elif y == 0:
            return battlemap[str(x) + "-" + str(1)]
        elif x == 8:
            return battlemap[str(7) + "-" + str(y)]
        elif y == 9:
            return battlemap[str(x) + "-" + str(8)]
        else:
            return battlemap[str(x) + "-" + str(y)]
"""