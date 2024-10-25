import runner
import unittest

class RunnerTest(unittest.TestCase):
    def test_run(self):
        testrun = runner.Runner('test1')
        for i in range(0,10):
            testrun.run()
        self.assertEqual(testrun.distance,100)

    def test_walk(self):
        testwalk = runner.Runner('walk')
        for i in range(0,10):
            testwalk.walk()
        self.assertEqual(testwalk.distance, 50)

    def test_challenge(self):
        testrun = runner.Runner('run')
        testwalk = runner.Runner('walk')
        for i in range(0,10):
            testrun.run()
            testwalk.walk()
        self.assertNotEqual(testwalk.distance, testrun.distance)



if __name__ == '__main__':
    unittest.main()
