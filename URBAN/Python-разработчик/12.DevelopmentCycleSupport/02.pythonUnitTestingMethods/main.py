import pprint
import unittest
from runner_and_tournament import Runner, Tournament


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.sportsman_1 = Runner("Усэйн", 10)
        self.sportsman_2 = Runner("Андрей", 9)
        self.sportsman_3 = Runner("Ник", 3)

    def test_race1(self):
        competitions1 = Tournament(90, self.sportsman_1, self.sportsman_3)
        result1 = competitions1.start()
        self.all_results['1 забег'] = result1
        test = result1[len(result1)].name
        self.assertTrue(test == "Ник")


    def test_race2(self):
        competitions2 = Tournament(90, self.sportsman_2, self.sportsman_3)
        result2 = competitions2.start()
        self.all_results['2 забег'] = result2
        test = result2[len(result2)].name
        self.assertTrue(test == "Ник")

    def test_race3(self):
        competitions3 = Tournament(90, self.sportsman_1, self.sportsman_2, self.sportsman_3)
        result3 = competitions3.start()
        self.all_results['3 забег'] = result3
        test = result3[len(result3)].name
        self.assertTrue(test == "Ник")

    @classmethod
    def tearDownClass(cls):
        for test_key, test_value in cls.all_results.items():
            print(f'Тест: {test_key}')
            for key, value in test_value.items():
                print(f'\t{key}: {value.name}')

if __name__ == '__main__':
    unittest.main()


