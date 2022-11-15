#!/usr/bin/env python

import sys

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc
from matplotlib.ticker import FuncFormatter

font = {"size": 33}

rc("font", **font)


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

    if len(ret) < len(x):
        ret.extend([0] * (len(x) - len(ret)))

    print(filename, idx)
    for i in range(len(ret)):
        print(int(ret[i]))
    return ret


def millions(x, pos):
    return "{}M".format(x * 1e-6)


def kilos(x, pos):
    return "{}K".format(x * 1e-3)


def draw():
    fig = plt.figure(figsize=(16, 9))

    mformatter = FuncFormatter(millions)
    kformatter = FuncFormatter(kilos)

    xaxis = list(range(0, 100))
    y1 = get_data(sys.argv[1], xaxis, 1)

    ax = fig.add_subplot(111)
    ax.yaxis.set_major_formatter(kformatter)
    lns1 = ax.plot(
        xaxis,
        y1,
        "--",
        label="Branch",
        linewidth="3",
        marker="X",
        markersize="20",
        markevery=5,
    )
    # lns2 = ax.plot(xaxis, Rn, "-", label="Rn")

    y2 = get_data(sys.argv[2], xaxis, 1)
    lns2 = ax.plot(
        xaxis,
        y2,
        "--b",
        label="Branch (Syzkaller)",
        linewidth="3",
        marker="o",
        markersize="15",
        markevery=5,
    )

    ax2 = ax.twinx()
    ax2.yaxis.set_major_formatter(mformatter)
    y3 = get_data(sys.argv[1], xaxis, 2)
    lns3 = ax2.plot(
        xaxis,
        y3,
        "--r",
        label="Interleaving segment",
        linewidth="3",
        marker="s",
        markersize="15",
        markevery=5,
    )

    y4 = get_data(sys.argv[3], xaxis, 2)
    lns4 = ax2.plot(
        xaxis,
        y4,
        "--",
        color="indigo",
        label="Interleaving segment" + "\n" + "(w/o scheduling control)",
        linewidth="3",
        marker="D",
        markersize="15",
        markevery=5,
    )

    lns = lns1 + lns2
    labs = [l.get_label() for l in lns]
    ax.legend(lns, labs, loc="upper left")

    ax2.legend(loc="lower right")

    ax.grid()
    ax.set_xlabel("Time (h)")
    ax.set_ylabel("# of branches")
    ax2.set_ylabel("# of interleaving segments")

    # plt.show()
    plt.savefig("coverage_graph.pdf", dpi=200, bbox_inches="tight")


draw()
