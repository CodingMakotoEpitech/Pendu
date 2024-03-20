#
#  pendu.py
#  Pendu
#

import misc
import const
import random

class Pendu():

  word_to_guess = ""
  guessed_letters = ""
  used_letters = ""
  error_count = 0

  def __init__(self, word=None):
    if (word != None):
      self.word_to_guess = word.upper()
    else:
      self.word_to_guess = random.choice(const.WORDS).upper()

    self.guessed_letters = "_" * len(self.word_to_guess)
    self.used_letters = " "
    self.error_count = 0

    self.update_guessed_letters(" ")

  def show_game_status(self):
    print(f'\n<< {self.guessed_letters} >>\n')
    print(f'Lettres utilisées :{self.used_letters}')
    print(f'Chances restantes : {const.MAX_ERROR - self.error_count}')
    print(f'{const.PENDU_ASCII[self.error_count]}\n')

  def _update_guessed_letters(self, char, indexes):
    for index in indexes:
      self.guessed_letters = self.guessed_letters[:index] + char + self.guessed_letters[index+1:]

  def update_guessed_letters(self, char):
    indexes = misc.all_indexes(self.word_to_guess, char)
    self._update_guessed_letters(char, indexes)
    return len(indexes)

