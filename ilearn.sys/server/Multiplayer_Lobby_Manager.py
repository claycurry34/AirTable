from typing import List


class MultiplayerLobbyManager:
    """
    A specialized type of NetworkManager that provides a multiplayer lobby before entering the main play scene of the
    game. It allows clients to become players
    """
    allClients: List[str] = None

    def __init__(self):
        pass
