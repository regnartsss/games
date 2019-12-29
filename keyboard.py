from config import *  # Импортируем объект бота

def keyboardmenu():
    keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
    keyboard.row('Карта')
    keyboard.row('Дом')
    return keyboard

def keyboardmap():
    keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
    keyboard.row('Вернуться в город')
    return keyboard

def keymap():
    keyboardmenu = telebot.types.ReplyKeyboardMarkup(True, False)
    keyboardmenu.row('Вернуться на карту')
    return keyboardmenu

def keyadmin():
    keyadmin = telebot.types.ReplyKeyboardMarkup(True, False)
    keyadmin.row('Создать карту')
    keyadmin.row("Кол-во ячеек")
    return keyadmin

def keyboarddom():
    keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
    keyboard.row('Герой', "Склад")
    keyboard.row('На карту')
    return keyboard

def keyrudnic():
    keyboardmenu = telebot.types.ReplyKeyboardMarkup(True, True)
    keyboardmenu.row('Копать')
    keyboardmenu.row('Назад')
    return keyboardmenu

def keyattaka():
    keyboardmenu = telebot.types.ReplyKeyboardMarkup(True, True)
    keyboardmenu.row('Атаковать')
    keyboardmenu.row('Назад')
    return keyboardmenu

def keyboardback():
    keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
    keyboard.row('Назад')
    return keyboard

def keyboardbattle():
    keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
    keyboard.row("Дальний бой")
    return keyboard