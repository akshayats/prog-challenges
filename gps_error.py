#!/usr/bin/env python3

import sys
import numpy as np


def parse_ip(ip):
    n = None  # Num of positions on running path
    dg = None  # GPS recording time period
    p_t = None
    for l in ip:
        if not (n or dg):
            n, dg = l  # Assign params
            p_t = []  # Init points container
        else:
            # [xi, yi, ti]
            p_t.append(tuple(l))
    return p_t, dg, n


# def velocity(pts, t):
#     bb = np.diff(np.asarray(pts), axis=0) / np.diff(t.astype(float).reshape((-1, 1)), axis=0)
#     return 0


def velocity(a, b):
    dt = float(b[2] - a[2])
    v = tuple([(b[0] - a[0]) / dt, (b[1] - a[1]) / dt])
    return v


# def get_gps_pts(dg, v, p, r):
#     pts = []
#     for i, dt, pp in zip(r, dg, np.array(p)[r, :]):
#         q = dt * v[i] + pp
#         pts.append(tuple(q))
#     return pts

def get_gps_pt(tg, t, vg, p0):
    dg = float(tg - t)  # delta between gps and most recent t
    # vg = v[r, :]  # relevant velocity vector
    # p0 = np.array(p)[r, :]  # relevant local origin
    p_g = tuple([p0[0] + vg[0] * dg, p0[1] + vg[1] * dg, tg])  # GPS point recorded
    return p_g


def path_distance(p):
    q = np.diff(p, axis=0)
    pathdist = np.sum(np.sqrt(np.sum(np.square(q), axis=1)))
    return pathdist


def gps_error(p_t, t_g):
    v = list(map(velocity, p_t[:-1], p_t[1:]))  # ds/dt
    v.append((0, 0))  # Stop velocity at last point

    # Which velocity vector for each t_g
    t = [i[2] for i in p_t]  # Actual time stamps
    r = [len(t) - 1 - [i >= j for j in t[::-1]].index(True) for i in t_g]

    # Find points at GPS times
    ans = get_gps_pt(t_g[2], t[r[2]], v[r[2]], p_t[r[2]])
    # dg = t_g - t[r]  # delta between gps and most recent t
    # vg = v[r, :]  # relevant velocity vector
    # p0 = np.array(p)[r, :]  # relevant local origin
    # q = p0 + vg * dg[:, np.newaxis]  # GPS point recorded
    print(ans)
    print(t_g)
    print(r)
    print(t)
    print(v)
    print(p_t)
    return 0
    #
    # # Percentage distance error
    # dist_run = path_distance(np.array(p))  # Actual path distance
    # dist_gps = path_distance(q)  # GPS path distance
    # err_percent = (1 - dist_gps / dist_run) * 100
    # # print("Percentage error in distance by GPS = {}%".format(err))
    # return err_percent


def main():
    ip_phrase = []
    # for ip_line in sys.stdin:
    #     if 'done' in ip_line.lower():
    #         break
    #     else:
    #         ip_num = [int(i) for i in ip_line.split(' ')[0:]]
    #         ip_phrase.append(ip_num)

    ip_phrase = [[6, 2], [0, 0, 0], [0, 3, 3], [-2, 5, 5], [0, 7, 7], [2, 5, 9], [0, 3, 11]]
    # p = [(0, 0), (1, 1), (4, 7), (6, 10), (5, 7), (3, -1), (0, -4), (-2, -1), (-3, 2), (2, 5), (-1, 13)]
    # t = np.arange(0, 32, 3)

    p_t, dg, n = parse_ip(ip_phrase)  # each recording is a tuple (xi, yi, ti)

    t_g = [i for i in range(0, p_t[-1][-1], dg)]  # GPS time stamps, start at 0 and ...
    t_g.append(p_t[-1][-1])  # end with last t

    E_percent = gps_error(p_t, t_g)
    # print(E_percent)
    return 0


if __name__ == "__main__":
    main()
