# -*- coding: utf-8 -*-
from numpy import random
import matplotlib.pyplot as plt

def main():
    var_v = 1
    var_w = 2
    n = 100

    true_values = [0]
    observed_values = [0]
    for v,w in zip(random.normal(0,var_v,n), random.normal(0,var_w,n)):
        x = true_values[-1] + v
        true_values.append(x)
        observed_values.append(x + w)

    p = 0
    estimated_value = [0]
    for y1 in observed_values[1:]:
        x_ = estimated_value[-1]
        p_ = p + var_v
        g = p_/(p_ + var_w)
        p = (1 - g)*p_
        estimated_value.append(x_ + g*(y1 - x_))

    plt.plot(true_values, label="true")
    plt.plot(observed_values, label="observed")
    plt.plot(estimated_value, label="estimated")
    plt.title("Kalman filter test")
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == '__main__':
    main()
