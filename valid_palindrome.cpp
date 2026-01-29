#include <string>
#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    bool isPalindrome(string s) {
        int i, j;
        i = 0;
        j = s.size()-1;

        for(;  i < j ;){
            char l = tolower(s[i]);
            char r = tolower(s[j]);


            while(!((l >= 48 && l <= 57) || (l >= 65 && l <= 90) || (l >= 97 && l <= 122)) && i < j){
                i++;
                l = tolower(s[i]);
            }
            while(!((r >= 48 && r <= 57) || (r >= 65 && r <= 90) || (r >= 97 && r <= 122)) && i < j){
                j--;
                r = tolower(s[j]);
            }
            if(l != r) return false;
            i++;
            j--;
        }
        return true;
    }
};

vector<string> test_cases = {
    "aman",
    "amanama",
    "ana",
    "",
    "a",
    "Was it a car or a cat I saw?",
    " "
};


int main(){
    Solution sol;
    for(string s: test_cases){
        if(sol.isPalindrome(s)) cout << "true\n";
        else cout << "false\n";
    }
    return 0;
}