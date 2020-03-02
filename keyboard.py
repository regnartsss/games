from config import telebot  # Импортируем объект бота

def keyboard_map():
    keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
    keyboard.row('Вернуться на карту 🗺')
    return keyboard

def keyboardmenu():
    keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
    keyboard.row('Карта 🗺')
    keyboard.row('Город')
    return keyboard

def keyboardmap():
    keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
    keyboard.row('Вернуться в город')

    return keyboard
def keyboarddel():
    keyboard = telebot.types.ReplyKeyboardRemove()
    return keyboard


def keyadmin():
    keyadmin = telebot.types.ReplyKeyboardMarkup(True, False)
    keyadmin.row('Создать карту')
    keyadmin.row("Кол-во ячеек")
    keyadmin.row("Оплатить")
    keyadmin.row("Новая атака")
    return keyadmin

def keyboard_main_menu():
    keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
    keyboard.row('Герой', "Строения")
    keyboard.row('На карту 🗺')
    keyboard.row('⚙ Настройки', 'Помощь')
    return keyboard

def keyboard_building():
    keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
    keyboard.row('Склад')
    keyboard.row('Казарма')
    keyboard.row('Назад')
    return keyboard

def keyrudnic():
    keyboardmenu = telebot.types.ReplyKeyboardMarkup(True, False)
    keyboardmenu.row('Копать')
    keyboardmenu.row('Назад')
    return keyboardmenu

def keyboard_battle():
    keyboardmenu = telebot.types.ReplyKeyboardMarkup(True, True)
    keyboardmenu.row('Атаковать')
    keyboardmenu.row('Отступить')
    return keyboardmenu

def keyboardback():
    keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
    keyboard.row('Назад')
    return keyboard

def keyboardbattle():
    keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
    keyboard.row("Дальний бой")
    return keyboard

def keyboaryesno():
    keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
    keyboard.row("Да", "Нет")
    return keyboard

def keyboardbarracks():
    keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
    keyboard.row("Обучить лучника")
    keyboard.row("Назад")
    return keyboard

def keyboard_info():
    keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
    keyboard.row("Пригласить", "Чат")
    keyboard.row("Обратная связь")
    keyboard.row("Помочь проекту")
    keyboard.row("Назад")
    return keyboard

def keyboard_buy():
    keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
    keyboard.row("Tranzzo")
    keyboard.row("QIWI")
    keyboard.row("Назад")
    return keyboard

def keyboard_start():
    keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
    keyboard.row("Всё понятно")
    return keyboard

def key_buy():
    keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
    keyboard.row("Оплата QIWI")
    return keyboard

def all_battle():
    keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
    keyboard.row("Покинуть поле боя")
    return keyboard