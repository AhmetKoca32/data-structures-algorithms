"""
Array Veri Yapısı Test Dosyası

Bu dosya, array.py modülündeki sınıfları test eder.
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import pytest
from data_structures.arrays.array import DynamicArray, StaticArray


class TestDynamicArray:
    """DynamicArray sınıfı için testler"""
    
    def test_init(self):
        """Başlangıç durumu testi"""
        arr = DynamicArray()
        assert len(arr) == 0
        assert arr.capacity == 10
        
        arr = DynamicArray(5)
        assert arr.capacity == 5
    
    def test_append(self):
        """Eleman ekleme testi"""
        arr = DynamicArray()
        arr.append(10)
        arr.append(20)
        arr.append(30)
        
        assert len(arr) == 3
        assert arr[0] == 10
        assert arr[1] == 20
        assert arr[2] == 30
    
    def test_getitem(self):
        """Index ile erişim testi"""
        arr = DynamicArray()
        arr.append(10)
        arr.append(20)
        
        assert arr[0] == 10
        assert arr[1] == 20
        
        with pytest.raises(IndexError):
            _ = arr[2]
        
        with pytest.raises(IndexError):
            _ = arr[-1]
    
    def test_setitem(self):
        """Index ile güncelleme testi"""
        arr = DynamicArray()
        arr.append(10)
        arr.append(20)
        
        arr[0] = 100
        arr[1] = 200
        
        assert arr[0] == 100
        assert arr[1] == 200
        
        with pytest.raises(IndexError):
            arr[2] = 300
    
    def test_insert(self):
        """Ortaya eleman ekleme testi"""
        arr = DynamicArray()
        arr.append(10)
        arr.append(30)
        
        arr.insert(1, 20)
        assert len(arr) == 3
        assert arr[0] == 10
        assert arr[1] == 20
        assert arr[2] == 30
        
        # Başa ekleme
        arr.insert(0, 5)
        assert arr[0] == 5
        assert len(arr) == 4
    
    def test_pop(self):
        """Eleman silme testi"""
        arr = DynamicArray()
        arr.append(10)
        arr.append(20)
        arr.append(30)
        
        # Son elemanı sil
        removed = arr.pop()
        assert removed == 30
        assert len(arr) == 2
        
        # Belirli index'ten sil
        removed = arr.pop(0)
        assert removed == 10
        assert len(arr) == 1
        assert arr[0] == 20
    
    def test_remove(self):
        """Değer ile silme testi"""
        arr = DynamicArray()
        arr.append(10)
        arr.append(20)
        arr.append(30)
        
        arr.remove(20)
        assert len(arr) == 2
        assert arr[0] == 10
        assert arr[1] == 30
        
        with pytest.raises(ValueError):
            arr.remove(50)
    
    def test_index(self):
        """Index bulma testi"""
        arr = DynamicArray()
        arr.append(10)
        arr.append(20)
        arr.append(30)
        
        assert arr.index(10) == 0
        assert arr.index(20) == 1
        assert arr.index(30) == 2
        
        with pytest.raises(ValueError):
            arr.index(50)
    
    def test_count(self):
        """Sayma testi"""
        arr = DynamicArray()
        arr.append(10)
        arr.append(20)
        arr.append(10)
        arr.append(30)
        arr.append(10)
        
        assert arr.count(10) == 3
        assert arr.count(20) == 1
        assert arr.count(50) == 0
    
    def test_reverse(self):
        """Ters çevirme testi"""
        arr = DynamicArray()
        arr.append(10)
        arr.append(20)
        arr.append(30)
        
        arr.reverse()
        assert arr[0] == 30
        assert arr[1] == 20
        assert arr[2] == 10
    
    def test_sort(self):
        """Sıralama testi"""
        arr = DynamicArray()
        arr.append(30)
        arr.append(10)
        arr.append(20)
        
        arr.sort()
        assert arr[0] == 10
        assert arr[1] == 20
        assert arr[2] == 30
    
    def test_resize(self):
        """Boyutlandırma testi"""
        arr = DynamicArray(2)
        arr.append(10)
        arr.append(20)
        
        # Kapasite dolduğunda otomatik genişleme
        arr.append(30)
        assert len(arr) == 3
        assert arr.capacity > 2
        
        # Elemanlar korunmuş mu?
        assert arr[0] == 10
        assert arr[1] == 20
        assert arr[2] == 30


class TestStaticArray:
    """StaticArray sınıfı için testler"""
    
    def test_init(self):
        """Başlangıç durumu testi"""
        arr = StaticArray(5)
        assert len(arr) == 5
        assert arr[0] is None
        assert arr[4] is None
    
    def test_setitem_getitem(self):
        """Atama ve erişim testi"""
        arr = StaticArray(3)
        arr[0] = 10
        arr[1] = 20
        arr[2] = 30
        
        assert arr[0] == 10
        assert arr[1] == 20
        assert arr[2] == 30
        
        with pytest.raises(IndexError):
            arr[3] = 40
        
        with pytest.raises(IndexError):
            _ = arr[3]


if __name__ == "__main__":
    pytest.main([__file__]) 