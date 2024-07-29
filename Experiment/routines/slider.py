    
from psychopy import visual, core, event
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
from psychopy.hardware import keyboard
from numpy.random import choice as randchoice
# --- Initialize components for Routine "choice" ---


'''
Notes:
 `Loss_image` -> `img_choice`
 'choice_resp' -> `key_choice`
 `text_Adown_Choice` -> `eval_indiff` (not changed yet)
'''
def slider_task(win, thisExp,
            img_choice, slider, text_Adown_Choice, text_Bmid_Choice,
            confirm_text, confirm_resp,
            routineTimer, defaultKeyboard):
    # --- Prepare stimulus for Routine "choice" --- 
    trial_choice = None
    # trigger_map = {'f': chr(1), 'j': chr(2)}

    frameTolerance = 0.001
    endExpNow = False
    # --- Prepare to start Routine "choice" ---
    continueRoutine = True
    # sendTrigger = False
    # update component parameters for each repeat
    # thisExp.addData('choice_task.started', globalClock.getTime())
    # Run 'Begin Routine' code from code_2
    slider.reset()
    event.clearEvents('keyboard') # not sure if needed 
    key_move = False
    # ChoiceKeyResponded = False
    # chosen_text = ""
    # rect_pos = (0, 0)
    confirm_resp.keys = []
    confirm_resp.rt = []
    _confirm_resp_allKeys = []
    # keep track of which components have finished
    choiceComponents = [img_choice, slider, text_Adown_Choice, text_Bmid_Choice, confirm_text, confirm_resp]
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

    # --- Run Routine "slider_task" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
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
        '''        
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
        '''

        # *text_Adown_Choice/text_Bmid_Choice* updates

        # if text_Adown_Choice is starting this frame...
        if text_Adown_Choice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_Adown_Choice.frameNStart = frameN  # exact frame index
            text_Adown_Choice.tStart = t  # local t and not account for scr refresh
            text_Adown_Choice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_Adown_Choice, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_Adown_Choice.started')
            # update status
            text_Adown_Choice.status = STARTED
            text_Adown_Choice.setAutoDraw(True)
        
        # if text_Adown_Choice is active this frame...
        if text_Adown_Choice.status == STARTED:
            # update params
            pass
        # if text_Adown_Choice is starting this frame...
        if text_Adown_Choice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_Adown_Choice.frameNStart = frameN  # exact frame index
            text_Adown_Choice.tStart = t  # local t and not account for scr refresh
            text_Adown_Choice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_Adown_Choice, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_Adown_Choice.started')
            # update status
            text_Adown_Choice.status = STARTED
            text_Adown_Choice.setAutoDraw(True)
        
        # if text_Adown_Choice is active this frame...
        if text_Adown_Choice.status == STARTED:
            # update params
            pass

        # text_Bmid_Choice
        # if text_Bmid_Choice is starting this frame...
        if text_Bmid_Choice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_Bmid_Choice.frameNStart = frameN  # exact frame index
            text_Bmid_Choice.tStart = t  # local t and not account for scr refresh
            text_Bmid_Choice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_Bmid_Choice, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_Bmid_Choice.started')
            # update status
            text_Bmid_Choice.status = STARTED
            text_Bmid_Choice.setAutoDraw(True)
        
        # if text_Bmid_Choice is active this frame...
        if text_Bmid_Choice.status == STARTED:
            # update params
            pass
        # if text_Bmid_Choice is starting this frame...
        if text_Bmid_Choice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_Bmid_Choice.frameNStart = frameN  # exact frame index
            text_Bmid_Choice.tStart = t  # local t and not account for scr refresh
            text_Bmid_Choice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_Bmid_Choice, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_Bmid_Choice.started')
            # update status
            text_Bmid_Choice.status = STARTED
            text_Bmid_Choice.setAutoDraw(True)
        
        # if text_Bmid_Choice is active this frame...
        if text_Bmid_Choice.status == STARTED:
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
                key_move = True
            elif 'j' in keys:
                slider.markerPos = slider.markerPos  + 1
                key_move = True
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
        
        # *confirm_resp* updates
        waitOnFlip = False
        
        # if confirm_resp is starting this frame...
        if confirm_resp.status == NOT_STARTED and key_move:
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
            
    # --- Ending Routine "slider" ---
    for thisComponent in choiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
            stoptime = win.getFutureFlipTime(clock=None)
            thisComponent.tStopRefresh = stoptime

    indiff = slider.getRating()
    # thisExp.addData('slider.rt', slider.getRT())
    if confirm_resp.keys in ['', [], None]:  # No response was made
        confirm_resp.keys = None
    # thisExp.addData('confirm_resp.keys',confirm_resp.keys)
    if confirm_resp.keys != None:  # we had a response
        thisExp.addData('confirm_resp.rt', confirm_resp.rt)
    thisExp.addData('slider.start', img_choice.tStartRefresh)
    thisExp.addData('slider.stop', img_choice.tStopRefresh)
    thisExp.addData('slider.response', indiff)

    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)

    # return indiff