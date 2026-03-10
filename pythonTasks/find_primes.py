import numpy as np
import sys
import time
import math

def simple_sieve(limit):
    is_prime = np.ones(limit + 1, dtype=bool)
    is_prime[0:2] = False  # 0 and 1 are not prime numbers
    for p in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[p]:
            is_prime[p*p:limit+1:p] = False
    return np.flatnonzero(is_prime)


def segmented_sieve(start, end):
    range_size = end - start
    limit = int(math.sqrt(end)) + 1
    base_primes = simple_sieve(limit)
    segment = np.ones(range_size, dtype=bool)

    if start == 1:
        segment[0] = False
    
    for p in base_primes:
        first_multiple = max(p * p, (start + p - 1) // p * p)

        start_index = first_multiple - start
       
        segment[start_index::p] = False

    return start + np.flatnonzero(segment)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Hata: Yanlış kullanım.")
        print("Kullanım: python3 find_primes.py <başlangıç_sayısı> <bitiş_sayısı>")
        print("Örnek:   python3 find_primes.py 1 10000001")
        sys.exit(1)

    try:
        start = int(sys.argv[1])
        end = int(sys.argv[2])
    except ValueError:
        print("Hata: Başlangıç ve bitiş değerleri sayısal olmalıdır.")
        sys.exit(1)
    
    if start < 1 or end <= start:
        print("Hata: Geçersiz aralık. Başlangıç 1'den büyük veya eşit ve bitiş başlangıçtan büyük olmalıdır.")
        sys.exit(1)

    range_size = end - start
    print(f"Verilen aralık: [{start}, {end}) (Toplam {range_size} sayı)")
    print("Asal sayılar bulunuyor...")

    comp_start_time = time.time()
    prime_numbers = segmented_sieve(start, end)

    comp_end_time = time.time()
    computation_time = comp_end_time - comp_start_time

    print(f"Asal sayılar bulundu. Toplam {len(prime_numbers)} asal sayı var.")
    print(f"Hesaplama süresi: {computation_time:.6f} saniye")  

    output_file = "primes_output.txt"

    print(f"Asal sayılar '{output_file}' dosyasına yazılıyor...")
    write_start_time = time.time()

    try: 
        with open(output_file, 'w') as f:
            f.write("\n".join(map(str, prime_numbers)))
    except MemoryError:
        print("Hata: Bellek hatası! Yavaş yazılma moduna geçiliyor...")
        with open(output_file, 'w') as f:
            for prime in prime_numbers:
                f.write(f"{prime}\n")
        
    write_end_time = time.time()
    write_time = write_end_time - write_start_time
    print(f"Asal sayılar dosyaya yazıldı. Yazma süresi: {write_time:.6f} saniye")
    print(f"Toplam süre: {computation_time + write_time:.6f} saniye")
