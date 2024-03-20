#
#  misc.py
#  Pendu
#

def all_indexes(string, char):
  return [i for i in range(len(string)) if string.startswith(char, i)]

def get_char(prompt=""):
  input_value = input(prompt)
  if len(input_value) >= 1:
    return input_value[0].upper()
  return " "
