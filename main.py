#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.1.3),
    on 七月 26, 2023, at 10:22
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

from random import random 
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

import pandas as pd
from Experiment.Experiment import Experiment # See ./Experiment/Experiment.py


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2023.1.3'
expName = 'LossAver_experiment'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{np.random.randint(0, 999999):06.0f}",
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='',
    savePickle=False, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
# winsize = (1280, 720)
winsize = (2560, 1440)
win = visual.Window(
    size=winsize, 
    # size=(1920, 1080), 
    # fullscr=False,
    fullscr=True,
    screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
    backgroundImage='', backgroundFit='none',
    blendMode='avg', useFBO=True, 
    units='pix')

win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

G = 2000
Exp = Experiment(win, thisExp, routineTimer, defaultKeyboard, size = winsize, G=G)

## instruction
# Exp.instruction()
# ---------------Text Stimuli-----------------
fixation = {"name": "fixation_1", 
             "text": "+", 
             "pos": (0,0), 
             "height": 48}

Hold = {"name": "Hold", 
             "text": "Hold on.", 
             "pos": (0,0), 
             "height": 48}

End = {"name": "tmp_End", 
             "text": "Thank You So Much.", 
             "pos": (0,0), 
             "height": 48}

# ---------------Setup-----------------
n_bisect = 10 
# n_bisect = 8 # 10
params = ["L", "x1pos", "x1neg"] 
# params = ["L","x1neg"] # for testing
# Initial parameter bounds 
bounds = {
    "L": np.array((-G*2, 0)),
    "x1pos": np.array((0,G)),
    "x1neg": np.array((-G,0))
}  
minimal_step = 5 # stop criterion, 5
trial = 0

## ---------Experiment Start-----------
# instruction
Exp.instruction()
for param in params:
    bound = bounds[param]
    bisect_bound = bounds[param].copy()
    PEST_trial = 0
    bisect_trial = 0
    PEST_params = {"eval_quan":int(0),
                "step": int(0),
                "last_choices": [None]*4,
                "extra_step":False}
    PESTconv = False
    converge = False
    # Exp.text_only(text_config=Hold, duration=0.5)
    while not converge:
        trial += 1
        if PEST_trial == bisect_trial: # random order
            run_PEST = random() > 0.5
        else:
            run_PEST = (PEST_trial < bisect_trial)

        Exp.text_only(text_config=fixation, duration=0.5)
        if run_PEST:
            PEST_trial += 1
            # PESTconv = True
            if not PESTconv:
                PEST_params, PESTconv = Exp.PESTTrial(trial, PEST_trial, param, bound, PEST_params, minimal_step)
            else: # if PEST converge before bisection end
                pass
        else:
            bisect_trial += 1
            bisect_bound = Exp.BisectionTrial(trial, bisect_trial, param, bisect_bound, n_bisect)
        # Slider Trial
        if (bisect_trial in [3, 6]) and (PEST_trial == bisect_trial): 
            trial += 1
            Exp.text_only(text_config=fixation, duration=0.5)
            Exp.SliderTrial(trial, bisect_trial, param, bisect_bound)
        
        converge = PESTconv & (bisect_trial >= (n_bisect+2))

for method in ["Bisection", "PEST", "Slider"]:
    Exp.RecordFinalEst(method)
Exp.text_only(text_config=End, duration=1)


# ## reward
# final_reward = np.random.choice(Exp.subj_correctness_list)
# Exp.text_only(text_config={"name": "reward", 
#                         "text": f'實驗結束\n本實驗得到的實驗報酬是 {final_reward} 法幣\n請通知實驗人員', 
#                         "height": 36,
#                         "pos": (0,0),
#                         "eeg_trigger": chr(98)}, duration=5)



