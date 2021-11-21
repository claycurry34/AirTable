import time
from typing import List


class NetworkConnection:
    """ Class : NetworkConnection
    Forms a high level API system supporting network capabilities for
    all functionality supported on the iLearn System"""
    client_name: str = None
    # identifies the name of the server name of the host that this is connected to.
    connection_ID: str = None
    # The unique identifier for this connection between client and server
    isAlive: bool = False
    # True if the client is connected to a server.
    isReady: bool = False
    # Flag to control whether state updates are sent to this
    lastMessageTime: float = 0
    # The last time that a message was received on this connection


class NetworkServer(NetworkConnection):
    serverIP: str = None
    # the IP address of the server that this client is connected to.
    serverPort: str = None
    # the port of the server that this client is connected to.


class SinglePlayerServer(NetworkServer):

    def __init__(self):
        pass


class MultiplayerServer(NetworkServer):
    lobby_ID: str = None
    # the name of the lobby on the server
    allClients: List[str] = None
    # List of active network clients (static).

    def __init__(self):
        pass

    def get_num_players(self) -> int:
        return len(self.allClients)
