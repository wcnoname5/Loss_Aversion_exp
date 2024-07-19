#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.2.3),
    on July 19, 2024, at 17:13
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
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# Store info about the experiment session
psychopyVersion = '2023.2.3'
expName = '2fac'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'date': data.getDateStr(),  # add a simple timestamp
    'expName': expName,
    'psychopyVersion': psychopyVersion,
}


def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # temporarily remove keys which the dialog doesn't need to show
    poppedKeys = {
        'date': expInfo.pop('date', data.getDateStr()),
        'expName': expInfo.pop('expName', expName),
        'psychopyVersion': expInfo.pop('psychopyVersion', psychopyVersion),
    }
    # show participant info dialog
    dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # restore hidden keys
    expInfo.update(poppedKeys)
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='E:\\Proj\\Loss_Aversion_exp\\exp_scripts\\psyexp_files\\routines.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # this outputs to the screen, not a file
    logging.console.setLevel(logging.EXP)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=logging.EXP)
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=[1280, 720], fullscr=False, screen=0,
            winType='pyglet', allowStencil=False,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='pix'
        )
        if expInfo is not None:
            # store frame rate of monitor if we can measure it
            expInfo['frameRate'] = win.getActualFrameRate()
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'pix'
    win.mouseVisible = True
    win.hideMessage()
    return win


def setupInputs(expInfo, thisExp, win):
    """
    Setup whatever inputs are available (mouse, keyboard, eyetracker, etc.)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    dict
        Dictionary of input devices by name.
    """
    # --- Setup input devices ---
    inputs = {}
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
    # return inputs dict
    return {
        'ioServer': ioServer,
        'defaultKeyboard': defaultKeyboard,
        'eyetracker': eyetracker,
    }

def pauseExperiment(thisExp, inputs=None, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # prevent components from auto-drawing
    win.stashAutoDraw()
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # make sure we have a keyboard
        if inputs is None:
            inputs = {
                'defaultKeyboard': keyboard.Keyboard(backend='ioHub')
            }
        # check for quit (typically the Esc key)
        if inputs['defaultKeyboard'].getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win, inputs=inputs)
        # flip the screen
        win.flip()
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, inputs=inputs, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # restore auto-drawn components
    win.retrieveAutoDraw()
    # reset any timers
    for timer in timers:
        timer.reset()


