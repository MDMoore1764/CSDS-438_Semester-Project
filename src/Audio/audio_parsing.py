import os
import numpy as np
from scipy.io import wavfile


def load_waveform(path: str) -> tuple[int, np.ndarray, int]:
    samplerate, data = wavfile.read(path)
    n_channels = data.shape[1]

    return samplerate, data, n_channels


output_dir = "predictions"


def encode_waveform_to_song(waveform: np.ndarray, sample_rate: int, path: str):
    full_filename = os.path.join(output_dir, path)
    wavfile.write(full_filename, sample_rate, waveform)
