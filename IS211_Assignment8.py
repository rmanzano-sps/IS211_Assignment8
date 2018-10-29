class PlayerBase:
    def __init__(self):
        self.name = None
        self.palyerType = None

    def getName(self):
        return self.name

    def getpalyerType(self):
        return self.palyerType

class ComputerPlayer(PlayerBase):
    pass
    #computer player

class HumanPlayer(PlayerBase):
    pass

class PlayerFactory:
    def getPerson(self, name, palyerType):
        if palyerType == 'H':
            return HumanPlayer(name)
        if palyerType == 'C':
            return ComputerPlayer(name)


class Game:
    pass


if __name__ == '__main__':
    playerType = PlayerFactory()

    