def run(expInfo, thisExp, win, inputs, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    inputs : dict
        Dictionary of input devices by name.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = inputs['ioServer']
    defaultKeyboard = inputs['defaultKeyboard']
    eyetracker = inputs['eyetracker']
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "choice_task" ---
    Loss_image = visual.ImageStim(
        win=win,
        name='Loss_image', units='pix', 
        image='../Stimuli/L.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1280, 720),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    choice_resp = keyboard.Keyboard()
    Left = visual.TextStim(win=win, name='Left',
        text='Left Choice',
        font='Open Sans',
        units='pix', pos=(-300, 200), height=32.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    Right = visual.TextStim(win=win, name='Right',
        text='Right Choice',
        font='Open Sans',
        units='pix', pos=(+300, 200), height=32.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    confirm_text_2fac = visual.TextStim(win=win, name='confirm_text_2fac',
        text='',
        font='Open Sans',
        pos=(0, -200), height=30.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    confirm_resp = keyboard.Keyboard()
    
    # --- Initialize components for Routine "Fixation" ---
    fix_stumili = visual.ShapeStim(
        win=win, name='fix_stumili', vertices='cross',units='pix', 
        size=(20, 20),
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=None, depth=0.0, interpolate=True)
    
    # --- Initialize components for Routine "slider_task" ---
    inform_text = visual.TextStim(win=win, name='inform_text',
        text='Choose ?',
        font='Open Sans',
        pos=(0, 200), height=50.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    slider = visual.Slider(win=win, name='slider',
        startValue=None, size=(720, 80), pos=(0, 0), units=win.units,
        labels=["0", "100"], ticks=(1, 2, 3, 4, 5), granularity=0.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=50.0,
        flip=False, ori=0.0, depth=-1, readOnly=False)
    confirm_text = visual.TextStim(win=win, name='confirm_text',
        text='',
        font='Open Sans',
        pos=(0, -200), height=30.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    confirm_resp_2 = keyboard.Keyboard()
    
    # create some handy timers
    if globalClock is None:
        globalClock = core.Clock()  # to track the time since experiment started
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6)
    
    # --- Prepare to start Routine "choice_task" ---
    continueRoutine = True
    # update component parameters for each repeat
    choice_resp.keys = []
    choice_resp.rt = []
    _choice_resp_allKeys = []
    thisExp.addData('choice_task.started', globalClock.getTime())
    # Run 'Begin Routine' code from code_2
    event.clearEvents('keyboard')
    KeyResponse = False
    confirm_text = ""
    left_text_color = "white"
    right_text_color = "white"
    confirm_resp.keys = []
    confirm_resp.rt = []
    _confirm_resp_allKeys = []
    # keep track of which components have finished
    choice_taskComponents = [Loss_image, choice_resp, Left, Right, confirm_text_2fac, confirm_resp]
    for thisComponent in choice_taskComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "choice_task" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Loss_image* updates
        
        # if Loss_image is starting this frame...
        if Loss_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Loss_image.frameNStart = frameN  # exact frame index
            Loss_image.tStart = t  # local t and not account for scr refresh
            Loss_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Loss_image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Loss_image.started')
            # update status
            Loss_image.status = STARTED
            Loss_image.setAutoDraw(True)
        
        # if Loss_image is active this frame...
        if Loss_image.status == STARTED:
            # update params
            pass
        
        # *choice_resp* updates
        waitOnFlip = False
        
        # if choice_resp is starting this frame...
        if choice_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            choice_resp.frameNStart = frameN  # exact frame index
            choice_resp.tStart = t  # local t and not account for scr refresh
            choice_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(choice_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'choice_resp.started')
            # update status
            choice_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(choice_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(choice_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if choice_resp.status == STARTED and not waitOnFlip:
            theseKeys = choice_resp.getKeys(keyList=['f','j'], ignoreKeys=["escape"], waitRelease=False)
            _choice_resp_allKeys.extend(theseKeys)
            if len(_choice_resp_allKeys):
                choice_resp.keys = _choice_resp_allKeys[-1].name  # just the last key pressed
                choice_resp.rt = _choice_resp_allKeys[-1].rt
                choice_resp.duration = _choice_resp_allKeys[-1].duration
        # Run 'Each Frame' code from code_2
        keys = event.getKeys()
        
        if len(keys):
            KeyResponse = True
            if 'f' in keys:
               confirm_text= "A"
               left_text_color = "red"
               right_text_color = "white"
            elif 'j' in keys:
                confirm_text= "B"
                left_text_color = "white"
                right_text_color = "red"
        #        slider.rating = True
        #        KeyResponse = True
        
        # *Left* updates
        
        # if Left is starting this frame...
        if Left.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Left.frameNStart = frameN  # exact frame index
            Left.tStart = t  # local t and not account for scr refresh
            Left.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Left, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Left.started')
            # update status
            Left.status = STARTED
            Left.setAutoDraw(True)
        
        # if Left is active this frame...
        if Left.status == STARTED:
            # update params
            pass
        
        # *Right* updates
        
        # if Right is starting this frame...
        if Right.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Right.frameNStart = frameN  # exact frame index
            Right.tStart = t  # local t and not account for scr refresh
            Right.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Right, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Right.started')
            # update status
            Right.status = STARTED
            Right.setAutoDraw(True)
        
        # if Right is active this frame...
        if Right.status == STARTED:
            # update params
            Right.setColor('white', colorSpace='rgb', log=False)
        
        # *confirm_text_2fac* updates
        
        # if confirm_text_2fac is starting this frame...
        if confirm_text_2fac.status == NOT_STARTED and KeyResponse:
            # keep track of start time/frame for later
            confirm_text_2fac.frameNStart = frameN  # exact frame index
            confirm_text_2fac.tStart = t  # local t and not account for scr refresh
            confirm_text_2fac.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(confirm_text_2fac, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'confirm_text_2fac.started')
            # update status
            confirm_text_2fac.status = STARTED
            confirm_text_2fac.setAutoDraw(True)
        
        # if confirm_text_2fac is active this frame...
        if confirm_text_2fac.status == STARTED:
            # update params
            confirm_text_2fac.setText(f"You've Choose {confirm_text} \n press Space to comfirm" , log=False)
        
        # *confirm_resp* updates
        waitOnFlip = False
        
        # if confirm_resp is starting this frame...
        if confirm_resp.status == NOT_STARTED and tThisFlip >= KeyResponse-frameTolerance:
            # keep track of start time/frame for later
            confirm_resp.frameNStart = frameN  # exact frame index
            confirm_resp.tStart = t  # local t and not account for scr refresh
            confirm_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(confirm_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'confirm_resp.started')
            # update status
            confirm_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(confirm_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(confirm_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if confirm_resp.status == STARTED and not waitOnFlip:
            theseKeys = confirm_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _confirm_resp_allKeys.extend(theseKeys)
            if len(_confirm_resp_allKeys):
                confirm_resp.keys = _confirm_resp_allKeys[-1].name  # just the last key pressed
                confirm_resp.rt = _confirm_resp_allKeys[-1].rt
                confirm_resp.duration = _confirm_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in choice_taskComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "choice_task" ---
    for thisComponent in choice_taskComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if choice_resp.keys in ['', [], None]:  # No response was made
        choice_resp.keys = None
    thisExp.addData('choice_resp.keys',choice_resp.keys)
    if choice_resp.keys != None:  # we had a response
        thisExp.addData('choice_resp.rt', choice_resp.rt)
        thisExp.addData('choice_resp.duration', choice_resp.duration)
    thisExp.nextEntry()
    thisExp.addData('choice_task.stopped', globalClock.getTime())
    # check responses
    if confirm_resp.keys in ['', [], None]:  # No response was made
        confirm_resp.keys = None
    thisExp.addData('confirm_resp.keys',confirm_resp.keys)
    if confirm_resp.keys != None:  # we had a response
        thisExp.addData('confirm_resp.rt', confirm_resp.rt)
        thisExp.addData('confirm_resp.duration', confirm_resp.duration)
    thisExp.nextEntry()
    # the Routine "choice_task" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Fixation" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Fixation.started', globalClock.getTime())
    # keep track of which components have finished
    FixationComponents = [fix_stumili]
    for thisComponent in FixationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Fixation" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix_stumili* updates
        
        # if fix_stumili is starting this frame...
        if fix_stumili.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix_stumili.frameNStart = frameN  # exact frame index
            fix_stumili.tStart = t  # local t and not account for scr refresh
            fix_stumili.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_stumili, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fix_stumili.started')
            # update status
            fix_stumili.status = STARTED
            fix_stumili.setAutoDraw(True)
        
        # if fix_stumili is active this frame...
        if fix_stumili.status == STARTED:
            # update params
            pass
        
        # if fix_stumili is stopping this frame...
        if fix_stumili.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix_stumili.tStartRefresh + .5-frameTolerance:
                # keep track of stop time/frame for later
                fix_stumili.tStop = t  # not accounting for scr refresh
                fix_stumili.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fix_stumili.stopped')
                # update status
                fix_stumili.status = FINISHED
                fix_stumili.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Fixation" ---
    for thisComponent in FixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Fixation.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    
    # --- Prepare to start Routine "slider_task" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('slider_task.started', globalClock.getTime())
    slider.reset()
    # Run 'Begin Routine' code from code
    event.clearEvents('keyboard')
    slider.markerPos = 3
    key_move = False
    confirm_resp_2.keys = []
    confirm_resp_2.rt = []
    _confirm_resp_2_allKeys = []
    # keep track of which components have finished
    slider_taskComponents = [inform_text, slider, confirm_text, confirm_resp_2]
    for thisComponent in slider_taskComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "slider_task" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *inform_text* updates
        
        # if inform_text is starting this frame...
        if inform_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            inform_text.frameNStart = frameN  # exact frame index
            inform_text.tStart = t  # local t and not account for scr refresh
            inform_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(inform_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'inform_text.started')
            # update status
            inform_text.status = STARTED
            inform_text.setAutoDraw(True)
        
        # if inform_text is active this frame...
        if inform_text.status == STARTED:
            # update params
            pass
        
        # *slider* updates
        
        # if slider is starting this frame...
        if slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider.frameNStart = frameN  # exact frame index
            slider.tStart = t  # local t and not account for scr refresh
            slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'slider.started')
            # update status
            slider.status = STARTED
            slider.setAutoDraw(True)
        
        # if slider is active this frame...
        if slider.status == STARTED:
            # update params
            pass
        # Run 'Each Frame' code from code
        keys = event.getKeys()
        
        if len(keys):
            key_move = True
            if 'f' in keys:
                slider.markerPos = slider.markerPos - 1
        #        slider.rating = True
            elif 'j' in keys:
                slider.markerPos = slider.markerPos  + 1
        #        slider.rating = True
            slider.Response = slider.markerPos
            slider.rating = slider.markerPos
        
        # *confirm_text* updates
        
        # if confirm_text is starting this frame...
        if confirm_text.status == NOT_STARTED and key_move:
            # keep track of start time/frame for later
            confirm_text.frameNStart = frameN  # exact frame index
            confirm_text.tStart = t  # local t and not account for scr refresh
            confirm_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(confirm_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'confirm_text.started')
            # update status
            confirm_text.status = STARTED
            confirm_text.setAutoDraw(True)
        
        # if confirm_text is active this frame...
        if confirm_text.status == STARTED:
            # update params
            confirm_text.setText(slider.markerPos, log=False)
        
        # *confirm_resp_2* updates
        waitOnFlip = False
        
        # if confirm_resp_2 is starting this frame...
        if confirm_resp_2.status == NOT_STARTED and key_move:
            # keep track of start time/frame for later
            confirm_resp_2.frameNStart = frameN  # exact frame index
            confirm_resp_2.tStart = t  # local t and not account for scr refresh
            confirm_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(confirm_resp_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'confirm_resp_2.started')
            # update status
            confirm_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(confirm_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(confirm_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if confirm_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = confirm_resp_2.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _confirm_resp_2_allKeys.extend(theseKeys)
            if len(_confirm_resp_2_allKeys):
                confirm_resp_2.keys = _confirm_resp_2_allKeys[-1].name  # just the last key pressed
                confirm_resp_2.rt = _confirm_resp_2_allKeys[-1].rt
                confirm_resp_2.duration = _confirm_resp_2_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in slider_taskComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "slider_task" ---
    for thisComponent in slider_taskComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('slider_task.stopped', globalClock.getTime())
    thisExp.addData('slider.response', slider.getRating())
    thisExp.addData('slider.rt', slider.getRT())
    # Run 'End Routine' code from code
    slider.Response = slider.markerPos
    # check responses
    if confirm_resp_2.keys in ['', [], None]:  # No response was made
        confirm_resp_2.keys = None
    thisExp.addData('confirm_resp_2.keys',confirm_resp_2.keys)
    if confirm_resp_2.keys != None:  # we had a response
        thisExp.addData('confirm_resp_2.rt', confirm_resp_2.rt)
        thisExp.addData('confirm_resp_2.duration', confirm_resp_2.duration)
    thisExp.nextEntry()
    # the Routine "slider_task" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win, inputs=inputs)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, inputs=None, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # shut down eyetracker, if there is one
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()


def quit(thisExp, win=None, inputs=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    inputs : dict
        Dictionary of input devices by name.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    inputs = setupInputs(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win, 
        inputs=inputs
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win, inputs=inputs)
