import random

class Player:

    def __init__(self):
        self.name = None
        self.playertype = None
        self.score = None

class ComputerPlayer(Player):
    def __init__(self, playertype):
        self.playertype = playertype

class HumanPlayer(Player):
    def __init__(self, playertype):
        self.playertype = playertype

class Factory:
    def getPlayer(self, playerone, playertwo):
        print(playerone.items()[1],'20')

class Game:
    pass
    # def __init__(self):

class StartGame:

    def __init__(self):
        self.playerone = {}
        self.playertwo = {}
        self.players = [1, 2]

    def setupPlayer(self):

        for player in self.players:
            print(player, '32')
            player_name = raw_input("Player, what is your name? ")
            player_type = raw_input("Player, are you a computer or human? ")

            if player == 1:
                self.playerone = {player_name: player_type}
            else:
                self.playertwo= {player_name: player_type}

        print(self.playerone, '36')
        print(self.playertwo, '37')
        factory = Factory()
        playerone = factory.getPlayer(self.playerone, self.playertwo)
        # playertwo = factory.getPlayer(self.playertwo)


if __name__ == '__main__':
    startgame = StartGame().setupPlayer()
    print(startgame, '47')
