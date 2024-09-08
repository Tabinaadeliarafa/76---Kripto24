/*
	Nama     : Tabina adelia rafa
	NPM      : 140810220076
	Kelas    : B
	Program  : Membuat program Shift Cipher dengan bahasa pemrograman bebas
*/

#include <iostream>
using namespace std;

string encrypt(string plainTeks, int shift){
    string encryptedText = "";
    for (char &c : plainTeks) {
        if (isalpha(c)) {
            char offset = isupper(c) ? 'A' : 'a';
            encryptedText += char(int((c - offset + shift) % 26 + offset));
        } else {
            encryptedText += c;
        }
    }
    return encryptedText;
}

string decrypt(string encrypedText, int shift) {
    string decryptedText = "";
    for (char &c : encrypedText) {
        if (isalpha(c)) {
            char offset = isupper(c) ? 'A' : 'a';
            decryptedText += c;
        } else {
            decryptedText += c;
        }
    }
    return decryptedText;

}

int main() {
    string plainText;
    int shift;

    cout << "Masukkan nama: ";
    getline(cin, plainText);  
    cout << "Masukkan kunci: ";
    cin >> shift; 

    string encryptedText = encrypt(plainText, shift);
    cout << "Hasil enkripsi: " << encryptedText << endl;

    string decryptedText = decrypt(encryptedText, shift);
    cout << "Teks setelah dekripsi: " << decryptedText << endl;

    return 0;
}