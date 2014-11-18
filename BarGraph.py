from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty#, NumericProperty, BooleanProperty
from kivy.graphics import *

class BarGraph(Widget):
    '''Provides a basic horizontal bar graph'''
    def __init__(self, **kwargs):
        super(BarGraph, self).__init__(**kwargs)
        with self.canvas:
            Color(1, 1, 1, 1)
            self.background = Rectangle(size = self.size, pos = self.pos)
            Color(0, 0, 0, 1)
            self.baseline = Line(points = [0.1*self.width, 0.1*self.height, 0.1*self.width, 0.9*self.height], width = 2)

        self.norm_vals = []
        self.bars = InstructionGroup()
        self.bind(pos = self.update_rect)
        self.bind(size = self.update_rect)

#The update_rect function is required to update the graphics instructions 
#for drawing the rectangles and the lines are not updated automatically. 
#Initially, a 100px widget is created, which is not scaled in size to 
#fill the window when the program is run. To implement the scaling, we
#bind any change in the size or pos of the widget to this function so that
#the background and the line are updated to fill the window automatically. 
    def update_rect(self, *args):
        self.background.size = self.size
        self.background.pos = self.pos
        self.baseline.points = [0.2*self.width, 0.1*self.height, 0.2*self.width, 0.9*self.height]
        self.draw_bars()
        self.canvas.add(self.bars)
        print self.baseline.points

    def set_bars(self, values, *args):
        self.norm_vals = []
        for value in values:
            self.norm_vals.append(float(value)/float(max(values)))

    def draw_bars(self, *args):
        self.bars.clear()
        try:
            bar_height = 0.8*(self.baseline.points[3] - self.baseline.points[1])/len(self.norm_vals)
            bar_space = 0.2*(self.baseline.points[3] - self.baseline.points[1])/(len(self.norm_vals) - 1)
            print bar_height, bar_space, self.norm_vals
        except ZeroDivisionError:
            pass

        self.bars.add(Color(1,0,0,1))
        for i,v in enumerate(self.norm_vals):
            self.bars.add(Rectangle(size = (v*0.8*(self.width - self.baseline.points[0]), bar_height), 
                    pos = (self.baseline.points[0] + self.baseline.width, (i)*(bar_height + bar_space) + self.baseline.points[1])))
        

class BarGraphApp(App):
    def build(self):
        bg = BarGraph()
        bg.set_bars([100, 200, 212, 86])
        return bg
        pass

if __name__ == "__main__":

# THIS IS TO ADJUST THE WINDOW SIZE THAT IS DISPLAYED. WILL BE DISCARDED WHEN PORTING TO ANDROID
    #Config.set('graphics', 'height', '600')
    #Config.set('graphics', 'width', '400')
    BarGraphApp().run()
