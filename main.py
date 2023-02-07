from Player import PLayer
from Team import Team
from inputimeout import inputimeout,TimeoutOccurred
import random
class Auction(PLayer,Team):
    unsoldPLayerList=[]
    def  bidding(self):
        for player in PLayer.PlayerList:
            print(f"{player.name} -->{player.base_price}")
            index=random.randint(0,Auction.TeamCount-1)
            passCount=0
            lastTeambid=Auction.team_list[0]
            pre_bid_amount=0
            bid_amount=0
            while  True:
                if passCount==Team.TeamCount-1 and bid_amount!=0 or passCount>=Team.TeamCount:
                    break
    
                team=Auction.team_list[index]
                print(team.name+" --> "+str(team.balance))
              
                try:
                   bid_amount=int(inputimeout(prompt="enter the bidding amount  ",timeout=10))
                  
                except TimeoutOccurred:
                    print("timeout occurred ")
                    passCount+=1
                    index=(index+1)%Team.TeamCount
                    continue
                
                if team.balance<bid_amount+player.base_price:
                    print("dont have sufficient balance left")
                    passCount+=1
                    ##giving  bonus amount
                else:
                    if bid_amount<pre_bid_amount:
                        print("less than previous")
                        ##again take the input
                    else:
                        player.sold_price=bid_amount+player.base_price
                        lastTeambid=team
                        pre_bid_amount=bid_amount
                index=(index+1)%Team.TeamCount
               

                
            if passCount==Team.TeamCount:
                print('player unsold')
                Auction.unsoldPLayerList.append(player.name)
            else:
                lastTeambid.selected_player_list.append(player.name)
                print(player.name+"  --> player sold")
                


ob=Auction()
ob.registerTeam()
ob.registerPlayer()
ob.bidding()