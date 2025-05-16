# This entrypoint file to be used in development. Start by reading README.md
from RPS_game import play, mrugesh, abbey, quincy, kris
from RPS import player

# Playing a game
print("Playing against Quincy:")
quincy_results = play(player, quincy, 1000)
print(f"Win rate against Quincy: {quincy_results[0]*100:.2f}%")
print(f"Loss rate against Quincy: {quincy_results[1]*100:.2f}%")
print(f"Tie rate against Quincy: {quincy_results[2]*100:.2f}%")

print("\nPlaying against Abbey:")
abbey_results = play(player, abbey, 1000)
print(f"Win rate against Abbey: {abbey_results[0]*100:.2f}%")
print(f"Loss rate against Abbey: {abbey_results[1]*100:.2f}%")
print(f"Tie rate against Abbey: {abbey_results[2]*100:.2f}%")

print("\nPlaying against Kris:")
kris_results = play(player, kris, 1000)
print(f"Win rate against Kris: {kris_results[0]*100:.2f}%")
print(f"Loss rate against Kris: {kris_results[1]*100:.2f}%")
print(f"Tie rate against Kris: {kris_results[2]*100:.2f}%")

print("\nPlaying against Mrugesh:")
mrugesh_results = play(player, mrugesh, 1000)
print(f"Win rate against Mrugesh: {mrugesh_results[0]*100:.2f}%")
print(f"Loss rate against Mrugesh: {mrugesh_results[1]*100:.2f}%")
print(f"Tie rate against Mrugesh: {mrugesh_results[2]*100:.2f}%")

# Uncomment line below to play interactively against a bot:
# play(human, abbey, 20, verbose=True)

# Uncomment line below to run unit tests automatically
# from unittest import main
# main(module='test_module', exit=False)