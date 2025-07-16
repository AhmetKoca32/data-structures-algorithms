"""
Graf Algoritmaları

Bu modül, temel graf algoritmalarının implementasyonlarını içerir.

Zaman Karmaşıklıkları:
- BFS: O(V + E)
- DFS: O(V + E)
- Dijkstra: O((V + E) log V) with binary heap
- Bellman-Ford: O(VE)
- Floyd-Warshall: O(V³)
- Topological Sort: O(V + E)
- Cycle Detection: O(V + E)
- Minimum Spanning Tree (Kruskal): O(E log E)
- Minimum Spanning Tree (Prim): O(E log V)
"""

from typing import List, Dict, Set, Tuple, Optional, Union
from collections import defaultdict, deque
import heapq
import sys


class Graph:
    """Graf veri yapısı"""
    
    def __init__(self, directed: bool = False):
        self.directed = directed
        self.adjacency_list = defaultdict(list)
        self.vertices = set()
    
    def add_edge(self, u: int, v: int, weight: float = 1.0):
        """Kenar ekleme"""
        self.vertices.add(u)
        self.vertices.add(v)
        self.adjacency_list[u].append((v, weight))
        
        if not self.directed:
            self.adjacency_list[v].append((u, weight))
    
    def get_vertices(self) -> Set[int]:
        """Tüm düğümleri döndür"""
        return self.vertices
    
    def get_edges(self) -> List[Tuple[int, int, float]]:
        """Tüm kenarları döndür"""
        edges = []
        for u in self.adjacency_list:
            for v, weight in self.adjacency_list[u]:
                edges.append((u, v, weight))
        return edges
    
    def get_neighbors(self, vertex: int) -> List[Tuple[int, float]]:
        """Bir düğümün komşularını döndür"""
        return self.adjacency_list[vertex]


def breadth_first_search(graph: Graph, start: int) -> Dict[int, int]:
    """
    Breadth First Search (Genişlik Öncelikli Arama)
    
    Zaman Karmaşıklığı: O(V + E)
    Uzay Karmaşıklığı: O(V)
    """
    visited = set()
    distances = {vertex: -1 for vertex in graph.get_vertices()}
    queue = deque([start])
    
    distances[start] = 0
    visited.add(start)
    
    while queue:
        current = queue.popleft()
        
        for neighbor, _ in graph.get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)
    
    return distances


def depth_first_search(graph: Graph, start: int) -> List[int]:
    """
    Depth First Search (Derinlik Öncelikli Arama)
    
    Zaman Karmaşıklığı: O(V + E)
    Uzay Karmaşıklığı: O(V)
    """
    visited = set()
    result = []
    
    def dfs_recursive(vertex: int):
        visited.add(vertex)
        result.append(vertex)
        
        for neighbor, _ in graph.get_neighbors(vertex):
            if neighbor not in visited:
                dfs_recursive(neighbor)
    
    dfs_recursive(start)
    return result


def depth_first_search_iterative(graph: Graph, start: int) -> List[int]:
    """
    Iterative Depth First Search
    
    Zaman Karmaşıklığı: O(V + E)
    Uzay Karmaşıklığı: O(V)
    """
    visited = set()
    result = []
    stack = [start]
    
    while stack:
        current = stack.pop()
        
        if current not in visited:
            visited.add(current)
            result.append(current)
            
            # Komşuları ters sırada ekle (doğru sıra için)
            for neighbor, _ in reversed(graph.get_neighbors(current)):
                if neighbor not in visited:
                    stack.append(neighbor)
    
    return result


def dijkstra_shortest_path(graph: Graph, start: int) -> Dict[int, float]:
    """
    Dijkstra En Kısa Yol Algoritması
    
    Zaman Karmaşıklığı: O((V + E) log V) with binary heap
    Uzay Karmaşıklığı: O(V)
    
    Not: Negatif ağırlık olmamalıdır
    """
    distances = {vertex: float('infinity') for vertex in graph.get_vertices()}
    distances[start] = 0
    
    # Priority queue: (distance, vertex)
    pq = [(0, start)]
    visited = set()
    
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        
        if current_vertex in visited:
            continue
        
        visited.add(current_vertex)
        
        for neighbor, weight in graph.get_neighbors(current_vertex):
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances


