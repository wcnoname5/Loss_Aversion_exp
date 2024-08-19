    
from psychopy import visual, core, event
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
from psychopy.hardware import keyboard
from numpy.random import choice as randchoice


def choice(win, thisExp,
            img_choice, choice_instruct,
            text_Aup_Choice, text_Adown_Choice, text_Bmid_Choice,
            key_choice, choosen_rect,
            confirm_text_2fac, confirm_resp,
            routineTimer, defaultKeyboard) -> str:
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
    # thisExp.addData('choice_task.started', globalClock.getTime())
    # Run 'Begin Routine' code from code_2
    event.clearEvents('keyboard') # not sure if needed 
    ChoiceKeyResponded = False
    chosen_text = ""
    x, y = (262.5*2, 165*2)
    rect_pos = (0, 0)
    confirm_resp.keys = []
    confirm_resp.rt = []
    _confirm_resp_allKeys = []
    # keep track of which components have finished
    choiceComponents = [img_choice, choice_instruct, text_Aup_Choice, text_Adown_Choice, text_Bmid_Choice , key_choice, choosen_rect, confirm_text_2fac, confirm_resp]
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
    while continueRoutine:
        win.mouseVisible = False
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

        # *choice_instruct/text_Adown_Choice/text_Bmid_Choice* updates
        # if choice_instruct is starting this frame...
        if choice_instruct.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            choice_instruct.frameNStart = frameN  # exact frame index
            choice_instruct.tStart = t  # local t and not account for scr refresh
            choice_instruct.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(choice_instruct, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'choice_instruct.started')
            # update status
            choice_instruct.status = STARTED
            choice_instruct.setAutoDraw(True)
        
        # if choice_instruct is active this frame...
        if choice_instruct.status == STARTED:
            # update params
            pass

        # if text_Aup_Choice is starting this frame...
        if text_Aup_Choice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_Aup_Choice.frameNStart = frameN  # exact frame index
            text_Aup_Choice.tStart = t  # local t and not account for scr refresh
            text_Aup_Choice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_Aup_Choice, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_Aup_Choice.started')
            # update status
            text_Aup_Choice.status = STARTED
            text_Aup_Choice.setAutoDraw(True)
        
        # if text_Aup_Choice is active this frame...
        if text_Aup_Choice.status == STARTED:
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
        if key_choice.status == STARTED and not waitOnFlip:
            theseKeys = key_choice.getKeys(keyList=['f','j'], ignoreKeys=["escape"], waitRelease=False)
            # print(f'length: {len(theseKeys)}')
            if len(theseKeys) > 0:
                if not ChoiceKeyResponded:
                    ChoiceKeyResponded = True
                _key_choice_allKeys.extend(theseKeys)
                key_choice.keys = _key_choice_allKeys[-1].name  # just the last key pressed
                key_choice.rt = _key_choice_allKeys[-1].rt
                key_choice.duration = _key_choice_allKeys[-1].duration
                # print(key_choice.keys)
                key_choice.clearEvents()
                # update choice:
                if key_choice.keys == 'f':
                    chosen_text = "F"
                    rect_pos = (-x, y)
                elif key_choice.keys == 'j':
                    chosen_text = "J"
                    rect_pos = (x, y)
                conf_text = f"{chosen_text} Chosen \n Press Space to Confirm"


         # *confirm_text_2fac* updates
        
        # if confirm_text_2fac is starting this frame...
        if confirm_text_2fac.status == NOT_STARTED and ChoiceKeyResponded:
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
            confirm_text_2fac.setText(conf_text, log=False)
        
        # *choosen_rect* updates

        # if choosen_rect is starting this frame...
        if choosen_rect.status == NOT_STARTED and ChoiceKeyResponded:
            # keep track of start time/frame for later
            choosen_rect.frameNStart = frameN  # exact frame index
            choosen_rect.tStart = t  # local t and not account for scr refresh
            choosen_rect.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(choosen_rect, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'choosen_rect.started')
            # update status
            choosen_rect.status = STARTED
            choosen_rect.pos = rect_pos
            choosen_rect.setAutoDraw(True)
        
        # if choosen_rect is active this frame...
        if choosen_rect.status == STARTED:
            # update params
            choosen_rect.pos = rect_pos
            # pass

        # *confirm_resp* updates
        waitOnFlip = False
        
        # if confirm_resp is starting this frame...
        if ChoiceKeyResponded:
            if confirm_resp.status == NOT_STARTED and tThisFlip >= ChoiceKeyResponded-frameTolerance:
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
            
    # --- Ending Routine "choice" ---
    for thisComponent in choiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
            stoptime = win.getFutureFlipTime(clock=None)
            thisComponent.tStopRefresh = stoptime
    


    # check responses
    key_map_choice = {'f': 'Left', 'j': 'Right'}
    if key_choice.keys in ['', [], None]:  # No response was made
        key_choice.keys = None
    thisExp.addData('key_choice.keys',key_choice.keys)
    if key_choice.keys != None:  # we had a response
        thisExp.addData('key_choice.rt', key_choice.rt)
        # thisExp.addData('key_choice.duration', key_choice.duration)
    if confirm_resp.keys in ['', [], None]:  # No response was made
        confirm_resp.keys = None
        thisExp.addData('confirm_resp.keys',confirm_resp.keys)
    if confirm_resp.keys != None:  # we had a response
        thisExp.addData('confirm_resp.rt', confirm_resp.rt)
    thisExp.addData('choice.start', img_choice.tStartRefresh)
    thisExp.addData('choice.stop', img_choice.tStopRefresh)
    # thisExp.nextEntry()
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)
    # print(key_choice.keys, key_map_choice[key_choice.keys])
    trial_choice = key_map_choice[key_choice.keys]
    thisExp.addData('chosen_lottery',trial_choice)

    return(trial_choice)