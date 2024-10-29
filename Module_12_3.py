import unittest
import  test_12_3



CompetitionST = unittest.TestSuite()
CompetitionST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3.RunnerTest))
CompetitionST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(CompetitionST)

