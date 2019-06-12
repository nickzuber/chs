class Colors:
  RESET = '\033[49;0m'
  DARK  = '\033[38;5;232;1m'
  LIGHT  = '\033[38;5;231;1m'
  class Backgrounds:
    DARK = '\033[48;5;172;1m'
    LIGHT = '\033[48;5;215;1m'
    BLACK = '\033[48;5;232;1m'
    WHITE = '\033[48;5;15;1m'

PADDING = '    '

def flatten(l):
  return [item for sublist in l for item in sublist]

class Board(object):
  FILES = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

  def get_board_from_fen(self, fen):
    # Label who's turn it is to move
    to_move = fen.split(' ')[1]
    board = self.get_title_from_move(to_move)

    # Draw the board and pieces
    positions = fen.split(' ')[0]
    ranks = positions.split('/')
    rank_i = 8
    for rank in ranks:
      file_i = 1
      pieces = flatten(map(self.get_piece, list(rank)))
      board += '{}{} '.format(PADDING, str(rank_i))
      # Add each piece + tile
      for piece in pieces:
        color = self.get_tile_color_from_position(rank_i, file_i)
        board = '{}{}{}'.format(board, color, piece)
        file_i = file_i + 1
      # Finish the rank
      board = '{}{}\n'.format(board, Colors.RESET)
      rank_i = rank_i - 1
    # Add files label
    board += '  {}'.format(PADDING)
    for f in self.FILES:
      board += ' {}'.format(f)
    return board

  def get_title_from_move(self, turn):
    player = '{} to move'.format('Black' if turn == 'b' else 'White')
    colors = '{}'.format(\
      Colors.Backgrounds.BLACK + Colors.LIGHT if turn == 'b' else\
      Colors.Backgrounds.WHITE + Colors.DARK)
    return '\n{}{}   {}   {}\n{}{}                   {}\n\n'\
      .format(PADDING, colors, player, Colors.RESET,\
              PADDING, colors, Colors.RESET)

  def get_tile_color_from_position(self, r, f):
    if r % 2 == 0:
      if f % 2 == 0:
        return Colors.Backgrounds.DARK
      return Colors.Backgrounds.LIGHT
    if f % 2 == 0:
      return Colors.Backgrounds.LIGHT
    return Colors.Backgrounds.DARK

  def get_piece(self, letter):
    pieces = {
      # White
      'R': [Colors.LIGHT + '♜ ' + Colors.RESET],
      'N': [Colors.LIGHT + '♞ ' + Colors.RESET],
      'B': [Colors.LIGHT + '♗ ' + Colors.RESET],
      'Q': [Colors.LIGHT + '♕ ' + Colors.RESET],
      'K': [Colors.LIGHT + '♔ ' + Colors.RESET],
      'P': [Colors.LIGHT + '♙ ' + Colors.RESET],
      # Black
      'r': [Colors.DARK + '♜ ' + Colors.RESET],
      'n': [Colors.DARK + '♞ ' + Colors.RESET],
      'b': [Colors.DARK + '♝ ' + Colors.RESET],
      'q': [Colors.DARK + '♛ ' + Colors.RESET],
      'k': [Colors.DARK + '♚ ' + Colors.RESET],
      'p': [Colors.DARK + '♙ ' + Colors.RESET],
      '1': ['  '],
      '2': ['  ', '  '],
      '3': ['  ', '  ', '  '],
      '4': ['  ', '  ', '  ', '  '],
      '5': ['  ', '  ', '  ', '  ', '  '],
      '6': ['  ', '  ', '  ', '  ', '  ', '  '],
      '7': ['  ', '  ', '  ', '  ', '  ', '  ', '  '],
      '8': ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']
    }
    return pieces.get(letter)
