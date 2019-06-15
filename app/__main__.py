#!/usr/bin/env python

import sys
from utils.core import Colors, Levels
from client.runner import Client

def main():
  try:
    num = int(sys.argv[1].split('=')[1])
    level = Levels.level_of_int(num)
  except:
    level = Levels.ONE
  client = Client(level)
  client.run()

if __name__ == '__main__':
  try:
    main()
  except Exception as exception:
    print(Colors.RED + '\nUncaught error "{}", exiting the app.\n'.format(
      exception.__class__.__name__
    ))
