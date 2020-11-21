from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

world = World()


map_file = "maps/main_maze.txt"

room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

world.print_rooms()

player = Player(world.starting_room)

traversal_path = []

visited = {}

my_path = []

back_direction = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}


visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")