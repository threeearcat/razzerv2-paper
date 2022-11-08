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
    naive = [100, 500, 100, 500, 500, 500, 1000, 700, 1000]

    x = np.arange(len(labels))  # the label locations
    width = 0.2  # the width of the bars

    fig, ax = plt.subplots(figsize=(20, 3))
    rects1 = ax.bar(x - width / 2 - width, c2fuzz, width, label="C2Fuzz")
    rects2 = ax.bar(x - width / 2, snowboard, width, label="Snowboard")
    rects3 = ax.bar(x + width / 2, krace, width, label="Krace")
    rects4 = ax.bar(x + width / 2 + width, naive, width, label="Naive")

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel("# of executions")
    ax.set_xticks(x, labels)
    ax.legend(
        loc="upper center",
        bbox_to_anchor=(0.5, 1.35),
        ncol=4,
    )

    ax.bar_label(rects1, padding=3, rotation=40)
    ax.bar_label(rects2, padding=3, rotation=40)
    ax.bar_label(rects3, padding=3, rotation=40)
    ax.bar_label(rects4, padding=3, rotation=40)

    plt.xticks(rotation=40)

    # plt.show()
    plt.savefig("comparison_graph.pdf", dpi=300, bbox_inches="tight")


draw()
