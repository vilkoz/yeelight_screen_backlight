# yeelight_screen_backlight
Use yeelight smart bulb as backlight for your screen

## Requirements

* Python3

Currently using `scrot` to take screen shot.

## Instalation and usage

```
python3 -m venv venv
source vevn/bin/activate
pip install -r requirements.txt
python3 main.py # stop with Ctrl-C
```

## Explanation

[Linux demo](https://www.yeelight.com/download/developer/yeelight_demo_lan_ctrl_python.zip) from yeelight developer site is used
to control the bulb.

Color selection is made by performing K-means clustering algorithm with number of clusters = 3, on scaled down screen shots, then selecting the largest cluster.

# Usefull links

[Yeelight API specs](https://www.yeelight.com/download/Yeelight_Inter-Operation_Spec.pdf)
[Yeelight Developer page](https://thirdparty.yeelight.com/)
