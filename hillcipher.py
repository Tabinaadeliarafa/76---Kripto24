#	Nama     : Tabina adelia rafa
#	NPM      : 140810220076
#	Kelas    : B
#	Program  : Buatlah program untuk enkripsi, dekripsi, dan mencari kunci Hill Cipher (bahasa pemrograman bebas)


import numpy as np

def char_to_number(x):
    return ord(x) - 65

def number_to_char(x):
    return chr(x + 65)

def mod_inverse(A, M):
    for X in range(1, M):
        if ((A % M) * (X % M)) % M == 1:
            return X
    return -1

def input_key(n):
    key = []
    print("Input angka/nilai key matrix (dipisahkan spasi):")
    for i in range(n):
        while True:
            row = list(map(int, input().split()))
            if len(row) == n:
                key.append([x % 26 for x in row])
                break
            else:
                print(f"Jumlah input pada baris ke-{i+1} tidak sesuai. Harus {n} angka.")
    
    print("Key Matrix:")
    for row in key:
        print(f"[{' '.join(map(str, row))}]")
    
    return np.array(key)


def input_text(type_text):
    text = input(f"Input {type_text}: ").upper()
    return text

def hill(method, text, key, n):
    key_det = round(np.linalg.det(key))
    if key_det % 2 == 0 or key_det == 13:
        print("Determinan bukan ganjil selain 13. Key ga ada karena invers ga ada.")
        return ""
    
    if len(text) % n != 0:
        last_char = text[-1]
        text += last_char * (n - len(text) % n)

    text_in_number = [char_to_number(c) for c in text]
    result = []

    if method == "dekripsi":
        det_inverse = mod_inverse(key_det % 26, 26)
        key = np.linalg.inv(key) * key_det
        key = (key * det_inverse).round().astype(int) % 26

    for i in range(0, len(text), n):
        block = np.dot(key, text_in_number[i:i + n]) % 26
        result.extend(block)

    output = ''.join(number_to_char(int(num)) for num in result)
    return output

def find_key(pt, ct, m):
    pt_in_number = [char_to_number(c) for c in pt]
    ct_in_number = [char_to_number(c) for c in ct]
    
    p_matrix = np.array(pt_in_number).reshape(m, m)
    c_matrix = np.array(ct_in_number).reshape(m, m)

    p_det = round(np.linalg.det(p_matrix))
    if p_det % 2 == 0 or p_det == 13:
        print("Determinan bukan ganjil selain 13. Key ga ada karena invers ga ada.")
        return np.zeros((m, m), dtype=int)

    p_det_inverse = mod_inverse(p_det % 26, 26)
    p_matrix = np.linalg.inv(p_matrix) * p_det
    p_matrix = (p_matrix * p_det_inverse).round().astype(int) % 26

    key = np.dot(c_matrix, p_matrix) % 26
    return key

def main():
    while True:
        print("\n========Menu========")
        print("A. Enkripsi")
        print("B. Dekripsi")
        print("C. Cari Key")
        print("D. Exit")
        
        pilihan = input("Pilihan: ").upper()

        if pilihan in ['A', 'B']:
            n = int(input("\nInput ukuran key matrix (n x n): "))
            key = input_key(n)
            text = input_text("text")
            
            if pilihan == 'A':
                print("\nPlaintext:", text)
                output = hill("enkripsi", text, key, n)
                print("Ciphertext:", output)
            else:
                print("\nCiphertext:", text)
                output = hill("dekripsi", text, key, n)
                print("Plaintext:", output)

        elif pilihan == 'C':
            pt = input_text("plaintext")
            ct = input_text("ciphertext")
            m = int(input("\nInput nilai m: "))
            key = find_key(pt, ct, m)
            print(f"\nPlaintext: {pt}")
            print(f"Ciphertext: {ct}")
            print("Key Matrix:")
            for row in key:
                print(f"[{' '.join(map(str, row))}]")

        elif pilihan == 'D':
            break
        else:
            print("\nInput ga sesuai.")

if __name__ == "__main__":
    main()
    