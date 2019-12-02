from Model import Model
from AI import AI
from DumbAI import DumbAI as dumb
from createDB import initDB
#Player one is smart AI and playerTwo is Dumb AI
class TrainAI:

    def __init__(self):
        self._model = Model(AI(), dumb())
        self._smartAIwins = 0
        self._smartAIlosses = 0
        self.gameLoop()

    def gameLoop(self):
               
        print("AI Trainer")
        print("===========")
        num_of_games = input("How games to play: ")

        while(not isinstance(num_of_games, int) and int(num_of_games) < 0):
            print("not a valid number of games")
            num_of_games = input("How games to play: ")

        print("Starting to train AI with {} Games...".format(num_of_games))
        for x in range(int(num_of_games)):

            #reinit each game
            self._model = Model(AI(), dumb())
            #Ship placement phase

            #place smart AI ships
            for ship in self._model.getPlayerOneShips():
                self._model.getPlayerOne().placeShip(ship)

            #dumb ai ship placement
            for ship in self._model.getPlayerTwoShips():
                self._model.getPlayerTwo().placeShip(ship)

            #Attack phase
            while not self._model.isGameOver():

                if self._model.allPlayerShipsSunk(self._model.getPlayerOne()) or self._model.allPlayerShipsSunk(self._model.getPlayerTwo()):
                    if(self._model.allPlayerShipsSunk(self._model.getPlayerOne())):
                        self._smartAIlosses += 1
                    elif(self._model.allPlayerShipsSunk(self._model.getPlayerTwo())):
                        self._smartAIwins += 1

                    self._model.endGame()

                else:
                    self._model.getPlayerOne().attack(self._model.getPlayerTwo())
                    self._model.getPlayerTwo().attack(self._model.getPlayerOne())
                    self._model.checkIfShipsNeedToBeSunk()

            print("{0}\r".format("Games Played " + str(x + 1)), end = "")

        print("SmartAI won: {}".format(self._smartAIwins))
        print("SmartAI losses: {}".format(self._smartAIlosses))
        print("Total: {}".format(num_of_games))
        print("...AI all Trained up")


game = TrainAI()