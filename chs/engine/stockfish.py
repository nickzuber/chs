import os
import platform
import math
import chess.engine
from chs.utils.core import Levels


file_path = os.path.dirname(os.path.abspath(__file__))

if 'Windows' in platform.system():
  engine_path = 'stockfish_10_x64_windows.exe'
elif 'Linux' in platform.system():
  engine_path = 'stockfish_10_x64_linux'
else:
  engine_path = 'stockfish_13_x64_mac'

class Engine(object):
  def __init__(self, level):
    self.engine = chess.engine.SimpleEngine.popen_uci(os.path.join(file_path, engine_path))
    self.engine.configure({'Skill Level': Levels.value(level)})

  def play(self, board, time=1.500):
    return self.engine.play(board, chess.engine.Limit(time=time))

  def score(self, board, pov=chess.WHITE):
    try:
      info = self.engine.analyse(board, chess.engine.Limit(time=0.500))
      cp = chess.engine.PovScore(info['score'], pov).pov(pov).relative.score()
      return cp
    except chess.engine.EngineTerminatedError:
      return None

  def normalize(self, cp):
    if cp is None:
      return None
    # https://github.com/ornicar/lila/blob/80646821b238d044aed5baf9efb7201cd4793b8b/ui/ceval/src/winningChances.ts#L10
    raw_score = 2 / (1 + math.exp(-0.004 * cp)) - 1
    return round(raw_score, 3)

  def done(self):
    try:
      return self.engine.quit()
    except chess.engine.EngineTerminatedError:
      return None
