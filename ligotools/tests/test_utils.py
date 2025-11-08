import numpy as np
import os
from ligotools.utils import whiten, write_wavfile, reqshift

def test_whiten_basic():
    # Create a simple fake strain signal
    strain = np.sin(np.linspace(0, 2*np.pi, 1024))
    interp_psd = lambda f: np.ones_like(f)
    dt = 1.0 / 4096

    white = whiten(strain, interp_psd, dt)
    
    # length must match
    assert len(white) == len(strain)
    # mean should be near zero
    assert abs(np.mean(white)) < 1e-3

def test_reqshift_changes_phase():
    t = np.linspace(0, 1, 1024)
    data = np.sin(2 * np.pi * 50 * t)
    shifted = reqshift(data, fshift=100, sample_rate=1024)
    
    # Same shape, but phase shifted signal
    assert len(shifted) == len(data)
    assert not np.allclose(data, shifted)

def test_write_wavfile_creates_file(tmp_path):
    # Create fake data
    filename = tmp_path / "test.wav"
    data = np.random.randn(1024)
    fs = 4096
    write_wavfile(filename, fs, data)
    
    # Check file created
    assert os.path.exists(filename)
    assert filename.stat().st_size > 0