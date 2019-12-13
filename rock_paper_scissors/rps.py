#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  #n stands for number of rounds
  # 3 available options results in 3 ^ n for total no. of plays

    outcomes = []#collect the combinations played
    plays = ['rock','paper','scissors']
    
    #Logic to play the game
    #In a round you can make simple plays of above stated, how it changes when you have two rouds
    def game(plays_done, rounds_left_play):
        if rounds_left_play == 0:#end case where rounds reach 0, do no more plays and break out
            outcomes.append(plays_done)
            return
        for i in range(0,len(plays)):
             # Add plays to each of plays_done, call the function itself again with less round
             #
    
    game([],n)

    return outcomes

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')