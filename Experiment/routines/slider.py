    
from psychopy import visual, core, event
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
from psychopy.hardware import keyboard
from numpy.random import choice as randchoice


def slider_task(win, thisExp, param,
            img_choice, choice_instruct, slider,
            text_Aup_Choice, text_Adown_Choice, text_Bmid_Choice,
            confirm_text,
            confirm_resp,
            routineTimer, defaultKeyboard) -> int:
    # --- Prepare stimulus for Routine "slider" --- 
    frameTolerance = 0.001
    endExpNow = False
    slider_ticks = slider.ticks 
    slider_granularity=5
    sliding = 0
    slideSpeed = 8
    oldRating = -1 # Not response yet
    thisFrame = 0  # Add a frame counter for delay

    # --- Prepare to start Routine "slider" ---
    continueRoutine = True

    # a keyboard object (must differ from object used online)
    mykb = keyboard.Keyboard()    
    # which keys are we watching? (these will differ depending on handedness)
    keysWatched=['f', 'j', 'space']
    # key statuses at the start of the routine
    keyStatus = {'f': 'up', 'j': 'up', 'space': 'up'}
    

    slider.reset()
    slider.Response = False
    # event.clearEvents('keyboard') # not sure if needed 
    confirm_resp.keys = []
    confirm_resp.rt = []
    _confirm_resp_allKeys = []
    def get_color(value: int) -> str:
        if value == 0:
            return "black"
        else:
            color_map = {True: "blue", False: "red"}
            return color_map[value>=0]
    # keep track of which components have finished
    choiceComponents = [img_choice, choice_instruct, slider, text_Aup_Choice, text_Adown_Choice, text_Bmid_Choice, confirm_text, confirm_resp]
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
            if param == "L" and slider.Response:
                update_value = int(slider.markerPos)
                text_Adown_Choice.setText(update_value, log=False)
                text_Adown_Choice.setColor(get_color(update_value), log=False)
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
            if (param != "L") and slider.Response:
                update_value = int(slider.markerPos)
                text_Bmid_Choice.setText(update_value, log=False)
                text_Bmid_Choice.setColor(get_color(update_value), log=False)
            pass
        
        # Poll the keyboard
        keys = mykb.getKeys(keysWatched, waitRelease = False, clear = False)

        for key in keysWatched:
            if any([k.name == key and k.duration is None for k in keys]):
                keyStatus[key] = 'down'
            else:
                keyStatus[key] = 'up'
        
        # End routine with keyboard
        if slider.markerPos and keyStatus['space'] == 'down':  # 'space' key
            continueRoutine = False

        # Move slider with keyboard
        if keyStatus['f'] == 'down':  # 'f' key
            sliding = -slider_granularity
        elif keyStatus['j'] == 'down':  # 'j' key
            sliding = slider_granularity
        else:
            sliding = 0

        # if thisFrame%5 == 0:
        #     print(f'{keyStatus}, Is sliding: {sliding}, {thisFrame}')
        
        if sliding != 0:
            if oldRating == -1:
                slider.markerPos = int((slider_ticks[0]+slider_ticks[-1])//2)
            if thisFrame%slideSpeed == 0:
                slider.markerPos += sliding
            slider.rating = slider.markerPos
            thisFrame += 1 # Increment the frame counter
            if thisFrame > 40:
                if thisFrame%20 == 0:
                    slider_granularity += 5
                    slideSpeed = max(slideSpeed-3, 1)

        # Reset the frame counter and slideSpeed if no key is pressed
        elif sliding == 0: 
            thisFrame = 0
            slideSpeed = 8
            slider_granularity = 5
        
        #Update slider text if needed
        if slider.markerPos:
            if not slider.Response:
                slider.Response = True
            if oldRating != slider.markerPos:
                confirm_text.setText(f"{int(slider.markerPos)}\n Press Space to Confirm",
                                      log=False)
                oldRating = slider.markerPos
        
        # thisFrame += 1


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

            
        # *confirm_text* updates
        
        # if confirm_text is starting this frame...
        if confirm_text.status == NOT_STARTED and slider.Response:
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
        
        # # if confirm_text is active this frame...
        # if confirm_text.status == STARTED and slider.Response:
        #     # update params
        #     # confirm_text.setText(f"{int(slider.markerPos)}\n Press Space to Confirm", log=False)
        #     pass
        
        # *confirm_resp* updates
        waitOnFlip = False
        
        # if confirm_resp is starting this frame...
        if confirm_resp.status == NOT_STARTED and slider.Response:
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
    thisExp.addData('slider.indiff_response', indiff)
    thisExp.addData('Lottery_value', indiff)

    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)
    return indiff