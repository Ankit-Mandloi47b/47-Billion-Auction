from abc import ABC,abstractclassmethod

class PLayerImpliment(ABC):

    @abstractclassmethod
    def registerPlayer(self):...

class TeamImpliment(ABC):
    
    @abstractclassmethod
    def registerTeam(self):...

    @abstractclassmethod
    def display_player_list(self):...