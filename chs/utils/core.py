from enum import Enum


class Colors:
  RESET  = '\x1b[49;0m'
  DARK   = '\x1b[38;5;232;1m'
  LIGHT  = '\x1b[38;5;231;1m'
  WHITE  = '\x1b[38;5;231;0m'
  GREEN  = '\x1b[38;5;2;1m'
  YELLOW = '\x1b[38;5;226;1m'
  ORANGE = '\x1b[38;5;208;1m'
  RED    = '\x1b[38;5;1m'
  GRAY   = '\x1b[38;5;242m'
  BOLD   = '\x1b[1m'
  UNDERLINE  = '\x1b[4m'
  DULL_GRAY  = '\x1b[38;5;238;1m'
  DULL_GREEN = '\x1b[38;5;28;1m'
  class Backgrounds:
    GREEN_DARK  = '\x1b[48;5;136;1m'
    GREEN_LIGHT = '\x1b[48;5;143;1m'
    PURPLE_DARK  = '\x1b[48;5;176;1m'
    PURPLE_LIGHT = '\x1b[48;5;177;1m'
    DARK  = '\x1b[48;5;172;1m'
    LIGHT = '\x1b[48;5;215;1m'
    BLACK = '\x1b[48;5;232;1m'
    WHITE = '\x1b[48;5;15;1m'
    RED   = '\x1b[48;5;9;1m'

class Styles:
  PADDING_SMALL  = '  '
  PADDING_MEDIUM = '      '
  PADDING_LARGE  = '          '

class Player(Enum):
  BLACK = 1
  WHITE = 2

class Levels:
  ONE   = 1
  TWO   = 2
  THREE = 3
  FOUR  = 4
  FIVE  = 5
  SIX   = 6
  SEVEN = 7
  EIGHT = 8

  @staticmethod
  def level_of_int(n):
    return max(1, min(n, 8))

  @staticmethod
  def value(l):
    print(l)
    lvls = [1, 4, 7, 10, 12, 14, 17, 20]
    return lvls[l - 1]
