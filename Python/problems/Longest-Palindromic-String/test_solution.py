import unittest
from solution import solution
class TestSolution(unittest.TestCase):
  def longest_palindromic_string(self):
    sol = solution()
    self.assertEqual (sol.longestPalindrome("babad","bab"),"bab")
    self.assertEqual (sol.longestPalindrome("cbbd","bb"),"bb")
if __name__== '__main__':
  unittest.main()
