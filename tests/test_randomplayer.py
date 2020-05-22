import random
import unittest
from src import game

class RandomPlayerTest(unittest.TestCase):
	
    def toggle_random_player(self):
        player = game.who_play_first()
		self.assertEqual(player, )

if __name__ == '__main__':
	unittest.main()
