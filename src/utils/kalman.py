from filterpy.kalman import KalmanFilter
import numpy as np

def apply_kalman_filter(data):
    kf = KalmanFilter(dim_x=2, dim_z=1)
    kf.x = np.array([0., 0.])  # initial state (location and velocity)
    kf.F = np.array([[1., 1.],
                     [0., 1.]])  # state transition matrix
    kf.H = np.array([[1., 0.]])  # measurement function
    kf.P *= 1000.  # covariance matrix
    kf.R = 100  # measurement noise
    kf.Q = np.array([[0.1, 0.1], [0.1, 0.1]])  # process noise

    filtered_data = []
    for value in data:
        kf.predict()
        kf.update(value)
        filtered_data.append(kf.x[0])
    return filtered_data