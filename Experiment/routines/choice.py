    
from psychopy import visual, core
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
from psychopy.hardware import keyboard
from numpy.random import choice as randchoice
# --- Initialize components for Routine "choice" ---



def choice(win, thisExp, img_choice, key_choice, text_choice, routineTimer, defaultKeyboard):

    # --- Prepare stimulus for Routine "choice" --- 
    trial_choice = None
    # trigger_map = {'f': chr(1), 'j': chr(2)}

    frameTolerance = 0.001
    endExpNow = False
    # --- Prepare to start Routine "choice" ---
    continueRoutine = True
    # sendTrigger = False
    # update component parameters for each repeat
    key_choice.keys = []
    key_choice.rt = []
    _key_choice_allKeys = []
    # keep track of which components have finished
    choiceComponents = [img_choice, key_choice, text_choice]
    for thisComponent in choiceComponents:
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

    # --- Run Routine "choice" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *img_choice* updates
        
        # if img_choice is starting this frame...
        if img_choice.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            img_choice.frameNStart = frameN  # exact frame index
            img_choice.tStart = t  # local t and not account for scr refresh
            img_choice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(img_choice, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            # thisExp.timestampOnFlip(win, 'img_choice.started')
            # update status
            img_choice.status = STARTED
            img_choice.setAutoDraw(True)
        
        # if img_choice is active this frame...
        if img_choice.status == STARTED:
            # update params
            pass
        
        # if img_choice is stopping this frame...
        if img_choice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > img_choice.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                img_choice.tStop = t  # not accounting for scr refresh
                img_choice.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'img_choice.stopped')
                # update status
                img_choice.status = FINISHED
                img_choice.setAutoDraw(False)
        
        # *key_choice* updates
        waitOnFlip = False
        
        # if key_choice is starting this frame...
        if key_choice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_choice.frameNStart = frameN  # exact frame index
            key_choice.tStart = t  # local t and not account for scr refresh
            key_choice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_choice, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            # thisExp.timestampOnFlip(win, 'key_choice.started')
            # update status
            key_choice.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_choice.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_choice.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if key_choice is stopping this frame...
        if key_choice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_choice.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                key_choice.tStop = t  # not accounting for scr refresh
                key_choice.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                # thisExp.timestampOnFlip(win, 'key_choice.stopped')
                # update status
                key_choice.status = FINISHED
                key_choice.status = FINISHED
        if key_choice.status == STARTED and not waitOnFlip:
            theseKeys = key_choice.getKeys(keyList=['f','j'], waitRelease=False)
            _key_choice_allKeys.extend(theseKeys)
            if len(_key_choice_allKeys):
                key_choice.keys = _key_choice_allKeys[-1].name  # just the last key pressed
                trial_choice = key_choice.keys
                key_choice.rt = _key_choice_allKeys[-1].rt
                key_choice.duration = _key_choice_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *text_choice* updates
        
        # if text_choice is starting this frame...
        if text_choice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_choice.frameNStart = frameN  # exact frame index
            text_choice.tStart = t  # local t and not account for scr refresh
            text_choice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_choice, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            # thisExp.timestampOnFlip(win, 'text_choice.started')
            # update status
            text_choice.status = STARTED
            text_choice.setAutoDraw(True)
        
        # if text_choice is active this frame...
        if text_choice.status == STARTED:
            # update params
            pass
        
        # if text_choice is stopping this frame...
        if text_choice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_choice.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                text_choice.tStop = t  # not accounting for scr refresh
                text_choice.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                # thisExp.timestampOnFlip(win, 'text_choice.stopped')
                # update status
                text_choice.status = FINISHED
                text_choice.setAutoDraw(False)
        
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
        for thisComponent in choiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            
    # --- Ending Routine "choice" ---
    for thisComponent in choiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
            stoptime = win.getFutureFlipTime(clock=None)
            thisComponent.tStopRefresh = stoptime
    # check responses
    if key_choice.keys in ['', [], None]:  # No response was made
        key_choice.keys = None
    thisExp.addData('key_choice.keys',key_choice.keys)
    if key_choice.keys != None:  # we had a response
        thisExp.addData('key_choice.rt', key_choice.rt)
        # thisExp.addData('key_choice.duration', key_choice.duration)
    thisExp.addData('choice.start', img_choice.tStartRefresh)
    thisExp.addData('choice.stop', img_choice.tStopRefresh)
    # thisExp.nextEntry()
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)

    return trial_choice