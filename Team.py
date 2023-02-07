from abstractClass import TeamImpliment

class Team(TeamImpliment):

    team_list=[]
    TeamCount=0
    
    def __init__(self) -> None:
        self.name=""
        self.balance=0
        self.bonus_balance=0
        self.selected_player_list=[]
        self.no_of_players_in_team=0

    def registerTeam(self):
        Team.TeamCount=int(input("enter no of teams  "))
        for count in range(0,Team.TeamCount):
            teamName=input("enter team name  ")
            bal=int(input("enter initial baalnce "))
            ob=Team()
            ob.name=teamName
            ob.balance=bal
            ob.bonus_balance=ob.balance*0.25
            Team.team_list.append(ob)
    
    def display_player_list():...