import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from ligotools import readligo

def test_readligo_structure():
    fn_H1 = "data/H-H1_LOSC_4_V2-1126259446-32.hdf5"
    strain, time, dq = readligo.loaddata(fn_H1, 'H1')
    assert len(strain) == len(time)
    assert isinstance(dq, dict)

def test_readligo_timing():
    fn_H1 = "data/H-H1_LOSC_4_V2-1126259446-32.hdf5"
    strain, time, dq = readligo.loaddata(fn_H1, 'H1')
    assert abs(time[0] - 1126259446.0) < 10