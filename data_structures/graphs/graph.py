"""
Graph Veri Yapısı

Bu modül, graf veri yapısının farklı temsillerini içerir.

Zaman Karmaşıklıkları:
- Adjacency List: O(V + E) uzay, O(degree(v)) komşu erişim
- Adjacency Matrix: O(V²) uzay, O(1) komşu erişim
- Edge List: O(E) uzay, O(E) komşu arama
"""

from typing import List, Dict, Set, Tuple, Optional, Union
from collections import defaultdict, deque
import heapq


class AdjacencyListGraph:
    """Adjacency List temsili ile Graf"""
    
    def __init__(self, directed: bool = False, weighted: bool = False):
        """
        Args:
            directed (bool): Yönlü graf mı?
            weighted (bool): Ağırlıklı graf mı?
        """
        self.directed = directed
        self.weighted = weighted
        self.adjacency_list = defaultdict(list)
        self.vertices = set()
        self.edge_count = 0
    
    def add_vertex(self, vertex: int) -> None:
        """Düğüm ekleme"""
        self.vertices.add(vertex)
    
    def add_edge(self, u: int, v: int, weight: float = 1.0) -> None:
        """Kenar ekleme"""
        self.vertices.add(u)
        self.vertices.add(v)
        
        if self.weighted:
            self.adjacency_list[u].append((v, weight))
            if not self.directed:
                self.adjacency_list[v].append((u, weight))
        else:
            self.adjacency_list[u].append(v)
            if not self.directed:
                self.adjacency_list[v].append(u)
        
        self.edge_count += 1
    
    def remove_edge(self, u: int, v: int) -> bool:
        """Kenar silme"""
        if u not in self.adjacency_list:
            return False
        
        if self.weighted:
            # Ağırlıklı kenarları bul ve sil
            for i, (neighbor, weight) in enumerate(self.adjacency_list[u]):
                if neighbor == v:
                    self.adjacency_list[u].pop(i)
                    if not self.directed:
                        for j, (n, w) in enumerate(self.adjacency_list[v]):
                            if n == u:
                                self.adjacency_list[v].pop(j)
                                break
                    self.edge_count -= 1
                    return True
        else:
            # Ağırlıksız kenarları bul ve sil
            if v in self.adjacency_list[u]:
                self.adjacency_list[u].remove(v)
                if not self.directed:
                    self.adjacency_list[v].remove(u)
                self.edge_count -= 1
                return True
        
        return False
    
    def remove_vertex(self, vertex: int) -> bool:
        """Düğüm silme"""
        if vertex not in self.vertices:
            return False
        
        # Gelen kenarları sil
        for u in self.adjacency_list:
            if self.weighted:
                self.adjacency_list[u] = [(v, w) for v, w in self.adjacency_list[u] if v != vertex]
            else:
                if vertex in self.adjacency_list[u]:
                    self.adjacency_list[u].remove(vertex)
        
        # Giden kenarları sil
        if vertex in self.adjacency_list:
            self.edge_count -= len(self.adjacency_list[vertex])
            del self.adjacency_list[vertex]
        
        self.vertices.remove(vertex)
        return True
    
    def get_neighbors(self, vertex: int) -> List[Union[int, Tuple[int, float]]]:
        """Bir düğümün komşularını döndür"""
        if vertex not in self.adjacency_list:
            return []
        return self.adjacency_list[vertex]
    
    def has_edge(self, u: int, v: int) -> bool:
        """Kenar var mı kontrol et"""
        if u not in self.adjacency_list:
            return False
        
        if self.weighted:
            return any(neighbor == v for neighbor, _ in self.adjacency_list[u])
        else:
            return v in self.adjacency_list[u]
    
    def get_edge_weight(self, u: int, v: int) -> Optional[float]:
        """Kenar ağırlığını döndür"""
        if not self.weighted or u not in self.adjacency_list:
            return None
        
        for neighbor, weight in self.adjacency_list[u]:
            if neighbor == v:
                return weight
        return None
    
    def get_vertices(self) -> Set[int]:
        """Tüm düğümleri döndür"""
        return self.vertices
    
    def get_edges(self) -> List[Tuple[int, int, float]]:
        """Tüm kenarları döndür"""
        edges = []
        for u in self.adjacency_list:
            if self.weighted:
                for v, weight in self.adjacency_list[u]:
                    edges.append((u, v, weight))
            else:
                for v in self.adjacency_list[u]:
                    edges.append((u, v, 1.0))
        return edges
    
    def get_vertex_count(self) -> int:
        """Düğüm sayısını döndür"""
        return len(self.vertices)
    
    def get_edge_count(self) -> int:
        """Kenar sayısını döndür"""
        return self.edge_count
    
    def get_degree(self, vertex: int) -> int:
        """Bir düğümün derecesini döndür"""
        if vertex not in self.adjacency_list:
            return 0
        return len(self.adjacency_list[vertex])
    
    def is_connected(self) -> bool:
        """Graf bağlı mı kontrol et"""
        if not self.vertices:
            return True
        
        start_vertex = next(iter(self.vertices))
        visited = set()
        queue = deque([start_vertex])
        visited.add(start_vertex)
        
        while queue:
            current = queue.popleft()
            for neighbor in self.get_neighbors(current):
                if self.weighted:
                    neighbor = neighbor[0]
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return len(visited) == len(self.vertices)
    
    def __str__(self) -> str:
        """String temsili"""
        result = f"Graph (directed={self.directed}, weighted={self.weighted})\n"
        result += f"Vertices: {self.get_vertex_count()}, Edges: {self.get_edge_count()}\n"
        
        for vertex in sorted(self.vertices):
            neighbors = self.get_neighbors(vertex)
            if self.weighted:
                neighbor_str = ", ".join([f"({v}, {w})" for v, w in neighbors])
            else:
                neighbor_str = ", ".join(map(str, neighbors))
            result += f"{vertex} -> [{neighbor_str}]\n"
        
        return result


