#include <string>
#include <unordered_map>
#include <vector>
#include <iostream>

using namespace std;


class Solution {
public:
    string minWindow(string s, string t) {
        if (t.size() == 0) return "";

        unordered_map<char, int> countT, countS;

        for(char c: t){
            countT[c]++;
        }

        int need = countT.size();
        int have = 0;
        int l = 0, r = 0;
        pair<int, int> res = {-1,-1};
        int resLen = __INT_MAX__;

        
        for(r = 0; r < s.size(); r++){
            countS[s[r]]++;

            if(countS[s[r]] == countT[s[r]]) have++;

            while(have == need){
                if((r-l+1) < resLen){
                    resLen = r-l+1;
                    res = {l, r};
                }
                countS[l]--;
                if(countS[s[l]] < countT[s[l]]) have--;
                l++;
            }
        }

        string finalres = (resLen == __INT_MAX__) ? "" : s.substr(res.first, resLen);
        return finalres;
    }
};


vector<pair<string, string>> test = {
    {"aa", "aa"}
};


int main(){
    Solution sol;
    for(auto t: test){
        cout<<sol.minWindow(t.first, t.second)<<"\n";
    }
    return 0;
}