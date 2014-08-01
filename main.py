# -*- coding: utf-8 -*-
"""
Created on Thu Jul 24 16:40:04 2014

@author: mortz
"""
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.config import Config
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from string import uppercase, upper

class CapitalInput(TextInput):
    def __init__(self, **kwargs):
        TextInput.__init__(self, **kwargs)

    def insert_text(self, substring, from_undo=False):
        s = substring.upper()
        if s in uppercase[:]:
            return super(CapitalInput, self).insert_text(s, from_undo=from_undo)

class ScorekeepWidget(Widget):
    pass


class ScorekeepApp(App):
    def build(self):
        wid = ScorekeepWidget()
        print wid.size
        return wid

if __name__ == "__main__":
# THIS IS TO ADJUST THE WINDOW SIZE THAT IS DISPLAYED. WILL BE DISCARDED WHEN PORTING TO ANDROID
    #Config.set('graphics', 'height', '600')
    #Config.set('graphics', 'width', '400')
    ScorekeepApp().run()
