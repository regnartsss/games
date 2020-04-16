import telebot  # Импортируем объект бота
import texting

def keyboard_map():
    keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
    keyboard.row(texting.button_mining_map)
    return keyboard

#def keyboardmenu():
#    keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
#    keyboard.row('🗺 Карта')
#    keyboard.row('🏘 Город')
#    return keyboard

def keyboardmap():
    keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
    keyboard.row (texting.button_castle)
    return keyboard

#def keyboarddel():
#    keyboard = telebot.types.ReplyKeyboardRemove()
#    return keyboard


#def keyadmin():
#    keyadmin = telebot.types.ReplyKeyboardMarkup(True, False)
#    keyadmin.row('Создать карту')
#    keyadmin.row("Кол-во ячеек")
#    keyadmin.row("Оплатить")
#    keyadmin.row("Новая атака")
#    return keyadmin

def keyboard_main_menu():
    keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
    keyboard.row(texting.button_heroes, texting.button_building, texting.button_location)
    keyboard.row(texting.button_maps, texting.button_shop)
    keyboard.row(texting.button_setting, texting.button_help, texting.button_top)
    return keyboard
def keyboard_statisctick():
    keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
    keyboard.row('Общий рейтинг за башни')
    keyboard.row('Последний бой за башни')
    keyboard.row (texting.button_back)
    return keyboard


def keyboard_keyrudnic():
    keyboardmenu = telebot.types.ReplyKeyboardMarkup(True, False)
    keyboardmenu.row(texting.button_mining)
    keyboardmenu.row(texting.button_mining_ataka)
    keyboardmenu.row (texting.button_maps)
    return keyboardmenu

def keyboard_battle():
    keyboardmenu = telebot.types.ReplyKeyboardMarkup(True, False)
    keyboardmenu.row (texting.button_attack)
    keyboardmenu.row (texting.button_goto_two)
    return keyboardmenu

#def keyboardback():
#    keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
#    keyboard.row('◀️Назад')
#    return keyboard


def keyboaryesno():
    keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
    keyboard.row("Да", "Нет")
    return keyboard


def keyboard_info():
    keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
    keyboard.row("Пригласить", "💬 Чат")
    keyboard.row("Обратная связь")
    keyboard.row("Помочь проекту")
    keyboard.row (texting.button_back)
    return keyboard

def keyboard_buy():
    keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
    keyboard.row("Tranzzo")
#    keyboard.row("QIWI")
    keyboard.row (texting.button_back)
    return keyboard

def keyboard_start():
    keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
    keyboard.row(texting.button_start)
    return keyboard

def key_buy():
    keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
    keyboard.row("Оплата QIWI")
    return keyboard

def keyboard_battle_back():
    keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
    keyboard.row("Покинуть поле боя")
    return keyboard

def keyboard_battle_one_back():
    keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
    keyboard.row (texting.button_goto)
    return keyboard

def keyboard_locat():
    keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
    keyboard.row("🗼 Осада башни")
    keyboard.row (texting.button_back)
    return keyboard
