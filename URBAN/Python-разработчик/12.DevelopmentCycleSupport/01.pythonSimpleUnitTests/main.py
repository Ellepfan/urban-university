import unittest
import runner


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        test1 = runner.Runner("test1")
        for i in range(10):
            test1.walk()
        self.assertEqual(test1.distance, 50)

    def test_run(self):
        test2 = runner.Runner("test2")
        for i in range(10):
            test2.run()
        self.assertEqual(test2.distance, 100)

    def test_challenge(self):
        test3 = runner.Runner("test3")
        test4 = runner.Runner("test4")
        for i in range(10):
            test3.walk()
            test4.run()
        self.assertNotEqual(test3.distance, test4.distance)



    def test_walk1(self):
        test11 = runner.Runner("test1")
        for i in range(10):
            test11.walk()
        self.assertEqual(test11.distance, 100)

    def test_run2(self):
        test22 = runner.Runner("test2")
        for i in range(10):
            test22.run()
        self.assertEqual(test22.distance, 50)


if __name__ == '__main__':
    unittest.main()


