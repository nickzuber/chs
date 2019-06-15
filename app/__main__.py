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
  print(level)
  _ = input('halt')
  client = Client()
  client.run()

if __name__ == '__main__':
  try:
    main()
  except:
    print(Colors.RED + '\n\nError: something went wrong, exiting the app.\n')
