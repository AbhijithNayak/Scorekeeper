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


