import numpy as np
import pytest
from src.fec import *

TEST_DATA_COMB = [
    {
    "TEST_NUM": 3,
    "COMB_NUM": 1,
    "T": [[0,0,0,0],[1,1,0,0],[1,0,0,1]],
    "L": [[0,0],[1,0],[0,1]],
    "GET_T" : [np.array([0,0,0,0,0,0,0,0,0,0]),np.array([0,0,1,0,0,0,0,0,0,0]),np.array([0,0,0,0,0,0,0,0,1,0])],
    "GET_L" : [np.array([0,0,0,0,0,0,0,0,0,0]),np.array([1,1,1,1,1,0,0,0,0,0]),np.array([0,0,0,0,0,1,1,1,1,1])],
    },
    {
    "TEST_NUM": 3,
    "COMB_NUM": 2,
    "T": [[0,0,0,0,0,0,0,0],[1,1,0,0,0,0,0,0],[1,1,0,0,1,0,0,1]],
    "L": [[0,0,0,0],[1,0,0,0],[0,1,1,0]],
    "GET_T" : [np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]),np.array([0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]),np.array([0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0])],
    "GET_L" : [np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]),np.array([1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]),np.array([0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0])],
    },
]

TEST_DATA_CONC = [
    {
    "TEST_NUM": 4,
    "T": [[0,0,0,0,0,0,0,0],[1,1,0,0,0,0,0,0],[0,0,0,0,1,0,0,1],[1,0,0,0,1,0,0,1]],
    "L": [[0,0],[1,0],[0,1],[1,1]],
    "GET_T" : [np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]),np.array([0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0]),np.array([0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0]),np.array([0,0,0,1,0,0,0,0,1,1,1,1,0,0,0,0,0,0])],
    "GET_L" : [np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]),np.array([1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0]),np.array([0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1]),np.array([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])],
    },
]

def test_CONB():
    for test_data in TEST_DATA_COMB:
        c = CombCode([FIVE() for i in range(test_data["COMB_NUM"])])
        for i in range(test_data["TEST_NUM"]):
            assert 0==sum(np.abs(c.get_T(test_data["T"][i]) - test_data["GET_T"][i]))
            assert 0==sum(np.abs(c.get_L(test_data["L"][i]) - test_data["GET_L"][i]))

def test_CONC():
    for test_data in TEST_DATA_CONC:
        c1 = CombCode([BIT_FLIP(),BIT_FLIP(),BIT_FLIP()])
        c0 = PHASE_FLIP()
        c = ConcCode([c0,c1])
        for i in range(test_data["TEST_NUM"]):
            print(test_data["GET_T"][i])
            assert 0==sum(np.abs(c.get_T(test_data["T"][i]) - test_data["GET_T"][i]))
            assert 0==sum(np.abs(c.get_L(test_data["L"][i]) - test_data["GET_L"][i]))