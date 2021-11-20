from typing import List
import Network_Connection


class Game:
    title: str = None
    # the (possibly trademarked) title of the game
    author: str = None
    # the entity/author who created the game
    publisher: str = None
    # the entity with publishing rights to the game
    age_requirement: int = None
    # the minimum age required to play the game

class SingleplayerGame(Game):
    session: Network_Connection.PlayerClient = None


class MultiplayerGame(Game):
    session: Network_Connection.MultiplayerClient = None
