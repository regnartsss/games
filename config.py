import telebot
from telebot import apihelper
import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup,ReplyKeyboardRemove
from telebot import types

TOKEN = '887257503:AAGYnE_ReTm9HzkN047WXgrx2Wh9GKqHYQ8'


try:
    apihelper.proxy = {'https': 'socks5://N2cAqr:oStNVN@45.133.226.158:8000'}
    bot = telebot.TeleBot(TOKEN, threaded=False)
except Exception as e:
    print(e)

ADMIN = 765333440

def find_location():
    return os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))).replace('\\', '/') + '/'