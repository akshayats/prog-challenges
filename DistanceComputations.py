import matplotlib.pyplot as plt
import numpy as np


def velocity(pts, t):
    return np.diff(np.asarray(pts), axis=0) / np.diff(t.astype(float))[:, np.newaxis]


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

    # Visualise the path
    x, y = zip(*p)
    plt.plot(x, y, 'o-')
    plt.plot(q[:, 0], q[:, 1], '.-')
    plt.grid('on')
    plt.show()

    # Percentage distance error
    dist_run = path_distance(np.array(p))  # Actual path distance
    dist_gps = path_distance(q)  # GPS path distance
    err = (1 - dist_gps / dist_run) * 100
    print("Percentage error in distance by GPS = {}%".format(err))
    return err


def main():
    p = [(0, 0), (1, 1), (4, 7), (6, 10), (5, 7), (3, -1), (0, -4), (-2, -1), (-3, 2), (2, 5), (-1, 13)]
    t = np.arange(0, 32, 3)
    g = np.arange(0, 32, 2)
    E = gps_error(p, t, g)
    return 0


if __name__ == "__main__":
    main()
