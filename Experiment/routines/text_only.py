
from psychopy import visual, core
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)



def text_only(textStim, duration, win, thisExp, routineTimer, defaultKeyboard):
    
    frameTolerance = 0.001
    endExpNow = False

    # --- Prepare to start Routine "showText" ---
    continueRoutine = True
    sendTrigger = False
    # update component parameters for each repeat
    # keep track of which components have finished
    showTextComponents = [textStim]
    for thisComponent in showTextComponents:
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
    # Ensure tThisFlipGlobal is initialized
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)

    # --- Run Routine "showText" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < duration:
        win.mouseVisible = False
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textStim* updates
        
        # if textStim is starting this frame...
        if textStim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textStim.frameNStart = frameN  # exact frame index
            textStim.tStart = t  # local t and not account for scr refresh
            textStim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textStim, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            # thisExp.timestampOnFlip(win, 'textStim.started')
            # update status
            textStim.status = STARTED
            textStim.setAutoDraw(True)
        
        # if textStim is active this frame...
        if textStim.status == STARTED:
            # update params
            pass
        
        # if textStim is stopping this frame...
        if textStim.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textStim.tStartRefresh + duration-frameTolerance:
                # keep track of stop time/frame for later
                textStim.tStop = t  # not accounting for scr refresh
                textStim.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                # thisExp.timestampOnFlip(win, 'textStim.stopped')
                # update status
                textStim.status = FINISHED
                textStim.setAutoDraw(False)
        
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
        for thisComponent in showTextComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            

    # --- Ending Routine "showText" ---
    for thisComponent in showTextComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
            stoptime = win.getFutureFlipTime(clock=None)
            print(tThisFlipGlobal)
            print(stoptime)
            print(stoptime-tThisFlipGlobal)
            print('=======================================')
            thisComponent.tStopRefresh = stoptime

    # --- Save timestamp
    thisExp.addData(f'{textStim.name}.start', textStim.tStartRefresh)
    thisExp.addData(f'{textStim.name}.stop', textStim.tStopRefresh)

    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-duration)