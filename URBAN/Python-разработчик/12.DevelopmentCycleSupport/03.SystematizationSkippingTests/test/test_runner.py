import unittest
from src import runner


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        test1 = runner.Runner("test1")
        for i in range(10):
            test1.walk()
        self.assertEqual(test1.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        test2 = runner.Runner("test2")
        for i in range(10):
            test2.run()
        self.assertEqual(test2.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        test3 = runner.Runner("test3")
        test4 = runner.Runner("test4")
        for i in range(10):
            test3.walk()
            test4.run()
        self.assertNotEqual(test3.distance, test4.distance)


if __name__ == '__main__':
    unittest.main()
