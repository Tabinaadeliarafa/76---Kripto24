/*
	Nama     : Tabina adelia rafa
	NPM      : 140810220076
	Kelas    : B
	Program  : Membuat program Vigenere Cipher dengan bahasa pemrograman bebas
*/
#include <iostream>
#include <string>

using namespace std;

string vigenereEncrypt(const string& plaintext, const string& key) {
    string ciphertext;
    int keyIndex = 0;
    int keyLength = key.length();

    for (char c : plaintext) {
        if (!isalpha(c)) {
            ciphertext += c;
            continue;
        }

        char offset = isupper(c) ? 'A' : 'a'; 
        char k = toupper(key[keyIndex % keyLength]); 
        
        char encryptedChar = (c - offset + (k - 'A')) % 26 + offset;
        ciphertext += encryptedChar;

        keyIndex++; 
    }
    return ciphertext;
}

string vigenereDecrypt(const string& ciphertext, const string& key) {
    string plaintext;
    int keyIndex = 0;
    int keyLength = key.length();

    for (char c : ciphertext) {
        if (!isalpha(c)) {
            plaintext += c;
            continue;
        }

        char offset = isupper(c) ? 'A' : 'a'; 
        char k = toupper(key[keyIndex % keyLength]); 
        
        char decryptedChar = (c - offset - (k - 'A') + 26) % 26 + offset;
        plaintext += decryptedChar;

        keyIndex++; 
    }
    return plaintext;
}

int main() {
    string plaintext, key;

    cout << "Masukkan plaintext: ";
    getline(cin, plaintext);
    cout << "Masukkan kunci: ";
    getline(cin, key);

    string encrypted = vigenereEncrypt(plaintext, key);
    cout << "Ciphertext: " << encrypted << endl;

    string decrypted = vigenereDecrypt(encrypted, key);
    cout << "Plaintext setelah dekripsi: " << decrypted << endl;

    return 0;
}
