import numpy as np
import sklearn.cluster
from imageio import imread
from subprocess import check_output as co
import time

import YeelightWifiBulbLanCtrl as yee

def calc_screen_light_mean_color():
    co("scrot -t 3% /tmp/real_test.png", shell=True)
    red = np.asarray(imread("/tmp/real_test-thumb.png"))
    print(red, red.shape)
    original_shape = red.shape # so we can reshape the labels later
    W = red.shape[0]
    H = red.shape[1]
    red = red.flatten().reshape(W * H, 3)
    print(red, red.shape)

    samples = red

    clf = sklearn.cluster.KMeans(n_clusters=3)
    labels = clf.fit_predict(samples).flatten().reshape(W,H)
    print(labels.shape)
    print(labels)

    # import matplotlib.pyplot as plt

    # plt.imshow(labels)
    # plt.show()

    red = red.flatten().reshape(W, H, 3)

    # plt.imshow(red)
    # plt.show()

    mean_color = [0] * 3
    for i in range(3):
        print("red:", red[labels==i])
        mean_color[i] = np.mean(red[labels==i],axis=(0))

        print("mean_color:", mean_color)

    mean_avg_arr = [sum(x) / 3 for x in mean_color]

    light_mean = mean_color[mean_avg_arr.index(max(mean_avg_arr))]
    max_elems_arr = [len(red[labels==x]) for x in range(3)]
    light_mean = mean_color[max_elems_arr.index(max(max_elems_arr))]
    print("light_mean:", light_mean)

    for i in range(W):
        for j in range(H):
            red[i,j] = mean_color[labels[i,j]]
    # plt.imshow(red)
    # plt.show()
    return (int(x) for x in light_mean)

def main():
    yee.start_detection_thread()
    yee.display_bulbs()
    yee.set_bright(1, "10")
    yee.stop_detection_thread()

    while True:
        color = calc_screen_light_mean_color()
        print(color)
        color_str = "0x" + "".join(["{:02X}".format(x) for x in color])
        # print(color_str)
        # co("tmux send-keys -t0:3.1 \"c 1 {}\" Enter".format(color_str), shell=True)
        yee.set_color(1, color_str)
        time.sleep(0.5)

if __name__ == "__main__":
    main()
