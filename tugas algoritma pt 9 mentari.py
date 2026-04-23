import random

# 1. Implementasi Binary Search Iterative [cite: 51, 62]
def binary_search_iterative(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# 2. Implementasi Binary Search Recursive [cite: 206]
def binary_search_recursive(arr, low, high, target):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, mid + 1, high, target)
    else:
        return binary_search_recursive(arr, low, mid - 1, target)

# --- PERSIAPAN DATA ---
# Membuat 20 angka acak [cite: 204]
data_list = [random.randint(1, 100) for _ in range(20)]
# Urutkan list sebelum pencarian (Syarat Mutlak) [cite: 12, 205]
data_list.sort()

# --- LOOP MENU UTAMA ---
while True:
    print("\n" + "="*30)
    print("   MENU BINARY SEARCH")
    print("="*30)
    print(f"Data Terurut: {data_list}")
    print("-" * 30)
    print("1. Cari angka (Metode Iteratif)")
    print("2. Cari angka (Metode Rekursif)")
    print("3. Keluar")
    
    pilihan = input("\nPilih menu (1/2/3): ")

    if pilihan == '3':
        print("Terima kasih! Program berakhir.") # Baris ini sekarang aman dari error cite
        break

    if pilihan in ['1', '2']:
        try:
            target = int(input("Masukkan angka yang dicari: "))
            
            if pilihan == '1':
                indeks = binary_search_iterative(data_list, target)
                metode = "Iteratif"
            else:
                indeks = binary_search_recursive(data_list, 0, len(data_list) - 1, target)
                metode = "Rekursif"

            print(f"\n[Hasil {metode}]")
            if indeks != -1:
                print(f"Angka {target} ditemukan pada indeks ke-{indeks}.")
            else:
                print(f"Angka {target} tidak ditemukan dalam list.")
                
        except ValueError:
            print("Input tidak valid! Harap masukkan angka.")
    else:
        print("Pilihan menu tidak tersedia.")

    input("\nTekan Enter untuk melanjutkan...")