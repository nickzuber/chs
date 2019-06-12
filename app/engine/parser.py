class FenParser(object):
  """
  Initializes with basic parsing of FEN notation.
  https://en.wikipedia.org/wiki/Forsyth%E2%80%93Edwards_Notation
  """
  def __init__(self, fen):
    parsed = fen.split(' ')
    self.positions = parsed[0].split('/')
    self.to_move = parsed[1]
    self.castles = parsed[2]
    self.en_passant = parsed[3]
    self.halfmove_clock = parsed[4]
    self.fullmove_number = parsed[4]

  def get_to_move(self, fen):
    parsed = fen.split(' ')
    return parsed[1]
