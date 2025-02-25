import unittest
from src.logic import determine_winner

class TestLogic(unittest.TestCase):

    def test_player_wins(self):
        self.assertEqual(determine_winner('rock', 'scissors'), 'player')
        self.assertEqual(determine_winner('scissors', 'paper'), 'player')
        self.assertEqual(determine_winner('paper', 'rock'), 'player')

    def test_computer_wins(self):
        self.assertEqual(determine_winner('scissors', 'rock'), 'computer')
        self.assertEqual(determine_winner('paper', 'scissors'), 'computer')
        self.assertEqual(determine_winner('rock', 'paper'), 'computer')

    def test_tie(self):
        self.assertEqual(determine_winner('rock', 'rock'), 'tie')
        self.assertEqual(determine_winner('paper', 'paper'), 'tie')
        self.assertEqual(determine_winner('scissors', 'scissors'), 'tie')

if __name__ == '__main__':
    unittest.main()