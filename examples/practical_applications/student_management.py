"""
Öğrenci Yönetim Sistemi - Pratik Uygulama

Bu örnek, veri yapıları ve algoritmaların gerçek hayatta nasıl kullanıldığını gösterir.
Öğrenci yönetim sisteminde array, sorting ve searching algoritmaları kullanılır.
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from data_structures.arrays.array import DynamicArray
from algorithms.sorting.sorting_algorithms import quick_sort, merge_sort


class Student:
    """Öğrenci sınıfı"""
    
    def __init__(self, student_id: int, name: str, age: int, gpa: float):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.gpa = gpa
    
    def __str__(self):
        return f"ID: {self.student_id}, İsim: {self.name}, Yaş: {self.age}, GPA: {self.gpa:.2f}"
    
    def __repr__(self):
        return self.__str__()


class StudentManagementSystem:
    """Öğrenci Yönetim Sistemi"""
    
    def __init__(self):
        self.students = DynamicArray()
        self.next_id = 1
    
    def add_student(self, name: str, age: int, gpa: float) -> int:
        """Yeni öğrenci ekleme"""
        student = Student(self.next_id, name, age, gpa)
        self.students.append(student)
        self.next_id += 1
        return student.student_id
    
    def remove_student(self, student_id: int) -> bool:
        """Öğrenci silme"""
        for i in range(len(self.students)):
            if self.students[i].student_id == student_id:
                self.students.pop(i)
                return True
        return False
    
    def find_student_by_id(self, student_id: int) -> Student:
        """ID ile öğrenci bulma (Linear Search)"""
        for i in range(len(self.students)):
            if self.students[i].student_id == student_id:
                return self.students[i]
        return None
    
    def find_students_by_name(self, name: str) -> list:
        """İsim ile öğrenci bulma"""
        results = []
        for i in range(len(self.students)):
            if name.lower() in self.students[i].name.lower():
                results.append(self.students[i])
        return results
    
    def sort_by_gpa(self, reverse: bool = True) -> list:
        """GPA'ya göre sıralama"""
        if len(self.students) == 0:
            return []
        
        # Student listesini GPA listesine çevir
        student_list = [self.students[i] for i in range(len(self.students))]
        
        # Quick sort kullanarak sırala
        sorted_students = quick_sort_by_gpa(student_list)
        
        if reverse:
            sorted_students.reverse()
        
        return sorted_students
    
    def sort_by_name(self) -> list:
        """İsme göre sıralama"""
        if len(self.students) == 0:
            return []
        
        student_list = [self.students[i] for i in range(len(self.students))]
        return merge_sort_by_name(student_list)
    
    def get_top_students(self, count: int = 5) -> list:
        """En yüksek GPA'lı öğrencileri getir"""
        sorted_students = self.sort_by_gpa(reverse=True)
        return sorted_students[:count]
    
    def get_average_gpa(self) -> float:
        """Ortalama GPA hesaplama"""
        if len(self.students) == 0:
            return 0.0
        
        total_gpa = sum(self.students[i].gpa for i in range(len(self.students)))
        return total_gpa / len(self.students)
    
    def get_student_count(self) -> int:
        """Toplam öğrenci sayısı"""
        return len(self.students)
    
    def display_all_students(self):
        """Tüm öğrencileri görüntüleme"""
        if len(self.students) == 0:
            print("Henüz öğrenci bulunmuyor.")
            return
        
        print(f"\n{'ID':<5} {'İsim':<20} {'Yaş':<5} {'GPA':<8}")
        print("-" * 40)
        
        for i in range(len(self.students)):
            student = self.students[i]
            print(f"{student.student_id:<5} {student.name:<20} {student.age:<5} {student.gpa:<8.2f}")


