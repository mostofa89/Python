class Player:
    total = 0
    players_list = []

    def __init__(self, name = None, jersey_num = 10, team = None):
        self.name = name
        self.jersey_num = jersey_num
        self.team = team
        Player.total +=1
        Player.players_list.append(name)



    def set_name(self, name):
        self.name = name
        for i in range(len(Player.players_list)):
            if Player.players_list[i] == None:
                Player.players_list[i] = name



    def set_team(self, team):
        self.team = team


    def set_number(self, num):
        self.jersey_num = num


    @classmethod
    def info(cls):
        print(f"Total number of players: {Player.total}")
        print("Players enlisted so far: ", end = "")
        for i in range(len(Player.players_list)):
            if i == len(Player.players_list) - 1:
                print(Player.players_list[i])

            else:
                print(Player.players_list[i], end = ", ")


    def player_detail(self):
        return f"""Player Name: {self.name}
Jersey Number: {self.jersey_num}
Country: {self.team}"""


print("Total number of players:", Player.total)
print("---------------------------")
p1 = Player()
p1.set_name("Neymar")
p1.set_team("Brazil")
print(p1.player_detail())
print('========================')
Player.info()
print("---------------------------")
p2 = Player("Ronaldo")
p2.set_number(7)
p2.set_team("Portugal")
print(p2.player_detail())
print('========================')
Player.info()
print("---------------------------")
p3 = Player("Messi")
p3.set_team("Argentina")
print(p3.player_detail())
print('========================')
Player.info()
print("---------------------------")
p4 = Player("Mbappe", 10, "France")
print(p4.player_detail())
print('========================')
Player.info()