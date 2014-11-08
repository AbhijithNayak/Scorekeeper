import matplotlib.pyplot as plt
from numpy import linspace

class ScoreDB():
    """Contains all the data required for the plotter"""
    def __init__(self):
        self.player_list = []
        self.total_list = []
        self.round_list = []
        self.nmax_list = []
        self.nmin_list = []
    
    def reset_db(self):
        """Currently the same as __init__, added only to avoid 
        using __init__ directly in the future"""
        self.player_list = []
        self.total_list = []
        self.round_list = []

    def add_player_info(self, player, total, roundscore):
        """Method to add a player *player to this database"""
        self.player_list.append(player)
        self.total_list.append(total)
        self.round_list.append(roundscore)

        for i in range(len(self.player_list) - len(self.nmax_list)):
            self.nmax_list.insert(0, 0)
            self.nmin_list.insert(0, 0)

    def update_max_min(self):
        """Update the nmax and nmin lists that count number of times max/
        min for each player"""
        print "PLAYER", "\t", "TOTAL", "\t", "ROUND", "\t", "NMAX", "\t", "NMIN"
        for i in range(len(self.round_list)):
            if self.round_list[i] == max(self.round_list):
                self.nmax_list[i] += 1

            if self.round_list[i] == min(self.round_list):
                self.nmin_list[i] += 1

            print self.player_list[i], "\t", self.total_list[i], "\t", self.round_list[i], "\t", self.nmax_list[i], "\t", self.nmin_list[i]


    def update_plots(self):
        """Generate and update plots - 
        Three plots are generated
        1. Plot of totals 
        2. Plot of nmax 
        3. Plot of nmin
        All plots are barh"""

#THIS IS THE COLOR MAP - GIST_EARTH SET IS CHOSEN in range 0.2 to 0.9
        clist = plt.cm.gist_earth(linspace(0.2, 0.9, len(self.player_list)))
        title_dict = {"tot_bars": "Total Scores", "nmax_bars": "High Counts", "nmin_bars": "Low Counts"}

        def setup_plot(values, save_as):
            #SETTING AXIS PARAMETERS TO BEAUTIFY 
            ax = plt.axes()
            ax.xaxis.set_visible(False)
            ax.spines['top'].set_color('none')
            ax.spines['bottom'].set_color('none')    
            ax.spines['right'].set_color('none')   

            #PLOT THE BARS
            h_bars = plt.barh(range(len(self.player_list)), width = values)

            #SET THE COLOURS
            for bar in h_bars:
                bar.set_fc(clist[h_bars.index(bar)])
                bar.set_ec(clist[h_bars.index(bar)])
                if int(bar.get_width()) is not 0:
                    ax.text(bar.get_x() + 0.5*bar.get_width(), bar.get_y() + 0.5*bar.get_height(), str(int(bar.get_width())))

            ax.set_yticks([h_bars[0].get_height()*0.5 + i for i in range(len(values))])
            ax.set_yticklabels(self.player_list, rotation = 45)
            ax.tick_params(right = 'off', left = 'off')
            plt.suptitle(title_dict[save_as], weight = 'bold', color = (0, 0.4, 0.8))
            plt.savefig(str(save_as) + ".png")
            plt.close()

        setup_plot(self.total_list, "tot_bars")
        setup_plot(self.nmax_list, "nmax_bars")
        setup_plot(self.nmin_list, "nmin_bars")
#        self.tot_bars = plt.barh(range(len(self.player_list)), width = self.total_list)
#        setup_axis(ax)
#        plt.savefig("tot_bars.png")
#
#        self.nmax_bars = plt.barh(range(len(self.player_list)), width = self.nmax_list)
#        ax = plt.axes()
#        setup_axis(ax)
#        plt.savefig("nmax_bars.png")
#        plt.close()
#
#        self.nmin_bars = plt.barh(range(len(self.player_list)), width = self.nmin_list)
#        ax = plt.axes()
#        setup_axis(ax)
#        plt.savefig("nmin_bars.png")
#        plt.close()


