#!/usr/bin/env python

import sys

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc

font = {"size": 20}

rc("font", **font)


def draw():
    labels = [
        "CVE-2016-8655",
        "CVE-2017-2636",
        "CVE-2017-7533",
        "CVE-2017-15649",
        "CVE-2017-17712",
        "CVE-2018-12232",
        "CVE-2019-6974",
        "CVE-2019-11486",
        "69e16d01d1de",
    ]

    c2fuzz = [3, 7, 21, 6, 8, 12, 7, 3, 17]
    snowboard = [300, 300, 300, 300, 300, 300, 300, 300, 300]
    krace = [300, 300, 300, 300, 300, 500, 1000, 300, 1000]
    naive = [294, 513, 505, 3009, 1089, 40, 10000, 10000, 10000]

    x = np.arange(len(labels))  # the label locations
    width = 0.2  # the width of the bars

    fig, (ay, ax) = plt.subplots(
        2, 1, figsize=(20, 3), gridspec_kw={"height_ratios": [1, 3]}
    )
    rects1 = ax.bar(x - width / 2 - width, c2fuzz, width, label="C2Fuzz")
    rects2 = ax.bar(x - width / 2, snowboard, width, label="Snowboard")
    rects3 = ax.bar(x + width / 2, krace, width, label="Krace")
    rects4 = ax.bar(x + width / 2 + width, naive, width, label="Naive")

    rects1 = ay.bar(x - width / 2 - width, c2fuzz, width, label="C2Fuzz")
    rects2 = ay.bar(x - width / 2, snowboard, width, label="Snowboard")
    rects3 = ay.bar(x + width / 2, krace, width, label="Krace")
    rects4 = ay.bar(x + width / 2 + width, naive, width, label="Naive")

    ax.set_ylim(0, 1000)
    ay.set_ylim(9000, 10000)

    ay.set(xlabel=None)
    ay.set_xticks(x, [])

    ay.xaxis.set_tick_params(bottom=False)

    # ay.xaxis.tick_top()

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel("# of executions")
    ax.set_xticks(x, labels)
    ay.legend(
        loc="upper center",
        bbox_to_anchor=(0.5, 2.25),
        ncol=4,
    )

    ax.bar_label(rects1, padding=3, rotation=0, size=15)
    ax.bar_label(rects2, padding=3, rotation=0, size=15)
    ax.bar_label(rects3, padding=3, rotation=0, size=15)
    ax.bar_label(rects4, padding=3, rotation=0, size=15)
    ay.bar_label(rects4, padding=3, rotation=0, size=15)

    plt.xticks(rotation=20)

    # plt.show()
    plt.savefig("comparison_graph.pdf", dpi=300, bbox_inches="tight")


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
