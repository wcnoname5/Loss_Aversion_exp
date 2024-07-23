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

    def choice(self, isMeasureL=True):
        # jar_random_pos = randchoice(['Stimuli/Int_1.png', 'Stimuli/Int_2.png'], size=1)
        trial_choice = choice(self.win, self.thisExp, self.choice_image,
                              self.text_Adown_Choice, self.text_Bmid_Choice, self.key_choice, self.choosen_rect,
                              self.confirm_text_2fac, self.confirm_resp,
                              self.routineTimer, self.defaultKeyboard, isMeasureL)
        try:
            return trial_choice
        except:
            print("Miss")
            # self.miss = True
            return None
        