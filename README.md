Murdle is a variant of the classic game 'Worlde'.


In Wordle, at the start of the day, a new five-letter word is chosen randomly. Each player has 6 turns.
During each turn, players enter a valid five-letter word, and are given feedback on each letter.
This feedback can be one of three options:
  Correct and in the correct place
  Correct but in the incorrect place
  Incorrect
Then, players can proceed to the next turn with this new information, and try again to guess the correct word.
The goal of Wordle is to guess the correct word within the 6 turns available.
If you fail, you must wait until the next day to try to guess a new random word.

Murdle is not exactly the same as Wordle.
Most notably, the correct answer is not chosen at the start of the day. Instead, Murdle is a deterministic game.
At the start of any given game, any possible five-letter word could still be the correct answer.
Each turn, the feedback given is selected such that the player is given the least information possible.

This will narrow down the number of possible words remaining.
In Murdle, the goal is not to guess the single correct word per se, but instead to narrow the pool of possible words to include only one word.
If you can do so and then guess that single word within your given 6 turns, you win.

Notably, since this version of Murdle is played in command-line, for feedback, instead of using colours (green, yellow, grey), the numbers (2,1,0) are used instead.

As explained above, Murdle is deterministic, and does not require a single new word to be selected every day.
These features give rise to a few important user-side differences:
  Murdle is much harder than Wordle
  You can play as many times as you want, without waiting for the next word tomorrow
  Murdle is predictable, so if you can win once, you can continue to win using the same sequence of guesses indefinitely

After a single solution has been found, it is suggested to try limiting yourself to different guesses to keep the game interesting.

I hope you enjoy Murdle!
In order to play, please download the game, and run main.py in python.
