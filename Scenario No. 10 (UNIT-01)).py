# Cricket Team Management System using OOP

class Player:
    def __init__(self, player_name, jersey_number, runs):
        self.player_name = player_name
        self.jersey_number = jersey_number
        self.runs = runs
        self.category = self.assign_category()

    # Assign category based on runs
    def assign_category(self):
        if self.runs >= 1000:
            return "Excellent"
        elif self.runs >= 500:
            return "Good"
        else:
            return "Average"

    # Display player details
    def display(self):
        print("Player Name   :", self.player_name)
        print("Jersey Number :", self.jersey_number)
        print("Runs          :", self.runs)
        print("Category      :", self.category)
        print("----------------------------")


class Team:
    def __init__(self, team_name):
        self.team_name = team_name
        self.players = []

    # Add player to team
    def add_player(self, player):
        self.players.append(player)

    # Display all players
    def display_all_players(self):
        print("\nTeam Name:", self.team_name)
        print("===== Player Records =====")

        for player in self.players:
            player.display()


# Create Team object
team = Team("Indian Cricket Team")

# Create Player objects
player1 = Player("Virat", 18, 1200)
player2 = Player("Rohit", 45, 850)
player3 = Player("Rahul", 1, 600)
player4 = Player("Hardik", 33, 350)

# Add players to team
team.add_player(player1)
team.add_player(player2)
team.add_player(player3)
team.add_player(player4)

# Display all players
team.display_all_players()
