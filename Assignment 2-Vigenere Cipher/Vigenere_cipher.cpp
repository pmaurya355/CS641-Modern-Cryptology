#include <bits/stdc++.h> 
#include <iostream>
using namespace std;

int main(){
    string cipher_text = "SIBRMYT SW WKJ LKGT DAFPZ OKQCPS IGCKH. XO'B OBCPQ RIECCW D FBFTNOKWCT";
    transform(cipher_text.begin(), cipher_text.end(), cipher_text.begin(), ::tolower); 
    unordered_map<char, int> mp;
    int alphabets = 0;

    // Calculate frequency of each character
    for(char ch : cipher_text){
        mp[ch]++;
        if(isalpha(ch)) alphabets++; // Count the number of alphabets
    }
    // Print all characters with their frequency
    for (const auto& pair : mp) 
            cout << pair.first << "->" << pair.second << endl;      
    
    // Calculate the Index of Coincidence
    double ioc = 0.0;
    for (const auto& pair : mp) {
        if(isalpha(pair.first)) ioc += pair.second * (pair.second - 1);
    }
    ioc /= alphabets * (alphabets - 1);
    cout << ioc << endl;

    int key[9] = {10, 2, 6, 2, 3, 5, 2, 2, 1}; 
    string deciphered_text;
    int j = 0;
    for (int i = 0; i < cipher_text.length(); i++){
        if(isalpha(cipher_text[i])){  
            int x = cipher_text[i] - 'a';  // Convert the ciphertext character into integer between 0-25
            char c = (x - key[j] + 26) % 26 + 'a'; // Take the difference between x and key value and convert it to character between 'a' to 'z'
            deciphered_text += c; 
        }
        else {
            deciphered_text += cipher_text[i]; // If the character in ciphertext is not an alphabet, copy the same character
            continue;
        }
        j = (j + 1) % 9;  // Run index j in cyclic manner
    }
    
     cout << deciphered_text;
    return 0;
}