def quick_sort_by_gpa(students: list) -> list:
    """GPA'ya göre quick sort"""
    if len(students) <= 1:
        return students
    
    pivot = students[len(students) // 2]
    left = [s for s in students if s.gpa < pivot.gpa]
    middle = [s for s in students if s.gpa == pivot.gpa]
    right = [s for s in students if s.gpa > pivot.gpa]
    
    return quick_sort_by_gpa(left) + middle + quick_sort_by_gpa(right)


def merge_sort_by_name(students: list) -> list:
    """İsme göre merge sort"""
    if len(students) <= 1:
        return students
    
    mid = len(students) // 2
    left = merge_sort_by_name(students[:mid])
    right = merge_sort_by_name(students[mid:])
    
    return merge_by_name(left, right)


def merge_by_name(left: list, right: list) -> list:
    """İsme göre merge"""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i].name.lower() <= right[j].name.lower():
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def binary_search_by_id(students: list, student_id: int) -> Student:
    """ID ile binary search (sıralı liste gerekli)"""
    left, right = 0, len(students) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if students[mid].student_id == student_id:
            return students[mid]
        elif students[mid].student_id < student_id:
            left = mid + 1
        else:
            right = mid - 1
    
    return None


def demo_student_management():
    """Öğrenci yönetim sistemi demo"""
    print("=== Öğrenci Yönetim Sistemi Demo ===")
    
    # Sistem oluştur
    sms = StudentManagementSystem()
    
    # Öğrenciler ekle
    print("\n1. Öğrenciler ekleniyor...")
    sms.add_student("Ahmet Yılmaz", 20, 3.85)
    sms.add_student("Fatma Demir", 19, 3.92)
    sms.add_student("Mehmet Kaya", 21, 3.45)
    sms.add_student("Ayşe Özkan", 20, 3.78)
    sms.add_student("Ali Çelik", 22, 3.15)
    sms.add_student("Zeynep Arslan", 19, 3.95)
    sms.add_student("Mustafa Şahin", 21, 3.67)
    
    # Tüm öğrencileri görüntüle
    print("\n2. Tüm öğrenciler:")
    sms.display_all_students()
    
    # GPA'ya göre sırala
    print("\n3. GPA'ya göre sıralama (yüksekten düşüğe):")
    sorted_by_gpa = sms.sort_by_gpa()
    for i, student in enumerate(sorted_by_gpa, 1):
        print(f"{i}. {student}")
    
    # İsme göre sırala
    print("\n4. İsme göre sıralama:")
    sorted_by_name = sms.sort_by_name()
    for student in sorted_by_name:
        print(f"- {student.name} (GPA: {student.gpa:.2f})")
    
    # En iyi öğrenciler
    print("\n5. En iyi 3 öğrenci:")
    top_students = sms.get_top_students(3)
    for i, student in enumerate(top_students, 1):
        print(f"{i}. {student}")
    
    # İstatistikler
    print(f"\n6. İstatistikler:")
    print(f"Toplam öğrenci sayısı: {sms.get_student_count()}")
    print(f"Ortalama GPA: {sms.get_average_gpa():.2f}")
    
    # Arama örnekleri
    print("\n7. Arama örnekleri:")
    
    # ID ile arama
    found_student = sms.find_student_by_id(3)
    if found_student:
        print(f"ID 3 ile bulunan öğrenci: {found_student}")
    
    # İsim ile arama
    students_with_a = sms.find_students_by_name("a")
    print(f"İsminde 'a' geçen öğrenciler ({len(students_with_a)} tane):")
    for student in students_with_a:
        print(f"  - {student}")
    
    # Binary search demo (sıralı liste gerekli)
    print("\n8. Binary Search Demo:")
    sorted_by_id = sorted([sms.students[i] for i in range(len(sms.students))], 
                         key=lambda x: x.student_id)
    found = binary_search_by_id(sorted_by_id, 4)
    if found:
        print(f"Binary search ile ID 4 bulundu: {found}")
    
    # Öğrenci silme
    print("\n9. Öğrenci silme:")
    if sms.remove_student(2):
        print("ID 2 olan öğrenci silindi.")
        print("Güncel öğrenci listesi:")
        sms.display_all_students()


if __name__ == "__main__":
    demo_student_management() 