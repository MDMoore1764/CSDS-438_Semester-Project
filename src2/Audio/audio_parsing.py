import os
import numpy as np
from scipy.io import wavfile


def int16_to_uint16(input: np.ndarray[np.int16]):
    uint16 = input + 2**15
    return uint16.astype(np.uint16)


def uint16_to_int16(input: np.ndarray[np.uint16]):
    int16 = input - 2**15
    return int16.astype(np.int16)


def float32_to_int16(input: np.ndarray[np.float32]):
    int16 = input * 2**15
    return int16.astype(np.int16)


def uint16_to_float32(input: np.ndarray[np.uint16]):
    float32 = input / 2**16 - 1
    return float32


def get_waveform_length(data_root: str):
    # if max_length is not None:
    #     return max_length
    max_length = 0

    for file in os.listdir(data_root):
        if file.endswith(".wav"):
            file_path = os.path.join(data_root, file)
            size = os.path.getsize(file_path)
            if size > max_length:
                max_length = size

    return max_length


def load_normalized_waveform(path: str) -> tuple[int, np.ndarray, int]:
    dir = os.path.dirname(path)

    # TODO: what do I do about different sample rates? Need to FILL.

    # length = get_waveform_length(dir)
    samplerate, data = wavfile.read(path)
    n_channels = data.shape[1]

    if n_channels > 1:
        data = data.mean(axis=1)
        data = data / np.max(data, axis=0)
        # data: np.ndarray[np.float32] = data.astype(np.float16)

    # data = data.flatten()
    # data = np.pad(data, (0, length - len(data)))
    # data = int16_to_uint16(data)
    # data = uint16_to_float32(data)

    return samplerate, data


output_dir = "predictions"


def encode_waveform_to_song(waveform: np.ndarray, sample_rate: int, path: str):
    int16 = float32_to_int16(waveform)
    full_filename = os.path.join(output_dir, path)
    wavfile.write(full_filename, sample_rate, int16)


sr, data = load_normalized_waveform("data/song.wav")

encode_waveform_to_song(data, sr, "song.wav")
