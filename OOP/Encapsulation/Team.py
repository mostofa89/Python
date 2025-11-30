class Team:
    def __init__(self, team=None):
        self.__team = team
        self.___players = []


    def setName(self, team_name):
        self.__team = team_name


    def addPlayer(self, player):
        self.___players.append(player.name)


    def printDetail(self):
        print(f"""=====================
Team: {self.__team}
List of Players:
{self.___players}
=====================""")


class Player:
  def __init__(self, name):
    self.name = name



# Driver code
b = Team()
b.setName('Bangladesh')
mashrafi = Player("Mashrafi")
b.addPlayer(mashrafi)
tamim = Player("Tamim")
b.addPlayer(tamim)
b.printDetail()
a = Team("Australia")
ponting = Player("Ponting")
a.addPlayer(ponting)
lee = Player("Lee")
a.addPlayer(lee)
a.printDetail()