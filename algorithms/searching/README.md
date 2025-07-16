# Arama Algoritmaları

Bu klasör, temel arama algoritmalarının Python implementasyonlarını içerir.

## 📁 Dosyalar

- `searching_algorithms.py` - Tüm arama algoritmalarının implementasyonu
- `README.md` - Bu dosya

## 🔧 Algoritmalar

### Temel Arama Algoritmaları
1. **Linear Search** - Doğrusal arama (O(n))
2. **Binary Search** - İkili arama (O(log n))
3. **Recursive Binary Search** - Özyinelemeli ikili arama (O(log n))
4. **Jump Search** - Sıçrama arama (O(√n))
5. **Interpolation Search** - İnterpolasyon arama (O(log log n) average)
6. **Exponential Search** - Üstel arama (O(log n))
7. **Fibonacci Search** - Fibonacci arama (O(log n))
8. **Ternary Search** - Üçlü arama (O(log₃ n))

### Özel Arama Fonksiyonları
9. **First Occurrence** - İlk tekrarı bulma
10. **Last Occurrence** - Son tekrarı bulma
11. **Count Occurrences** - Tekrar sayısını bulma

## 🚀 Kullanım

```python
from searching_algorithms import (
    linear_search, binary_search, jump_search,
    interpolation_search, exponential_search,
    fibonacci_search, ternary_search
)

# Sıralı array
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Arama
result = binary_search(arr, 7)
if result is not None:
    print(f"Bulundu! Index: {result}")
else:
    print("Bulunamadı")
```

## 📊 Zaman Karmaşıklıkları

| Algoritma | En İyi | Ortalama | En Kötü | Uzay |
|-----------|--------|----------|---------|------|
| Linear Search | O(1) | O(n) | O(n) | O(1) |
| Binary Search | O(1) | O(log n) | O(log n) | O(1) |
| Recursive Binary | O(1) | O(log n) | O(log n) | O(log n) |
| Jump Search | O(1) | O(√n) | O(√n) | O(1) |
| Interpolation | O(1) | O(log log n) | O(n) | O(1) |
| Exponential | O(1) | O(log n) | O(log n) | O(1) |
| Fibonacci | O(1) | O(log n) | O(log n) | O(1) |
| Ternary | O(1) | O(log₃ n) | O(log₃ n) | O(1) |

## 🎯 Hangi Algoritma Ne Zaman Kullanılır?

### Küçük Veri Setleri (n < 50)
- **Linear Search**: Basit ve anlaşılır
- **Binary Search**: Sıralı veriler için

### Orta Büyüklükte Veri Setleri (50 < n < 1000)
- **Binary Search**: En yaygın kullanım
- **Jump Search**: Linear search'dan daha hızlı
- **Interpolation Search**: Uniform dağılım varsa

### Büyük Veri Setleri (n > 1000)
- **Binary Search**: Standart seçim
- **Exponential Search**: Sınırlı bilgi varsa
- **Fibonacci Search**: Bellek optimizasyonu gerekliyse

### Özel Durumlar
- **Ternary Search**: Üç parçaya bölme avantajlıysa
- **Interpolation Search**: Veriler uniform dağılmışsa

## 💡 Pratik Uygulamalar

- **Linear Search**: Küçük listeler, sıralanmamış veriler
- **Binary Search**: Sıralı listeler, veritabanı indeksleri
- **Jump Search**: Büyük sıralı listeler
- **Interpolation Search**: Telefon rehberi, sözlük
- **Exponential Search**: Sınırlı bilgi, sonsuz listeler
- **Fibonacci Search**: Bellek kısıtlı sistemler
- **Ternary Search**: Üçlü karar ağaçları

## 🧪 Test

```bash
python searching_algorithms.py
```

Bu komut tüm algoritmaları test eder ve performans karşılaştırması yapar.

## 📝 Notlar

- **Binary Search** ve türevleri için array sıralı olmalıdır
- **Interpolation Search** uniform dağılım gerektirir
- **Linear Search** herhangi bir sıralama gerektirmez
- **Recursive** versiyonlar call stack kullanır 