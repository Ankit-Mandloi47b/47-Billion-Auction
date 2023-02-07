from abstractClass import PLayerImpliment

class PLayer(PLayerImpliment):
    PlayerCount=0
    PlayerList=[]
    def __init__(self) -> None:
        self.name=""
        self.base_price=0
        self.sold_price=0

    def registerPlayer(self):
        PLayer.PlayerCount=int(input("enter no of players"))
        for count in range(0,PLayer.PlayerCount):
            PlayerName=input("enter Player name  ")
            basePrice=int(input("enter  basePrice "))
            ob=PLayer()
            ob.name=PlayerName
            ob.base_price=basePrice          
            PLayer.PlayerList.append(ob)    
    