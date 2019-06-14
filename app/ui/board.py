import chess
from os import system, name

from utils.core import Colors

PADDING = '    '

def flatten(l):
  return [item for sublist in l for item in sublist]

class Board(object):
  def __init__(self):
    self._score = 0

  FILES = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

  def generate(self, fen, board, engine):
    if board.turn:
      # Print board before generating the score
      board_loading = self._generate(fen, board, True)
      print(board_loading)
      # Analyze the score and print the board again when we're done
      new_score = engine.score(board)
      self._score = new_score if new_score is not None else self._score
      board_loaded = self._generate(fen, board)
      print(board_loaded)
    else:
      # Print board without generating the score
      board_loading = self._generate(fen, board)
      print(board_loading)

  def _generate(self, fen, board, loading=False):
    self.clear()
    is_check = board.is_check()
    loading_text = 'loading...' if loading else ''

    # Label who's turn it is to move
    turn = fen.split(' ')[1]
    board = self.get_title_from_move(turn)

    board += '{}\n'.format(loading_text)

    # Draw the board and pieces
    positions = fen.split(' ')[0]
    ranks = positions.split('/')
    rank_i = 8

    def get_piece_composed(piece):
      if turn == 'b':
        return self.get_piece(piece, is_check, False)
      else:
        return self.get_piece(piece, False, is_check)

    for rank in ranks:
      file_i = 1
      pieces = flatten(map(get_piece_composed, list(rank)))
      board += '{}{} '.format(PADDING, str(rank_i))
      # Add each piece + tile
      for piece in pieces:
        color = self.get_tile_color_from_position(rank_i, file_i)
        board = '{}{}{}'.format(board, color, piece)
        file_i = file_i + 1
      # Finish the rank
      board = '{}{}  {}\n'.format(board, Colors.RESET, self.get_bar_section(rank_i))
      rank_i = rank_i - 1
    # Add files label
    board += ' {}'.format(PADDING)
    for f in self.FILES:
      board += ' {}'.format(f)
    board += '\n'
    return board

  def get_bar_section(self, rank):
    color = Colors.LIGHT
    score = ''
    if rank == 1:
      score = '{}{}{}%'.format(Colors.RESET, Colors.GRAY, self._score)
    return '{}█ {}{}'.format(color, score, Colors.RESET)

  def get_title_from_move(self, turn):
    player = '{} to move'.format('Black' if turn == 'b' else 'White')
    colors = '{}'.format(\
      Colors.Backgrounds.BLACK + Colors.LIGHT if turn == 'b' else\
      Colors.Backgrounds.WHITE + Colors.DARK)
    return '\n {}{}  {}  {} \n{}\n'\
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

  def get_piece(self, letter, is_black_check, is_white_check):
    black_king_color = Colors.Backgrounds.RED if is_black_check else Colors.DARK
    white_king_color = Colors.Backgrounds.RED if is_white_check else Colors.LIGHT
    pieces = {
      # White
      'R': [Colors.LIGHT + '♜ ' + Colors.RESET],
      'N': [Colors.LIGHT + '♞ ' + Colors.RESET],
      'B': [Colors.LIGHT + '♗ ' + Colors.RESET],
      'Q': [Colors.LIGHT + '♕ ' + Colors.RESET],
      'K': [white_king_color + '♔ ' + Colors.RESET],
      'P': [Colors.LIGHT + '♙ ' + Colors.RESET],
      # Black
      'r': [Colors.DARK + '♜ ' + Colors.RESET],
      'n': [Colors.DARK + '♞ ' + Colors.RESET],
      'b': [Colors.DARK + '♝ ' + Colors.RESET],
      'q': [Colors.DARK + '♛ ' + Colors.RESET],
      'k': [black_king_color + '♚ ' + Colors.RESET],
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

  def clear(self):
    if name == 'nt': # For windows
      system('cls')
    else: # For mac and linux
      system('clear')
