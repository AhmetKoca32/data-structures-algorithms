# Graf Algoritmaları

Bu klasör, temel graf algoritmalarının Python implementasyonlarını içerir.

## 📁 Dosyalar

- `graph_algorithms.py` - Tüm graf algoritmalarının implementasyonu
- `README.md` - Bu dosya

## 🔧 Algoritmalar

### Graf Gezinme Algoritmaları
1. **Breadth First Search (BFS)** - Genişlik öncelikli arama
2. **Depth First Search (DFS)** - Derinlik öncelikli arama (recursive)
3. **Iterative DFS** - Derinlik öncelikli arama (iterative)

### En Kısa Yol Algoritmaları
4. **Dijkstra** - Tek kaynak en kısa yol (negatif ağırlık yok)
5. **Bellman-Ford** - Tek kaynak en kısa yol (negatif ağırlık var)
6. **Floyd-Warshall** - Tüm çiftler en kısa yol

### Graf Analiz Algoritmaları
7. **Topological Sort** - Topolojik sıralama (DAG)
8. **Cycle Detection** - Döngü tespiti

### Minimum Spanning Tree Algoritmaları
9. **Kruskal** - Minimum spanning tree (Union-Find)
10. **Prim** - Minimum spanning tree (Priority Queue)

## 🚀 Kullanım

```python
from graph_algorithms import Graph, breadth_first_search, dijkstra_shortest_path

# Graf oluştur
graph = Graph(directed=False)
graph.add_edge(0, 1, 4)
graph.add_edge(0, 2, 2)
graph.add_edge(1, 2, 1)

# BFS
distances = breadth_first_search(graph, 0)
print(f"BFS mesafeleri: {distances}")

# Dijkstra
shortest_paths = dijkstra_shortest_path(graph, 0)
print(f"En kısa yollar: {shortest_paths}")
```

## 📊 Zaman Karmaşıklıkları

| Algoritma | Zaman | Uzay | Açıklama |
|-----------|-------|------|----------|
| BFS | O(V + E) | O(V) | Genişlik öncelikli |
| DFS | O(V + E) | O(V) | Derinlik öncelikli |
| Dijkstra | O((V + E) log V) | O(V) | Binary heap ile |
| Bellman-Ford | O(VE) | O(V) | Negatif ağırlık |
| Floyd-Warshall | O(V³) | O(V²) | Tüm çiftler |
| Topological Sort | O(V + E) | O(V) | DAG gerekli |
| Cycle Detection | O(V + E) | O(V) | DFS tabanlı |
| Kruskal MST | O(E log E) | O(V) | Union-Find |
| Prim MST | O(E log V) | O(V) | Priority Queue |

## 🎯 Hangi Algoritma Ne Zaman Kullanılır?

### Graf Gezinme
- **BFS**: En kısa yol (ağırlıksız), seviye bazlı arama
- **DFS**: Derinlik öncelikli, backtracking, cycle detection

### En Kısa Yol
- **Dijkstra**: Pozitif ağırlıklı graf, tek kaynak
- **Bellman-Ford**: Negatif ağırlık var, negatif döngü tespiti
- **Floyd-Warshall**: Tüm çiftler, küçük graf (V < 1000)

### Graf Analizi
- **Topological Sort**: DAG sıralama, bağımlılık çözümleme
- **Cycle Detection**: Döngü tespiti, graf validasyonu

### Minimum Spanning Tree
- **Kruskal**: Kenar sayısı az, Union-Find verimli
- **Prim**: Düğüm sayısı az, yoğun graf

## 💡 Pratik Uygulamalar

### BFS Uygulamaları
- Web crawler
- Sosyal ağ arkadaş önerisi
- GPS navigasyon (ağırlıksız)
- Oyun AI (seviye bazlı)

### DFS Uygulamaları
- Maze solver
- Dependency resolution
- Backtracking algoritmaları
- Cycle detection

### En Kısa Yol Uygulamaları
- **Dijkstra**: GPS navigasyon, network routing
- **Bellman-Ford**: Arbitrage detection, network protocols
- **Floyd-Warshall**: Distance matrix, all-pairs shortest path

### MST Uygulamaları
- Network design
- Clustering algorithms
- Circuit design
- Water supply networks

### Topological Sort Uygulamaları
- Build systems
- Course scheduling
- Task scheduling
- Dependency management

## 🧪 Test

```bash
python graph_algorithms.py
```

Bu komut tüm graf algoritmalarını test eder ve örnek çıktılar gösterir.

## 📝 Notlar

- **Graph sınıfı** hem yönlü hem yönsüz graf destekler
- **Dijkstra** sadece pozitif ağırlıklarla çalışır
- **Bellman-Ford** negatif döngü tespit eder
- **Topological Sort** sadece DAG için çalışır
- **MST algoritmaları** aynı sonucu verir (farklı sırada)

## 🔧 Graf Temsilleri

Bu implementasyon **Adjacency List** kullanır:
- **Avantaj**: Seyrek graf için verimli
- **Dezavantaj**: Yoğun graf için daha fazla bellek
- **Alternatif**: Adjacency Matrix (yoğun graf için) 