def bellman_ford_shortest_path(graph: Graph, start: int) -> Optional[Dict[int, float]]:
    """
    Bellman-Ford En Kısa Yol Algoritması
    
    Zaman Karmaşıklığı: O(VE)
    Uzay Karmaşıklığı: O(V)
    
    Negatif döngü tespit eder
    """
    distances = {vertex: float('infinity') for vertex in graph.get_vertices()}
    distances[start] = 0
    
    # V-1 iterasyon
    for _ in range(len(graph.get_vertices()) - 1):
        for u, v, weight in graph.get_edges():
            if distances[u] != float('infinity') and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
    
    # Negatif döngü kontrolü
    for u, v, weight in graph.get_edges():
        if distances[u] != float('infinity') and distances[u] + weight < distances[v]:
            return None  # Negatif döngü var
    
    return distances


def floyd_warshall_shortest_path(graph: Graph) -> Dict[Tuple[int, int], float]:
    """
    Floyd-Warshall En Kısa Yol Algoritması
    
    Zaman Karmaşıklığı: O(V³)
    Uzay Karmaşıklığı: O(V²)
    
    Tüm düğüm çiftleri arasındaki en kısa yolları bulur
    """
    vertices = list(graph.get_vertices())
    n = len(vertices)
    
    # Distance matrix başlat
    dist = {}
    for i in vertices:
        for j in vertices:
            if i == j:
                dist[(i, j)] = 0
            else:
                dist[(i, j)] = float('infinity')
    
    # Kenarları ekle
    for u, v, weight in graph.get_edges():
        dist[(u, v)] = weight
    
    # Floyd-Warshall algoritması
    for k in vertices:
        for i in vertices:
            for j in vertices:
                if dist[(i, k)] + dist[(k, j)] < dist[(i, j)]:
                    dist[(i, j)] = dist[(i, k)] + dist[(k, j)]
    
    return dist


def topological_sort(graph: Graph) -> Optional[List[int]]:
    """
    Topological Sort (Topolojik Sıralama)
    
    Zaman Karmaşıklığı: O(V + E)
    Uzay Karmaşıklığı: O(V)
    
    Not: Sadece DAG (Directed Acyclic Graph) için çalışır
    """
    if not graph.directed:
        return None
    
    in_degree = {vertex: 0 for vertex in graph.get_vertices()}
    
    # In-degree hesapla
    for u, v, _ in graph.get_edges():
        in_degree[v] += 1
    
    # In-degree 0 olan düğümleri bul
    queue = deque([vertex for vertex, degree in in_degree.items() if degree == 0])
    result = []
    
    while queue:
        current = queue.popleft()
        result.append(current)
        
        for neighbor, _ in graph.get_neighbors(current):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # Eğer tüm düğümler sıralanmadıysa döngü var
    if len(result) != len(graph.get_vertices()):
        return None
    
    return result


def has_cycle(graph: Graph) -> bool:
    """
    Döngü Tespiti
    
    Zaman Karmaşıklığı: O(V + E)
    Uzay Karmaşıklığı: O(V)
    """
    visited = set()
    rec_stack = set()
    
    def dfs_cycle(vertex: int) -> bool:
        visited.add(vertex)
        rec_stack.add(vertex)
        
        for neighbor, _ in graph.get_neighbors(vertex):
            if neighbor not in visited:
                if dfs_cycle(neighbor):
                    return True
            elif neighbor in rec_stack:
                return True
        
        rec_stack.remove(vertex)
        return False
    
    for vertex in graph.get_vertices():
        if vertex not in visited:
            if dfs_cycle(vertex):
                return True
    
    return False


def kruskal_mst(graph: Graph) -> List[Tuple[int, int, float]]:
    """
    Kruskal Minimum Spanning Tree Algoritması
    
    Zaman Karmaşıklığı: O(E log E)
    Uzay Karmaşıklığı: O(V)
    """
    def find(parent: Dict[int, int], vertex: int) -> int:
        if parent[vertex] != vertex:
            parent[vertex] = find(parent, parent[vertex])
        return parent[vertex]
    
    def union(parent: Dict[int, int], rank: Dict[int, int], x: int, y: int):
        root_x = find(parent, x)
        root_y = find(parent, y)
        
        if root_x != root_y:
            if rank[root_x] < rank[root_y]:
                root_x, root_y = root_y, root_x
            parent[root_y] = root_x
            if rank[root_x] == rank[root_y]:
                rank[root_x] += 1
    
    # Kenarları ağırlığa göre sırala
    edges = sorted(graph.get_edges(), key=lambda x: x[2])
    
    parent = {vertex: vertex for vertex in graph.get_vertices()}
    rank = {vertex: 0 for vertex in graph.get_vertices()}
    mst = []
    
    for u, v, weight in edges:
        if find(parent, u) != find(parent, v):
            mst.append((u, v, weight))
            union(parent, rank, u, v)
    
    return mst


