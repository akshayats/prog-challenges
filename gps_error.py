#!/usr/bin/env python3

import sys


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


def velocity(a, b):
    dt = float(b[2] - a[2])
    v = tuple([(b[0] - a[0]) / dt, (b[1] - a[1]) / dt])
    return v


def get_gps_pt(tg, t, vg, p0):
    dg = float(tg - t)  # delta between gps and most recent t
    p_g = tuple([p0[0] + vg[0] * dg, p0[1] + vg[1] * dg, tg])  # GPS point recorded
    return p_g


def l2_dist(p, q):
    s = ((q[0] - p[0]) ** 2 + (q[1] - p[1]) ** 2) ** 0.5
    return s


def path_distance(p):
    dist = 0
    for i, j in zip(p[:-1], p[1:]):
        dist += l2_dist(i, j)
    return dist


def gps_error(p_t, t_g):
    v = list(map(velocity, p_t[:-1], p_t[1:]))  # ds/dt
    v.append((0, 0))  # Stop velocity at last point

    # Which velocity vector for each t_g
    t = [i[2] for i in p_t]  # Actual time stamps
    anchor_idxs = [len(t) - 1 - [i >= j for j in t[::-1]].index(True) for i in t_g]

    # Find points at GPS times
    a = get_gps_pt(t_g[2], t[anchor_idxs[2]], v[anchor_idxs[2]], p_t[anchor_idxs[2]])

    t_pick = []
    v_pick = []
    p_pick = []
    for k in anchor_idxs:
        t_pick.append(t[k])
        v_pick.append(v[k])
        p_pick.append(p_t[k])

    p_g = list(map(get_gps_pt, t_g, t_pick, v_pick, p_pick))
    dist_run = path_distance(p_t)
    dist_gps = path_distance(p_g)
    err_percent = (1-dist_gps/dist_run)*100
    return err_percent


def main():
    # ip_phrase = []
    # n = None
    # for line in sys.stdin:
    #     ip_num = [int(i) for i in line.split(' ')[0:]]
    #     ip_phrase.append(ip_num)
    #     if not n:
    #         n = ip_num[0]
    #         l = 0
    #     l += 1
    #     if l > n:
    #         break


    ip_phrase = [[6, 2], [0, 0, 0], [0, 3, 3], [-2, 5, 5], [0, 7, 7], [2, 5, 9], [0, 3, 11]]

    # p = [(0, 0), (1, 1), (4, 7), (6, 10), (5, 7), (3, -1), (0, -4), (-2, -1), (-3, 2), (2, 5), (-1, 13)]
    # t = np.arange(0, 32, 3)

    p_t, dg, n = parse_ip(ip_phrase)  # each recording is a tuple (xi, yi, ti)

    t_g = [i for i in range(0, p_t[-1][-1], dg)]  # GPS time stamps, start at 0 and ...
    t_g.append(p_t[-1][-1])  # end with last t

    E_percent = gps_error(p_t, t_g)
    print(E_percent)
    return 0


if __name__ == "__main__":
    main()
