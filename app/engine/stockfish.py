import os
import chess.engine

file_path = os.path.dirname(os.path.abspath(__file__))
engine_path = 'chess-engine/stockfish-10-64'

class Engine(object):
  def __init__(self):
    self.engine = chess.engine.SimpleEngine.popen_uci(os.path.join(file_path, engine_path))

  def play(self, board):
    return self.engine.play(board, chess.engine.Limit(time=1.500))

  def score(self, board):
    info = self.engine.analyse(board, chess.engine.Limit(time=0.100))
    return chess.engine.PovScore(info['score'], chess.WHITE)

  def done(self):
    return self.engine.quit()
