
import chess
import editdistance

from ui.board import Board
from engine.parser import FenParser
from engine.stockfish import Engine
from utils.core import Colors

class GameOverException(Exception):
  pass

class WhiteWinsException(GameOverException):
  pass

class BlackWinsException(GameOverException):
  pass

class DrawException(GameOverException):
  pass

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
      self.ui_board.generate(self.fen(), self.board, self.engine)
      print('Black wins')
    except WhiteWinsException:
      # TODO
      self.ui_board.generate(self.fen(), self.board, self.engine)
      print('White wins')
    except DrawException:
      # TODO
      self.ui_board.generate(self.fen(), self.board, self.engine)
      print('Draw')
    finally:
      self.engine.done()

  def white_resigns(self):
    self.ui_board.generate(self.fen(), self.board, self.engine)
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
    self.ui_board.generate(self.fen(), self.board, self.engine)
    if failed:
      if prev_move == self.BACK:
        print('You cannot go back, no moves were made')
      else:
        error_string = 'Illegal move, try again'
        maybe_move = self.closest_move(prev_move)
        if maybe_move is not None:
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
        san = self.board.push_san(move)
        # print(self.board.uci(san))
        # _ = input('halt!')
    except ValueError:
      self.make_turn((True, move))
    except IndexError:
      self.make_turn((True, move))

  def computer_turn(self):
    self.ui_board.generate(self.fen(), self.board, self.engine)
    print('\nWaiting for Stockfish...')
    result = self.engine.play(self.board)
    self.board.push(result.move)

  def fen(self):
    return self.board.fen()
