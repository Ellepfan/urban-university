import unittest
import test_runner
import test_runner_and_tournament


runST = unittest.TestSuite()
runST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_runner.RunnerTest))
runST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_runner_and_tournament.TournamentTest))

run = unittest.TextTestRunner(verbosity=2)
run.run(runST)