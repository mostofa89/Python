class Player:
    def __init__(self, name, score, team="TeamA"):
        self.name = name
        self.score = score
        self.team = team


    def printDetails(self):
        print(f"{self.name}: Score {self.score}, Team: {self.team}")


    def merge(self, *players):
        for p in players:
            self.score += p.score
            if p.team != self.team:
                self.team = "MixedTeam"


if __name__ == "__main__":
    # Creating Player objects
    p1 = Player("Joy", 50, "TeamA")
    p2 = Player("Rahim", 30, "TeamA")
    p3 = Player("Karim", 40, "TeamB")

    print("---- Before Merge ----")
    p1.printDetails()
    p2.printDetails()
    p3.printDetails()

    print("\n---- Merging p2 and p3 into p1 ----")
    p1.merge(p2, p3)

    print("\n---- After Merge ----")
    p1.printDetails()
