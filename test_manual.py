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


def test_graph_data_structures():
    """Graph veri yapılarını test et"""
    print("\n" + "=" * 50)
    print("GRAPH VERİ YAPISI TESTİ")
    print("=" * 50)
    
    try:
        from data_structures.graphs.graph import (
            AdjacencyListGraph, AdjacencyMatrixGraph, EdgeListGraph
        )
        
        # Test verileri
        edges = [(0, 1, 4), (0, 2, 2), (1, 2, 1), (1, 3, 5)]
        
        # Adjacency List Graph testi
        print("\n1. Adjacency List Graph Testi:")
        adj_list_graph = AdjacencyListGraph(directed=False, weighted=True)
        
        for u, v, w in edges:
            adj_list_graph.add_edge(u, v, w)
        
        print(f"   Düğüm sayısı: {adj_list_graph.get_vertex_count()}")
        print(f"   Kenar sayısı: {adj_list_graph.get_edge_count()}")
        print(f"   0'ın komşuları: {adj_list_graph.get_neighbors(0)}")
        print(f"   0-1 arası ağırlık: {adj_list_graph.get_edge_weight(0, 1)}")
        print(f"   Graf bağlı mı: {adj_list_graph.is_connected()}")
        print(f"   ✅ Adjacency List Graph testi başarılı!")
        
        # Adjacency Matrix Graph testi
        print("\n2. Adjacency Matrix Graph Testi:")
        adj_matrix_graph = AdjacencyMatrixGraph(directed=False, weighted=True)
        
        for u, v, w in edges:
            adj_matrix_graph.add_edge(u, v, w)
        
        print(f"   Düğüm sayısı: {adj_matrix_graph.get_vertex_count()}")
        print(f"   Kenar sayısı: {adj_matrix_graph.get_edge_count()}")
        print(f"   0'ın komşuları: {adj_matrix_graph.get_neighbors(0)}")
        print(f"   0-1 arası ağırlık: {adj_matrix_graph.get_edge_weight(0, 1)}")
        print(f"   ✅ Adjacency Matrix Graph testi başarılı!")
        
        # Edge List Graph testi
        print("\n3. Edge List Graph Testi:")
        edge_list_graph = EdgeListGraph(directed=False, weighted=True)
        
        for u, v, w in edges:
            edge_list_graph.add_edge(u, v, w)
        
        print(f"   Düğüm sayısı: {edge_list_graph.get_vertex_count()}")
        print(f"   Kenar sayısı: {edge_list_graph.get_edge_count()}")
        print(f"   0'ın komşuları: {edge_list_graph.get_neighbors(0)}")
        print(f"   0-1 arası ağırlık: {edge_list_graph.get_edge_weight(0, 1)}")
        print(f"   ✅ Edge List Graph testi başarılı!")
        
    except Exception as e:
        print(f"   ❌ Graph veri yapısı testi başarısız: {e}")


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


def test_searching_algorithms():
    """Arama algoritmalarını test et"""
    print("\n" + "=" * 50)
    print("ARAMA ALGORİTMALARI TESTİ")
    print("=" * 50)
    
    try:
        from algorithms.searching.searching_algorithms import (
            linear_search, binary_search, jump_search,
            interpolation_search, exponential_search,
            fibonacci_search, ternary_search
        )
        
        # Test array'i (sıralı)
        sorted_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
        target = 7
        
        algorithms = [
            ("Linear Search", linear_search),
            ("Binary Search", binary_search),
            ("Jump Search", jump_search),
            ("Interpolation Search", interpolation_search),
            ("Exponential Search", exponential_search),
            ("Fibonacci Search", fibonacci_search),
            ("Ternary Search", ternary_search)
        ]
        
        print(f"Test array: {sorted_array}")
        print(f"Aranan hedef: {target}")
        
        for name, algorithm in algorithms:
            try:
                result = algorithm(sorted_array, target)
                if result is not None:
                    print(f"   ✅ {name}: Bulundu (Index: {result})")
                else:
                    print(f"   ❌ {name}: Bulunamadı")
            except Exception as e:
                print(f"   ❌ {name}: Hata - {e}")
        
        print("   ✅ Arama algoritmaları testi tamamlandı!")
        
    except Exception as e:
        print(f"   ❌ Arama testi başarısız: {e}")


def test_graph_algorithms():
    """Graf algoritmalarını test et"""
    print("\n" + "=" * 50)
    print("GRAF ALGORİTMALARI TESTİ")
    print("=" * 50)
    
    try:
        from algorithms.graph_algorithms.graph_algorithms import (
            Graph, breadth_first_search, depth_first_search,
            dijkstra_shortest_path, kruskal_mst, prim_mst
        )
        
        # Test grafı oluştur
        graph = Graph(directed=False)
        edges = [(0, 1, 4), (0, 2, 2), (1, 2, 1), (1, 3, 5), (2, 3, 8)]
        
        for u, v, w in edges:
            graph.add_edge(u, v, w)
        
        print(f"Graf düğümleri: {graph.get_vertices()}")
        print(f"Graf kenarları: {graph.get_edges()}")
        
        # BFS testi
        bfs_result = breadth_first_search(graph, 0)
        print(f"   ✅ BFS mesafeleri: {bfs_result}")
        
        # DFS testi
        dfs_result = depth_first_search(graph, 0)
        print(f"   ✅ DFS sırası: {dfs_result}")
        
        # Dijkstra testi
        dijkstra_result = dijkstra_shortest_path(graph, 0)
        print(f"   ✅ Dijkstra en kısa yollar: {dijkstra_result}")
        
        # MST testi
        kruskal_result = kruskal_mst(graph)
        prim_result = prim_mst(graph, 0)
        print(f"   ✅ Kruskal MST: {kruskal_result}")
        print(f"   ✅ Prim MST: {prim_result}")
        
        print("   ✅ Graf algoritmaları testi tamamlandı!")
        
    except Exception as e:
        print(f"   ❌ Graf testi başarısız: {e}")


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
    test_graph_data_structures()
    test_sorting_algorithms()
    test_searching_algorithms()
    test_graph_algorithms()
    test_student_management()
    test_performance()
    
    print("\n" + "=" * 60)
    print("TÜM TESTLER TAMAMLANDI!")
    print("=" * 60)


if __name__ == "__main__":
    main() 