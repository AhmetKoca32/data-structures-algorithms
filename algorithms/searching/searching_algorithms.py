"""
Arama Algoritmaları

Bu modül, temel arama algoritmalarının implementasyonlarını içerir.

Zaman Karmaşıklıkları:
- Linear Search: O(n)
- Binary Search: O(log n)
- Jump Search: O(√n)
- Interpolation Search: O(log log n) average, O(n) worst
- Exponential Search: O(log n)
- Fibonacci Search: O(log n)
- Ternary Search: O(log₃ n)
"""

from typing import List, Optional, Callable
import math


def linear_search(arr: List[int], target: int) -> Optional[int]:
    """
    Linear Search (Doğrusal Arama) Algoritması
    
    Zaman Karmaşıklığı: O(n)
    Uzay Karmaşıklığı: O(1)
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return None


def binary_search(arr: List[int], target: int) -> Optional[int]:
    """
    Binary Search (İkili Arama) Algoritması
    
    Zaman Karmaşıklığı: O(log n)
    Uzay Karmaşıklığı: O(1)
    
    Not: Array sıralı olmalıdır
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return None


def binary_search_recursive(arr: List[int], target: int, left: int = 0, right: int = None) -> Optional[int]:
    """
    Recursive Binary Search (Özyinelemeli İkili Arama)
    
    Zaman Karmaşıklığı: O(log n)
    Uzay Karmaşıklığı: O(log n) - call stack
    """
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return None
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


def jump_search(arr: List[int], target: int) -> Optional[int]:
    """
    Jump Search (Sıçrama Arama) Algoritması
    
    Zaman Karmaşıklığı: O(√n)
    Uzay Karmaşıklığı: O(1)
    
    Not: Array sıralı olmalıdır
    """
    n = len(arr)
    if n == 0:
        return None
    
    # Sıçrama boyutu
    step = int(math.sqrt(n))
    
    # Hedef aralığı bul
    prev = 0
    while prev < n and arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return None
    
    # Linear search ile hedef aralıkta ara
    while prev < min(step, n):
        if arr[prev] == target:
            return prev
        prev += 1
    
    return None


def interpolation_search(arr: List[int], target: int) -> Optional[int]:
    """
    Interpolation Search (İnterpolasyon Arama) Algoritması
    
    Zaman Karmaşıklığı: O(log log n) average, O(n) worst
    Uzay Karmaşıklığı: O(1)
    
    Not: Array sıralı olmalıdır ve uniform dağılım gerekir
    """
    left, right = 0, len(arr) - 1
    
    while left <= right and target >= arr[left] and target <= arr[right]:
        if left == right:
            if arr[left] == target:
                return left
            return None
        
        # İnterpolasyon formülü
        pos = left + int(((right - left) * (target - arr[left])) / (arr[right] - arr[left]))
        
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            left = pos + 1
        else:
            right = pos - 1
    
    return None


