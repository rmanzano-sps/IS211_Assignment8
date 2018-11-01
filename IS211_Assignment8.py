import random

class Player:
    def __init__(self):
        self.playertype = None

    def getType(self):
        if self.playertype == 'h':
            self.playertype = 'Human Player'
        if self.playertype == 'c':
            self.playertype = 'Computer Player'
        return self.playertype

class ComputerPlayer(Player):
    def __init__(self, playertype):
        self.playertype = playertype

class HumanPlayer(Player):
    def __init__(self, playertype):
        self.playertype = playertype

class Pig:

    def __init__(self, player):
        self.player= player
        self.score = 0
        self.roll_value = 0

    def start_game(self):
        roll_die = self.roll_die()
        if roll_die != 1:
            current_score = ('{} your rolled a {}'.format(self.player, self.roll_value))
            print(current_score)
            return self.player_decision(roll_die)
        return roll_die

    def player_decision(self, roll_die):
        if self.score >= 100:
            return True
        decision = raw_input('{} your score is {}, would you like to roll again?(type r and return) or to hold(press return key)? '.format(self.player, self.score))
        return decision

    def roll_die(self):
        for x in range(1):
            self.roll_value = random.randint(1,6)
        if self.roll_value > 1:
            self.score = self.roll_value + self.score
            return self.score
        return self.roll_value


class PlayerFactory:
    def getPlayerType(self, player):
        if player == 'h':
            return HumanPlayer(player)
        if 'Human Player' in player:
            player_turn = Pig(player)
            return player_turn.start_game()
        if player == 'c':
            return ComputerPlayer(player)
        if 'Computer Player' in player:
            player_turn = Pig(player)
            return player_turn.start_game()
        assert 0, 'Invalid Entry' + player

class Game:

    def player_setup(self):
        factory = PlayerFactory()
        player_one = factory.getPlayerType(raw_input("Player One, computer or human?(type c or h and return key) ")).getType() + 'One'
        player_two = factory.getPlayerType(raw_input("Player One, computer or human?(type c or h and return key) ")).getType() + 'Two'
        return player_one, player_two

    def start_game(self, player_one, player_two):

        game_over = False
        factory = PlayerFactory()
        print(player_one, player_two, 'here')

        while not game_over:
            player_one_turn = factory.getPlayerType(player_one)
            if player_one_turn is not True:
                while player_one_turn == 'r':
                    player_one_turn = factory.getPlayerType(player_one)
            if player_one_turn is True:
                game_over = player_one_turn
                print('The winner is {}, with a score of {}, {} your score was {}.'.format(Pig.player, Pig.player_one, player_two, player_two))
                return game_over
            if player_one_turn == 1:
                print('Sorry {} you rolled a 1 and lost a turn, your current score is {}.'.format(player_one, player_one))
            else:
                print('Sorry {} you gave up a turn, your current score is {}.'.format(player_one, player_one))

            player_two_turn = factory.getPlayerType(player_two)
            if player_two_turn is not True:
                while player_two_turn == 'r':
                    player_two_turn = factory.getPlayerType(player_two)
            if player_two_turn is True:
                game_over = player_two_turn
                print('The winner is {}, with a score of {}, {} your score was {}.'.format(player_two, player_two, player_one, player_one))
                return game_over
            if player_two_turn == 1:
                print('Sorry {} you rolled a 1 and lost turn, your current score is {}.'.format(player_two, player_two))
            else:
                print('Sorry {} you gave up a turn, your current score is {}.'.format(player_two, player_two))


if __name__ == '__main__':
    game = Game()
    player_one, player_two = game.player_setup()
    game.start_game(player_one, player_two)
