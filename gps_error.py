#!/usr/bin/env python3
import sys


def get_input():
    """
    Reads input from stdin into data containers.
    First line: n t
    Following lines: xi yi ti
    :return: GPS time interval, list of actual datapoint tuples
    """
    # Read first line
    # n : Num of positions on actual running path
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
    """
    Find velocity vector from a to b
    :param a: tuple (xa, ya, ta)
    :param b: tuple (xb, yb, tb)
    :return: velocity: tuple (vx, vy)
    """
    dt = float(b[2] - a[2])
    return tuple([(b[0] - a[0]) / dt, (b[1] - a[1]) / dt])


def get_gps_pt(t_gps, t_run, vg, p0):
    """
    Calculate GPS position recording for a given GPS time stamp.
    p = p0 + v * dt
    :param t_gps: GPS time stamp
    :param t_run: Most recent actual time stamp
    :param vg: Velocity vector at reference point at t_run
    :param p0: Reference point at t_run
    :return: GPS point: tuple (x_gps, y_gps, t_gps)
    """
    dt = float(t_gps - t_run)  # time interval
    return tuple([p0[0] + vg[0] * dt, p0[1] + vg[1] * dt, t_gps])  # GPS point recorded


def l2_dist(p, q):
    """ Computes Euclidean distance between 2 points"""
    return ((q[0] - p[0]) ** 2 + (q[1] - p[1]) ** 2) ** 0.5


def path_distance(points):
    """
    Computes total distance spanned by a sequence of datapoints
    :param points: all datapoints on the path -- list of tuples
    :return: dist: distance spanned by path
    """
    dist = 0
    for p, q in zip(points[:-1], points[1:]):
        dist += l2_dist(p, q)
    return dist


def gps_error(pts_run, T_gps):
    """
    Computes percentage error incurred by GPS distance in comparison to the actual running path distance.
    :param pts_run: all datapoints of run -- list of tuples
    :param T_gps: GPS sampling time period -- scalar
    :return: Percentage error -- scalar
    """
    # get all GPS time stamps
    t_g = list(range(0, pts_run[-1][-1], T_gps))  # GPS time stamps, start at 0 and ...
    t_g.append(pts_run[-1][-1])  # end with last t_run

    # velocity vectors at running positions
    v = list(map(velocity, pts_run[:-1], pts_run[1:]))  # ds/dt
    v.append((0, 0))  # stop velocity at final position

    # which velocity vector for each t_g?
    t_run_all = [i[2] for i in pts_run]  # actual time stamp sequence
    # selected index for each GPS time stamp:
    anchor_idxs = [len(t_run_all) - 1 - [i >= j for j in t_run_all[::-1]].index(True) for i in t_g]
    # selected index corresponds to  most recent actual time stamp (includes coinciding time stamps)

    # Select actual time stamp, velocity vector, running data position -- corresponding to anchoring indices.
    t_run_ref = []
    v_seg = []
    pts_ref = []
    for k in anchor_idxs:
        t_run_ref.append(t_run_all[k])
        v_seg.append(v[k])
        pts_ref.append(pts_run[k])

    pts_gps = list(map(get_gps_pt, t_g, t_run_ref, v_seg, pts_ref))  # compute GPS point at GPS time stamp
    dist_run = path_distance(pts_run)  # actual distance
    dist_gps = path_distance(pts_gps)  # GPS distance
    err_percent = (1-dist_gps/dist_run)*100  # error percent in GPS distance
    return err_percent


def main():
    T_gps, p_t = get_input()  # read input = running data
    print(gps_error(p_t, T_gps))  # print output = percentage error of gps distance


if __name__ == "__main__":
    main()
