import unittest
from solution import Solution
class TestSolution(unittest.TestCase):
  def permute(self):
    sol = solution()
    self.assertEqual (sol.permute([1,2,3],[[3,2,1],[2,3,1],[1,3,2],[3,1,2],[2,1,3],[1,2,3]]),[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]])
    self.assertEqual (sol.permute([0,1],[[1,0],[0,1]]),[[0,1],[1,0]])
    self.assertEqual (sol.permute([1][[1]]),[[0,1],[[1]])
if __name__== '__main__':
  unittest.main()
