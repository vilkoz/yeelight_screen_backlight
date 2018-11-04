#!/usr/bin/env python3

import YeelightWifiBulbLanCtrl as yee

yee.start_detection_thread()
yee.display_bulbs()

print("set_color start")
yee.set_bright(1, "10")
yee.set_color(1, "0xff")
print("set_color end")

yee.stop_detection_thread()
