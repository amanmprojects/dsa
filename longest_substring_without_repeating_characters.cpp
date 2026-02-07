#include <string>
#include <unordered_set>
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<int> set;
        int l = 0, maxi = 0;
        
        for(int r = 0; r < s.size(); r++){
            while(set.count(s[r])) {
                set.erase(s[l]);
                l += 1;
            }
            set.insert(s[r]);
            maxi = max(maxi, r-l+1);
        }

        return maxi;
    }
};


vector<pair<string, int>> test = {
    {"zxyzxyz",3}, 
    {"xxxx", 1}
};

int main(){
    Solution sol;
    for(auto t: test){
        int res = sol.lengthOfLongestSubstring(t.first);
        if(res == t.second) cout<<"Matched!\n";
    }

    return 0;
}
