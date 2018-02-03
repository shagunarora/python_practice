import random
print("SET NUMBER OF PLAYERS")
x=int(input())
print("                    RULES                    ")
print("    All {} players will roll dice for 3 times      ".format(x))
print("    the player having maximum sum will WIN     ")



class players:
    def __init__(self):
        pass

    def throw_dice(self):
        self.player=random.randint(1,6)
        return(self.player)

player_list=[]
for i in range(0,3*x):
    player=players()
    input("PRESS ENTER TO THROW DICE")
    player_list.append(player.throw_dice())
    print(player_list[i])

print()
print("          AFTER   THREE   TURNS        ")
print()
t=0
for i in range(0,x):
        print("{} player:".format(i+1),player_list[i],player_list[i+x],player_list[i+2*x],"  total:",player_list[i]+player_list[i+x]+player_list[i+2*x])
        y=player_list[i]+player_list[i+x]+player_list[i+2*x]
        if y>t:
            t=y
            cout=i+1



print()
print("                 WINNER             ")
print("")
print("{} player".format(cout))
print()
