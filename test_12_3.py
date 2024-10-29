import runner
import unittest

class RunnerTest(unittest.TestCase):
    is_frozen= False

    @unittest.skipIf(is_frozen, 'test выполняется')
    def test_run(self):
        testrun = runner.Runner('test1')
        for i in range(0,10):
            testrun.run()
        self.assertEqual(testrun.distance,100)

    @unittest.skipIf(is_frozen, 'test выполняется')
    def test_walk(self):
        testwalk = runner.Runner('walk')
        for i in range(0,10):
            testwalk.walk()
        self.assertEqual(testwalk.distance, 50)

    @unittest.skipIf(is_frozen, 'test выполняется')
    def test_challenge(self):
        testrun = runner.Runner('run')
        testwalk = runner.Runner('walk')
        for i in range(0,10):
            testrun.run()
            testwalk.walk()
        self.assertNotEqual(testwalk.distance, testrun.distance)



if __name__ == '__main__':
    unittest.main()

import runner_and_tournament as rt
import unittest

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(is_frozen, 'Тест заморожен')
    def setUp(self):
        self.r_1 = rt.Runner('Усейн', 10)
        self.r_2 = rt.Runner('Андрей', 9)
        self.r_3 = rt.Runner('Ник', 3)

    @unittest.skipIf(is_frozen, 'Тест заморожен')
    def test1(self):
        t1 = rt.Tournament(90, self.r_1, self.r_3)
        self.all_results[1] = t1.start()
        self.assertTrue(self.all_results[1][2] == self.r_3.name)

    @unittest.skipIf(is_frozen, 'Тест заморожен')
    def test2(self):
        t2 = rt.Tournament(90, self.r_2, self.r_3)
        self.all_results[2] = t2.start()
        self.assertTrue(self.all_results[2][2] == self.r_3.name)

    @unittest.skipIf(is_frozen, 'Тест заморожен')
    def test3(self):
        t3 = rt.Tournament(90, self.r_1, self.r_2, self.r_3)
        self.all_results[3] = t3.start()
        self.assertTrue(self.all_results[3][3] == self.r_3.name)



    @classmethod
    def tearDownClass(cls):

        for i in cls.all_results.values():
            res = {}
            for a,b in i.items():
                res[a]=b.name
            print(res)






