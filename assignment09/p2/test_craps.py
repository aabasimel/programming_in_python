# test_craps.py

# CTMS-14
# a9 p2.py
# Ahmed Abasimel
# aabasimel@constructor.university

"""
This program tests the functionality of the Player class from craps.py
by playing a few games of craps.
"""

from craps import Player, playOneGame, playManyGames

def main():
    
    print("Testing single game:\n")
    playOneGame()  # Plays one full game and prints outcome
    
    print("\nTesting multiple games:\n")
    playManyGames()  # Asks user for number of games, then shows stats

if __name__ == "__main__":
    main()
