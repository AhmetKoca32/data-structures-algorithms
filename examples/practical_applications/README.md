# Pratik Uygulamalar

Bu klasör, veri yapıları ve algoritmaların gerçek hayatta nasıl kullanıldığını gösteren pratik örnekler içerir.

## 📁 Dosyalar

- `student_management.py` - Öğrenci yönetim sistemi örneği
- `README.md` - Bu dosya

## 🎯 Öğrenci Yönetim Sistemi

Bu örnek, aşağıdaki veri yapıları ve algoritmaları kullanır:

### Kullanılan Veri Yapıları
- **DynamicArray**: Öğrenci listesini saklamak için
- **List**: Geçici veri işlemleri için

### Kullanılan Algoritmalar
- **Quick Sort**: GPA'ya göre sıralama
- **Merge Sort**: İsme göre sıralama
- **Linear Search**: ID ve isim ile arama
- **Binary Search**: Sıralı listede ID arama

### Özellikler
1. **Öğrenci Ekleme/Silme**: DynamicArray kullanarak
2. **Sıralama**: GPA ve isme göre farklı algoritmalar
3. **Arama**: Linear ve binary search
4. **İstatistikler**: Ortalama GPA hesaplama
5. **En İyi Öğrenciler**: Top-k sorgulama

## 🚀 Kullanım

```bash
cd examples/practical_applications
python student_management.py
```

## 📊 Örnek Çıktı

```
=== Öğrenci Yönetim Sistemi Demo ===

1. Öğrenciler ekleniyor...

2. Tüm öğrenciler:
ID    İsim                 Yaş   GPA     
----------------------------------------
1     Ahmet Yılmaz         20    3.85
2     Fatma Demir          19    3.92
3     Mehmet Kaya          21    3.45
...

3. GPA'ya göre sıralama (yüksekten düşüğe):
1. ID: 6, İsim: Zeynep Arslan, Yaş: 19, GPA: 3.95
2. ID: 2, İsim: Fatma Demir, Yaş: 19, GPA: 3.92
...
```

## 💡 Öğrenilen Kavramlar

### Veri Yapıları
- **Array**: Veri saklama ve erişim
- **Dynamic Array**: Otomatik boyutlandırma
- **Object-Oriented Design**: Sınıf yapısı

### Algoritmalar
- **Sorting**: Farklı kriterlere göre sıralama
- **Searching**: Verimli arama teknikleri
- **Time Complexity**: Algoritma performansı

### Yazılım Mühendisliği
- **Modular Design**: Modüler kod yapısı
- **Error Handling**: Hata yönetimi
- **Documentation**: Kod dokümantasyonu

## 🔧 Gelecek Örnekler

Bu klasöre eklenebilecek diğer pratik uygulamalar:

1. **E-ticaret Sistemi**: Hash table, tree, graph kullanımı
2. **Sosyal Medya**: Graph algoritmaları
3. **Dosya Sistemi**: Tree yapısı
4. **Cache Sistemi**: LRU cache implementasyonu
5. **Task Scheduler**: Priority queue
6. **Database Index**: B-tree implementasyonu

## 🎓 Eğitim Değeri

Bu örnekler sayesinde:
- Teorik kavramları pratikte görme
- Gerçek problemleri çözme
- Kod organizasyonu öğrenme
- Performans analizi yapma
- Test yazma alışkanlığı kazanma 