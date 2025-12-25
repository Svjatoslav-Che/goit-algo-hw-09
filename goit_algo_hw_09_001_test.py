import unittest
from goit_algo_hw_09_001 import find_coins_greedy, find_min_coins


class TestCashRegister(unittest.TestCase):
    def setUp(self):
        self.coins = [50, 25, 10, 5, 2, 1]
    
    def test_greedy_basic(self):
        # Тестування жадібного алгоритму з базовими випадками
        self.assertEqual(find_coins_greedy(113, self.coins), {50: 2, 10: 1, 2: 1, 1: 1})
        self.assertEqual(find_coins_greedy(1, self.coins), {1: 1})
        self.assertEqual(find_coins_greedy(50, self.coins), {50: 1})
        self.assertEqual(find_coins_greedy(27, self.coins), {25: 1, 2: 1})
    
    def test_dp_basic(self):
        # Тестування DP алгоритму з базовими випадками
        self.assertEqual(find_min_coins(113, self.coins), {50: 2, 10: 1, 2: 1, 1: 1})
        self.assertEqual(find_min_coins(1, self.coins), {1: 1})
        self.assertEqual(find_min_coins(50, self.coins), {50: 1})
        self.assertEqual(find_min_coins(27, self.coins), {25: 1, 2: 1})
    
    def test_edge_cases(self):
        # Тестування крайніх випадків
        # Сума нуль
        self.assertEqual(find_coins_greedy(0, self.coins), {})
        self.assertEqual(find_min_coins(0, self.coins), {})
        
        # Велика сума
        large_greedy = find_coins_greedy(1000, self.coins)
        large_dp = find_min_coins(1000, self.coins)
        self.assertEqual(sum(large_greedy.values()), 20)  # 20 монет по 50
        self.assertEqual(sum(large_dp.values()), 20)
    
    def test_custom_coins(self):
        # Тестування з користувацькою системою монет
        custom_coins = [30, 20, 10, 5, 1]
        
        # Для суми 55, жадібний дасть 30+20+5 = 3 монети
        # Але оптимальне рішення 30+30 = 2 монети (якщо є дві монети по 30)
        # Насправді з монетами [30, 20, 10, 5, 1], 55 = 30 + 20 + 5 = 3 монети
        # DP повинен знайти те ж саме для цієї системи
        greedy = find_coins_greedy(55, custom_coins)
        dp = find_min_coins(55, custom_coins)
        
        # Обидва повинні знайти оптимальне рішення для цієї системи
        self.assertEqual(sum(greedy.values()), 3)
        self.assertEqual(sum(dp.values()), 3)


if __name__ == "__main__":
    unittest.main()