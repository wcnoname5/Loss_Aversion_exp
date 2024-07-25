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
winsize = (1280, 720)
win = visual.Window(
    size=winsize, 
    # size=(1920, 1080), 
    fullscr=False,
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

Exp = Experiment(win, thisExp, routineTimer, defaultKeyboard, size = winsize)

## instruction
# Exp.instruction()
# ---------------Text Stimuli-----------------
fixation = {"name": "fixation_1", 
             "text": "+", 
             "pos": (0,0), 
             "height": 48}

End = {"name": "tmp_End", 
             "text": "Thank You So Much.", 
             "pos": (0,0), 
             "height": 48}

# ---------------Setup-----------------
n_bisect = 10 
G = 2000
param = ["L", "x1pos", "x1neg"]
stumuli_path = "./Stimuli" 
param_est = {} #store estimations
bounds = [np.array((-G*2, 0)),
          np.array((0,G)),
          np.array((-G,0))]
minimal_step = 5 # stop crition 
# step_size = 512

def get_color(value): # *int -> str
    color_map = {True: "blue", False: "red"}
    return color_map[value>=0]

def PEST_only(param, stumuli_path, bounds, minimal_step):
    trial = 0 # trial counting 
    def init_step_size(bound): 
        # Ensure n is greater than 1
        n = bound[1] - bound[0]
        power = 1
        while power * 2 < n/10:
            power *= 2
        step = power*10
        return step
    
    for index, param_name in enumerate(param):
        # Stimuli Setup
        indiff_bound = bounds[index]
        filepath = f"{stumuli_path}/{param_name}.png"
        Exp.choice_image.image = filepath
        if param_name == "L":
            Exp.text_Bmid_Choice.setText("", log=False)
        elif param_name == "x1pos":
            Exp.text_Adown_Choice.setText("", log=False)
        elif param_name == "x1neg":
            indiff_bound[0] = param_est['L']
            Exp.text_Adown_Choice.setText(f"{param_est['L']}", log=False)
        
        # PEST settings
        PEST_trial = 0
        strat_point = sum(indiff_bound)//2 # Midpoint as starting point
        step = init_step_size(indiff_bound) # step_size
        print(f"Bound:{indiff_bound}; Inital Setp Size: {step}" )
        last_choices = [None]*4 # index 0 has nearest history
        extra_step = False

        # PEST iteration
        while step > minimal_step:
            trial += 1
            PEST_trial += 1

            # PEST update
            if PEST_trial==1:
                eval_quan = strat_point
            else:
                ## Calculating steps
                if PEST_trial <4:
                    if (last_choices[0] != last_choices[1]) : # Reversal
                        step = step//2
                    elif (PEST_trial == 3) & (last_choices[1] == last_choices[2]):
                        step = step*2 # double
                    else: pass
                else:
                    # Reversal:half the step size
                    if (last_choices[0] != last_choices[1]):
                        step = step//2
                        ## Reversal after Doubled: extra step
                        if (last_choices[1] == last_choices[2] == last_choices[3]):
                            extra_step = True 
                    # Same direction for 3 streak: Double
                    elif (last_choices[0] == last_choices[1] == last_choices[2]):
                        if extra_step:
                            extra_step = False
                        else:
                            step = step * 2

                direction = int(last_choices[0]=="Left")*2 - 1 # T:1, F:-1
                if (param_name == "L"):
                    direction = -direction
                else: pass
                # Update Lottery parir value
                eval_quan = eval_quan + (direction * step)

            # Record Trial Information
            Exp.thisExp.addData('Trial', trial)
            Exp.thisExp.addData('Task_Type', "PEST")
            Exp.thisExp.addData('Estimate', param_name)
            Exp.thisExp.addData('Iteration', PEST_trial)
            Exp.thisExp.addData('Step_Size', step)                    
            Exp.thisExp.addData('Lottery_value', eval_quan) # updated lottery value in this trial
            
            # Choice Pair Update
            if param_name == "L":
                Exp.text_Adown_Choice.setText(f"{int(eval_quan)}", log=False)
                Exp.text_Adown_Choice.setColor(get_color(eval_quan), colorSpace='rgb')
            elif param_name == "x1pos":
                Exp.text_Bmid_Choice.setText(f"{int(eval_quan)}", log=False)
                Exp.text_Bmid_Choice.setColor(get_color(eval_quan), colorSpace='rgb')
            elif param_name == "x1neg":
                Exp.text_Bmid_Choice.setText(f"{int(eval_quan)}", log=False)
                Exp.text_Bmid_Choice.setColor(get_color(eval_quan), colorSpace='rgb')

            # fixation + choice
            Exp.text_only(text_config=fixation, duration=0.5)
            prev_choice = Exp.choice()

            # Update choice history
            last_choices.insert(0, prev_choice)
            last_choices.pop()

            # Exp.thisExp.addData('indiff_bound', indiff_bound)
            # record next trial
            Exp.thisExp.nextEntry()

        param_est[param_name] = eval_quan

def Bisection_only(n_bisect, param, stumuli_path, bounds):
    trial = 0 # trial counting 
    for index, param_name in enumerate(param):
        # Stimuli Setup 
        indiff_bound = bounds[index]
        filepath = f"{stumuli_path}/{param_name}.png"
        Exp.choice_image.image = filepath
        if param_name == "L":
            Exp.text_Bmid_Choice.setText("", log=False)
        elif param_name == "x1pos":
            Exp.text_Adown_Choice.setText("", log=False)
        elif param_name == "x1neg":
            indiff_bound[0] = param_est['L']
            Exp.text_Adown_Choice.setText(f"{param_est['L']}", log=False)
        
        for bisect in range(n_bisect):
            trial += 1
            eval_quan = sum(indiff_bound)//2 # Bisection
            # Record Trial Information
            Exp.thisExp.addData('Trial', trial)
            Exp.thisExp.addData('Task_Type', "Bisection")
            Exp.thisExp.addData('Estimate', param_name)
            Exp.thisExp.addData('Iteration', bisect+1)
            Exp.thisExp.addData('Lottery_value', eval_quan) # updated lottery value in this trial

            # Choice Pair Update
            if param_name == "L":
                Exp.text_Adown_Choice.setText(f"{int(eval_quan)}", log=False)
                Exp.text_Adown_Choice.setColor(get_color(eval_quan), colorSpace='rgb')
            elif param_name == "x1pos":
                Exp.text_Bmid_Choice.setText(f"{int(eval_quan)}", log=False)
                Exp.text_Bmid_Choice.setColor(get_color(eval_quan), colorSpace='rgb')
            elif param_name == "x1neg":
                Exp.text_Bmid_Choice.setText(f"{int(eval_quan)}", log=False)
                Exp.text_Bmid_Choice.setColor(get_color(eval_quan), colorSpace='rgb')

            # Show Fixation + choice
            Exp.text_only(text_config=fixation, duration=0.5)
            prev_choice = Exp.choice()

            # Update bound
            if (param_name == "L"):
                if (prev_choice == "Right"): # lower bound
                    indiff_bound[0] = eval_quan 
                else: # choose "Left"
                    indiff_bound[1] = eval_quan
            else:
                if (prev_choice == "Right"):
                    indiff_bound[1] = eval_quan
                else:
                    indiff_bound[0] = eval_quan

            Exp.thisExp.addData('indiff_bound', indiff_bound)
            # record next trial
            Exp.thisExp.nextEntry()
        param_est[param_name] = sum(indiff_bound)//2

Exp.PEST_only(param, stumuli_path, bounds, minimal_step)
Exp.Bisection_only(n_bisect, param, stumuli_path, bounds)
# Bisection_only()
Exp.text_only(text_config=End, duration=1)

# for trial in range(520):

#     ## fixation_1 0.5s
#     Exp.text_only(text_config=fixation1, duration=0.5)

#     ## choice
#     choice_jar = Exp.choice()

#     # -- Prepare stimlus for Routine "jar_reminder" --- 
#     if choice_jar:
#         ## jar_reminder
#         Exp.jar_reminder(choice_jar)

#         ## fixation_2 0.5s
#         Exp.text_only(text_config=fixation2, duration=0.5) f

#         ## get_cues
#         cueslist, ans_jar = Exp.get_cue(trial)

#         ## cue
#         Exp.cues(choice_jar, cueslist)

#         ## fixation_3 0.7s
#         Exp.text_only(text_config=fixation3, duration=0.7)

#         ## feedback 0.5s
#         isCorrect = ans_jar == choice_jar
#         if isCorrect:
#             thisExp.addData('isCorrect', 1)
#             text_feedback = '+200'
#             Exp.subj_correctness_list.append(200)
#         else:
#             thisExp.addData('isCorrect', 0)
#             text_feedback = '+0'
#             Exp.subj_correctness_list.append(0)

#         Exp.text_only(text_config={"name": "feedback", 
#                                "text": text_feedback, 
#                                "height": 72,
#                                "pos": (0,0),
#                                "eeg_trigger": Exp.feedback_trigger[f'{isCorrect}|{choice_jar}|{sum(cueslist)}']}, 
#                                duration=1)
            
#     else:
#         ## miss
#         Exp.text_only(text_config={"name": "missed", 
#                                "text": "Missed", 
#                                "height": 48,
#                                "pos": (0,0),
#                                "eeg_trigger": chr(93)}, duration=0.5)
            
#     if trial == 258: # Break after the trial of no. 259 trial (index = 258)
#         ## break
#         Exp.break_screen()

#     # record next trial
#     Exp.thisExp.nextEntry()

# ## reward
# final_reward = np.random.choice(Exp.subj_correctness_list)
# Exp.text_only(text_config={"name": "reward", 
#                         "text": f'實驗結束\n本實驗得到的實驗報酬是 {final_reward} 法幣\n請通知實驗人員', 
#                         "height": 36,
#                         "pos": (0,0),
#                         "eeg_trigger": chr(98)}, duration=5)



