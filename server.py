import socket
from model.game_model import GameModel
from model.objct_to_dict_recursion import get_json
from _thread import *
from threading import Lock
from online_multiplayer.game_thread import game_thread
import json
from model.direction import Dir
import global_variables as gv

import sys
# import win32api as api
# import win32process as proc


def server():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    # print("Enter port: ", end="")
    # port = sys.stdin.readline().split("\n")[0]
    # port = input("Enter port: ")
    port = 7777
    # print(port)
    # if not port.isdigit():
    #     port = 0
    # else:
    #     port = int(port)
    # print(int(ip))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    """ tries to create socket at host ip address and port"""
    try:
        # s.bind((host_ip, port))
        s.bind((ip, port))
    except socket.error as err:
        print(err)
        return

    port = s.getsockname()[1]
    print(f'{ip}:{port}')

    """ sets the socket to start listening for incoming connections """
    s.listen(2)

    def client_connection_thread(client_connection, player_index, game_id, has_ended_ref):
        ready_sent = False
        highest = 0
        client_connection.send(str(player_index).encode())  # sends to client if they are player 1 or 2
        while True:
            try:
                player_input = json.loads(client_connection.recv(11))
                if not player_input:
                    print("NOT PLAYER")
                    games[game_id][2].acquire()
                    has_ended_ref[0] = True
                    print("Game has ended")
                    client_connection.sendall("none".encode())
                    games[game_id][2].release()
                    break
                else:
                    player_input = Dir[player_input]

                if game_id in games:
                    game = games[game_id]

                    # if game[0].ready and not ready_sent:
                    #     print("sending ready")
                    #     ready_sent = True
                    #     client_connection.sendall("ready".encode())

                    game[2].acquire()
                    game[1][player_index] = player_input
                    output_vehicles = []
                    for vehicle in game[0].vehicles:
                        # output_vehicles.append(vehicle.movement_pattern)
                        for i, movement in enumerate(gv.MOVEMENT_PATTERNS):
                            if movement == vehicle.movement_pattern:
                                output_vehicles.append(i)
                                break
                        output_vehicles.append(vehicle.x)
                        output_vehicles.append(vehicle.y)
                        output_vehicles.append(vehicle.health)
                        # output_vehicles.append(gv.WINDOW_W)
                        # output_vehicles.append(gv.WINDOW_L+gv.PLAYER_LENGTH)
                        # output_vehicles.append(1000)
                    game[2].release()
                    # print(output_vehicles)
                    # game_model_dict = get_json(game[0])
                    # game_model_str = json.dumps(game_model_dict)
                    # game_model_str = json.dumps(game_model_dict, indent=4)
                    if has_ended_ref[0]:
                        print("Game has ended")
                        client_connection.sendall("none".encode())
                        break
                    x = client_connection.send(json.dumps(output_vehicles).encode())
                    # highest = max(highest, x)
                    # print(highest)
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
            print("closing game:", game_id)
        except Exception as err:
            print("game closed")
        client_connection.close()

    player_id = 0
    games = {}
    while True:
        client_connection, client_ip = s.accept()
        print("Connected to:", client_ip)
        game_id = player_id // 2
        player_index = player_id % 2
        if player_id % 2 == 0:
            has_ended_ref = [False]
            game_model = GameModel(ready=False, num_players=2)
            games[game_id] = (game_model, [Dir.NONE, Dir.NONE], Lock(), has_ended_ref)
            print(f"Creating game: {game_id}, waiting for player 2")
            start_new_thread(game_thread, (games[game_id],))
        else:
            if game_id in games:
                print("Game Start!")
                games[game_id][0].ready = True
            else:
                player_id += 1
                game_id = player_id // 2
                player_index = player_id % 2
                games[game_id] = (GameModel(ready=False, num_players=2), [Dir.NONE, Dir.NONE], Lock(), [False])
                print(f"Creating game: {game_id}, waiting for player 2")
                start_new_thread(game_thread, (games[game_id],))
        start_new_thread(client_connection_thread, (client_connection, player_index, game_id, games[game_id][3]))
        player_id += 1
        if player_id >= 999999999:
            print("After 999,999,999 iterations, the server stops")
            break

server()

# if game_id >= 50:
#     print("Server is full, please try again later")
#     continue

