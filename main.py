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
from kivy.properties import ObjectProperty, NumericProperty, BooleanProperty
from string import uppercase, upper
import re
import scoredb
from BarGraph import BarGraph

class CapitalInput(TextInput):

    def __init__(self, **kwargs):
        TextInput.__init__(self, **kwargs)

    def insert_text(self, substring, from_undo=False):
        s = substring.upper()
        if s in uppercase[:]:
            return super(CapitalInput, self).insert_text(s, from_undo=from_undo)


class FloatInput(TextInput):
    def insert_text(self, substring, from_undo=False):
        p = re.compile('[^0-9]')
        s = re.sub(p,'',substring)
        if '.' in self.text:
            s = re.sub(p, '', substring)
        else:
            s = '.'.join([re.sub(p, '', s) for s in substring.split('.', 1)])
        return super(FloatInput, self).insert_text(s, from_undo=from_undo)

class UserLayout(BoxLayout):
    name_ti = ObjectProperty(None)
    score_ti  = ObjectProperty(None)
    total_ti  = ObjectProperty(None)
    is_name_nonblank = BooleanProperty(False)
    current_score = NumericProperty(0.0)

    def __init__(self, **kwargs):
        BoxLayout.__init__(self, **kwargs)
        self.score_list = []
        self.name_ti.bind(text = self.on_name_update)
        self.score_ti.bind(text = self.current_score_track)

    ## Callbacks within Kivy require a *args argument to be passed , I don't know why
    def on_name_update(self, *args):
        if len(self.name_ti.text) > 0:
            self.is_name_nonblank = True
        else:
            self.is_name_nonblank = False

    def current_score_track(self, *args):
        try:
            self.current_score = float(self.score_ti.text)
            #print float(self.score_ti.text)
        except ValueError:
            self.current_score = 0.0

    def push_score(self, *args):
        self.score_list.append(self.current_score)
        self.total_ti.text = str(int(sum(self.score_list)))
        self.score_ti.text = ""


class ScorekeepWidget(Widget):
    parousel = ObjectProperty(None)
    databox = ObjectProperty(None)
    scrollview = ObjectProperty(None)
    addbutton =  ObjectProperty(None)

    def __init__(self, **kwargs):
        Widget.__init__(self, **kwargs)
        self.scoredb = scoredb.ScoreDB()

##In a function, the *args contains everything that is passed to the function/ created within the function
##that is not explicitly mentioned. In this case, *args contains the value of the evaluated expression 
##obj.is_name_nonblank and obj contains the ul object. If, instead, the function was defined as
## def enable_addbutn(self, *args): then the *args would contain both the ul object and the evaluated expression.
## The function has been defined this way only to make the code easier to read, i.e., assuming it is easier to
## read obj.<property> than (*arg[0]).property  
    def enable_addbutton(self, obj, *args):
        self.addbutton.disabled = not(obj.is_name_nonblank)

    def add_player(self):
        self.addbutton.disabled = True
        ul = UserLayout(height = 0.16*self.scrollview.height)
        ul.bind(is_name_nonblank = self.enable_addbutton)
        self.databox.add_widget(ul)
        try:
            self.databox.height = max(ul.height, (len(self.databox.children)*(self.databox.children[0]).height*1.0))
        except IndexError:
            print "IE PASS\n"
            pass
            
    def update_round(self):
        self.scoredb.reset_db()
        for child in self.databox.children:
            child.push_score()
            self.scoredb.add_player_info(child.name_ti.text, sum(child.score_list), child.score_list[-1])

        self.scoredb.update_max_min() 

        print [type(s) for s in self.parousel.slides]

#        try:
#            self.parousel.slides[1].reload()
#            self.parousel.slides[2].reload()
#            self.parousel.slides[3].reload()
#        except AttributeError:
#            self.parousel.slides[1].source = "tot_bars.png"
#            self.parousel.slides[2].source = "nmax_bars.png"
#            self.parousel.slides[3].source = "nmin_bars.png"

        #self.parent.add_widget(Image(source = "./tot_bars.png"))

#        for i in range(len(self.databox.children)):
#            print i, "\t", (self.databox.children[i]).name_ti.text


class ScorekeepApp(App):
    def build(self):
        pass


if __name__ == "__main__":
# THIS IS TO ADJUST THE WINDOW SIZE THAT IS DISPLAYED. WILL BE DISCARDED WHEN PORTING TO ANDROID
    #Config.set('graphics', 'height', '600')
    #Config.set('graphics', 'width', '400')
    ScorekeepApp().run()
