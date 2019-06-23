import os
import subprocess

from chs.ui.board import Board
from tests.framework.base_command_test_case import BaseCommandTestCase


ui = Board(1)

class TestInit(BaseCommandTestCase):
  def test_no_captured_pieces(self):
    fen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'
    (w, b) = ui._get_captured_pieces(fen)
    self.assertEqual(w, '', 'Failed on no white pieces captured.')
    self.assertEqual(b, '', 'Failed on no black pieces captured.')

  def test_one_captured_pawn(self):
    fen = 'rnbqkbnr/pppp1ppp/8/8/8/8/PPP1PPPP/RNBQKBNR'
    (w, b) = ui._get_captured_pieces(fen)
    self.assertEqual(w, 'P', 'Failed on one captured white pawn.')
    self.assertEqual(b, 'p', 'Failed on one captured black pawn.')

  def test_multi_captured_pawns(self):
    fen = 'rnbqkbnr/p4ppp/8/2P1p3/8/8/PP5P/RNBQKBNR'
    (w, b) = ui._get_captured_pieces(fen)
    self.assertEqual(w, 'PPPP', 'Failed on multiple captured white pawns.')
    self.assertEqual(b, 'ppp', 'Failed on multiple captured black pawns.')

  def test_one_captured_knight(self):
    fen = 'r1bqkbnr/pppppppp/8/8/8/8/PPPPPPPP/R1BQKBNR'
    (w, b) = ui._get_captured_pieces(fen)
    self.assertEqual(w, 'N', 'Failed on one captured white knight.')
    self.assertEqual(b, 'n', 'Failed on one captured black knight.')

  def test_multi_captured_knights(self):
    fen = 'r1bqkb1r/pppppppp/8/8/8/8/PPPPPPPP/R1BQKB1R'
    (w, b) = ui._get_captured_pieces(fen)
    self.assertEqual(w, 'NN', 'Failed on multiple captured white knights.')
    self.assertEqual(b, 'nn', 'Failed on multiple captured black knights.')

  def test_multi_captured_pieces(self):
    fen = '1Qb2rk1/5ppp/1p1p4/3p4/8/4PN2/PPP2PPP/R1B1KB1R'
    (w, b) = ui._get_captured_pieces(fen)
    self.assertEqual(w, 'PN', 'Failed on a variety of captured white pieces.')
    self.assertEqual(b, 'pprbnnq', 'Failed on a variety of captured black pieces.')

  def tearDown(self):
    pass
