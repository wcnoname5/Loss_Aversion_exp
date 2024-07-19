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
            depth=0.0);

        # prepare stimuli for choice.py
        self.img_est_L = visual.ImageStim(
            win=self.win,
            name='img_choice',
            size = self.size,
            image='Stimuli/L.png', mask=None, anchor='center',
            ori=0.0, pos=(0, 0), # tbd
            color=[1,1,1], colorSpace='rgb', opacity=None,
            flipHoriz=False, flipVert=False,
            texRes=128.0, interpolate=True, depth=0.0)

        self.text_choice = visual.TextStim(win=self.win, name='text_choice',
            text='請選擇',
            font='Open Sans',
            pos=(0, 480), height=32.0, wrapWidth=None, ori=0.0, 
            color='black', colorSpace='rgb', opacity=None, 
            languageStyle='LTR',
            depth=-2.0)
        
        self.key_choice = keyboard.Keyboard()

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
        trial_choice = choice(self.win, self.thisExp, self.img_est_L,
                              self.key_choice, self.text_choice, self.routineTimer, self.defaultKeyboard)
        key_map_choice = {'f': 'Left', 'j': 'Right'}
        
        # if jar_random_pos == 'Stimuli/Int_1.png':
        #     trial_choice = choice(self.win, self.thisExp, self.img_choice_red_on_right, self.key_choice, self.text_choice, 
        #                           self.routineTimer, self.defaultKeyboard)
        #     jar_img_map = {'f': 'blue_jar', 'j': 'red_jar'} # 1 for blue and 2 for red
        # else:
        #     trial_choice = choice(self.win, self.thisExp, self.img_choice_red_on_left, self.key_choice, self.text_choice, 
        #                           self.routineTimer, self.defaultKeyboard)
        #     jar_img_map = {'f': 'red_jar', 'j': 'blue_jar'} # 2 for blue and 1 for red
        try:
            # trial_choice = 'f' or 'j'
            choice_lott = key_map_choice[trial_choice] # get "red_jar" or "blue_jar"
            self.thisExp.addData('choosen_lottery', choice_lott)
            self.miss = False
            return choice_lott
        except:
            self.miss = True
            return None
        
    # def jar_reminder(self, choice_jar):
    #     if choice_jar == 'red_jar':
    #         jar_reminder(self.img_redjar, self.text_jar_reminder, self.win, self.thisExp, self.routineTimer, self.defaultKeyboard)
    #     else:
    #         jar_reminder(self.img_bluejar, self.text_jar_reminder, self.win, self.thisExp, self.routineTimer, self.defaultKeyboard)

    # def get_cue(self, no_trial):
    #     # Choose the Cue 
    #     subset = self.df[self.df.cond == self.cond_array[no_trial]] # all rows w/ condition == current trial
    #     current_trial = subset.sample(n=1).iloc[0]
    #     self.thisExp.addData('cond', current_trial['cond'])
    #     self.thisExp.addData('cond_jar', current_trial['jar'])
    #     cueslist = current_trial[['result_1', 'result_2', 'result_3']].tolist()
    #     jar_mapping = {1: 'blue_jar', 2: 'red_jar'}
    #     ans_jar = jar_mapping[current_trial['jar']] # get the color of the jar: 'blue_jar' or 'red_jar'
    #     return cueslist, ans_jar

    # def cues(self, choice_jar, cueslist):
    #     print(cueslist)
    #     img_key = ''.join(map(str, cueslist))
    #     cues(choice_jar, self.cue_img_dict[img_key], self.win, self.thisExp, self.routineTimer, self.defaultKeyboard)
