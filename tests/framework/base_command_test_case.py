import re
import json
import os
import subprocess
from unittest import TestCase


class BaseCommandTestCase(TestCase):

  _working_directory = os.path.dirname(os.path.realpath(__file__))

  def call(self, *commands):
    response = subprocess.check_output(list(commands))
    if 'done' in response:
      return True
    if 'failed' in response:
      return False
    return None

  def is_success(self, result):
    return result == self._success

  def is_failed(self, result):
    return result == self._failed

  def is_warning(self, result):
    return result == self._warning

  def tearDown(self):
    pass
