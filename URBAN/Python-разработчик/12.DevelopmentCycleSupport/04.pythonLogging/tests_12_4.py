import unittest
import rt_with_exceptions
import logging


class RunnerTest(unittest.TestCase):
    logging.basicConfig(level=logging.INFO,
                        filename="runner_tests.log",
                        filemode='w',
                        encoding='utf-8',
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    def test_walk(self):
        try:
            test1 = rt_with_exceptions.Runner("test1", -5)
            for i in range(10):
                test1.walk()
            self.assertEqual(test1.distance, 50)
            logging.info('"test_walk" выполнен успешно', exc_info=True)
        except:
            logging.warning("Неверная скорость для Runner", exc_info=True)

    def test_run(self):
        try:
            test2 = rt_with_exceptions.Runner(5)
            for i in range(10):
                test2.run()
            self.assertEqual(test2.distance, 100)
            logging.info('"test_run" выполнен успешно', exc_info=True)
        except:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    def test_challenge(self):
        test3 = rt_with_exceptions.Runner("test3")
        test4 = rt_with_exceptions.Runner("test4")
        for i in range(10):
            test3.walk()
            test4.run()
        self.assertNotEqual(test3.distance, test4.distance)


if __name__ == '__main__':
    unittest.main()
