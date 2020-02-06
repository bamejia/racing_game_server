import socket
import json
from model.direction import Dir
from model.game_model import GameModel
from model.objct_to_dict_recursion import get_json


class Client:
    def __init__(self, server_addr):
        self.__client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__server_addr = server_addr
        self.__player_index = self.connect()

    """ METHODS """
    def connect(self):
        """
        connects to server
        :return:
        player index (0:player 1 | 1:player 2)
        if could not connect, returns None
        """
        self.client.connect(self.server_addr)
        js = json.loads(self.client.recv(2048 * 2))
        return js

    """ METHODS """
    def communicate(self, player_inputs):
        """
        sending and receiving off information between the client and server
        :param player_inputs:
        player movement inputs of their vehicle
        :return:
        GameModel object
        """
        if isinstance(player_inputs, Dir):
            player_input = player_inputs.name
            self.client.sendall(json.dumps(player_input).encode())
        else:
            player_input = "false"
            self.client.sendall(player_input.encode())
        try:
            json_string = self.client.recv(1024*55).decode()  # 1024 * 63
            if json_string == "none":
                return None
            obj = GameModel.from_json(json_string)
            return obj
        except Exception as err:
            print("ERROR IN receiving:", err)
            return None

    """ GETTERS """
    @property
    def client(self):
        return self.__client

    @property
    def server_addr(self):
        return self.__server_addr

    @property
    def player_index(self):
        return self.__player_index
