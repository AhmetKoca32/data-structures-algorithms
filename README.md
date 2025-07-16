# Veri Yapıları ve Algoritmalar

Bu repository, temel veri yapıları ve algoritmaların Python implementasyonlarını içerir.

## 📁 Klasör Yapısı

```
data-structures-algorithms/
├── data_structures/
│   ├── arrays/
│   ├── linked_lists/
│   ├── stacks/
│   ├── queues/
│   ├── trees/
│   ├── graphs/
│   ├── heaps/
│   └── hash_tables/
├── algorithms/
│   ├── sorting/
│   ├── searching/
│   ├── graph_algorithms/
│   ├── dynamic_programming/
│   └── greedy_algorithms/
└── examples/
    └── practical_applications/
```

## 🚀 Kullanım

Her klasörde ilgili veri yapısı veya algoritmanın:
- Temel implementasyonu
- Kullanım örnekleri
- Zaman karmaşıklığı analizi
- Pratik uygulamalar

bulunmaktadır.

## 📚 İçerik

### Veri Yapıları
- **Arrays**: Diziler ve dinamik diziler
- **Linked Lists**: Tek yönlü, çift yönlü ve dairesel bağlı listeler
- **Stacks**: Yığın veri yapısı
- **Queues**: Kuyruk veri yapısı
- **Trees**: İkili ağaçlar, AVL ağaçları, B-ağaçları
- **Graphs**: Graf veri yapısı ve temsilleri
- **Heaps**: Yığın ağaçları
- **Hash Tables**: Hash tabloları

### Algoritmalar
- **Sorting**: 8 farklı sıralama algoritması (Bubble, Selection, Insertion, Merge, Quick, Heap, Counting, Radix)
- **Searching**: 8 farklı arama algoritması (Linear, Binary, Jump, Interpolation, Exponential, Fibonacci, Ternary)
- **Graph Algorithms**: Graf gezinme, en kısa yol, MST algoritmaları (BFS, DFS, Dijkstra, Bellman-Ford, Floyd-Warshall, Kruskal, Prim)
- **Dynamic Programming**: Dinamik programlama (henüz oluşturulmadı)
- **Greedy Algorithms**: Açgözlü algoritmalar (henüz oluşturulmadı)

## 🛠️ Gereksinimler

- Python 3.7+
- pytest (testler için)

## 🧪 Test Yapıları

Bu repository'deki uygulamaları test etmek için birkaç farklı yöntem bulunmaktadır:

### 1. Manuel Test Dosyası (Önerilen)
```bash
python test_manual.py
```
Bu komut tüm veri yapıları ve algoritmaları otomatik olarak test eder.

### 2. Tek Tek Test Etme

**Array Veri Yapısı:**
```bash
python data_structures/arrays/array.py
```

**Sıralama Algoritmaları:**
```bash
python algorithms/sorting/sorting_algorithms.py
```

**Arama Algoritmaları:**
```bash
python algorithms/searching/searching_algorithms.py
```

**Graf Algoritmaları:**
```bash
python algorithms/graph_algorithms/graph_algorithms.py
```

**Öğrenci Yönetim Sistemi:**
```bash
python examples/practical_applications/student_management.py
```

### 3. Pytest ile Otomatik Testler
```bash
# Pytest kurulumu
pip install pytest

# Array testlerini çalıştır
pytest tests/test_array.py -v

# Tüm testleri çalıştır
pytest tests/ -v
```

### 4. Python Interactive Mode
```python
# Python konsolunda test etme
python
>>> from data_structures.arrays.array import DynamicArray
>>> arr = DynamicArray()
>>> arr.append(10)
>>> arr.append(20)
>>> print(arr)
[10, 20]
```

### 📋 Test Kontrol Listesi

Manuel test yaparken şunları kontrol edin:

#### ✅ Array Veri Yapısı:
- [ ] Eleman ekleme çalışıyor mu?
- [ ] Index ile erişim çalışıyor mu?
- [ ] Eleman güncelleme çalışıyor mu?
- [ ] Eleman silme çalışıyor mu?
- [ ] Ters çevirme çalışıyor mu?
- [ ] Sıralama çalışıyor mu?

#### ✅ Sıralama Algoritmaları:
- [ ] Tüm algoritmalar doğru sıralıyor mu?
- [ ] Boş array ile çalışıyor mu?
- [ ] Tek elemanlı array ile çalışıyor mu?
- [ ] Tekrarlı elemanlarla çalışıyor mu?

#### ✅ Arama Algoritmaları:
- [ ] Linear search sıralanmamış array'de çalışıyor mu?
- [ ] Binary search sıralı array'de çalışıyor mu?
- [ ] Diğer arama algoritmaları doğru sonuç veriyor mu?
- [ ] Bulunamayan elemanlar için None döndürüyor mu?

#### ✅ Graf Algoritmaları:
- [ ] BFS doğru mesafeleri hesaplıyor mu?
- [ ] DFS doğru sırayla geziyor mu?
- [ ] Dijkstra en kısa yolları buluyor mu?
- [ ] MST algoritmaları minimum ağacı oluşturuyor mu?

#### ✅ Öğrenci Yönetim Sistemi:
- [ ] Öğrenci ekleme çalışıyor mu?
- [ ] Öğrenci arama çalışıyor mu?
- [ ] GPA'ya göre sıralama çalışıyor mu?
- [ ] İsme göre sıralama çalışıyor mu?
- [ ] İstatistikler doğru hesaplanıyor mu?

### 🎯 Önerilen Test Sırası:

1. **Önce manuel test dosyasını çalıştırın:**
   ```bash
   python test_manual.py
   ```

2. **Sonra tek tek test edin:**
   ```bash
   python data_structures/arrays/array.py
   python algorithms/sorting/sorting_algorithms.py
   python algorithms/searching/searching_algorithms.py
   python algorithms/graph_algorithms/graph_algorithms.py
   python examples/practical_applications/student_management.py
   ```

3. **Hata alırsanız:**
   - Hata mesajını okuyun
   - Import path'lerini kontrol edin
   - Python versiyonunuzu kontrol edin (3.7+ gerekli)

## 🚀 Hızlı Başlangıç

1. **Repository'yi klonlayın:**
   ```bash
   git clone <repository-url>
   cd data-structures-algorithms
   ```

2. **Gerekli paketleri yükleyin:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Testleri çalıştırın:**
   ```bash
   python test_manual.py
   ```

## 📈 Katkıda Bulunma

1. Fork yapın
2. Feature branch oluşturun (`git checkout -b feature/AmazingFeature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add some AmazingFeature'`)
4. Branch'inizi push edin (`git push origin feature/AmazingFeature`)
5. Pull Request oluşturun
