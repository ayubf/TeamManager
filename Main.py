from Classes.Team import Team
from Classes.Coach import Coach
from Classes.Player import Player

def main():
    rockets = Team("82-0", {}, "Houston", "Rockets", 20, "Toyota Center", 69, "logo.png", "Run As One")
    rockets.add(Player("John John",20, 21, 69.4, 20.1, 3.1, 3, 39, 1.0, "", "2019", [10000, 5], False, "Small Forward", "Hey"))
    rockets.add(Coach("Joseph Joestar", rockets.name, 55, 15, [500, 1], [1000, 2], "coach.png", "Really good coach ngl"))
    print(rockets.getRoster())
    rockets.drop(21)
    print(rockets.coach.getSummary())
    print(rockets.getRoster())
    print(rockets.getSummary())



main()