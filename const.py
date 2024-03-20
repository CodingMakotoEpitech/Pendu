#
#  main.py
#  Pendu
#

WORDS = [
  "Noeud",
  "Pomme",
  "Poire",
  "Radis",
  "Robot",
  "Alarme",
  "Ananas",
  "Humour",
  "Podium",
  "Puzzle",
  "Tomate",
  "Billard",
  "Corbeau",
  "Journal",
  "Sifflet",
  "Sucette",
  "Trousse",
  "Batterie",
  "Logiciel",
  "Objectif",
  "Tabouret",
  "Scorpion",
  "Ascenseur",
  "Forteresse",
  "Populaire",
  "Attraction",
  "Bouillotte",
  "Aventurier",
  "Grenouille",
  "Impossible",
  "Qualification",
  "Sorcellerie",
  "Banquise",
  "Aquarium",
  "Losange",
  "Grandir",
  "Tomate",
  "Cabane",
  "manger",
  "boire",
  "aimer",
  "dormir",
  "jouer",
  "maison",
  "jardin",
  "parler",
  "Crayon",
  "Maman",
  "Livre"
]

PENDU_ASCII = [
  """






  ==========
  """,
  """

    |
    |
    |
    |
    |
  ==========
  """,
  """
    +---+
    |
    |
    |
    |
    |
  ==========
  """,
  """
    +---+
    |   |
    |   o
    |
    |
    |
  ==========
  """,
  """
    +---+
    |   |
    |   o
    |   |
    |
    |
  ==========
  """,
  """
    +---+
    |   |
    |   o
    |  /|
    |
    |
  ==========
  """,
  """
    +---+
    |   |
    |   o
    |  /|\\
    |
    |
  ==========
  """,
  """
    +---+
    |   |
    |   o
    |  /|\\
    |  /
    |
  ==========
  """,
  """
    +---+
    |   |
    |   o
    |  /|\\
    |  / \\
    |
  ==========
  """
]

MAX_ERROR = len(PENDU_ASCII) - 1
