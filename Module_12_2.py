import runner_and_tournament as rt
import unittest

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}



    def setUp(self):
        self.r_1 = rt.Runner('Усейн', 10)
        self.r_2 = rt.Runner('Андрей', 9)
        self.r_3 = rt.Runner('Ник', 3)


    def test1(self):
        t1 = rt.Tournament(90, self.r_1, self.r_3)
        self.all_results[1] = t1.start()
        self.assertTrue(self.all_results[1][2] == self.r_3.name)


    def test2(self):
        t2 = rt.Tournament(90, self.r_2, self.r_3)
        self.all_results[2] = t2.start()
        self.assertTrue(self.all_results[2][2] == self.r_3.name)

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








if __name__ == '__main__':
    unittest.main()

# {1: Усэйн, 2: Ник}
# {1: Андрей, 2: Ник}
# {1: Андрей, 2: Усэйн, 3: Ник}