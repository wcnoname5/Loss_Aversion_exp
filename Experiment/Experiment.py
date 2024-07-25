from .routines.instruction import instruction
from .routines.text_only import text_only
from .routines.choice import choice
# from .routines.jar_reminder import jar_reminder
# from .routines.cues import cues
# from .routines.break_screen import break_screen
from psychopy.hardware import keyboard
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from numpy.random import choice as randchoice
import numpy as np
import pandas as pd

class Experiment():
    def __init__(self, win, thisExp, routineTimer, defaultKeyboard, size) -> None:
        self.win = win
        self.thisExp = thisExp
        self.routineTimer = routineTimer
        self.defaultKeyboard = defaultKeyboard
        self.size = size

        # --- Initialize components for Routine "showText" ---
        self.textStim = visual.TextStim(win=win,
            font='Open Sans', wrapWidth=1000, ori=0.0, 
            color='white', colorSpace='rgb', opacity=None, 
            languageStyle='LTR',
            depth=0.0)
        
        # store param estimates
        self.param_est = {} 

        self.fixation = {"name": "fixation_1", 
             "text": "+", 
             "pos": (0,0), 
             "height": 48}

        # prepare stimuli for choice.py
        self.choice_image = visual.ImageStim(
            win=self.win,
            name='img_choice',
            size = self.size,
            image='Stimuli/L.png', mask=None, anchor='center',
            ori=0.0, pos=(0, 0), # tbd
            color=[1,1,1], colorSpace='rgb', opacity=None,
            flipHoriz=False, flipVert=False,
            texRes=128.0, interpolate=True, depth=0.0)

        # self.text_choice = visual.TextStim(win=self.win, name='text_choice',
        #     text='請選擇',
        #     font='Open Sans',
        #     pos=(0, 480), height=32.0, wrapWidth=None, ori=0.0, 
        #     color='black', colorSpace='rgb', opacity=None, 
        #     languageStyle='LTR',
        #     depth=-2.0)
        
        self.text_Adown_Choice = visual.TextStim(
            win=self.win, name='text_Adown_Choice',
            text="-2000",
            font='Open Sans', #'Arial'
            # 原本 pos(-150.6,-75.8)
            pos=(-150.6, -69.8), height=35, wrapWidth=None, ori=0,
            color='red', colorSpace='rgb', opacity=1,
            languageStyle='LTR',
            depth=-5.0)
        
        self.text_Bmid_Choice = visual.TextStim(
            win=self.win, name='text_Amid_Choice',
            text="",
            font='Open Sans', #'Arial'
            pos=(376.5, 3), height=35, wrapWidth=None, ori=0,
            color='red', colorSpace='rgb', opacity=1,
            languageStyle='LTR',
            depth=-5.0)
        
        self.key_choice = keyboard.Keyboard()

        self.choosen_rect = visual.Rect(
            win=self.win, name='choosen_rect',
            width=100, height=100,
            ori=0.0, pos=(200, -200), anchor='center',
            lineWidth=2.0, colorSpace='rgb', lineColor='red', fillColor=None,
            opacity=None, depth=-5.0, interpolate=True)
        
        self.confirm_text_2fac = visual.TextStim(
            win=self.win, name='confirm_text_2fac',
            text='Press F/J to choose Left/Right Lottery',
            font='Open Sans',
            pos=(0, -200), height=36.0, wrapWidth=None, ori=0.0, 
            color='black', colorSpace='rgb', opacity=None, 
            languageStyle='LTR',
            depth=-3.0)
        
        self.confirm_resp = keyboard.Keyboard()

    def instruction(self):
        instruction(self.win, self.thisExp, self.routineTimer, self.defaultKeyboard)

    # def break_screen(self):
    #     break_screen(self.win, self.thisExp, self.routineTimer, self.defaultKeyboard)

    def text_only(self, text_config, duration):
        self.textStim.text = text_config['text']
        self.textStim.name = text_config['name']
        self.textStim.pos = text_config['pos']
        self.textStim.height = text_config['height']
        text_only(self.textStim, duration, self.win, self.thisExp, self.routineTimer, self.defaultKeyboard)

    def choice(self):
        # jar_random_pos = randchoice(['Stimuli/Int_1.png', 'Stimuli/Int_2.png'], size=1)
        trial_choice = choice(self.win, self.thisExp, self.choice_image,
                              self.text_Adown_Choice, self.text_Bmid_Choice, self.key_choice, self.choosen_rect,
                              self.confirm_text_2fac, self.confirm_resp,
                              self.routineTimer, self.defaultKeyboard)
        try:
            return trial_choice
        except:
            print("Miss")
            # self.miss = True
            return None
    
    def get_color(self, value): # *int -> str
        color_map = {True: "blue", False: "red"}
        return color_map[value>=0]
    
    def Bisection_only(self, n_bisect, param, stumuli_path, bounds):
        trial = 0 # trial counting 
        for index, param_name in enumerate(param):
            # Stimuli Setup 
            indiff_bound = bounds[index]
            filepath = f"{stumuli_path}/{param_name}.png"
            self.choice_image.image = filepath
            if param_name == "L":
                self.text_Bmid_Choice.setText("", log=False)
            elif param_name == "x1pos":
                self.text_Adown_Choice.setText("", log=False)
            elif param_name == "x1neg":
                indiff_bound[0] = self.param_est['L']
                self.text_Adown_Choice.setText(f"{self.param_est['L']}", log=False)
            
            for bisect in range(n_bisect):
                trial += 1
                eval_quan = sum(indiff_bound)//2 # Bisection
                # Record Trial Information
                self.thisExp.addData('Trial', trial)
                self.thisExp.addData('Task_Type', "Bisection")
                self.thisExp.addData('Estimate', param_name)
                self.thisExp.addData('Iteration', bisect+1)
                self.thisExp.addData('Lottery_value', eval_quan) # updated lottery value in this trial

                # Choice Pair Update
                if param_name == "L":
                    self.text_Adown_Choice.setText(f"{int(eval_quan)}", log=False)
                    self.text_Adown_Choice.setColor(self.get_color(eval_quan), colorSpace='rgb')
                elif param_name == "x1pos":
                    self.text_Bmid_Choice.setText(f"{int(eval_quan)}", log=False)
                    self.text_Bmid_Choice.setColor(self.get_color(eval_quan), colorSpace='rgb')
                elif param_name == "x1neg":
                    self.text_Bmid_Choice.setText(f"{int(eval_quan)}", log=False)
                    self.text_Bmid_Choice.setColor(self.get_color(eval_quan), colorSpace='rgb')

                # Show Fixation + choice
                self.text_only(text_config=self.fixation, duration=0.5)
                prev_choice = self.choice()

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

                self.thisExp.addData('indiff_bound', indiff_bound)
                # record next trial
                self.thisExp.nextEntry()
            self.param_est[param_name] = sum(indiff_bound)//2
    
    def PEST_only(self, param, stumuli_path, bounds, minimal_step):
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
            self.choice_image.image = filepath
            if param_name == "L":
                self.text_Bmid_Choice.setText("", log=False)
            elif param_name == "x1pos":
                self.text_Adown_Choice.setText("", log=False)
            elif param_name == "x1neg":
                indiff_bound[0] = self.param_est['L']
                self.text_Adown_Choice.setText(f"{self.param_est['L']}", log=False)
            
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
                self.thisExp.addData('Trial', trial)
                self.thisExp.addData('Task_Type', "PEST")
                self.thisExp.addData('Estimate', param_name)
                self.thisExp.addData('Iteration', PEST_trial)
                self.thisExp.addData('Step_Size', step)                    
                self.thisExp.addData('Lottery_value', eval_quan) # updated lottery value in this trial
                
                # Choice Pair Update
                if param_name == "L":
                    self.text_Adown_Choice.setText(f"{int(eval_quan)}", log=False)
                    self.text_Adown_Choice.setColor(self.get_color(eval_quan), colorSpace='rgb')
                elif param_name == "x1pos":
                    self.text_Bmid_Choice.setText(f"{int(eval_quan)}", log=False)
                    self.text_Bmid_Choice.setColor(self.get_color(eval_quan), colorSpace='rgb')
                elif param_name == "x1neg":
                    self.text_Bmid_Choice.setText(f"{int(eval_quan)}", log=False)
                    self.text_Bmid_Choice.setColor(self.get_color(eval_quan), colorSpace='rgb')

                # fixation + choice
                self.text_only(text_config=self.fixation, duration=0.5)
                prev_choice = self.choice()

                # Update choice history
                last_choices.insert(0, prev_choice)
                last_choices.pop()

                # Exp.thisExp.addData('indiff_bound', indiff_bound)
                # record next trial
                self.thisExp.nextEntry()

            self.param_est[param_name] = eval_quan
