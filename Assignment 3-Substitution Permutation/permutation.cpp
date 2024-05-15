#include <iostream>

using namespace std;

int main() {
    char s[1000];
    cin.getline(s, sizeof(s)); //Get original ciphertext
    
    int P[5];
    P[0] = 3; P[1] = 2; P[2] = 4; P[3] = 0; P[4] = 1; //Define permutation
    int count = 0;
    
    //Ciphertext without space and punctuation
    string t = "qmnjvsanvwewcflctvprjtjtvvplvlfvxjavqildhcxmlnvcnacyclpafcgytvfvwfvwgqyppqqpqcsywsqrxqmnjvafycgvtlvhfcwtylaeuqfvxjatkbvcqnsqslhfavawnccveasfuqbqvqtcyllrqrxxwacfypsdcuqfavrqcgefqpyattracxwvtaawwddveasflcbqvdtrawmvupqquwxdecgqcwtyqyaflvlqsyqklhqsnafqvmllhvqpawrnqgvfusrecwawyqpfnwgawdgf";

    string ans;
    
    //Use permuation in blocks of 5
    for(int i = 0; s[i] != '\0'; i++) {
        if(isalpha(s[i])) {
            char ch = t[(count / 5) * 5 + P[count % 5]];
            ans.push_back(ch);
            count++;
        }
        else {
            ans.push_back(s[i]);
        }
    }
    
    cout << ans;
}