class AdjacencyMatrixGraph:
    """Adjacency Matrix temsili ile Graf"""
    
    def __init__(self, directed: bool = False, weighted: bool = False):
        """
        Args:
            directed (bool): Yönlü graf mı?
            weighted (bool): Ağırlıklı graf mı?
        """
        self.directed = directed
        self.weighted = weighted
        self.matrix = {}
        self.vertices = set()
        self.vertex_to_index = {}
        self.index_to_vertex = {}
        self.next_index = 0
    
    def _get_vertex_index(self, vertex: int) -> int:
        """Düğüm için index döndür"""
        if vertex not in self.vertex_to_index:
            self.vertex_to_index[vertex] = self.next_index
            self.index_to_vertex[self.next_index] = vertex
            self.next_index += 1
        return self.vertex_to_index[vertex]
    
    def add_vertex(self, vertex: int) -> None:
        """Düğüm ekleme"""
        self._get_vertex_index(vertex)
        self.vertices.add(vertex)
    
    def add_edge(self, u: int, v: int, weight: float = 1.0) -> None:
        """Kenar ekleme"""
        u_idx = self._get_vertex_index(u)
        v_idx = self._get_vertex_index(v)
        
        self.vertices.add(u)
        self.vertices.add(v)
        
        if self.weighted:
            self.matrix[(u_idx, v_idx)] = weight
            if not self.directed:
                self.matrix[(v_idx, u_idx)] = weight
        else:
            self.matrix[(u_idx, v_idx)] = 1
            if not self.directed:
                self.matrix[(v_idx, u_idx)] = 1
    
    def remove_edge(self, u: int, v: int) -> bool:
        """Kenar silme"""
        u_idx = self.vertex_to_index.get(u)
        v_idx = self.vertex_to_index.get(v)
        
        if u_idx is None or v_idx is None:
            return False
        
        if (u_idx, v_idx) in self.matrix:
            del self.matrix[(u_idx, v_idx)]
            if not self.directed:
                del self.matrix[(v_idx, u_idx)]
            return True
        
        return False
    
    def has_edge(self, u: int, v: int) -> bool:
        """Kenar var mı kontrol et"""
        u_idx = self.vertex_to_index.get(u)
        v_idx = self.vertex_to_index.get(v)
        
        if u_idx is None or v_idx is None:
            return False
        
        return (u_idx, v_idx) in self.matrix
    
    def get_edge_weight(self, u: int, v: int) -> Optional[float]:
        """Kenar ağırlığını döndür"""
        u_idx = self.vertex_to_index.get(u)
        v_idx = self.vertex_to_index.get(v)
        
        if u_idx is None or v_idx is None:
            return None
        
        return self.matrix.get((u_idx, v_idx))
    
    def get_neighbors(self, vertex: int) -> List[Union[int, Tuple[int, float]]]:
        """Bir düğümün komşularını döndür"""
        vertex_idx = self.vertex_to_index.get(vertex)
        if vertex_idx is None:
            return []
        
        neighbors = []
        for (u_idx, v_idx), weight in self.matrix.items():
            if u_idx == vertex_idx:
                neighbor_vertex = self.index_to_vertex[v_idx]
                if self.weighted:
                    neighbors.append((neighbor_vertex, weight))
                else:
                    neighbors.append(neighbor_vertex)
        
        return neighbors
    
    def get_vertices(self) -> Set[int]:
        """Tüm düğümleri döndür"""
        return self.vertices
    
    def get_edges(self) -> List[Tuple[int, int, float]]:
        """Tüm kenarları döndür"""
        edges = []
        for (u_idx, v_idx), weight in self.matrix.items():
            u = self.index_to_vertex[u_idx]
            v = self.index_to_vertex[v_idx]
            edges.append((u, v, weight))
        return edges
    
    def get_vertex_count(self) -> int:
        """Düğüm sayısını döndür"""
        return len(self.vertices)
    
    def get_edge_count(self) -> int:
        """Kenar sayısını döndür"""
        return len(self.matrix) // (2 if not self.directed else 1)
    
    def get_degree(self, vertex: int) -> int:
        """Bir düğümün derecesini döndür"""
        return len(self.get_neighbors(vertex))
    
    def __str__(self) -> str:
        """String temsili"""
        result = f"Adjacency Matrix Graph (directed={self.directed}, weighted={self.weighted})\n"
        result += f"Vertices: {self.get_vertex_count()}, Edges: {self.get_edge_count()}\n"
        
        # Matrix görünümü
        vertices_list = sorted(self.vertices)
        result += "    " + " ".join(f"{v:2}" for v in vertices_list) + "\n"
        
        for u in vertices_list:
            row = f"{u:2} "
            for v in vertices_list:
                weight = self.get_edge_weight(u, v)
                if weight is not None:
                    row += f"{weight:2} "
                else:
                    row += " 0 "
            result += row + "\n"
        
        return result