def exponential_search(arr: List[int], target: int) -> Optional[int]:
    """
    Exponential Search (Üstel Arama) Algoritması
    
    Zaman Karmaşıklığı: O(log n)
    Uzay Karmaşıklığı: O(1)
    
    Not: Array sıralı olmalıdır
    """
    n = len(arr)
    if n == 0:
        return None
    
    # İlk elemanı kontrol et
    if arr[0] == target:
        return 0
    
    # Üstel olarak artan aralık bul
    i = 1
    while i < n and arr[i] <= target:
        i = i * 2
    
    # Binary search ile aralıkta ara
    return binary_search_recursive(arr, target, i // 2, min(i, n - 1))


def fibonacci_search(arr: List[int], target: int) -> Optional[int]:
    """
    Fibonacci Search (Fibonacci Arama) Algoritması
    
    Zaman Karmaşıklığı: O(log n)
    Uzay Karmaşıklığı: O(1)
    
    Not: Array sıralı olmalıdır
    """
    n = len(arr)
    if n == 0:
        return None
    
    # Fibonacci sayılarını hesapla
    fib2 = 0  # (k-2)'inci Fibonacci sayısı
    fib1 = 1  # (k-1)'inci Fibonacci sayısı
    fib = fib1 + fib2  # k'inci Fibonacci sayısı
    
    # En küçük Fibonacci sayısını bul
    while fib < n:
        fib2 = fib1
        fib1 = fib
        fib = fib1 + fib2
    
    # Offset'i başlat
    offset = -1
    
    while fib > 1:
        # Check if fib2 is a valid index
        i = min(offset + fib2, n - 1)
        
        if arr[i] < target:
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = i
        elif arr[i] > target:
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1
        else:
            return i
    
    # Son elemanı kontrol et
    if fib1 and offset < n - 1 and arr[offset + 1] == target:
        return offset + 1
    
    return None


def ternary_search(arr: List[int], target: int) -> Optional[int]:
    """
    Ternary Search (Üçlü Arama) Algoritması
    
    Zaman Karmaşıklığı: O(log₃ n)
    Uzay Karmaşıklığı: O(1)
    
    Not: Array sıralı olmalıdır
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        # İki orta nokta hesapla
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
        
        if arr[mid1] == target:
            return mid1
        if arr[mid2] == target:
            return mid2
        
        if target < arr[mid1]:
            right = mid1 - 1
        elif target > arr[mid2]:
            left = mid2 + 1
        else:
            left = mid1 + 1
            right = mid2 - 1
    
    return None


def find_first_occurrence(arr: List[int], target: int) -> Optional[int]:
    """
    İlk Tekrarı Bulma (First Occurrence)
    
    Zaman Karmaşıklığı: O(log n)
    Uzay Karmaşıklığı: O(1)
    """
    left, right = 0, len(arr) - 1
    result = None
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            result = mid
            right = mid - 1  # Sol tarafa devam et
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result


def find_last_occurrence(arr: List[int], target: int) -> Optional[int]:
    """
    Son Tekrarı Bulma (Last Occurrence)
    
    Zaman Karmaşıklığı: O(log n)
    Uzay Karmaşıklığı: O(1)
    """
    left, right = 0, len(arr) - 1
    result = None
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            result = mid
            left = mid + 1  # Sağ tarafa devam et
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result


def count_occurrences(arr: List[int], target: int) -> int:
    """
    Tekrar Sayısını Bulma (Count Occurrences)
    
    Zaman Karmaşıklığı: O(log n)
    Uzay Karmaşıklığı: O(1)
    """
    first = find_first_occurrence(arr, target)
    if first is None:
        return 0
    
    last = find_last_occurrence(arr, target)
    return last - first + 1


def test_searching_algorithm(search_func: Callable, arr: List[int], target: int, name: str):
    """Arama algoritmasını test et"""
    print(f"\n=== {name} ===")
    print(f"Array: {arr}")
    print(f"Aranan: {target}")
    
    result = search_func(arr, target)
    if result is not None:
        print(f"✅ Bulundu! Index: {result}, Değer: {arr[result]}")
    else:
        print(f"❌ Bulunamadı")


# Kullanım örnekleri
if __name__ == "__main__":
    print("Arama Algoritmaları Test")
    print("=" * 50)
    
    # Test array'leri
    sorted_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    unsorted_array = [64, 34, 25, 12, 22, 11, 90]
    duplicate_array = [1, 2, 2, 2, 3, 4, 5, 5, 6]
    
    # Test hedefleri
    targets = [7, 10, 1, 19]
    
    # Sıralı array için testler
    print("Sıralı Array Testleri:")
    for target in targets:
        algorithms = [
            (linear_search, "Linear Search"),
            (binary_search, "Binary Search"),
            (binary_search_recursive, "Recursive Binary Search"),
            (jump_search, "Jump Search"),
            (interpolation_search, "Interpolation Search"),
            (exponential_search, "Exponential Search"),
            (fibonacci_search, "Fibonacci Search"),
            (ternary_search, "Ternary Search")
        ]
        
        for search_func, name in algorithms:
            test_searching_algorithm(search_func, sorted_array, target, name)
    
    # Sıralanmamış array için linear search
    print("\nSıralanmamış Array Testleri:")
    test_searching_algorithm(linear_search, unsorted_array, 25, "Linear Search (Unsorted)")
    
    # Tekrar sayısı testleri
    print("\nTekrar Sayısı Testleri:")
    print(f"Array: {duplicate_array}")
    print(f"2'nin tekrar sayısı: {count_occurrences(duplicate_array, 2)}")
    print(f"5'in tekrar sayısı: {count_occurrences(duplicate_array, 5)}")
    print(f"7'nin tekrar sayısı: {count_occurrences(duplicate_array, 7)}")
    
    # Performans karşılaştırması
    print("\n" + "=" * 50)
    print("Performans Testi (10000 eleman)")
    print("=" * 50)
    
    import random
    import time
    
    # Büyük sıralı array oluştur
    large_array = sorted([random.randint(1, 100000) for _ in range(10000)])
    test_target = large_array[5000]  # Ortadaki bir eleman
    
    algorithms = [
        (linear_search, "Linear Search"),
        (binary_search, "Binary Search"),
        (jump_search, "Jump Search"),
        (interpolation_search, "Interpolation Search"),
        (exponential_search, "Exponential Search"),
        (fibonacci_search, "Fibonacci Search"),
        (ternary_search, "Ternary Search")
    ]
    
    for search_func, name in algorithms:
        start_time = time.time()
        result = search_func(large_array, test_target)
        end_time = time.time()
        print(f"{name}: {end_time - start_time:.6f} saniye") 