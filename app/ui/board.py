import chess
import pwd
import os

from client.ending import GameOver
from utils.core import Colors

PADDING = '    '

def flatten(l):
  return [item for sublist in l for item in sublist]

def safe_pop(l):
  try:
    return l.pop()
  except IndexError:
    return None

class Board(object):
  def __init__(self):
    self._score = 0
    self._cp = 0

  FILES = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

  def generate(self, fen, board, engine, game_over=None):
    if board.turn:
      # Print board before generating the score
      board_loading = self._generate(fen, board, game_over, True)
      print(board_loading)
      # Analyze the score and print the board again when we're done
      new_cp = engine.score(board)
      new_score = engine.normalize(new_cp)
      self._score = new_score if new_score is not None else self._score
      self._cp = new_cp if new_cp is not None else self._cp
      board_loaded = self._generate(fen, board, game_over)
      print(board_loaded)
    else:
      # Print board without generating the score
      board_loading = self._generate(fen, board, game_over)
      print(board_loading)

  def _generate(self, fen, board, game_over, loading=False):
    self.clear()
    is_check = board.is_check()
    loading_text = '   {}↻{}\n'.format(Colors.GRAY, Colors.RESET) if loading else '\n'

    # Label who's turn it is to move
    turn = fen.split(' ')[1]
    ui_board = self.get_title_from_move(turn)
    ui_board += '{}\n'.format(loading_text)

    position_changes = None
    try:
      san = board.peek()
      uci = board.uci(san)
      starting_position = uci[0:2]
      ending_position = uci[2:4]
      position_changes = (starting_position, ending_position)
    except IndexError:
      position_changes = None

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
      ui_board += '{}{}{} '.format(PADDING, Colors.GRAY, str(rank_i))
      # Add each piece + tile
      for piece in pieces:
        color = self.get_tile_color_from_position(rank_i, file_i, position_changes)
        ui_board += '{}{}'.format(color, piece)
        file_i = file_i + 1
      # Finish the rank
      ui_board += '{}  {}{}\n'.format(Colors.RESET, self.get_bar_section(rank_i), self.get_meta_section(board, rank_i, game_over))
      rank_i = rank_i - 1
    # Add files label
    ui_board += ' {}{}'.format(PADDING, Colors.GRAY)
    for f in self.FILES:
      ui_board += ' {}'.format(f)
    ui_board += '\n{}'.format(Colors.RESET)
    return ui_board

  def get_meta_section(self, board, rank, game_over):
    padding = '    '
    padding_alt = '   '
    just_played = game_over or (
      chess.WHITE
      if len(board.san_move_stack_white) > len(board.san_move_stack_black)
      else chess.BLACK
    )
    if rank == 1:
      return '  {}'.format(self.get_user())
    if rank == 2 and isinstance(just_played, GameOver):
      text = '{}{}'.format(Colors.ORANGE, self.string_of_game_over(game_over))
      return '{}{}'.format(padding, text)
    if rank == 3:
      return '{}{}┗━━━━━━━━━━━┛'.format(padding_alt, Colors.DULL_GRAY)
    if rank == 4:
      white_move = safe_pop(board.san_move_stack_white[-1:]) or ''
      black_move = safe_pop(board.san_move_stack_black[-1:]) or ''
      if just_played is chess.WHITE:
        text = '{}{}{}'.format(Colors.LIGHT, white_move.ljust(6), ''.ljust(4))
      elif just_played is chess.BLACK:
        text = '{}{}{}{}'.format(Colors.GRAY, white_move.ljust(6), Colors.LIGHT, black_move.ljust(4))
      else:
        text = '{}{}{}{}'.format(Colors.GRAY, white_move.ljust(6), Colors.GRAY, black_move.ljust(4))
      return '{}{}┃ {}{}┃'.format(padding_alt, Colors.DULL_GRAY, text, Colors.DULL_GRAY)
    if rank == 5:
      white_move = safe_pop(board.san_move_stack_white[-2:-1]) or ''
      black_move = safe_pop(board.san_move_stack_black[-2:-1]) or ''
      if just_played is chess.WHITE:
        black_move = safe_pop(board.san_move_stack_black[-1:]) or ''
      text = '{}{}{}{}'.format(Colors.GRAY, white_move.ljust(6), Colors.GRAY, black_move.ljust(4))
      return '{}{}┃ {}{}┃'.format(padding_alt, Colors.DULL_GRAY, text, Colors.DULL_GRAY)
    if rank == 6:
      return '{}{}┏━━━━━━━━━━━┓'.format(padding_alt, Colors.DULL_GRAY)
    if rank == 7:
      return '{}{}wp:{}%  cp:{}'.format(padding, Colors.DULL_GRAY, self._score, self._cp)
    if rank == 8:
      return '  {}'.format(self.get_user(True))
    return ''

  def get_user(self, is_computer=False):
    title = '{}BOT {}'.format(Colors.ORANGE, Colors.RESET) if is_computer else ''
    name = 'stockfish' if is_computer else pwd.getpwuid(os.getuid()).pw_name
    return '{}● {}{}{}{}'.format(Colors.DULL_GREEN, title, Colors.LIGHT, name, Colors.RESET)

  def get_bar_section(self, rank):
    percentage = ''
    tick = ' '
    color = Colors.DULL_GRAY
    normalized_score = self._score + 100
    block_range = rank * 25
    # Color the bar blocks
    if normalized_score > block_range:
      color = Colors.GREEN if self._score >= 0 else Colors.RED
    # Current bar block is within the block's value range
    # if normalized_score - block_range < 25 and normalized_score > block_range:
    #   percentage = '{}{}{}{}%'.format(Colors.RESET, Colors.BOLD, Colors.GRAY, self._score)
    if block_range == 125:
      tick = '{}_{}'.format(Colors.DULL_GRAY, color)
    return '{}{}█ {}{}'.format(color, tick, percentage, Colors.RESET)

  def get_title_from_move(self, turn):
    player = '{} to move'.format('Black' if turn == 'b' else 'White')
    colors = '{}'.format(\
      Colors.Backgrounds.BLACK + Colors.LIGHT if turn == 'b' else\
      Colors.Backgrounds.WHITE + Colors.DARK)
    return '\n\n {}{}  {}  {}'\
      .format(PADDING, colors, player, Colors.RESET)

  def get_tile_color_from_position(self, r, f, pos_delta):
    square_coordinates = self.get_coordinates_from_rank_file(r, f)
    highlight_dark = None
    highlight_light = None
    if pos_delta is not None:
      if square_coordinates in [pos_delta[0], pos_delta[1]]:
        highlight_light = Colors.Backgrounds.GREEN_LIGHT
        highlight_dark = Colors.Backgrounds.GREEN_DARK
    if r % 2 == 0:
      if f % 2 == 0:
        return highlight_dark or Colors.Backgrounds.DARK
      return highlight_light or Colors.Backgrounds.LIGHT
    if f % 2 == 0:
      return highlight_light or Colors.Backgrounds.LIGHT
    return highlight_dark or Colors.Backgrounds.DARK

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

  def get_coordinates_from_rank_file(self, r, f):
    file = self.FILES[f - 1]
    return '{}{}'.format(file, r)

  def string_of_game_over(self, game_over):
    if game_over is GameOver.BLACK_WINS:
      return 'Black wins by checkmate 0-1'
    if game_over is GameOver.WHITE_WINS:
      return 'White wins by checkmate 1-0'
    if game_over is GameOver.DRAW:
      return 'Draw ½ ½'
    if game_over is GameOver.RESIGN:
      return 'White resigns 0-1'
    return 'Game over'

  def clear(self):
    if os.name == 'nt': # For windows
      os.system('cls')
    else: # For mac and linux
      os.system('clear')
