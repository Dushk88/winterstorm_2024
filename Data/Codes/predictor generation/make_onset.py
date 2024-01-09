

import eelbrain
import glob
import os
import numpy as np
from eelbrain import *
import matplotlib.pyplot as plt
import pandas

separator = '/'
stimuli_directory = 'Volumes/Expansion/Winterstorm/MEG/Data/stimuli'
saving_directory = 'Volumes/Expansion/Winterstorm/MEG/Data/predictors'
textgrid_location = 'Volumes/Expansion/Winterstorm/MEG/Data/stimuli/alignments'

stimNames = glob.glob(os.path.join(stimuli_directory, '*' + '.wav'))


for filename in stimNames:
    stimulusName1 = filename.split(separator)[-1]
    stimulusName = stimulusName1.split('.wav')[0]

    # read the textgrid csv file
    textgrid_name = textgrid_location + stimulusName + '.csv'
    raw_textgrid = pandas.read_csv(textgrid_name)

    # remove silence annotations
    textgriddata = raw_textgrid.loc[raw_textgrid['text'] != 'sp']

    # generate word onsets dataset object
    dswords = Dataset()
    temp_data = textgriddata[textgriddata['tier'] == 'words']['tmin'].to_list()
    dswords['time'] = eelbrain.Var(np.asarray(temp_data))
    dswords['word'] = [True] * len(dswords['time'])
    dswords['value'] = np.ones(len(dswords['time']))

    eelbrain.save.pickle(dswords, os.path.join(saving_directory, stimulusName + '|word' + '.pickle'))

    # generate phoneme onsets dataset object
    dsphonems = Dataset()
    temp_data = textgriddata[textgriddata['tier'] == 'phones']['tmin'].to_list()
    dsphonems['time'] = eelbrain.Var(np.asarray(temp_data))
    dsphonems['phoneme'] = [True] * len(dsphonems['time'])
    dsphonems['value'] = np.ones(len(dsphonems['time']))
    eelbrain.save.pickle(dsphonems, os.path.join(saving_directory, stimulusName + '|phoneme' + '.pickle'))

