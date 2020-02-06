import socket
from model.game_model import GameModel
from model.objct_to_dict_recursion import get_json
from _thread import *
from threading import Lock
from online_multiplayer.game_thread import game_thread
import json
from model.direction import Dir


def server(ip, port):
    # hostname = socket.gethostname()
    # host_ip = socket.gethostbyname(hostname)
    # port = 0
    # print(int(ip))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    """ tries to create socket at host ip address and port"""
    try:
        # s.bind((host_ip, port))
        s.bind((ip, port))
    except socket.error as err:
        print(err)
        return

    port = s.getsockname()[0]

    """ sets the socket to start listening for incoming connections """
    s.listen(2)

    def client_connection_thread(client_connection, player_index, game_id, has_ended_ref):
        client_connection.send(str(player_index).encode())  # sends to client if they are player 1 or 2
        while True:
            try:
                player_input = json.loads(client_connection.recv(1024 * 1))
                if not player_input:
                    games[game_id][2].acquire()
                    has_ended_ref[0] = True
                    games[game_id][2].release()
                else:
                    player_input = Dir[player_input]

                if len(games) > game_id:
                    game = games[game_id]

                    game[2].acquire()
                    game[1][player_index] = player_input
                    game[2].release()
                    game_model_dict = get_json(game[0])
                    game_model_str = json.dumps(game_model_dict)
                    # game_model_str = json.dumps(game_model_dict, indent=4)
                    if has_ended_ref[0]:
                        client_connection.sendall("none".encode())
                        break
                    # client_connection.sendall(game_model_str.encode())
                    print("sending:", client_connection.sendall(game_model_str.encode()))
                else:
                    print("No game found")
                    client_connection.sendall("none".encode())
                    break
            except Exception as err:
                print("ERROR in client thread:", err)
                break
        has_ended_ref[0] = True
        print("Connection Lost")
        try:
            del games[game_id]
            print("Game has closed")
        except Exception as err:
            print("closing game:", err)
        client_connection.close()

    player_id = 0
    games = {}
    while True:
        client_connection, client_ip = s.accept()
        print("Connected to:", client_ip)
        print(client_connection)

        if player_id < 2:
            game_id = player_id // 2
            player_index = player_id % 2
            if player_id % 2 == 0:
                lock = Lock()
                has_ended_ref = [False]
                game_model = GameModel(ready=False, num_players=2)
                games[game_id] = (game_model, [Dir.NONE, Dir.NONE], lock, has_ended_ref)
                print("Creating game, waiting for player 2")
                start_new_thread(game_thread, (games[game_id],))
            else:
                games[game_id][0].ready = True
                print("Game Start!")
            start_new_thread(client_connection_thread, (client_connection, player_index, game_id, games[game_id][3]))

        else:
            print("Game is full and/or in session")

        player_id += 1
        if player_id >= 2:
            break

