import os
import math
import chess.engine

file_path = os.path.dirname(os.path.abspath(__file__))
engine_path = 'chess-engine/stockfish-10-64'

class Engine(object):
  def __init__(self):
    self.engine = chess.engine.SimpleEngine.popen_uci(os.path.join(file_path, engine_path))
    self.engine.configure({'Skill Level': 1})

  def play(self, board):
    return self.engine.play(board, chess.engine.Limit(time=1.500))

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
    return round(100 * raw_score)

  def done(self):
    try:
      return self.engine.quit()
    except chess.engine.EngineTerminatedError:
      return None
