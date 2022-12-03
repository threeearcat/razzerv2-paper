#!/usr/bin/env python

import sys

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc

font = {"size": 25}

rc("font", **font)


def draw():
    labels = [
        "   #1",
        "   #2",
        "   #3",
        "   #4",
        "   #5",
        "   #6",
        "   #7",
        "   #8",
        "   #9",
        # "CVE-2016-8655",
        # "CVE-2017-2636",
        # "CVE-2017-7533",
        # "CVE-2017-17712",
        # "CVE-2017-15649",
        # "CVE-2018-12232",
        # "CVE-2019-6974",
        # "CVE-2019-11486",
        # "69e16d01d1de",
    ]

    c2fuzz = [6, 22, 30, 17, 38, 12, 81, 3, 41]
    snowboard = [12, 58, 191, 79, 31, 8, 229, 37, 156]
    krace = [96, 9, 53, 1296, 342, 14, 10000, 494, 10000]
    naive = [270, 721, 274, 1757, 1852, 78, 10000, 10000, 10000]

    x = np.arange(len(labels))  # the label locations
    width = 0.2  # the width of the bars

    # fig = plt.figure(figsize=(16, 5))
    # ax = fig.add_subplot(111)
    fig, (ax, ay) = plt.subplots(1, 2, figsize=(32, 5))

    # rects1 = ax.bar(x - width / 2 - width, c2fuzz, width, label="SegFuzz")
    # rects2 = ax.bar(x - width / 2, snowboard, width, label="Snowboard")
    # rects3 = ax.bar(x + width / 2, krace, width, label="KRACE")
    # rects4 = ax.bar(x + width / 2 + width, naive, width, label="Naive")
    rects1 = ax.bar(x + 0.2, c2fuzz, width, label="SegFuzz", color="#449cd4")
    rects2 = ax.bar(
        x + 0.2 + width, snowboard, width, label="Snowboard", color="#f3c975"
    )
    rects3 = ax.bar(x + 0.2 + width * 2, krace, width, label="KRACE", color="#7c64bc")
    rects4 = ax.bar(x + 0.2 + width * 3, naive, width, label="Naive", color="#39a767")

    ax.set_xlim(0, 9)
    ax.set_ylim(0, 300)

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel("# of executions")
    ax.set_xticks(x, labels, horizontalalignment="left")
    ax.legend(
        loc="upper center",
        ncol=4,
        bbox_to_anchor=(1.1, 1.4),
    )

    r = -30

    for i in range(len(x)):
        val = c2fuzz[i]
        y = val
        if y > 300:
            y = 300
        ax.text(i + 0.2, y, c2fuzz[i], ha="center", size=18, rotation=r)

    for i in range(len(x)):
        val = snowboard[i]
        y = val
        if y > 300:
            y = 300
        ax.text(i + 0.2 + width, y, snowboard[i], ha="center", size=18, rotation=r)

    for i in range(len(x)):
        val = krace[i]
        y = val
        xdiff = 0
        if y > 300:
            y = 300
            xdiff = -0.05
        if val == 10000:
            val = ">10000"
        ax.text(i + 0.2 + width * 2 + xdiff, y, val, ha="center", size=18, rotation=r)

    for i in range(len(x)):
        val = naive[i]
        y = val
        xdiff = 0
        if y > 300:
            y = 300
            xdiff = 0.15
        if val == 10000:
            val = ">10000"
        ax.text(i + 0.2 + width * 3 + xdiff, y, val, ha="center", size=18, rotation=r)

    ########################### time
    c2fuzz = [2, 7, 16, 5, 13, 3, 52, 1, 23]
    snowboard = [4, 26, 58, 22, 10, 2, 139, 16, 61]
    krace = [44, 4, 24, 359, 100, 4, 5720, 222, 3410]
    naive = [85, 377, 83, 474, 460, 29, 5578, 3810, 3358]

    x = np.arange(len(labels))  # the label locations
    width = 0.2  # the width of the bars

    # rects1 = ay.bar(x - width / 2 - width, c2fuzz, width, label="SegFuzz")
    # rects2 = ay.bar(x - width / 2, snowboard, width, label="Snowboard")
    # rects3 = ay.bar(x + width / 2, krace, width, label="KRACE")
    # rects4 = ay.bar(x + width / 2 + width, naive, width, label="Naive")
    rects1 = ay.bar(x + 0.2, c2fuzz, width, label="SegFuzz", color="#449cd4")
    rects2 = ay.bar(
        x + 0.2 + width, snowboard, width, label="Snowboard", color="#f3c975"
    )
    rects3 = ay.bar(x + 0.2 + width * 2, krace, width, label="KRACE", color="#7c64bc")
    rects4 = ay.bar(x + 0.2 + width * 3, naive, width, label="Naive", color="#39a767")

    ay.set_xlim(0, 9)
    ay.set_ylim(0, 200)

    # Add some text for labels, title and custom x-ayis tick labels, etc.
    ay.set_ylabel("Elapsed time (s)")
    ay.set_xticks(x, labels, horizontalalignment="left")

    for i in range(len(x)):
        val = c2fuzz[i]
        y = val
        if y > 200:
            y = 200
        ay.text(i + 0.2, y, c2fuzz[i], ha="center", size=18, rotation=r)

    for i in range(len(x)):
        val = snowboard[i]
        y = val
        if y > 200:
            y = 200
        ay.text(i + 0.2 + width, y, snowboard[i], ha="center", size=18, rotation=r)

    for i in range(len(x)):
        val = krace[i]
        y = val
        xdiff = 0
        if y > 200:
            y = 200
            xdiff = -0.05
        if val == 5720 or val == 3410:
            val = ">" + str(val)
        ay.text(i + 0.2 + width * 2 + xdiff, y, val, ha="center", size=18, rotation=r)

    for i in range(len(x)):
        val = naive[i]
        y = val
        xidff = 0
        if y > 200:
            y = 200
            xdiff = 0.15
        if val == 5578 or val == 3810 or val == 3358:
            val = ">" + str(val)
        ay.text(i + 0.2 + width * 3 + xdiff, y, val, ha="center", size=18, rotation=r)
    # ay.bar_label(rects1, padding=3, rotation=0, size=18)
    # ay.bar_label(rects2, padding=3, rotation=0, size=18)
    # ay.bar_label(rects3, padding=3, rotation=0, size=18)
    # ay.bar_label(rects4, padding=3, rotation=0, size=18)

    # plt.xticks(rotation=35)
    ax.tick_params(axis="x", length=20)
    ay.tick_params(axis="x", length=20)

    # plt.show()

    plt.savefig("comparison_graph_execution.pdf", dpi=300, bbox_inches="tight")  #


draw()


# ./cve-2016-8655/noscheduling
#     294    3527   25599
# ./cve-2017-15649/noscheduling
#    3009   36135  262168
# ./cve-2017-17712/noscheduling
#    1089   13069   94790
# ./cve-2017-2636/noscheduling
#     513    6163   44756
# ./cve-2017-7533/noscheduling
#     505    6056   43917
# ./cve-2018-12232/noscheduling
#      40     476    3462
