from psychopy import visual, core
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
from psychopy.hardware import keyboard

def instruction(win, thisExp, routineTimer, defaultKeyboard, size):
    # --- Initialize components for Routine "inst" ---
    key_inst = keyboard.Keyboard()
    img_inst = visual.ImageStim(
        win=win,
        name='img_inst', units='pix', 
        image='Stimuli/inst.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=size,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    

    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    frameTolerance = 0.001  # how close to onset before 'same' frame

    # --- Prepare to start Routine "inst" ---
    continueRoutine = True
    # update component parameters for each repeat
    key_inst.keys = []
    key_inst.rt = []
    _key_inst_allKeys = []
    # keep track of which components have finished
    instComponents = [key_inst, img_inst]
    for thisComponent in instComponents:
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

    # --- Run Routine "inst" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        win.mouseVisible = False
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_inst* updates
        waitOnFlip = False
        
        # if key_inst is starting this frame...
        if key_inst.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_inst.frameNStart = frameN  # exact frame index
            key_inst.tStart = t  # local t and not account for scr refresh
            key_inst.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_inst, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            # thisExp.timestampOnFlip(win, 'key_inst.started')
            # update status
            key_inst.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_inst.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_inst.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_inst.status == STARTED and not waitOnFlip:
            theseKeys = key_inst.getKeys(keyList=['space'], waitRelease=False)
            _key_inst_allKeys.extend(theseKeys)
            if len(_key_inst_allKeys):
                key_inst.keys = _key_inst_allKeys[-1].name  # just the last key pressed
                key_inst.rt = _key_inst_allKeys[-1].rt
                key_inst.duration = _key_inst_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *img_inst* updates
        
        # if img_inst is starting this frame...
        if img_inst.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            img_inst.frameNStart = frameN  # exact frame index
            img_inst.tStart = t  # local t and not account for scr refresh
            img_inst.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(img_inst, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            # thisExp.timestampOnFlip(win, 'img_inst.started')
            # update status
            img_inst.status = STARTED
            img_inst.setAutoDraw(True)
        
        # if img_inst is active this frame...
        if img_inst.status == STARTED:
            # update params
            pass

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            # if eyetracker:
            #     eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # --- Ending Routine "inst" ---
    for thisComponent in instComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
            stoptime = win.getFutureFlipTime(clock=None)
            thisComponent.tStopRefresh = stoptime
            
    # check responses
    if key_inst.keys in ['', [], None]:  # No response was made
        key_inst.keys = None
    thisExp.addData('img_inst.start', img_inst.tStartRefresh)
    thisExp.addData('img_inst.stop', img_inst.tStopRefresh)
    thisExp.addData('key_inst.keys',key_inst.keys)
    if key_inst.keys != None:  # we had a response
        thisExp.addData('key_inst.rt', key_inst.rt)
        # thisExp.addData('key_inst.duration', key_inst.duration)
    # thisExp.nextEntry()
    # the Routine "inst" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
