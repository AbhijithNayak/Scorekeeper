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
from kivy.uix.scrollview import ScrollView
from kivy.uix.carousel import Carousel
from kivy.uix.image import Image
from kivy.properties import ObjectProperty, NumericProperty
from string import uppercase, upper
import re

class CapitalInput(TextInput):
    def __init__(self, **kwargs):
        TextInput.__init__(self, **kwargs)

    def insert_text(self, substring, from_undo=False):
        s = substring.upper()
        if s in uppercase[:]:
            return super(CapitalInput, self).insert_text(s, from_undo=from_undo)

class IntegerInput(TextInput):
    def insert_text(self, substring, from_undo=False):
        p = re.compile('[^0-9]')
        s = re.sub(p,'',substring)
        return super(IntegerInput, self).insert_text(s, from_undo=from_undo)

class UserLayout(BoxLayout):
    name = ObjectProperty(None)
    score = ObjectProperty(None)
    total = ObjectProperty(None)
    pass

class ScorekeepWidget(Widget):

    databox = ObjectProperty(None)
    scrollview = ObjectProperty(None)

    def add_player(self):
        ul = UserLayout(height = 0.16*self.scrollview.height)
        self.databox.add_widget(ul)

        try:
            self.databox.height = max(ul.height, (len(self.databox.children)*(self.databox.children[0]).height*1.0))
            #self.databox.pos = [0, 1*self.scrollview.top]
        except IndexError:
            print "IE PASS\n"
            pass

       

class ScorekeepApp(App):
    def build(self):
        #wid = ScorekeepWidget()
        #return wid
        print "ROOT SIZE:\t"
        print self.root.size
        pass


if __name__ == "__main__":
# THIS IS TO ADJUST THE WINDOW SIZE THAT IS DISPLAYED. WILL BE DISCARDED WHEN PORTING TO ANDROID
    #Config.set('graphics', 'height', '600')
    #Config.set('graphics', 'width', '400')
    ScorekeepApp().run()
