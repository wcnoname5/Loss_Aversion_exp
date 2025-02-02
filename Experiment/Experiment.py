from .routines.instruction import instruction
from .routines.text_only import text_only
from .routines.choice import choice
from .routines.slider import slider_task
# from .routines.break_screen import break_screen
from psychopy.hardware import keyboard
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
import numpy as np
import pandas as pd

class Experiment():
    def __init__(self, win, thisExp, routineTimer, defaultKeyboard, size, G:int) -> None:
        self.win = win
        self.thisExp = thisExp
        self.routineTimer = routineTimer
        self.defaultKeyboard = defaultKeyboard
        self.size = size
        self.G = G

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
            image='Stimuli/choices.png', mask=None, anchor='center',
            ori=0.0, pos=(0, 0), # tbd
            color=[1,1,1], colorSpace='rgb', opacity=None,
            flipHoriz=False, flipVert=False,
            texRes=128.0, interpolate=True, depth=0.0)

        # --- Initialize components for Routine "choice" ---  
        self.choosen_rect = visual.Rect(
            win=self.win, name='choosen_rect',
            ori=0.0, anchor='center',
            # pos=(262.5, -165), width=90, height=90,
            pos=(262.5*2, 165*2), width=180, height=180,
            lineWidth=3.0, colorSpace='rgb', lineColor='red', fillColor=None,
            opacity=None, depth=-5.0, interpolate=True)
        self.key_choice = keyboard.Keyboard()

        # --- Initialize components for Routine "slider" ---
        self.slider = visual.Slider(win=win, name='slider',
            # size=(540, 40), pos=(0, -180),
            size=(540*2, 40*2), pos=(0, -360),
            units=win.units,
            ticks=None, granularity=5,
            style='scrollbar', styleTweaks=(), opacity=None,
            labelColor='LightGray', markerColor='Grey', lineColor='White', colorSpace='rgb',
            font='Open Sans', labelHeight=50.0,
            flip=False, ori=0.0, depth=-2, readOnly=False)
        
        # --- Initialize common components ---
        self.choice_instruct = visual.TextStim(win=self.win, name='choice_instruct',
            text='Press F/J to Choose the Preferred Option.',
            font='Open Sans',
            # pos=(0, 260), height=30.0,
            pos=(0, 260*2), height=60.0,
            wrapWidth=1500, ori=0.0, 
            color='black', colorSpace='rgb', opacity=None, 
            languageStyle='LTR',
            depth=-2.0)
        self.text_Aup_Choice = visual.TextStim(
            win=self.win, name='text_up_Choice',
            text="",
            font='Open Sans', #'Arial'
            # 原本 pos(-150.6,-75.8)
            # pos=(-135, 75), height=35, # For winsize = (1280, 720)            
            pos=(-135*2, 75*2), height=70,
            wrapWidth=None, ori=0,
            color='red', colorSpace='rgb', opacity=1,
            languageStyle='LTR',
            depth=-5.0)
        self.text_Adown_Choice = visual.TextStim(
            win=self.win, name='text_Adown_Choice',
            text="-2000",
            font='Open Sans', #'Arial'
            # 原本 pos(-150.6,-75.8)
            # pos=(-135, -75), height=35, # For winsize = (1280, 720)            
            pos=(-135*2, -75*2), height=70,
            wrapWidth=None, ori=0,
            color='red', colorSpace='rgb', opacity=1,
            languageStyle='LTR',
            depth=-5.0)
        self.text_Bmid_Choice = visual.TextStim(
            win=self.win, name='text_Amid_Choice',
            text="",
            font='Open Sans', #'Arial'
            # pos=(415, 0), height=35,
            pos=(415*2, 0), height=35*2,
            wrapWidth=None, ori=0,
            color='red', colorSpace='rgb', opacity=1,
            languageStyle='LTR',
            depth=-5.0)
        self.confirm_text = visual.TextStim(
            win=self.win, name='confirm_text',
            text='',
            font='Open Sans',
            # pos=(0, -250), height = 32.0, 
            pos=(0, -500), height=64.0, 
            wrapWidth=1500, ori=0.0, 
            color='black', colorSpace='rgb', opacity=None, 
            languageStyle='LTR',
            depth=-3.0)
        self.confirm_resp = keyboard.Keyboard()

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
            "Slider": {"L": [], "x1pos": [], "x1neg": []},
            # "Slider_choice": {"L": [], "x1pos": [], "x1neg": []}
        } 
        self.total_history = {
            "trial": [], 
            "choice": [],
            "param": [], # L, x1pos, x1neg 
            "method": [], # Bisection, PEST, Slider
        }

    def instruction(self):
        instruction(self.win, self.thisExp, self.routineTimer, self.defaultKeyboard, self.size)

    # def break_screen(self):
    #     break_screen(self.win, self.thisExp, self.routineTimer, self.defaultKeyboard)

    def text_only(self, text_config, duration):
        self.textStim.text = text_config['text']
        self.textStim.name = text_config['name']
        self.textStim.pos = text_config['pos']
        self.textStim.height = text_config['height']
        text_only(self.textStim, duration, self.win, self.thisExp, self.routineTimer, self.defaultKeyboard)


    def StimSetup(self, param: str, method: str, **kwargs) -> None:
        '''Setup the gamble set, Background texts'''
        self.CheckValidInput(param = param, method = method)
        
        isSlider = kwargs.get("isSlider", False) 
        print(f"{method}: {self.param_est[method]}")
        if isSlider:
            self.choice_instruct.setText("Press F/J to Adjust Until Two Options are Indifferent to You.", log=False)
            text_map = {            
                "L": self.text_Adown_Choice,
                "x1pos": self.text_Bmid_Choice,
                "x1neg": self.text_Bmid_Choice
                }
            text_map[param].setText("", log = False) # no prompt in initial value
        else:
            self.choice_instruct.setText("Press F/J to Choose the Preferred Option.", log=False)

        fixed_text_map = {
            "L": [self.text_Aup_Choice, self.text_Bmid_Choice],
            "x1pos": [self.text_Aup_Choice, self.text_Adown_Choice],
            "x1neg": [self.text_Aup_Choice, self.text_Adown_Choice]
            }
        
        if param != "x1neg":
            if isSlider: 
                print(fixed_text_map[param][0].text)
            fixed_text_map[param][0].setText(f'{int(self.G)}', log=False)
            fixed_text_map[param][0].setColor("blue", colorSpace='rgb')
            fixed_text_map[param][1].setText(f'{0}', log=False)
            fixed_text_map[param][1].setColor("black", colorSpace='rgb')
        else: # param == "x1neg"
            fixed_text_map[param][0].setText(f'{0}', log=False)
            fixed_text_map[param][0].setColor("black", colorSpace='rgb')
            if isSlider:
                L_val = self.param_est['Bisection']['L']
            else:
                L_val = self.param_est[method]['L']
            fixed_text_map[param][1].setText(f"{int(L_val)}", log=False)
            fixed_text_map[param][1].setColor(self.GetColor(L_val), colorSpace='rgb')


    def ChoiceUpdate(self, param, updated_lottery_value) -> str:
        '''Return the Participant's Choice (Left or Right)'''
        self.CheckValidInput(param = param)
        # Choice Pair Update
        if param == "L":
            self.text_Adown_Choice.setText(f"{int(updated_lottery_value)}", log=False)
            self.text_Adown_Choice.setColor(self.GetColor(updated_lottery_value), colorSpace='rgb')
        elif param == "x1pos" or param == "x1neg":
            self.text_Bmid_Choice.setText(f"{int(updated_lottery_value)}", log=False)
            self.text_Bmid_Choice.setColor(self.GetColor(updated_lottery_value), colorSpace='rgb')
        
        # Choice update
        trial_choice = choice(self.win, self.thisExp, self.choice_image, self.choice_instruct, 
                              self.text_Aup_Choice, self.text_Adown_Choice, self.text_Bmid_Choice,
                              self.key_choice, self.choosen_rect, self.confirm_text, self.confirm_resp,
                              self.routineTimer, self.defaultKeyboard)        
        try:
            return trial_choice
        except:
            print("Miss")
            # self.miss = True
            return None


    def HistoryUpdate(self, trial:int, choice:str, param:str, method:str, eval_quan:int):
        '''Store Choice and Lottery Values for Final bonus calculate'''
        self.CheckValidInput(param = param, method = method)

        self.est_history[method][param].append(eval_quan)
        if method != "Slider":
            self.est_history[f'{method}_choice'][param].append(choice)

        self.total_history["trial"].append(trial)
        self.total_history["choice"].append(choice)
        self.total_history["param"].append(param)
        self.total_history["method"].append(method)
        pass


    def BisectionTrial(self, current_trial, current_bisect, param, bound, n_bisect=10):
        # Setup Choice-Pair Background
        self.StimSetup(param, "Bisection")
        if (param == "x1neg") & (current_bisect == 1):
            bound[0] = self.param_est["Bisection"]["L"]
        # Bisection update
        if (current_bisect <= n_bisect):
            eval_quan = sum(bound)//2
        else: # consistency check
            # ConsistCheckTrial = ((current_bisect+2)%n_bisect)-1
            def repeatedTrial(rep_seq = [4, 6]):
                ExtraTrial = ((current_bisect-1) % n_bisect)
                for num in range(1, n_bisect+1): # the sequence
                    if num not in rep_seq:
                        rep_seq.append(num)
                # Return the element at the given index
                if 0 <= ExtraTrial < len(rep_seq):
                    return rep_seq[ExtraTrial]
                else:
                    return "Index out of range"
            ConsistCheckTrial = repeatedTrial()
            eval_quan = self.est_history['Bisection'][param][ConsistCheckTrial-1]
            self.thisExp.addData('Consist_Check_Trial', ConsistCheckTrial)
             
        print(f"Bisection: {param}-{current_bisect}; {eval_quan}, Total Trial:{current_trial}")
        # Record Trial Information
        self.thisExp.addData('Trial', current_trial)
        self.thisExp.addData('Task_Type', "Bisection")
        self.thisExp.addData('Estimate', param)
        self.thisExp.addData('Iteration', current_bisect)
        self.thisExp.addData('Lottery_value', eval_quan) # updated lottery value in this trial

        # Choice Pair Update
        prev_choice = self.ChoiceUpdate(param, eval_quan)
        ## Update choice history
        self.HistoryUpdate(current_trial, prev_choice, param, "Bisection", eval_quan)
        
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
        # Store indiff bound only for non-consistency check bounds
        if current_bisect <= n_bisect: 
            self.thisExp.addData('indiff_bound', bound)
        else: pass
        if current_bisect == n_bisect:
            self.param_est["Bisection"][param] = sum(bound)//2
        else: pass
        # record next trial
        self.thisExp.nextEntry()
        return bound


    def PESTTrial(self, current_trial, current_PEST, param, bound, PEST_params, minimal_step) -> tuple:
        eval_quan = PEST_params["eval_quan"] # updating lottery value: int
        step = PEST_params["step"] # step size: int
        last_choices = PEST_params["last_choices"] # last 4 choices: list
        extra_step = PEST_params["extra_step"] # should extra step: bool
        # function: find initial step 
        def InitStepSize(bound):
            """
            Step size = 5 times 2^k, and is smaller than 1/2 of the interval size.
            """
            # Ensure n is greater than 1
            interval = bound[1] - bound[0]
            step = 5
            while step*2 < interval/2:
                step *= 2
            return step
        
        # Setup Choice-Pair Background
        self.StimSetup(param, "PEST")
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
        print(f"PEST: {param}-{current_PEST}; {eval_quan}, Step Size: {step} Total Trial:{current_trial}")

        # Record Trial Information
        self.thisExp.addData('Trial', current_trial)
        self.thisExp.addData('Task_Type', "PEST")
        self.thisExp.addData('Estimate', param)
        self.thisExp.addData('Iteration', current_PEST)
        self.thisExp.addData('Lottery_value', eval_quan) # updated lottery value in this trial

        # 2. Record and Update Choice
        prev_choice = self.ChoiceUpdate(param, eval_quan)
        ## Update choice history
        self.HistoryUpdate(current_trial, prev_choice, param, "PEST", eval_quan)
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


    def SliderTrial(self, current_trial, current_bisect, param, bound: np.array) -> None:
        # Setup Choice-Pair Background
        self.StimSetup(param, "Slider", isSlider = True)
        # functions
        def multOf5Low(n): # closest lower multiple of 5
            return int((n // 5) * 5)
        def multOf5Up(n): # closest upper multiple of 5
            return int(((n + 4) // 5) * 5)
        def adjust_to_multiples_of_5(lst):
            a, b = lst
            a2 = multOf5Low(a)
            b2 = multOf5Up(b)
            return [int(a2), int(b2)]
        expand = (bound[1] - bound[0])//2 # half of range
        new_bound = adjust_to_multiples_of_5([(bound[0] - expand), (bound[1] + expand)])
        self.slider.ticks = [ i for i in range(new_bound[0], new_bound[1]+1, 5)]
        self.slider.rating = multOf5Low(sum(new_bound)//2 ) # midpoint
        self.slider.markerPos = multOf5Low(sum(new_bound)//2 ) # midpoint

        # Record Trial Information
        self.thisExp.addData('Trial', current_trial)
        self.thisExp.addData('Task_Type', "Slider")
        self.thisExp.addData('Estimate', param)
        self.thisExp.addData('Iteration', current_bisect)
        self.thisExp.addData('indiff_bound', new_bound)
        indiff = slider_task(self.win, self.thisExp, param,
                             self.choice_image, self.choice_instruct, self.slider,
                             self.text_Aup_Choice, self.text_Adown_Choice, self.text_Bmid_Choice, 
                             self.confirm_text, self.confirm_resp,
                             self.routineTimer, self.defaultKeyboard)

        # Update Choice History
        self.HistoryUpdate(current_trial, None, param, "Slider", indiff)
        self.est_history["Slider"][param].append(indiff)
        # Set mean of slider respnese as indiff estimation
        sliderHistory = self.est_history["Slider"][param]
        self.param_est["Slider"][param] = int(sum(sliderHistory)//len(sliderHistory))
        
        # record next trial
        self.thisExp.nextEntry()
        return


    def RecordFinalEst(self, method:str) -> None:   
        self.thisExp.addData("Task_Type", method) # updated lottery value in this trial
        for est in self.param_est[method]:
            self.thisExp.addData(est, self.param_est[method][est]) # updated lottery value in this trial
        self.thisExp.nextEntry()


    def FinalBonus(self):
        '''
        Returns the extra bonus from participant's choice.
        Randomly pick one trial to play.
        '''
        # TODO
        pass


    def CheckValidInput(self, **kwargs):
        param = kwargs.get("param", "L")
        method = kwargs.get("method", "PEST")
        allowed_params = ["L", "x1pos", "x1neg"]
        allowed_methods = ['Bisection', 'PEST', 'Slider']
        if param not in allowed_params:
            raise ValueError(f"Invalid param: {param}. Expected one of {allowed_params}")
        if method not in allowed_methods:
            raise ValueError(f"Invalid method: {method}. Expected one of {allowed_methods}")
        pass


    def GetColor(self, value: int) -> str:
        if value == 0:
            return "black"
        else:
            color_map = {True: "blue", False: "red"}
            return color_map[value>=0]