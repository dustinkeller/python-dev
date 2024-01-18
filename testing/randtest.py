import unittest
import random_guess2

class TestRandom(unittest.TestCase):
    def test_input(self):
        answer = 5
        guess = 5
        result = random_guess2.run_guess(guess, answer)
        self.assertTrue(result)

    def test_input_wrong_guess(self):
        answer = 5
        guess = 1
        result = random_guess2.run_guess(guess, answer)
        self.assertFalse(result)

    def test_input_oor(self):
        answer = 5
        guess = 11
        result = random_guess2.run_guess(guess, answer)
        self.assertFalse(result)

    def test_input_wrong_type(self):
        pass #test if the type is wrong

if __name__ == '__main__':
    unittest.main()