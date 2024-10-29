
import unittest
import logging
import rt_with_exceptions

class RunnerTest(unittest.TestCase):


    def test_run(self):
        try:
            testrun = rt_with_exceptions.Runner(1000)
            for i in range(0,10):
                testrun.run()
            self.assertEqual(testrun.distance,200)
            logging.info('"test_run" выполнен успешно', exc_info = True)
        except:
            logging.error('Неверный тип данных для объекта Runner', exc_info=True)

    def test_walk(self):
        try:
            testwalk = rt_with_exceptions.Runner('walk', -5)
            for i in range(0,10):
                testwalk.walk()
            self.assertEqual(testwalk.distance, 50)
            logging.info('"test_walk" выполнен успешно', exc_info=True)
        except:
            logging.error('Неверная скорость для Runner', exc_info=True)

    def test_challenge(self):
        testrun = rt_with_exceptions.Runner('run')
        testwalk = rt_with_exceptions.Runner('walk')
        for i in range(0,10):
            testrun.run()
            testwalk.walk()
        self.assertNotEqual(testwalk.distance, testrun.distance)

    logging.basicConfig(level=logging.INFO, filename='runner_tests.log', filemode='w', encoding='utf-8',
                        format="%(asctime)s | %(levelname)s | %(message)s" )


if __name__ == '__main__':
    unittest.main()
