import time
from typing import Dict, List


def find_coins_greedy(amount: int, coins: List[int] = [50, 25, 10, 5, 2, 1]) -> Dict[int, int]:

    # Жадібний алгоритм для знаходження решти.
    result = {}
    
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= count * coin
        
        if amount == 0:
            break
    
    return result


def find_min_coins(amount: int, coins: List[int] = [50, 25, 10, 5, 2, 1]) -> Dict[int, int]:
 
    # Сортуємо монети для консистентності
    coins = sorted(coins)
    
    # DP таблиця: min_coins[i] = мінімальна кількість монет для суми i
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0
    
    # Вказівник для відновлення рішення
    coin_used = [-1] * (amount + 1)
    
    # Заповнюємо DP таблицю
    for i in range(1, amount + 1):
        for coin in coins:
            if coin > i:
                continue
                
            if min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                coin_used[i] = coin
    
    # Якщо рішення не знайдено
    if min_coins[amount] == float('inf'):
        return {}
    
    # Відновлюємо рішення
    result = {}
    remaining = amount
    
    while remaining > 0:
        coin = coin_used[remaining]
        result[coin] = result.get(coin, 0) + 1
        remaining -= coin
    
    return result


def measure_performance(amounts: List[int]) -> None:

    # Вимірювання та порівняння продуктивності обох алгоритмів.
    coins = [50, 25, 10, 5, 2, 1]
    
    print("Порівняння продуктивності")
    print("=" * 60)
    print(f"{'Сума':<12} {'Час жадібного':<15} {'Час DP':<15} {'Однаковий результат?'}")
    print("-" * 60)
    
    for amount in amounts:
        # Тестуємо жадібний алгоритм
        start = time.perf_counter()
        greedy_result = find_coins_greedy(amount, coins)
        greedy_time = time.perf_counter() - start
        
        # Тестуємо DP алгоритм
        start = time.perf_counter()
        dp_result = find_min_coins(amount, coins)
        dp_time = time.perf_counter() - start
        
        # Перевіряємо чи результати однакові (для канонічних систем монет)
        same_result = greedy_result == dp_result
        
        print(f"{amount:<12} {greedy_time:<15.10f} {dp_time:<15.10f} {same_result}")
    
    print("=" * 60)


def test_examples() -> None:

    # Тестування обох алгоритмів з прикладами з домашнього завдання.
    print("Тестування з прикладними сумами")
    print("=" * 60)
    
    # Тестовий випадок 1: 113
    amount = 113
    coins = [50, 25, 10, 5, 2, 1]
    
    print(f"Сума: {amount}")
    print(f"Монети: {coins}")
    print()
    
    greedy_result = find_coins_greedy(amount, coins)
    dp_result = find_min_coins(amount, coins)
    
    print("Результат жадібного алгоритму:")
    print(f"  {greedy_result}")
    print(f"  Загальна кількість монет: {sum(greedy_result.values())}")
    print()
    
    print("Результат динамічного програмування:")
    print(f"  {dp_result}")
    print(f"  Загальна кількість монет: {sum(dp_result.values())}")
    print()
    
    print("=" * 60)
    print()


def analyze_large_amounts() -> None:

    # Аналіз продуктивності для великих сум.
    print("Аналіз для великих сум")
    print("=" * 60)
    
    large_amounts = [1000, 5000, 10000, 50000, 100000]
    
    for amount in large_amounts:
        print(f"\nСума: {amount:,}")
        
        # Жадібний алгоритм
        start = time.perf_counter()
        greedy_result = find_coins_greedy(amount)
        greedy_time = time.perf_counter() - start
        greedy_coins = sum(greedy_result.values())
        
        # DP алгоритм
        start = time.perf_counter()
        dp_result = find_min_coins(amount)
        dp_time = time.perf_counter() - start
        dp_coins = sum(dp_result.values())
        
        print(f"  Жадібний:  {greedy_coins} монет, {greedy_time:.6f} секунд")
        print(f"  DP:        {dp_coins} монет, {dp_time:.6f} секунд")
        
        if greedy_coins != dp_coins:
            print(f"  Різні результати! Жадібний:{greedy_coins} vs DP:{dp_coins}")
    
    print("\n" + "=" * 60)


if __name__ == "__main__":
    print("Система видачі решти для касового апарату")
    print("=" * 60)
    
    # Запускаємо тести
    test_examples()
    
    # Тестуємо різні суми
    test_amounts = [1, 13, 27, 47, 113, 256, 789]
    measure_performance(test_amounts)
    
    # Аналізуємо великі суми
    analyze_large_amounts()