import os
import platform
import math
import chess.engine
from chs.utils.core import Levels


file_path = os.path.dirname(os.path.abspath(__file__))

if 'Windows' in platform.system():
  engine_path = 'stockfish_10_x64_windows.exe'
elif 'Linux' in platform.system():
  engine_path = '/usr/games/stockfish'
else:  
  engine_path = 'stockfish_10_x64_mac'

class Engine(object):
  def __init__(self, level):
    self.engine = chess.engine.SimpleEngine.popen_uci(os.path.join(file_path, engine_path))
    self.engine.configure({'Skill Level': Levels.value(level)})

  def play(self, board, time=1.500):
    return self.engine.play(board, chess.engine.Limit(time=time))

  def score(self, board):
    try:
      info = self.engine.analyse(board, chess.engine.Limit(time=0.500))
      cp = chess.engine.PovScore(info['score'], chess.WHITE).pov(chess.WHITE).relative.score()
      return cp
    except chess.engine.EngineTerminatedError:
      return None

  def normalize(self, cp):
    if cp is None:
      return None
    raw_score = 2 / (1 + math.exp(-0.004 * cp)) - 1
    return round(raw_score, 1)

  def done(self):
    try:
      return self.engine.quit()
    except chess.engine.EngineTerminatedError:
      return None
