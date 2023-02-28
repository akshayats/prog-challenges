#!/usr/bin/env python3
import sys


def get_input():
    # Read first line
    # n : Num of positions on running path
    # T_gps : GPS recording time period
    n, T_gps = [int(i) for i in input().split(' ')]
    # Read running data
    datalist = []
    for line in sys.stdin:
        datapoint = [int(i) for i in line.split(' ')[0:]]
        datalist.append(tuple(datapoint))
        if len(datalist) >= n:
            break
    return T_gps, datalist


def velocity(a, b):
    dt = float(b[2] - a[2])
    return tuple([(b[0] - a[0]) / dt, (b[1] - a[1]) / dt])


def get_gps_pt(t_gps, t_run, vg, p0):
    dt = float(t_gps - t_run)  # delta between gps and most recent t_run
    return tuple([p0[0] + vg[0] * dt, p0[1] + vg[1] * dt, t_gps])  # GPS point recorded


def l2_dist(p, q):
    return ((q[0] - p[0]) ** 2 + (q[1] - p[1]) ** 2) ** 0.5


def path_distance(points):
    dist = 0
    for p, q in zip(points[:-1], points[1:]):
        dist += l2_dist(p, q)
    return dist


def gps_error(pts_run, T_gps):
    # All GPS time stamps
    t_g = list(range(0, pts_run[-1][-1], T_gps))  # GPS time stamps, start at 0 and ...
    t_g.append(pts_run[-1][-1])  # end with last t_run

    # Velocity vectors at running positions
    v = list(map(velocity, pts_run[:-1], pts_run[1:]))  # ds/dt
    v.append((0, 0))  # Stop velocity at final position

    # Which velocity vector for each t_g?
    t_run_all = [i[2] for i in pts_run]  # Actual time stamps
    anchor_idxs = [len(t_run_all) - 1 - [i >= j for j in t_run_all[::-1]].index(True) for i in t_g]

    t_run_ref = []
    v_seg = []
    pts_ref = []
    for k in anchor_idxs:
        t_run_ref.append(t_run_all[k])
        v_seg.append(v[k])
        pts_ref.append(pts_run[k])

    pts_gps = list(map(get_gps_pt, t_g, t_run_ref, v_seg, pts_ref))
    dist_run = path_distance(pts_run)
    dist_gps = path_distance(pts_gps)
    err_percent = (1-dist_gps/dist_run)*100
    return err_percent


def main():
    T_gps, p_t = get_input()
    print(gps_error(p_t, T_gps))


if __name__ == "__main__":
    main()
