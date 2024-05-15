#include <bits/stdc++.h> 
#include <iostream>
using namespace std;

int main(){
    string cipher_text = "qmnjvsa nv wewc flct vprj tj tvvplvl fv xja vqildhc xmlnvc nacyclpa fc gyt vfvw. fv wgqyp, pqq pqcs y wsq rx qmnjvafy cgv tlvhf cw tyl aeuq fv xja tkbv cqnsqs. lhf avawnc cv eas fuqb qvq tc yllrqr xxwa cfy. psdc uqf avrqc gefq pyat trac xwv taa wwd dv eas flcbq. vd trawm vupq quw x decgqcwt, yq yafl vlqs yqklhq! snafq vml lhvqpawr nqg_vfusr_ec_wawy qp fn wgawdgf";
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

    cout << ioc;

    return 0;
}