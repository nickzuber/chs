#!/usr/bin/env python

import sys
import os
from chs.utils.core import Colors, Levels
from chs.client.runner import Client


def get_version():
  file_path = os.path.dirname(os.path.abspath(__file__))
  version_file = open(os.path.join(file_path, '../VERSION'), 'r')
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

def main():
  if len(sys.argv) > 1 and is_help_command(sys.argv[1]):
    print('Usage: chs [COMMAND]\n')
    print('Valid values for [COMMAND]')
    print('  help         Print all the possible usage information')
    print('  version      Print the current version')
    print('  level=[LVL]  Start a game with the given difficulty level')
    print('\nValid values for [LVL]')
    print('  1     The least difficult setting')
    print('  2..7  Increasing difficulty')
    print('  8     The most difficult setting')
    print('')
  elif len(sys.argv) > 1 and is_version_command(sys.argv[1]):
    print('Running chs {}v{}{}\n'.format(Colors.BOLD, get_version(), Colors.RESET))
    print('')
  else:
    try:
      num = int(sys.argv[1].split('=')[1])
      level = Levels.level_of_int(num)
    except:
      level = Levels.ONE
    client = Client(level)
    client.run()

def run():
  try:
    main()
  except Exception as exception:
    print(Colors.RED + '\nUncaught error "{}", exiting the app.\n'.format(
      exception.__class__.__name__
    ))
