# Graph Veri Yapısı

Bu klasör, graf veri yapısının farklı temsillerini içerir.

## 📁 Dosyalar

- `graph.py` - Farklı graf temsillerinin implementasyonu
- `README.md` - Bu dosya

## 🔧 Graf Temsilleri

### 1. Adjacency List Graph
- **Açıklama**: Her düğüm için komşularının listesi
- **Uzay Karmaşıklığı**: O(V + E)
- **Komşu Erişim**: O(degree(v))
- **Kenar Ekleme**: O(1)

### 2. Adjacency Matrix Graph
- **Açıklama**: V×V boyutunda matris
- **Uzay Karmaşıklığı**: O(V²)
- **Komşu Erişim**: O(1)
- **Kenar Ekleme**: O(1)

### 3. Edge List Graph
- **Açıklama**: Tüm kenarların listesi
- **Uzay Karmaşıklığı**: O(E)
- **Komşu Erişim**: O(E)
- **Kenar Ekleme**: O(1)

## 🚀 Kullanım

```python
from graph import AdjacencyListGraph, AdjacencyMatrixGraph, EdgeListGraph

# Adjacency List Graph
graph = AdjacencyListGraph(directed=False, weighted=True)
graph.add_edge(0, 1, 4)
graph.add_edge(0, 2, 2)
graph.add_edge(1, 2, 1)

print(f"0'ın komşuları: {graph.get_neighbors(0)}")
print(f"0-1 arası ağırlık: {graph.get_edge_weight(0, 1)}")
print(f"Graf bağlı mı: {graph.is_connected()}")
```

## 📊 Zaman Karmaşıklıkları

| İşlem | Adjacency List | Adjacency Matrix | Edge List |
|-------|----------------|------------------|-----------|
| Uzay | O(V + E) | O(V²) | O(E) |
| Kenar Ekleme | O(1) | O(1) | O(1) |
| Kenar Silme | O(degree(v)) | O(1) | O(E) |
| Kenar Kontrolü | O(degree(v)) | O(1) | O(E) |
| Komşu Listesi | O(degree(v)) | O(V) | O(E) |
| Düğüm Silme | O(V + E) | O(V²) | O(E) |

## 🎯 Hangi Temsil Ne Zaman Kullanılır?

### Adjacency List
**Avantajlar:**
- Seyrek graf için verimli
- Az bellek kullanımı
- Komşu listesi hızlı

**Dezavantajlar:**
- Kenar kontrolü yavaş
- Yoğun graf için uygun değil

**Kullanım Alanları:**
- Sosyal ağlar
- Web sayfaları arası linkler
- Seyrek graf algoritmaları

### Adjacency Matrix
**Avantajlar:**
- Kenar kontrolü O(1)
- Matris operasyonları
- Basit implementasyon

**Dezavantajlar:**
- Çok bellek kullanır
- Seyrek graf için verimsiz

**Kullanım Alanları:**
- Yoğun graf
- Floyd-Warshall algoritması
- Matris tabanlı algoritmalar

### Edge List
**Avantajlar:**
- En az bellek kullanımı
- Kenar bazlı işlemler
- Basit yapı

**Dezavantajlar:**
- Komşu arama yavaş
- Düğüm bazlı işlemler zor

**Kullanım Alanları:**
- Kruskal algoritması
- Kenar bazlı algoritmalar
- Bellek kısıtlı sistemler

## 💡 Özellikler

### Ortak Özellikler
- ✅ Yönlü/Yönsüz graf desteği
- ✅ Ağırlıklı/Ağırlıksız kenar desteği
- ✅ Düğüm ve kenar ekleme/silme
- ✅ Komşu listesi alma
- ✅ Kenar ağırlığı sorgulama
- ✅ Derece hesaplama

### Özel Özellikler
- **Adjacency List**: Bağlılık kontrolü
- **Adjacency Matrix**: Matris görünümü
- **Edge List**: Kenar listesi görünümü

## 🧪 Test

```bash
python graph.py
```

Bu komut tüm graf temsillerini test eder ve performans karşılaştırması yapar.

## 📝 Notlar

- **Yönlü Graf**: Kenarlar tek yönlü
- **Yönsüz Graf**: Kenarlar çift yönlü
- **Ağırlıklı Graf**: Kenarların ağırlığı var
- **Ağırlıksız Graf**: Tüm kenarlar ağırlık 1

## 🔧 Graf Türleri

### Yönlü Graf (Directed Graph)
- Kenarlar tek yönlü
- A → B ≠ B → A
- Uygulama: Bağımlılık grafları

### Yönsüz Graf (Undirected Graph)
- Kenarlar çift yönlü
- A — B = B — A
- Uygulama: Sosyal ağlar

### Ağırlıklı Graf (Weighted Graph)
- Kenarların ağırlığı var
- Uygulama: Mesafe, maliyet

### Ağırlıksız Graf (Unweighted Graph)
- Tüm kenarlar eşit ağırlık
- Uygulama: Bağlantı durumu 