# Sıralama Algoritmaları

Bu klasör, temel sıralama algoritmalarının Python implementasyonlarını içerir.

## 📁 Dosyalar

- `sorting_algorithms.py` - Tüm sıralama algoritmalarının implementasyonu
- `README.md` - Bu dosya

## 🔧 Algoritmalar

### Basit Algoritmalar (O(n²))
1. **Bubble Sort** - Komşu elemanları karşılaştırarak sıralama
2. **Selection Sort** - En küçük elemanı bulup başa taşıma
3. **Insertion Sort** - Elemanları sıralı kısma ekleme

### Gelişmiş Algoritmalar (O(n log n))
4. **Merge Sort** - Böl ve fethet stratejisi
5. **Quick Sort** - Pivot tabanlı bölme
6. **Heap Sort** - Heap veri yapısı kullanarak

### Özel Algoritmalar
7. **Counting Sort** - Sayma tabanlı sıralama (O(n + k))
8. **Radix Sort** - Basamak tabanlı sıralama (O(d * (n + k)))

## 🚀 Kullanım

```python
from sorting_algorithms import (
    bubble_sort, selection_sort, insertion_sort,
    merge_sort, quick_sort, heap_sort,
    counting_sort, radix_sort
)

# Test array
arr = [64, 34, 25, 12, 22, 11, 90]

# Sıralama
sorted_arr = quick_sort(arr)
print(sorted_arr)  # [11, 12, 22, 25, 34, 64, 90]
```

## 📊 Zaman Karmaşıklıkları

| Algoritma | En İyi | Ortalama | En Kötü | Uzay |
|-----------|--------|----------|---------|------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) |
| Counting Sort | O(n + k) | O(n + k) | O(n + k) | O(k) |
| Radix Sort | O(d * (n + k)) | O(d * (n + k)) | O(d * (n + k)) | O(n + k) |

## 🎯 Hangi Algoritma Ne Zaman Kullanılır?

### Küçük Veri Setleri (n < 50)
- **Insertion Sort**: Basit ve hızlı
- **Bubble Sort**: Eğitim amaçlı

### Orta Büyüklükte Veri Setleri (50 < n < 1000)
- **Quick Sort**: Genellikle en hızlı
- **Merge Sort**: Kararlı sıralama gerekliyse

### Büyük Veri Setleri (n > 1000)
- **Quick Sort**: Çoğu durumda en iyi
- **Heap Sort**: O(1) uzay karmaşıklığı gerekliyse

### Özel Durumlar
- **Counting Sort**: Küçük sayı aralığı
- **Radix Sort**: String veya çok basamaklı sayılar

## 💡 Pratik Uygulamalar

- **Bubble Sort**: Eğitim ve küçük veri setleri
- **Insertion Sort**: Küçük veri setleri, online sıralama
- **Quick Sort**: Genel amaçlı sıralama
- **Merge Sort**: Kararlı sıralama gerektiren durumlar
- **Heap Sort**: Priority queue implementasyonu
- **Counting Sort**: Histogram oluşturma
- **Radix Sort**: String sıralama, tarih sıralama

## 🧪 Test

```bash
python sorting_algorithms.py
```

Bu komut tüm algoritmaları test eder ve performans karşılaştırması yapar. 