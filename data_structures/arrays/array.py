"""
Array Veri Yapısı

Bu modül, temel array operasyonlarını ve dinamik array implementasyonunu içerir.

Zaman Karmaşıklıkları:
- Erişim: O(1)
- Arama: O(n)
- Ekleme (sona): O(1) amortized
- Ekleme (başa/ortaya): O(n)
- Silme: O(n)
- Güncelleme: O(1)
"""

class DynamicArray:
    """Dinamik Array implementasyonu"""
    
    def __init__(self, initial_capacity=10):
        """
        Args:
            initial_capacity (int): Başlangıç kapasitesi
        """
        self.capacity = initial_capacity
        self.size = 0
        self.data = [None] * initial_capacity
    
    def __len__(self):
        """Array'in boyutunu döndürür"""
        return self.size
    
    def __getitem__(self, index):
        """Index ile elemana erişim"""
        if not 0 <= index < self.size:
            raise IndexError("Index out of range")
        return self.data[index]
    
    def __setitem__(self, index, value):
        """Index ile eleman güncelleme"""
        if not 0 <= index < self.size:
            raise IndexError("Index out of range")
        self.data[index] = value
    
    def append(self, value):
        """Array'in sonuna eleman ekleme"""
        if self.size == self.capacity:
            self._resize(2 * self.capacity)
        self.data[self.size] = value
        self.size += 1
    
    def insert(self, index, value):
        """Belirtilen index'e eleman ekleme"""
        if not 0 <= index <= self.size:
            raise IndexError("Index out of range")
        
        if self.size == self.capacity:
            self._resize(2 * self.capacity)
        
        # Elemanları sağa kaydır
        for i in range(self.size, index, -1):
            self.data[i] = self.data[i - 1]
        
        self.data[index] = value
        self.size += 1
    
    def remove(self, value):
        """İlk bulunan değeri silme"""
        for i in range(self.size):
            if self.data[i] == value:
                self.pop(i)
                return
        raise ValueError("Value not found")
    
    def pop(self, index=None):
        """Belirtilen index'teki elemanı silme (varsayılan: son eleman)"""
        if index is None:
            index = self.size - 1
        
        if not 0 <= index < self.size:
            raise IndexError("Index out of range")
        
        value = self.data[index]
        
        # Elemanları sola kaydır
        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]
        
        self.size -= 1
        self.data[self.size] = None  # Garbage collection için
        
        # Kapasiteyi küçült (opsiyonel)
        if self.size < self.capacity // 4:
            self._resize(self.capacity // 2)
        
        return value
    
    def _resize(self, new_capacity):
        """Array'i yeniden boyutlandırma"""
        new_data = [None] * new_capacity
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_capacity
    
    def index(self, value):
        """Değerin index'ini bulma"""
        for i in range(self.size):
            if self.data[i] == value:
                return i
        raise ValueError("Value not found")
    
    def count(self, value):
        """Değerin kaç kez geçtiğini sayma"""
        count = 0
        for i in range(self.size):
            if self.data[i] == value:
                count += 1
        return count
    
    def reverse(self):
        """Array'i ters çevirme"""
        left, right = 0, self.size - 1
        while left < right:
            self.data[left], self.data[right] = self.data[right], self.data[left]
            left += 1
            right -= 1
    
    def sort(self):
        """Array'i sıralama (built-in sort kullanarak)"""
        self.data[:self.size] = sorted(self.data[:self.size])
    
    def __str__(self):
        """String temsili"""
        return str(self.data[:self.size])
    
    def __repr__(self):
        """Detaylı string temsili"""
        return f"DynamicArray(size={self.size}, capacity={self.capacity}, data={self.data[:self.size]})"


class StaticArray:
    """Statik Array implementasyonu"""
    
    def __init__(self, size):
        """
        Args:
            size (int): Array boyutu
        """
        self.size = size
        self.data = [None] * size
    
    def __len__(self):
        return self.size
    
    def __getitem__(self, index):
        if not 0 <= index < self.size:
            raise IndexError("Index out of range")
        return self.data[index]
    
    def __setitem__(self, index, value):
        if not 0 <= index < self.size:
            raise IndexError("Index out of range")
        self.data[index] = value
    
    def __str__(self):
        return str(self.data)
    
    def __repr__(self):
        return f"StaticArray(size={self.size}, data={self.data})"


# Kullanım örnekleri
if __name__ == "__main__":
    print("=== Dinamik Array Örnekleri ===")
    
    # Dinamik array oluşturma
    arr = DynamicArray()
    print(f"Boş array: {arr}")
    
    # Eleman ekleme
    arr.append(10)
    arr.append(20)
    arr.append(30)
    print(f"3 eleman eklendikten sonra: {arr}")
    
    # Index ile erişim
    print(f"Index 1'deki eleman: {arr[1]}")
    
    # Eleman güncelleme
    arr[1] = 25
    print(f"Index 1 güncellendikten sonra: {arr}")
    
    # Ortaya eleman ekleme
    arr.insert(1, 15)
    print(f"Index 1'e 15 eklendikten sonra: {arr}")
    
    # Eleman silme
    removed = arr.pop(2)
    print(f"Index 2'den {removed} silindi: {arr}")
    
    # Array'i ters çevirme
    arr.reverse()
    print(f"Ters çevrildikten sonra: {arr}")
    
    # Array'i sıralama
    arr.sort()
    print(f"Sıralandıktan sonra: {arr}")
    
    print(f"\nArray boyutu: {len(arr)}")
    print(f"Array kapasitesi: {arr.capacity}")
    
    print("\n=== Statik Array Örnekleri ===")
    
    # Statik array oluşturma
    static_arr = StaticArray(5)
    print(f"Boş statik array: {static_arr}")
    
    # Eleman atama
    static_arr[0] = 1
    static_arr[1] = 2
    static_arr[2] = 3
    print(f"Elemanlar atandıktan sonra: {static_arr}")
    
    print(f"Index 1'deki eleman: {static_arr[1]}") 