#!/usr/bin/env python

import sys

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc
from matplotlib.ticker import FuncFormatter

font = {"size": 33}

rc("font", **font)


temp = np.random.random(10) * 30
Swdown = np.random.random(10) * 100 - 10
Rn = np.random.random(10) * 100 - 10


def get_data(filename, x, idx):
    with open(filename) as f:
        lines = f.readlines()

    ret = []
    j = 0
    for line in lines:
        toks = line.split(", ")
        ts = int(float(toks[0]))
        h = ts / 3600
        if h > x[j]:
            j += 1
            ret.append(int(toks[idx]))
        if j >= len(x):
            break

    return ret


def millions(x, pos):
    return "{}M".format(x * 1e-6)


def kilos(x, pos):
    return "{}K".format(x * 1e-3)


def draw():
    fig = plt.figure(figsize=(16, 9))

    mformatter = FuncFormatter(millions)
    kformatter = FuncFormatter(kilos)

    xaxis = list(range(0, 96))
    y1 = get_data(sys.argv[1], xaxis, 3)

    ax = fig.add_subplot(111)
    ax.yaxis.set_major_formatter(kformatter)
    lns1 = ax.plot(
        xaxis,
        y1,
        "-",
        label="# of branches",
        linewidth="3",
        marker="X",
        markersize="15",
        markevery=5,
    )
    # lns2 = ax.plot(xaxis, Rn, "-", label="Rn")

    ax2 = ax.twinx()
    ax2.yaxis.set_major_formatter(mformatter)
    y3 = get_data(sys.argv[1], xaxis, 5)
    lns3 = ax2.plot(
        xaxis,
        y3,
        "-r",
        label="# of segments",
        linewidth="3",
        marker="s",
        markersize="15",
        markevery=5,
    )

    # added these three lines
    lns = lns1  # + lns2
    labs = [l.get_label() for l in lns]
    ax.legend(lns, labs, loc="upper left")

    ax2.legend(loc="lower right")

    ax.grid()
    ax.set_xlabel("Time (h)")
    ax.set_ylabel("Code coverage")
    ax2.set_ylabel("Interleaving coverage")

    # plt.show()
    plt.savefig("coverage_graph.pdf", dpi=200, bbox_inches="tight")


draw()
