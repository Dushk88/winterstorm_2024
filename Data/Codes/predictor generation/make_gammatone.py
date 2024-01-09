"""Generate high-resolution gammatone spectrograms"""
from pathlib import Path
import eelbrain
import trftools
from eelbrain import *
import os
import glob
from trftools import gammatone_bank

separator = '/'
stimuli_directory = '/Volumes/Expansion/Winterstorm/MEG/Data/stimuli'
saving_directory = '/Volumes/Expansion/Winterstorm/MEG/Data/predictors'

stimNames = glob.glob(os.path.join(stimuli_directory, '*' + '.wav'))

for filename in stimNames:

    stimulusName1 = filename.split(separator)[-1]
    stimulusName = stimulusName1.split('.wav')[0]

    wav = eelbrain.load.wav(filename) # load .wav file
    print([filename,wav.min(),wav.max()])
    gt = gammatone_bank(wav, 20, 5000, 256, location='left', pad=False) # apply gammatone filter bank
    gt = resample(gt, 1000) # resample to 1000 Hz

    gt = gt[:, 0:60] # use only 0-60 s data

    eelbrain.save.pickle(gt, os.path.join(saving_directory, stimulusName + '|gammatone' + '.pickle')) # save



