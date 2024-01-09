"""Predictors based on gammatone spectrograms"""

import eelbrain
import glob
import os
import numpy as np
from eelbrain import *
from trftools.neural import edge_detector


separator = '/'
stimuli_directory = '/Volumes/Expansion/Winterstorm/MEG/Data/stimuli'
saving_directory = '/Volumes/Expansion/Winterstorm/MEG/Data/predictors'


stimNames = glob.glob(os.path.join(stimuli_directory, '*' + '.wav'))

for filename in stimNames:

    stimulusName1 = filename.split(separator)[-1]
    stimulusName = stimulusName1.split('.wav')[0]

    gt = load.unpickle(os.path.join(saving_directory, stimulusName+'|gammatone.pickle'))

    # Remove resampling artifacts
    gt = gt.clip(0, out=gt)

    # apply powerlaw compression/log 
    gt=(gt+1).log() # gt**0.6#

    # generate on- and offset detector model
    gt_on = edge_detector(gt, c=30)

    # # 1 band predictors
    eelbrain.save.pickle(gt.sum('frequency'), os.path.join(saving_directory, stimulusName + '|gammatonelog-1.pickle'))
    eelbrain.save.pickle(gt_on.sum('frequency'), os.path.join(saving_directory, stimulusName + '|gammatonelog-on-1.pickle'))

    # 8 band predictors
    x = gt.bin(nbins=8, func=np.sum, dim='frequency')
    eelbrain.save.pickle(x, os.path.join(saving_directory, stimulusName + '|gammatonelog-8.pickle'))

    x = gt_on.bin(nbins=8, func=np.sum, dim='frequency')
    eelbrain.save.pickle(x, os.path.join(saving_directory, stimulusName + '|gammatonelog-on-8.pickle'))
