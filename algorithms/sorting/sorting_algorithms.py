"""
Sıralama Algoritmaları

Bu modül, temel sıralama algoritmalarının implementasyonlarını içerir.

Zaman Karmaşıklıkları:
- Bubble Sort: O(n²)
- Selection Sort: O(n²)
- Insertion Sort: O(n²)
- Merge Sort: O(n log n)
- Quick Sort: O(n log n) average, O(n²) worst
- Heap Sort: O(n log n)
- Counting Sort: O(n + k)
- Radix Sort: O(d * (n + k))
"""

import random
from typing import List, Callable


def bubble_sort(arr: List[int]) -> List[int]:
    """
    Bubble Sort Algoritması
    
    Zaman Karmaşıklığı: O(n²)
    Uzay Karmaşıklığı: O(1)
    """
    n = len(arr)
    arr = arr.copy()  # Orijinal array'i değiştirmemek için kopyala
    
    for i in range(n):
        # Son i eleman zaten sıralı
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # Eğer hiç swap olmadıysa array sıralı
        if not swapped:
            break
    
    return arr


def selection_sort(arr: List[int]) -> List[int]:
    """
    Selection Sort Algoritması
    
    Zaman Karmaşıklığı: O(n²)
    Uzay Karmaşıklığı: O(1)
    """
    n = len(arr)
    arr = arr.copy()
    
    for i in range(n):
        # En küçük elemanı bul
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # En küçük elemanı başa taşı
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr


def insertion_sort(arr: List[int]) -> List[int]:
    """
    Insertion Sort Algoritması
    
    Zaman Karmaşıklığı: O(n²)
    Uzay Karmaşıklığı: O(1)
    """
    arr = arr.copy()
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # key'den büyük elemanları sağa kaydır
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
    
    return arr


def merge_sort(arr: List[int]) -> List[int]:
    """
    Merge Sort Algoritması
    
    Zaman Karmaşıklığı: O(n log n)
    Uzay Karmaşıklığı: O(n)
    """
    if len(arr) <= 1:
        return arr
    
    # Array'i ikiye böl
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    # İki sıralı array'i birleştir
    return merge(left, right)


def merge(left: List[int], right: List[int]) -> List[int]:
    """İki sıralı array'i birleştirme"""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Kalan elemanları ekle
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result


def quick_sort(arr: List[int]) -> List[int]:
    """
    Quick Sort Algoritması
    
    Zaman Karmaşıklığı: O(n log n) average, O(n²) worst
    Uzay Karmaşıklığı: O(log n) average, O(n) worst
    """
    if len(arr) <= 1:
        return arr
    
    arr = arr.copy()
    quick_sort_helper(arr, 0, len(arr) - 1)
    return arr


def quick_sort_helper(arr: List[int], low: int, high: int):
    """Quick sort yardımcı fonksiyonu"""
    if low < high:
        # Pivot'u doğru pozisyona yerleştir
        pivot_index = partition(arr, low, high)
        
        # Sol ve sağ alt array'leri sırala
        quick_sort_helper(arr, low, pivot_index - 1)
        quick_sort_helper(arr, pivot_index + 1, high)


def partition(arr: List[int], low: int, high: int) -> int:
    """Lomuto partition scheme"""
    # Son elemanı pivot olarak seç
    pivot = arr[high]
    i = low - 1  # Küçük elemanların son pozisyonu
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def heap_sort(arr: List[int]) -> List[int]:
    """
    Heap Sort Algoritması
    
    Zaman Karmaşıklığı: O(n log n)
    Uzay Karmaşıklığı: O(1)
    """
    arr = arr.copy()
    n = len(arr)
    
    # Max heap oluştur
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Heap'ten elemanları çıkar
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Root'u sona taşı
        heapify(arr, i, 0)  # Kalan heap'i düzenle
    
    return arr


def heapify(arr: List[int], n: int, i: int):
    """Heap property'yi koruma"""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def counting_sort(arr: List[int]) -> List[int]:
    """
    Counting Sort Algoritması
    
    Zaman Karmaşıklığı: O(n + k) where k is the range of input
    Uzay Karmaşıklığı: O(k)
    """
    if not arr:
        return []
    
    # Maksimum değeri bul
    max_val = max(arr)
    min_val = min(arr)
    range_val = max_val - min_val + 1
    
    # Count array oluştur
    count = [0] * range_val
    output = [0] * len(arr)
    
    # Her elemanın sayısını say
    for num in arr:
        count[num - min_val] += 1
    
    # Cumulative count hesapla
    for i in range(1, range_val):
        count[i] += count[i - 1]
    
    # Output array'i oluştur
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i] - min_val] - 1] = arr[i]
        count[arr[i] - min_val] -= 1
    
    return output


def radix_sort(arr: List[int]) -> List[int]:
    """
    Radix Sort Algoritması
    
    Zaman Karmaşıklığı: O(d * (n + k)) where d is number of digits
    Uzay Karmaşıklığı: O(n + k)
    """
    if not arr:
        return []
    
    arr = arr.copy()
    max_val = max(arr)
    
    # Her basamak için counting sort uygula
    exp = 1
    while max_val // exp > 0:
        counting_sort_by_digit(arr, exp)
        exp *= 10
    
    return arr


def counting_sort_by_digit(arr: List[int], exp: int):
    """Belirli bir basamak için counting sort"""
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    
    # Count array'i doldur
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1
    
    # Cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    # Output array'i oluştur
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
    
    # Orijinal array'i güncelle
    for i in range(n):
        arr[i] = output[i]


def test_sorting_algorithm(sort_func: Callable, arr: List[int], name: str):
    """Sıralama algoritmasını test et"""
    print(f"\n=== {name} ===")
    print(f"Orijinal array: {arr}")
    
    sorted_arr = sort_func(arr)
    print(f"Sıralanmış array: {sorted_arr}")
    print(f"Doğru mu: {sorted_arr == sorted(arr)}")


# Kullanım örnekleri
if __name__ == "__main__":
    # Test array'i oluştur
    test_array = [64, 34, 25, 12, 22, 11, 90]
    print("Sıralama Algoritmaları Test")
    print("=" * 50)
    
    # Farklı sıralama algoritmalarını test et
    algorithms = [
        (bubble_sort, "Bubble Sort"),
        (selection_sort, "Selection Sort"),
        (insertion_sort, "Insertion Sort"),
        (merge_sort, "Merge Sort"),
        (quick_sort, "Quick Sort"),
        (heap_sort, "Heap Sort"),
        (counting_sort, "Counting Sort"),
        (radix_sort, "Radix Sort")
    ]
    
    for sort_func, name in algorithms:
        test_sorting_algorithm(sort_func, test_array, name)
    
    # Büyük array ile performans testi
    print("\n" + "=" * 50)
    print("Performans Testi (1000 eleman)")
    print("=" * 50)
    
    large_array = [random.randint(1, 1000) for _ in range(1000)]
    
    # Sadece hızlı algoritmaları test et
    fast_algorithms = [
        (merge_sort, "Merge Sort"),
        (quick_sort, "Quick Sort"),
        (heap_sort, "Heap Sort"),
        (counting_sort, "Counting Sort"),
        (radix_sort, "Radix Sort")
    ]
    
    for sort_func, name in fast_algorithms:
        import time
        start_time = time.time()
        sorted_arr = sort_func(large_array)
        end_time = time.time()
        print(f"{name}: {end_time - start_time:.4f} saniye") 