from .routines.instruction import instruction
from .routines.text_only import text_only
from .routines.choice import choice
from .routines.slider import slider_task
# from .routines.jar_reminder import jar_reminder
# from .routines.cues import cues
# from .routines.break_screen import break_screen
from psychopy.hardware import keyboard
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
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
        
        # --- Initialize components for Routine "choice" ---
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

        # --- Initialize components for Routine "choice" ---
        self.Instruction_Text = visual.TextStim(
            win=self.win, name='Instruction_Text',
            text='Press F/J to choose Left/Right Lottery',
            font='Open Sans',
            pos=(0, +200), height=36.0, wrapWidth=None, ori=0.0, 
            color='black', colorSpace='rgb', opacity=None, 
            languageStyle='LTR',
            depth=-3.0)  
        self.choosen_rect = visual.Rect(
            win=self.win, name='choosen_rect',
            width=100, height=100,
            ori=0.0, pos=(200, -200), anchor='center',
            lineWidth=2.0, colorSpace='rgb', lineColor='red', fillColor=None,
            opacity=None, depth=-5.0, interpolate=True)
        self.key_choice = keyboard.Keyboard()

        # --- Initialize components for Routine "slider" ---
        self.slider = visual.Slider(win=win, name='slider',
            startValue=None, size=(540, 40), pos=(0, -200), units=win.units,
            labels=["0", "100"], ticks=None, granularity=1.0,
            style='scrollbar', styleTweaks=(), opacity=None,
            labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
            font='Open Sans', labelHeight=50.0,
            flip=False, ori=0.0, depth=-2, readOnly=False)
        
        # --- Initialize common components ---
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
        self.confirm_text = visual.TextStim(
            win=self.win, name='confirm_text',
            text='',
            font='Open Sans',
            pos=(0, -200), height=36.0, wrapWidth=None, ori=0.0, 
            color='black', colorSpace='rgb', opacity=None, 
            languageStyle='LTR',
            depth=-3.0)
        self.confirm_resp = keyboard.Keyboard()
        # self.text_choice = visual.TextStim(win=self.win, name='text_choice',
        #     text='請選擇',
        #     font='Open Sans',
        #     pos=(0, 480), height=32.0, wrapWidth=None, ori=0.0, 
        #     color='black', colorSpace='rgb', opacity=None, 
        #     languageStyle='LTR',
        #     depth=-2.0)

        # store param estimates
        self.param_est = {
            "Bisection": {"L": None, "x1pos": None, "x1neg": None},
            "PEST": {"L": None, "x1pos": None, "x1neg": None},
            "Slider": {"L": None, "x1pos": None, "x1neg": None},
        } 
        # store choice history
        self.est_history = {
            "Bisection": {"L": [], "x1pos": [], "x1neg": []},
            "Bisection_choice": {"L": [], "x1pos": [], "x1neg": []},
            "PEST": {"L": [], "x1pos": [], "x1neg": []},
            "PEST_choice": {"L": [], "x1pos": [], "x1neg": []},
            # "Slider": {"L": [], "x1pos": [], "x1neg": []},
            # "Slider_choice": {"L": [], "x1pos": [], "x1neg": []}
        } 

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

    
    def StimSetup(self, bound, param: str, method: str, current_trial,
                   stumuli_path = "./Stimuli") -> None: 
        allowed_params = ["L", "x1pos", "x1neg"]
        allowed_methods = ['Bisection', 'PEST', 'Slider']
        if param not in allowed_params:
            raise ValueError(f"Invalid param: {param}. Expected one of {allowed_params}")
        if method not in allowed_methods:
            raise ValueError(f"Invalid method: {method}. Expected one of {allowed_methods}")
        
        print(f"{method}: {self.param_est[method]}")
        filepath = f"{stumuli_path}/{param}.png"
        self.choice_image.image = filepath
        if param == "L":
            self.text_Bmid_Choice.setText("", log=False)
        elif param == "x1pos":
            self.text_Adown_Choice.setText("", log=False)
        elif param == "x1neg":
            if current_trial==1: # bound update is primally for Bisection
                bound[0] = self.param_est[method]['L']
            self.text_Adown_Choice.setText(f"{self.param_est[method]['L']}", log=False)


    def ChoiceUpdate(self, param, updated_lottery_value):
        allowed_params = ["L", "x1pos", "x1neg"]
        if param not in allowed_params:
            raise ValueError(f"Invalid param: {param}. Expected one of {allowed_params}")
        def get_color(value): # *int -> str
            color_map = {True: "blue", False: "red"}
            return color_map[value>=0]
        # Choice Pair Update
        if param == "L":
            self.text_Adown_Choice.setText(f"{int(updated_lottery_value)}", log=False)
            self.text_Adown_Choice.setColor(get_color(updated_lottery_value), colorSpace='rgb')
        elif param == "x1pos":
            self.text_Bmid_Choice.setText(f"{int(updated_lottery_value)}", log=False)
            self.text_Bmid_Choice.setColor(get_color(updated_lottery_value), colorSpace='rgb')
        elif param == "x1neg":
            self.text_Bmid_Choice.setText(f"{int(updated_lottery_value)}", log=False)
            self.text_Bmid_Choice.setColor(get_color(updated_lottery_value), colorSpace='rgb')
        
        # Choice update
        trial_choice = choice(self.win, self.thisExp, self.choice_image,
                              self.text_Adown_Choice, self.text_Bmid_Choice, self.key_choice, self.choosen_rect,
                              self.confirm_text, self.confirm_resp,
                              self.routineTimer, self.defaultKeyboard)
        try:
            return trial_choice
        except:
            print("Miss")
            # self.miss = True
            return None


    def BisectionTrial(self, current_trial, current_bisect, param, bound,
                        n_bisect=10, stumuli_path = "./Stimuli"):
        # Setup Choice-Pair Background
        self.StimSetup(bound, param, "Bisection", current_bisect, stumuli_path)
        if (param == "x1neg") & (current_bisect == 1):
            bound[0] = self.param_est["Bisection"]["L"]
        # Bisection update
        if (current_bisect <= n_bisect):
            eval_quan = sum(bound)//2
        # elif (current_bisect <= n_bisect):
        #     pass
        else: # consistency check
            ConsistCheckTrial = (current_bisect%n_bisect)-1
            eval_quan = self.est_history['Bisection'][param][ConsistCheckTrial]
            self.thisExp.addData('Consist_Check_Trial', ConsistCheckTrial)
             
        print(f"Bisection: {param} - {current_bisect};{eval_quan}, Total Trial:{current_trial}")
        # Record Trial Information
        self.thisExp.addData('Trial', current_trial)
        self.thisExp.addData('Task_Type', "Bisection")
        self.thisExp.addData('Estimate', param)
        self.thisExp.addData('Iteration', current_bisect)
        self.thisExp.addData('Lottery_value', eval_quan) # updated lottery value in this trial

        # Choice Pair Update
        prev_choice = self.ChoiceUpdate(param, eval_quan)
        ## Update choice history
        self.est_history["Bisection"][param].append(eval_quan)
        self.est_history["Bisection_choice"][param].append(prev_choice)

        # Update bound
        if (param == "L"):
            if (prev_choice == "Right"): # lower bound
                bound[0] = eval_quan 
            else: # choose "Left"
                bound[1] = eval_quan
        else:
            if (prev_choice == "Right"):
                bound[1] = eval_quan
            else:
                bound[0] = eval_quan

        self.thisExp.addData('indiff_bound', bound)
        # record next trial
        self.thisExp.nextEntry()
        if current_bisect == n_bisect:
            self.param_est["Bisection"][param] = sum(bound)//2
        else: pass
        return bound


    def PESTTrial(self, current_trial, current_PEST, param, bound,
                  PEST_params, minimal_step, stumuli_path = "./Stimuli") -> dict:
        eval_quan = PEST_params["eval_quan"] # updating lottery value: int
        step = PEST_params["step"] # step size: int
        last_choices = PEST_params["last_choices"] # last 4 choices: list
        extra_step = PEST_params["extra_step"] # should extra step: bool
        # function: find initial step 
        def InitStepSize(bound): 
            # Ensure n is greater than 1
            interval = bound[1] - bound[0]
            step = 5
            while step*2 < interval/4:
                step *= 2
            return step
        
        # Setup Choice-Pair Background
        self.StimSetup(bound, param, "PEST", current_PEST, stumuli_path)
        if (param == "x1neg") & (current_PEST == 1):
            bound[0] = self.param_est["PEST"]["L"]

        # 1. PEST Update: Lottery Pair Value
        if current_PEST == 1: # initial setup
            eval_quan = sum(bound)//2 # Midpoint as starting point
            step = InitStepSize(bound) # step_size
            last_choices = [None]*4 # index 0 stores last choice 
        else:
            step = PEST_params["step"]
            direction = int(last_choices[0]=="Left")*2 - 1 # T:1, F:-1
            if (param == "L"):
                direction = -direction
            else: pass
            # Update Lottery Pair Value
            eval_quan = eval_quan + (direction * step)
        print(f"PEST: {param} - {current_PEST};{eval_quan}, Step Size: {step} Total Trial:{current_trial}")

        # Record Trial Information
        self.thisExp.addData('Trial', current_trial)
        self.thisExp.addData('Task_Type', "PEST")
        self.thisExp.addData('Estimate', param)
        self.thisExp.addData('Iteration', current_PEST)
        self.thisExp.addData('Lottery_value', eval_quan) # updated lottery value in this trial

        # 2. Record and Update Choice
        prev_choice = self.ChoiceUpdate(param, eval_quan)
        ## Update choice history
        self.est_history["PEST"][param].append(eval_quan)
        self.est_history["PEST_choice"][param].append(prev_choice)
        last_choices.insert(0, prev_choice)
        last_choices.pop()

        # 3. Update Step Size 
        if current_PEST == 1:
            pass
        elif current_PEST < 4: # 2nd or 3rd
            if (last_choices[0] != last_choices[1]) : # Reversal
                step = step//2
            elif (current_PEST == 3) & (last_choices[0] == last_choices[1] == last_choices[2]):
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
        
        updated_params = {"eval_quan":eval_quan,
                          "step":step, 
                          "last_choices": last_choices,
                          "extra_step":extra_step}
        
        if step < minimal_step:
            self.param_est["PEST"][param] = eval_quan
            converge = True
        else: 
            converge = False
        # Exp.thisExp.addData('indiff_bound', indiff_bound)
        # record next trial
        self.thisExp.nextEntry()
        return updated_params, converge


    def SliderTrial(self, current_trial, current_bisect, param, bound: np.array, 
                    stumuli_path = "./Stimuli"):
        # Setup Choice-Pair Background
        self.StimSetup(bound, param, "Slider", current_bisect, stumuli_path)
        expand = (bound[1]-bound[0])//2 # half of range
        new_bound = [(bound[0] - expand), (bound[1] + expand)]
        self.slider.labels = [str(i) for i in new_bound]
        self.slider.ticks = new_bound
        self.slider.setValue((bound[1] + bound[0])//2 ) # midpoint

        # Record Trial Information
        self.thisExp.addData('Trial', current_trial)
        self.thisExp.addData('Task_Type', "Slider")
        self.thisExp.addData('Estimate', param)
        self.thisExp.addData('Iteration', current_bisect)
        slider_task()
        self.thisExp.nextEntry()
        # slider setup
        # 1. bound values
        # 2. starting point

        pass


    def RecordFinalEst(self, method:str) -> None:   
        self.thisExp.addData("Task_Type", method) # updated lottery value in this trial
        for est in self.param_est[method]:
            self.thisExp.addData(est, self.param_est[method][est]) # updated lottery value in this trial
        self.thisExp.nextEntry()