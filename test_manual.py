"""
Manuel Test Dosyası

Bu dosya, tüm veri yapıları ve algoritmaları manuel olarak test etmenizi sağlar.
Çalıştırmak için: python test_manual.py
"""

import sys
import os

# Proje klasörünü Python path'ine ekle
sys.path.append(os.path.dirname(__file__))

def test_arrays():
    """Array veri yapılarını test et"""
    print("=" * 50)
    print("ARRAY VERİ YAPISI TESTİ")
    print("=" * 50)
    
    try:
        from data_structures.arrays.array import DynamicArray, StaticArray
        
        # DynamicArray testi
        print("\n1. DynamicArray Testi:")
        arr = DynamicArray()
        
        # Eleman ekleme
        arr.append(10)
        arr.append(20)
        arr.append(30)
        print(f"   Elemanlar eklendi: {arr}")
        
        # Index ile erişim
        print(f"   Index 1'deki eleman: {arr[1]}")
        
        # Eleman güncelleme
        arr[1] = 25
        print(f"   Index 1 güncellendi: {arr}")
        
        # Ortaya eleman ekleme
        arr.insert(1, 15)
        print(f"   Index 1'e 15 eklendi: {arr}")
        
        # Eleman silme
        removed = arr.pop(2)
        print(f"   Index 2'den {removed} silindi: {arr}")
        
        # Array'i ters çevirme
        arr.reverse()
        print(f"   Ters çevrildi: {arr}")
        
        # Array'i sıralama
        arr.sort()
        print(f"   Sıralandı: {arr}")
        
        print(f"   ✅ DynamicArray testi başarılı!")
        
        # StaticArray testi
        print("\n2. StaticArray Testi:")
        static_arr = StaticArray(5)
        static_arr[0] = 1
        static_arr[1] = 2
        static_arr[2] = 3
        print(f"   Statik array: {static_arr}")
        print(f"   ✅ StaticArray testi başarılı!")
        
    except Exception as e:
        print(f"   ❌ Array testi başarısız: {e}")


def test_sorting_algorithms():
    """Sıralama algoritmalarını test et"""
    print("\n" + "=" * 50)
    print("SIRALAMA ALGORİTMALARI TESTİ")
    print("=" * 50)
    
    try:
        from algorithms.sorting.sorting_algorithms import (
            bubble_sort, selection_sort, insertion_sort,
            merge_sort, quick_sort, heap_sort,
            counting_sort, radix_sort
        )
        
        # Test array'i
        test_array = [64, 34, 25, 12, 22, 11, 90]
        expected = sorted(test_array)
        
        algorithms = [
            ("Bubble Sort", bubble_sort),
            ("Selection Sort", selection_sort),
            ("Insertion Sort", insertion_sort),
            ("Merge Sort", merge_sort),
            ("Quick Sort", quick_sort),
            ("Heap Sort", heap_sort),
            ("Counting Sort", counting_sort),
            ("Radix Sort", radix_sort)
        ]
        
        print(f"Test array: {test_array}")
        print(f"Beklenen sonuç: {expected}")
        
        for name, algorithm in algorithms:
            try:
                result = algorithm(test_array.copy())
                is_correct = result == expected
                status = "✅" if is_correct else "❌"
                print(f"   {status} {name}: {result}")
            except Exception as e:
                print(f"   ❌ {name}: Hata - {e}")
        
        print("   ✅ Sıralama algoritmaları testi tamamlandı!")
        
    except Exception as e:
        print(f"   ❌ Sıralama testi başarısız: {e}")


def test_student_management():
    """Öğrenci yönetim sistemini test et"""
    print("\n" + "=" * 50)
    print("ÖĞRENCİ YÖNETİM SİSTEMİ TESTİ")
    print("=" * 50)
    
    try:
        from examples.practical_applications.student_management import (
            StudentManagementSystem, Student
        )
        
        # Sistem oluştur
        sms = StudentManagementSystem()
        
        # Öğrenciler ekle
        print("\n1. Öğrenciler ekleniyor...")
        sms.add_student("Ahmet Yılmaz", 20, 3.85)
        sms.add_student("Fatma Demir", 19, 3.92)
        sms.add_student("Mehmet Kaya", 21, 3.45)
        
        print(f"   Toplam öğrenci sayısı: {sms.get_student_count()}")
        
        # Öğrenci bulma
        print("\n2. Öğrenci arama testi:")
        found = sms.find_student_by_id(2)
        if found:
            print(f"   ID 2 ile bulunan: {found}")
        
        # GPA'ya göre sıralama
        print("\n3. GPA'ya göre sıralama:")
        sorted_by_gpa = sms.sort_by_gpa()
        for i, student in enumerate(sorted_by_gpa, 1):
            print(f"   {i}. {student.name} (GPA: {student.gpa:.2f})")
        
        # İstatistikler
        print(f"\n4. İstatistikler:")
        print(f"   Ortalama GPA: {sms.get_average_gpa():.2f}")
        
        print("   ✅ Öğrenci yönetim sistemi testi başarılı!")
        
    except Exception as e:
        print(f"   ❌ Öğrenci yönetim testi başarısız: {e}")


def test_performance():
    """Performans testi"""
    print("\n" + "=" * 50)
    print("PERFORMANS TESTİ")
    print("=" * 50)
    
    try:
        import random
        import time
        from algorithms.sorting.sorting_algorithms import quick_sort, merge_sort
        
        # Büyük array oluştur
        large_array = [random.randint(1, 1000) for _ in range(1000)]
        
        print(f"1000 elemanlı array ile performans testi:")
        
        # Quick Sort
        start_time = time.time()
        quick_sort(large_array.copy())
        quick_time = time.time() - start_time
        
        # Merge Sort
        start_time = time.time()
        merge_sort(large_array.copy())
        merge_time = time.time() - start_time
        
        print(f"   Quick Sort: {quick_time:.4f} saniye")
        print(f"   Merge Sort: {merge_time:.4f} saniye")
        
        print("   ✅ Performans testi tamamlandı!")
        
    except Exception as e:
        print(f"   ❌ Performans testi başarısız: {e}")


def main():
    """Ana test fonksiyonu"""
    print("VERİ YAPILARI VE ALGORİTMALAR - MANUEL TEST")
    print("=" * 60)
    
    # Tüm testleri çalıştır
    test_arrays()
    test_sorting_algorithms()
    test_student_management()
    test_performance()
    
    print("\n" + "=" * 60)
    print("TÜM TESTLER TAMAMLANDI!")
    print("=" * 60)


if __name__ == "__main__":
    main() 