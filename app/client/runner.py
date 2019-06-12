
import chess
import editdistance
from os import system, name

from ui.board import Board
from engine.parser import FenParser
from engine.stockfish import Engine
from utils.core import Colors

class GameOverException(Exception):
  """
  Raised when the game is over.
  """

class WhiteWinsException(GameOverException):
  """
  Raised when White wins.
  """

class BlackWinsException(GameOverException):
  """
  Raised when Black wins.
  """

class DrawException(GameOverException):
  """
  Raised when there is a draw.
  """

class Client(object):
  BACK = 'back'

  def __init__(self):
    self.ui_board = Board()
    self.board = chess.Board()
    self.parser = FenParser(self.board.fen())
    self.engine = Engine()

  def run(self):
    try:
      while True:
        self.check_game_over()
        to_move = self.parser.get_to_move(self.fen())
        if to_move == 'w':
          self.make_turn()
        else:
          self.computer_turn()
    except KeyboardInterrupt:
      self.white_resigns()
    except BlackWinsException:
      # TODO
      self.clear()
      print(self.ui_board.get_board_from_fen(self.fen(), self.board.is_check()))
      print('Black wins')
    except WhiteWinsException:
      # TODO
      self.clear()
      print(self.ui_board.get_board_from_fen(self.fen(), self.board.is_check()))
      print('White wins')
    except DrawException:
      # TODO
      self.clear()
      print(self.ui_board.get_board_from_fen(self.fen(), self.board.is_check()))
      print('Draw')
    self.engine.done()

  def white_resigns(self):
    self.clear()
    print(self.ui_board.get_board_from_fen(self.fen(), self.board.is_check()))
    print('\nWhite resigns')

  def check_game_over(self):
    if self.board.is_game_over():
      result = self.board.result()
      if result == '1-0':
        raise WhiteWinsException
      if result == '0-1':
        raise BlackWinsException
      if result == '1/2-1/2':
        raise DrawException

  def moves(self):
    return map(self.board.san, self.board.legal_moves)

  def closest_move(self, illegal_move):
    for move in self.moves():
      distance = editdistance.eval(move, illegal_move)
      if distance <= 1:
        return move
    return None

  def make_turn(self, meta=(False, None)):
    (failed, prev_move) = meta
    self.clear()
    print(self.ui_board.get_board_from_fen(self.fen(), self.board.is_check()))
    if failed:
      if prev_move == self.BACK:
        print('You cannot go back, no moves were made')
      else:
        error_string = 'Illegal move, try again'
        maybe_move = self.closest_move(prev_move)
        if maybe_move != None:
          error_string += '. Did you mean {}{}{}?'.format(Colors.BOLD, maybe_move, Colors.RESET)
        print(error_string)
    else:
      print('')
    move = input('Your move: ')
    try:
      if move == self.BACK:
        self.board.pop()
        self.board.pop()
      else:
        self.board.push_san(move)
    except ValueError:
      self.make_turn((True, move))
    except IndexError:
      self.make_turn((True, move))

  def computer_turn(self):
    self.clear()
    print(self.ui_board.get_board_from_fen(self.fen(), self.board.is_check()))
    print('\nWaiting for Stockfish...')
    result = self.engine.play(self.board)
    self.board.push(result.move)

  def fen(self):
    return self.board.fen()

  def clear(self):
    if name == 'nt': # For windows
      system('cls')
    else: # For mac and linux
      system('clear')