def prim_mst(graph: Graph, start: int) -> List[Tuple[int, int, float]]:
    """
    Prim Minimum Spanning Tree Algoritması
    
    Zaman Karmaşıklığı: O(E log V)
    Uzay Karmaşıklığı: O(V)
    """
    visited = set()
    mst = []
    pq = [(0, start, start)]  # (weight, current, parent)
    
    while pq and len(visited) < len(graph.get_vertices()):
        weight, current, parent = heapq.heappop(pq)
        
        if current in visited:
            continue
        
        visited.add(current)
        if current != parent:
            mst.append((parent, current, weight))
        
        for neighbor, edge_weight in graph.get_neighbors(current):
            if neighbor not in visited:
                heapq.heappush(pq, (edge_weight, neighbor, current))
    
    return mst


def test_graph_algorithms():
    """Graf algoritmalarını test et"""
    print("Graf Algoritmaları Test")
    print("=" * 50)
    
    # Test grafı oluştur
    graph = Graph(directed=False)
    
    # Kenarlar ekle
    edges = [
        (0, 1, 4), (0, 2, 2), (1, 2, 1), (1, 3, 5),
        (2, 3, 8), (2, 4, 10), (3, 4, 2), (3, 5, 6),
        (4, 5, 3)
    ]
    
    for u, v, w in edges:
        graph.add_edge(u, v, w)
    
    print(f"Graf düğümleri: {graph.get_vertices()}")
    print(f"Graf kenarları: {graph.get_edges()}")
    
    # BFS testi
    print("\n=== BFS Testi ===")
    bfs_distances = breadth_first_search(graph, 0)
    print(f"BFS mesafeleri (başlangıç: 0): {bfs_distances}")
    
    # DFS testi
    print("\n=== DFS Testi ===")
    dfs_result = depth_first_search(graph, 0)
    print(f"DFS sırası (başlangıç: 0): {dfs_result}")
    
    # Dijkstra testi
    print("\n=== Dijkstra Testi ===")
    dijkstra_distances = dijkstra_shortest_path(graph, 0)
    print(f"Dijkstra en kısa yollar (başlangıç: 0): {dijkstra_distances}")
    
    # Kruskal MST testi
    print("\n=== Kruskal MST Testi ===")
    kruskal_mst_edges = kruskal_mst(graph)
    total_weight = sum(weight for _, _, weight in kruskal_mst_edges)
    print(f"Kruskal MST kenarları: {kruskal_mst_edges}")
    print(f"Toplam ağırlık: {total_weight}")
    
    # Prim MST testi
    print("\n=== Prim MST Testi ===")
    prim_mst_edges = prim_mst(graph, 0)
    total_weight = sum(weight for _, _, weight in prim_mst_edges)
    print(f"Prim MST kenarları: {prim_mst_edges}")
    print(f"Toplam ağırlık: {total_weight}")
    
    # Döngü tespiti testi
    print("\n=== Döngü Tespiti Testi ===")
    has_cycle_result = has_cycle(graph)
    print(f"Döngü var mı: {has_cycle_result}")
    
    # Yönlü graf testi
    print("\n=== Yönlü Graf Testi ===")
    directed_graph = Graph(directed=True)
    directed_edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)]  # Döngü oluştur
    for u, v in directed_edges:
        directed_graph.add_edge(u, v)
    
    cycle_result = has_cycle(directed_graph)
    print(f"Yönlü grafta döngü var mı: {cycle_result}")
    
    # Topolojik sıralama testi (DAG)
    print("\n=== Topolojik Sıralama Testi ===")
    dag = Graph(directed=True)
    dag_edges = [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4)]
    for u, v in dag_edges:
        dag.add_edge(u, v)
    
    topo_sort = topological_sort(dag)
    print(f"Topolojik sıralama: {topo_sort}")


if __name__ == "__main__":
    test_graph_algorithms() 