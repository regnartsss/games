import os
import json
import time
import threading
#import datetime
from datetime import datetime, timedelta, date
from pprint import pprint
from data import buildings

global test

def find_location():
    return os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))).replace('\\', '/') + '/'
PATH = find_location()

def save_farm():
    global test
    with open(PATH + "tmp/" + 'test.json', 'w', encoding="utf-16") as f:
        json.dump(test, f)
    with open(PATH + "tmp/" + 'test.json', 'rb') as f:
        test = json.load(f)

def open_buy():
    global test
    test = {}
    with open(PATH + "tmp/" + 'test.json', 'rb') as f:
            test = json.load(f)

def start_farm():
    global test
    user = "765333440"
    farm_time_old = datetime.now().strftime("%Y:%m:%d:%H:%M:%S")
    a = farm_time_old.split(':')
    aa = datetime(int(a[0]), int(a[1]), int(a[2]), int(a[3]), int(a[4]), int(a[5]))
    farm_time = test[user]["farm_time"]
    b = farm_time.split(':')
    bb = datetime(int(b[0]), int(b[1]), int(b[2]), int(b[3]), int(b[4]), int(b[5]))
    ss = (aa-bb).seconds
    lvl_farm = test[user]["building"]["farm"]
    num_farm = buildings["farm"][lvl_farm]["production"]
    num_farm = num_farm * ss
    lvl_storage = test[user]["building"]["storage"]
    num_storage = buildings["storage"][lvl_storage]["capacity"]
#    print(num_storage)
#    print(num_farm)
    test[user]["food"] += num_farm
    if test[user]["food"] > num_storage:
        print("Склад полон")
        test[user]["food"] = num_storage
    else:
        test[user]["food"] += num_farm

    test[user]["farm_time"] = farm_time_old
    print(test[user]["food"])


open_buy()
start_farm()
save_farm()
