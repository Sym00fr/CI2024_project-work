# Copyright © 2024 Giovanni Squillero <giovanni.squillero@polito.it>
# https://github.com/squillero/computational-intelligence
# Free under certain conditions — see the license for details.

import numpy as np

# All numpy's mathematical functions can be used in formulas
# see: https://numpy.org/doc/stable/reference/routines.math.html


# Notez bien: No need to include f0 -- it's just an example!
def f0(x: np.ndarray) -> np.ndarray:
    return x[0] + np.sin(x[1]) / 5


def f1(x: np.ndarray) -> np.ndarray: 
    return np.sin(x[0])

def f2(x: np.ndarray) -> np.ndarray: 
    return np.multiply(np.add(-4.96298038190269, -4.801680558775369), np.multiply(x[0], -4.788819956725789 ))


def f3(x: np.ndarray) -> np.ndarray: 
    return np.multiply(-3.7581108710214233, np.multiply(4.05439171552027, x[1]))


def f4(x: np.ndarray) -> np.ndarray:
    return np.multiply(np.sin(np.add(x[1], -4.747206614884439)), 4.906649644328816)


def f5(x: np.ndarray) -> np.ndarray:
    return np.power(np.power(np.subtract(x[0], x[0]), 0.7886202837357699), x[0])


def f6(x: np.ndarray) -> np.ndarray: 
    return np.subtract(np.add(x[1], x[1]), x[0])


def f7(x: np.ndarray) -> np.ndarray:
    return np.divide(np.power(np.add(1.9009667214981012, 1.931586328452286), np.multiply(x[1], x[0])), 0.6811262807731358)


def f8(x: np.ndarray) -> np.ndarray:
    return np.multiply(x[5], np.power(4.634904234718745, 4.64379509168962))
