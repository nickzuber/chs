#!/usr/bin/env python

import sys
import os
from chs.utils.core import Colors, Levels
from chs.client.runner import Client, Player


def get_version():
  file_path = os.path.dirname(os.path.abspath(__file__))
  version_file = open(os.path.join(file_path, 'VERSION'), 'r')
  return version_file.read().rstrip()

def is_help_command(arg):
  return (
    arg == 'help' or
    arg == '--h' or
    arg == '--help' or
    arg == '-help' or
    arg == '-h'
  )

def is_version_command(arg):
  return (
    arg == 'version' or
    arg == '--v' or
    arg == '--version' or
    arg == '-version' or
    arg == '-v'
  )

def get_level_from_args(args):
  lvl = [arg for arg in args if "--level" in arg]
  if lvl:
    try:
      num = int(lvl[0].split('=')[1])
      return Levels.level_of_int(num)
    except:
      return Levels.ONE
  return Levels.ONE

def get_player_from_args(args):
  player = [arg for arg in args if "--play-black" in arg]
  if player:
    return Player.BLACK
  return Player.WHITE

def main():
  if len(sys.argv) > 1 and is_help_command(sys.argv[1]):
    print('Usage: chs [COMMAND] [FLAGS]\n')
    print('Valid values for [COMMAND]')
    print('  help         Print all the possible usage information')
    print('  version      Print the current version')
    print('\nValid values for [FLAGS]')
    print('  --play-black   Play the game with the black pieces')
    print('  --level=[LVL]  Start a game with the given difficulty level')
    print('\nValid values for [LVL]')
    print('  1     The least difficult setting')
    print('  2..7  Increasing difficulty')
    print('  8     The most difficult setting')
    print('')
    print('How to play: Your move: [MOVE]\n')
    print('Valid values for [MOVE]:')
    print('        Make moves using valid alegraic notation (e.g. Nf3, e4, etc.)')
    print('  back  Take back your last move')
    print('  hint  Get a hint from the engine')
    print('')
  elif len(sys.argv) > 1 and is_version_command(sys.argv[1]):
    print('Running chs {}v{}{}\n'.format(Colors.BOLD, get_version(), Colors.RESET))
  else:
    try:
      level = get_level_from_args(sys.argv)
      play_as = get_player_from_args(sys.argv)
    except:
      level = Levels.ONE
      play_as = Player.WHITE
    print(play_as)
    client = Client(level)
    client.run()

def run():
  try:
    main()
  except Exception as exception:
    print(Colors.RED + '\nUncaught error "{}", exiting the app.\n'.format(
      exception.__class__.__name__
    ))