class EdgeListGraph:
    """Edge List temsili ile Graf"""
    
    def __init__(self, directed: bool = False, weighted: bool = False):
        """
        Args:
            directed (bool): Yönlü graf mı?
            weighted (bool): Ağırlıklı graf mı?
        """
        self.directed = directed
        self.weighted = weighted
        self.edges = []
        self.vertices = set()
    
    def add_vertex(self, vertex: int) -> None:
        """Düğüm ekleme"""
        self.vertices.add(vertex)
    
    def add_edge(self, u: int, v: int, weight: float = 1.0) -> None:
        """Kenar ekleme"""
        self.vertices.add(u)
        self.vertices.add(v)
        
        if self.weighted:
            self.edges.append((u, v, weight))
            if not self.directed:
                self.edges.append((v, u, weight))
        else:
            self.edges.append((u, v, 1.0))
            if not self.directed:
                self.edges.append((v, u, 1.0))
    
    def remove_edge(self, u: int, v: int) -> bool:
        """Kenar silme"""
        original_length = len(self.edges)
        
        if self.weighted:
            self.edges = [(x, y, w) for x, y, w in self.edges if not (x == u and y == v)]
            if not self.directed:
                self.edges = [(x, y, w) for x, y, w in self.edges if not (x == v and y == u)]
        else:
            self.edges = [(x, y, w) for x, y, w in self.edges if not (x == u and y == v)]
            if not self.directed:
                self.edges = [(x, y, w) for x, y, w in self.edges if not (x == v and y == u)]
        
        return len(self.edges) < original_length
    
    def has_edge(self, u: int, v: int) -> bool:
        """Kenar var mı kontrol et"""
        return any(x == u and y == v for x, y, _ in self.edges)
    
    def get_edge_weight(self, u: int, v: int) -> Optional[float]:
        """Kenar ağırlığını döndür"""
        for x, y, weight in self.edges:
            if x == u and y == v:
                return weight
        return None
    
    def get_neighbors(self, vertex: int) -> List[Union[int, Tuple[int, float]]]:
        """Bir düğümün komşularını döndür"""
        neighbors = []
        for u, v, weight in self.edges:
            if u == vertex:
                if self.weighted:
                    neighbors.append((v, weight))
                else:
                    neighbors.append(v)
        return neighbors
    
    def get_vertices(self) -> Set[int]:
        """Tüm düğümleri döndür"""
        return self.vertices
    
    def get_edges(self) -> List[Tuple[int, int, float]]:
        """Tüm kenarları döndür"""
        return self.edges.copy()
    
    def get_vertex_count(self) -> int:
        """Düğüm sayısını döndür"""
        return len(self.vertices)
    
    def get_edge_count(self) -> int:
        """Kenar sayısını döndür"""
        return len(self.edges) // (2 if not self.directed else 1)
    
    def get_degree(self, vertex: int) -> int:
        """Bir düğümün derecesini döndür"""
        return len(self.get_neighbors(vertex))
    
    def __str__(self) -> str:
        """String temsili"""
        result = f"Edge List Graph (directed={self.directed}, weighted={self.weighted})\n"
        result += f"Vertices: {self.get_vertex_count()}, Edges: {self.get_edge_count()}\n"
        result += "Edges:\n"
        
        for u, v, weight in self.edges:
            if self.weighted:
                result += f"  {u} -> {v} (weight: {weight})\n"
            else:
                result += f"  {u} -> {v}\n"
        
        return result


