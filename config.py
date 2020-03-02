import telebot
from telebot import apihelper
import os

#TOKEN = '887257503:AAGYnE_ReTm9HzkN047WXgrx2Wh9GKqHYQ8'
#TOKEN = '929931340:AAEEgS76qCc8gM0XY6veED3sRhdRwrNFpJY'
TOKEN = '1089789060:AAE1Y0dWyjZfsRLunoXPXP3TYbAz73c7eZM' #HeroesLifeBot
#TOKEN = '1037757927:AAGYbYD3z_wKg3UD9QsbX4_QdqUjrFK50tc'
publicKey = '48e7qUxn9T7RyYE1MVZswX1FRSbE6iyCj2gCRwwF3Dnh5XrasNTx3BGPiMsyXQFNKQhvukniQG8RTVhYm3iPtoMap5fEJ7DxRtZW86kKJmVXxgA2xF7dxEzfwp2DCyiBaXHWxHTWxq6vNkuRTP3fe8UDCbb3iJmCULHj7VFQyozq2V61LuWSYEVQw6RcT' #QIWI
provider_token = "535936410:LIVE:1089789060_e7e9f8ef-74dc-4011-be12-c84cc861b72d" #Tranzzo

try:

    apihelper.proxy = {'https': 'socks5://N2cAqr:oStNVN@45.133.226.158:8000'}
    bot = telebot.TeleBot(TOKEN, threaded=False)

except Exception as e:
    print(e)



def find_location():
    return os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))).replace('\\', '/') + '/'