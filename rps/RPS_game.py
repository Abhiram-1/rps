# DO NOT MODIFY THIS FILE

import random


def play(player1, player2, num_games, verbose=False):
    p1_prev_play = ""
    p2_prev_play = ""
    results = [0, 0, 0]
    for _ in range(num_games):
        p1_play = player1(p2_prev_play)
        p2_play = player2(p1_prev_play)

        if p1_play == p2_play:
            results[2] += 1
            winner = "Tie."
        elif (p1_play == "R" and p2_play == "S") or (
                p1_play == "P" and p2_play == "R") or (
                p1_play == "S" and p2_play == "P"):
            results[0] += 1
            winner = "Player 1 wins."
        elif (p2_play == "R" and p1_play == "S") or (
                p2_play == "P" and p1_play == "R") or (
                p2_play == "S" and p1_play == "P"):
            results[1] += 1
            winner = "Player 2 wins."

        if verbose:
            print("Player 1:", p1_play, "| Player 2:", p2_play, "| Winner:", winner)

        p1_prev_play = p1_play
        p2_prev_play = p2_play

    games_won = results[0] + results[1]

    if games_won == 0:
        win_rate = 0
    else:
        win_rate = results[0] / games_won

    print("Final results:", results)
    print(f"Player 1 win rate: {win_rate:.2%}")

    return [win_rate, results[1] / games_won if games_won > 0 else 0, results[2] / num_games]


def quincy(prev_play, counter=[0]):
    counter[0] += 1
    choices = ["R", "R", "P", "P", "S"]
    return choices[counter[0] % len(choices)]


def mrugesh(prev_play, prev_play_2=""):
    if prev_play == "":
        prev_play = "R"
    ideal_response = {"P": "S", "R": "P", "S": "R"}
    return ideal_response[prev_play]


def abbey(prev_play, history=[]):
    if prev_play == "":
        history.clear()
        return "S"

    history.append(prev_play)

    last_ten = history[-10:]
    most_frequent = max(set(last_ten), key=last_ten.count)

    ideal_response = {"P": "S", "R": "P", "S": "R"}
    return ideal_response[most_frequent]


def kris(prev_play):
    if prev_play == "":
        return "R"
    elif prev_play == "R":
        return "P"
    elif prev_play == "P":
        return "S"
    else:
        return "R"


def human(prev_play):
    valid_play = False
    play = ""
    while not valid_play:
        play = input("Select R, P, or S: ")
        if play in ["R", "P", "S"]:
            valid_play = True

    return play