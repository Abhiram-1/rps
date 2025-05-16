Rock Paper Scissors 
Overview
This project implements an intelligent Rock, Paper, Scissors  that uses multiple strategies to win against four different opponents. The bot analyzes opponent patterns, adapts its strategy, and consistently achieves a win rate of over 60% against each opponent.
Features

Pattern recognition to detect opponent strategies
Frequency analysis to counter most common moves
Adaptive learning that improves as games progress
Memory management between function calls
Multi-strategy approach to handle different opponent styles

Files

RPS.py - Contains the bot implementation
RPS_game.py - Game logic and opponent bots (provided by freeCodeCamp)
main.py - Test script to run games against each opponent
test_module.py - Unit tests to verify the bot's performance

How to Run

Ensure all files are in the same directory
Run the bot against all opponents:
python main.py

To run the unit tests, uncomment the last two lines in main.py and run again

Performance
The bot consistently achieves:

~73% win rate against Quincy
~69% win rate against Abbey
~69% win rate against Kris
~68% win rate against Mrugesh

All win rates exceed the 60% requirement for passing the challenge.
Strategy
The bot uses a combination of pattern matching and frequency analysis:

It tracks the opponent's previous moves to identify patterns
It predicts the next move based on identified patterns
It falls back to countering the most frequent move when patterns aren't clear
It starts with Paper as a default first move (beats Rock, which is a common first choice)

Challenge Requirements
This solution passes all tests in the freeCodeCamp "Rock Paper Scissors" Machine Learning Project challenge.