def test_graph_implementations():
    """Farklı graf temsillerini test et"""
    print("Graph Veri Yapısı Testleri")
    print("=" * 50)
    
    # Test verileri
    edges = [(0, 1, 4), (0, 2, 2), (1, 2, 1), (1, 3, 5), (2, 3, 8)]
    
    # Adjacency List Graph testi
    print("\n=== Adjacency List Graph ===")
    adj_list_graph = AdjacencyListGraph(directed=False, weighted=True)
    
    for u, v, w in edges:
        adj_list_graph.add_edge(u, v, w)
    
    print(adj_list_graph)
    print(f"0'ın komşuları: {adj_list_graph.get_neighbors(0)}")
    print(f"0-1 arası ağırlık: {adj_list_graph.get_edge_weight(0, 1)}")
    print(f"Graf bağlı mı: {adj_list_graph.is_connected()}")
    
    # Adjacency Matrix Graph testi
    print("\n=== Adjacency Matrix Graph ===")
    adj_matrix_graph = AdjacencyMatrixGraph(directed=False, weighted=True)
    
    for u, v, w in edges:
        adj_matrix_graph.add_edge(u, v, w)
    
    print(adj_matrix_graph)
    print(f"0'ın komşuları: {adj_matrix_graph.get_neighbors(0)}")
    print(f"0-1 arası ağırlık: {adj_matrix_graph.get_edge_weight(0, 1)}")
    
    # Edge List Graph testi
    print("\n=== Edge List Graph ===")
    edge_list_graph = EdgeListGraph(directed=False, weighted=True)
    
    for u, v, w in edges:
        edge_list_graph.add_edge(u, v, w)
    
    print(edge_list_graph)
    print(f"0'ın komşuları: {edge_list_graph.get_neighbors(0)}")
    print(f"0-1 arası ağırlık: {edge_list_graph.get_edge_weight(0, 1)}")
    
    # Performans karşılaştırması
    print("\n=== Performans Karşılaştırması ===")
    print("Adjacency List:")
    print(f"  Uzay: O(V + E)")
    print(f"  Komşu erişim: O(degree(v))")
    print(f"  Kenar ekleme: O(1)")
    
    print("\nAdjacency Matrix:")
    print(f"  Uzay: O(V²)")
    print(f"  Komşu erişim: O(1)")
    print(f"  Kenar ekleme: O(1)")
    
    print("\nEdge List:")
    print(f"  Uzay: O(E)")
    print(f"  Komşu erişim: O(E)")
    print(f"  Kenar ekleme: O(1)")


if __name__ == "__main__":
    test_graph_implementations() 