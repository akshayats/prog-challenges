#!/usr/bin/env python3

import sys
import numpy as np


def parse_ip(ip):
    n = None  # Num of positions on running path
    dg = None  # GPS recording time period
    p, t = None, None
    for i,  l in enumerate(ip):
        if not (n or dg):
            n, dg = l  # Assign params
            p = np.zeros((n, 2))  # Init points container
            t = np.zeros(n)  # Init time-stamps container
        else:
            # [xi, yi, ti]
            p[i-1, :] = l[0:2]
            t[i-1] = l[2]
    return p, t, dg, n


def velocity(pts, t):
    return np.diff(np.asarray(pts), axis=0) / np.diff(t.astype(float).reshape((-1, 1)), axis=0)


def get_gps_pts(dg, v, p, r):
    pts = []
    for i, dt, pp in zip(r, dg, np.array(p)[r, :]):
        q = dt * v[i] + pp
        pts.append(tuple(q))
    return pts


def path_distance(p):
    q = np.diff(p, axis=0)
    pathdist = np.sum(np.sqrt(np.sum(np.square(q), axis=1)))
    return pathdist


def gps_error(p, t, g):
    v = velocity(p, t)  # Velocity vectors at each p except last
    v = np.vstack((v, np.asarray((0, 0))))  # Last velocity at stop
    # Which velocity vector for each g
    r = [np.squeeze(np.argwhere(i >= t), -1)[-1] for i in g]

    # Find points at GPS times
    dg = g - t[r]  # delta between gps and most recent t
    vg = v[r, :]  # relevant velocity vector
    p0 = np.array(p)[r, :]  # relevant local origin
    q = p0 + vg * dg[:, np.newaxis]  # GPS point recorded

    # Percentage distance error
    dist_run = path_distance(np.array(p))  # Actual path distance
    dist_gps = path_distance(q)  # GPS path distance
    err_percent = (1 - dist_gps / dist_run) * 100
    # print("Percentage error in distance by GPS = {}%".format(err))
    return err_percent


def main():
    ip_phrase = []
    for ip_line in sys.stdin:
        if 'done' in ip_line.lower():
            break
        else:
            ip_num = [int(i) for i in ip_line.split(' ')[0:]]
            ip_phrase.append(ip_num)

    # ip = [[6, 2], [0, 0, 0], [0, 3, 3,], [-2, 5, 5], [0, 7, 7], [2, 5, 9], [0, 3, 11]]
    p, t, dg, n = parse_ip(ip_phrase)
    # p = [(0, 0), (1, 1), (4, 7), (6, 10), (5, 7), (3, -1), (0, -4), (-2, -1), (-3, 2), (2, 5), (-1, 13)]
    # t = np.arange(0, 32, 3)
    g = np.append(np.arange(0, t[-1], dg), t[-1])  # GPS time stamps, start at 0 and end with last t
    # print(g)
    E_percent = gps_error(p, t, g)
    # stdout
    print(E_percent)
    return 0


if __name__ == "__main__":
    main()
