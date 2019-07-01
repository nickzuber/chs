#!/usr/bin/env python

import sys
import os

file_path = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(file_path, 'chs/VERSION')

if len(sys.argv) > 1 and sys.argv[1] == 'major':
  opened_file = open(file, 'r')
  [major, minor, patch] = opened_file.read().rstrip().split('.')
  old_version = '{}.{}.{}'.format(major, minor, patch)
  new_major = int(major) + 1
  new_version = '{}.{}.{}'.format(new_major, '0', '0')
  opened_file.close()
  opened_file = open(file, 'w')
  opened_file.write(new_version)
  opened_file.close()
  print('\x1b[38;5;1m ↘ \x1b[38;5;231;1m' + old_version + '\x1b[49;0m\n\x1b[38;5;2m ↗ \x1b[38;5;231;1m' + new_version + '\x1b[49;0m')

if len(sys.argv) > 1 and sys.argv[1] == 'minor':
  opened_file = open(file, 'r')
  [major, minor, patch] = opened_file.read().rstrip().split('.')
  old_version = '{}.{}.{}'.format(major, minor, patch)
  new_minor = int(minor) + 1
  new_version = '{}.{}.{}'.format(major, new_minor, '0')
  opened_file.close()
  opened_file = open(file, 'w')
  opened_file.write(new_version)
  opened_file.close()
  print('\x1b[38;5;1m ↘ \x1b[38;5;231;1m' + old_version + '\x1b[49;0m\n\x1b[38;5;2m ↗ \x1b[38;5;231;1m' + new_version + '\x1b[49;0m')

if len(sys.argv) > 1 and sys.argv[1] == 'patch':
  opened_file = open(file, 'r')
  [major, minor, patch] = opened_file.read().rstrip().split('.')
  old_version = '{}.{}.{}'.format(major, minor, patch)
  new_patch = int(patch) + 1
  new_version = '{}.{}.{}'.format(major, minor, new_patch)
  opened_file.close()
  opened_file = open(file, 'w')
  opened_file.write(new_version)
  opened_file.close()
  print('\x1b[38;5;1m ↘ \x1b[38;5;231;1m' + old_version + '\x1b[49;0m\n\x1b[38;5;2m ↗ \x1b[38;5;231;1m' + new_version + '\x1b[49;0m')
