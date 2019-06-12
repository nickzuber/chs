
import chess

from ui.board import Board
from engine.parser import FenParser
from engine.stockfish import Engine
from os import system, name

class Client(object):
  def __init__(self):
    self.ui_board = Board()
    self.board = chess.Board()
    self.parser = FenParser(self.board.fen())
    self.engine = Engine()

  def run(self):
    try:
      while True:
        to_move = self.parser.get_to_move(self.fen())
        if to_move == 'w':
          self.make_turn()
        else:
          self.computer_turn()
    except KeyboardInterrupt:
      self.clear()
      print(self.ui_board.get_board_from_fen(self.fen(), self.board.is_check()))
      print('\nWhite resigns 0-1')
    self.engine.done()

  def make_turn(self, failed=False):
    self.clear()
    print(self.ui_board.get_board_from_fen(self.fen(), self.board.is_check()))
    if failed:
      print('Illegal move, try again')
    else:
      print('')
    move = input('Your move: ')
    try:
      self.board.push_san(move)
    except ValueError:
      self.make_turn(True)

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
