import os
import os.path
from IPython.display import clear_output
import matplotlib.pyplot as plt
import scipy.signal as signal
import pandas as pd
import numpy as np
from scipy.io.wavfile import read

NEW_SAMPLE_RATE = 200
OUTPUT_DIR = "out/niceRootFolder/"
import math

# Excellent resource on GAF - https://gist.github.com/devitrylouis/eabdda10ea96d81389d42aeeb3f9ab3e
def tabulate(x, y, f):
    return np.vectorize(f)(*np.meshgrid(x, y, sparse=True))


def cos_sum(a, b):
    return (math.cos(a + b))


def sin_sum(a, b):
    return (math.sin(a - b))


def tan_sum(a, b):
    return (math.tan(a + b))

class GAF:

    def __init__(self):
        pass

    def __call__(self, serie, gasf=True):
        min_ = np.amin(serie)
        max_ = np.amax(serie)
        scaled_serie = (serie - min_)/(max_ - min_ + 1)

#        scaled_serie = np.where(scaled_serie >= 1, 1, scaled_serie)
#        scaled_serie = np.where(scaled_serie <= -1, -1, scaled_serie)

        phi = np.arccos(scaled_serie)
        r = np.linspace(0, 1, len(scaled_serie))

        gaf = tabulate(phi, phi, cos_sum if gasf else sin_sum)

        return (gaf, phi, r, scaled_serie)


def checkIfFileExists(path):
    return os.path.isfile(path)


def readAudio(path):
    samplerate, data = read('AudioMNIST/data/' + path)
    duration = len(data) / samplerate
    samples = round(duration * float(NEW_SAMPLE_RATE))
    new_data = signal.resample(data, samples)
    new_time_vector = np.arange(0, duration, 1 / NEW_SAMPLE_RATE)
    return pd.DataFrame(new_data).fillna(0).to_numpy(), duration, new_time_vector, NEW_SAMPLE_RATE


def drawGAF(X, GASF=True, fileNameToSave=None):
    wav_path = "gasf_wav/" if GASF else "gadf_wav/"
    gaf_path = "gasf/" if GASF else "gadf/"
    gaf_title = "GASF" if GASF else "GADF"
    gaf_map_path = "gasf_map/" if GASF else "gadf_map/"
    pathsToCheck = [OUTPUT_DIR + wav_path + fileNameToSave + '_o.jpg', OUTPUT_DIR + gaf_path + fileNameToSave + '.jpg',
                    OUTPUT_DIR + gaf_map_path + fileNameToSave + '_map.jpg']
    if (checkIfFileExists(pathsToCheck[0]) and checkIfFileExists(pathsToCheck[1]) and checkIfFileExists(
            pathsToCheck[2])):
        return {"filename": False}
    gaf = GAF()
    g, _, _, _ = gaf(X, GASF)

    plt.figure(figsize=(16, 8))
    plt.subplot(121)
    plt.plot(X)
    if fileNameToSave is not None:
        plt.savefig(OUTPUT_DIR + wav_path + fileNameToSave + '_o.jpg')
    plt.title("Original", fontsize=16)
    plt.subplot(122)
    plt.imshow(g, cmap='gray', origin='lower')
    if fileNameToSave is not None:
        plt.imsave(OUTPUT_DIR + gaf_path + fileNameToSave + '.jpg', g, cmap='gray')
    plt.title(gaf_title, fontsize=16)
    plt.savefig(OUTPUT_DIR + gaf_map_path + fileNameToSave + '_map.jpg')
    plt.show()
    plt.close()


def costly_simulation(row):
    clear_output(wait=True)
    if not row['index'] or not row['path'] or not row['filename'] or not row['speaker']:
        return {"filename": False}
    print(f"2Attempting: {row['index']}: {row['path']}")
    data, duration, time, samplerate = readAudio(row['speaker'] + "/" + row['path'])
    drawGAF(data, True, row['filename'] + "_gasf")
    drawGAF(data, False, row['filename'] + "_gadf")
