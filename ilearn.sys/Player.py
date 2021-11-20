from typing import List
from User import User
from Game import Game


class Player(User):
    activeGame: Game
    # the game the player is currently playing
    active_statistics: List[str]
