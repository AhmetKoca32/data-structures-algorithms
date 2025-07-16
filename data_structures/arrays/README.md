# Array Veri Yapısı

Bu klasör, array veri yapısının farklı implementasyonlarını içerir.

## 📁 Dosyalar

- `array.py` - Dinamik ve statik array implementasyonları
- `README.md` - Bu dosya

## 🔧 Özellikler

### DynamicArray
- Otomatik boyutlandırma
- O(1) amortized ekleme (sona)
- O(n) ekleme (başa/ortaya)
- O(1) erişim ve güncelleme
- O(n) silme

### StaticArray
- Sabit boyut
- O(1) erişim ve güncelleme
- Boyut değiştirilemez

## 🚀 Kullanım

```python
from array import DynamicArray, StaticArray

# Dinamik array
arr = DynamicArray()
arr.append(10)
arr.append(20)
print(arr[0])  # 10

# Statik array
static_arr = StaticArray(5)
static_arr[0] = 1
static_arr[1] = 2
```

## 📊 Zaman Karmaşıklıkları

| İşlem | Dinamik Array | Statik Array |
|-------|---------------|--------------|
| Erişim | O(1) | O(1) |
| Arama | O(n) | O(n) |
| Ekleme (sona) | O(1) amortized | - |
| Ekleme (başa/ortaya) | O(n) | - |
| Silme | O(n) | - |
| Güncelleme | O(1) | O(1) |

## 💡 Pratik Uygulamalar

- Liste yönetimi
- Buffer yönetimi
- Matris işlemleri
- Veri saklama 