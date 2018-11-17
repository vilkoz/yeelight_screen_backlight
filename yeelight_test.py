#!/usr/bin/env python3

import YeelightWifiBulbLanCtrl as yee
import subprocess
from subprocess import check_output as co
from time import sleep
import datetime

PHONE_IP = "192.168.0.221"

def check_phone():
    try:
        s = co("ping -c 1 " + PHONE_IP + " | grep 'bytes from'", shell=True)
    except subprocess.CalledProcessError as e:
        return False
    sleep(0.5)
    return True

def check_if_dark():
    from astral import Astral
    city_name = 'Kiev'
    a = Astral()
    a.solar_depression = 'civil'
    city = a[city_name]
    sun = city.sun(date=datetime.datetime.now(), local=True)
    T = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=2)))
    if (sun['sunrise'] < T < sun['sunset']):
        return False
    return True

yee.start_detection_thread()
yee.display_bulbs()

try:
    while True:
        phone_status = check_phone()
        bulb_status = yee.display_bulb(1)["power"]
        print("phone_status:", phone_status)
        print("bulb_status:", bulb_status)
        if phone_status == True and bulb_status == "off" and check_if_dark():
            yee.toggle_bulb(1)
            yee.refresh_bulbs()
        elif phone_status == False and bulb_status == "on":
            yee.toggle_bulb(1)
            yee.refresh_bulbs()
        elif bulb_status == "on" and not check_if_dark():
            yee.toggle_bulb(1)
            yee.refresh_bulbs()

except KeyboardInterrupt:
    print('stopping thread')
    yee.stop_detection_thread()

yee.stop_detection_thread()
