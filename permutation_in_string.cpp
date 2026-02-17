#include <string>

#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        if (s1.size() > s2.size()) return false;

        vector<int> m1(26, 0);
        vector<int> m2(26, 0);

        for (char c : s1) {
            m1[c - 'a']++;
        }

        int l = 0;
        int r = 0;
        int s1_size = s1.size();
        int s2_size = s2.size();

        while (r < s2_size) {
            m2[s2[r] - 'a']++;

            if (r - l + 1 > s1_size) {
                m2[s2[l] - 'a']--;
                l++;
            }

            if (m1 == m2) return true;
            r++;
        }
        return false;
    }
};


vector<pair<pair<string, string>, bool>> test = {
    {{"abc", "lecabee"}, true},
    {{"abc", "lecaabee"}, false}
};

int main(){
    Solution sol;
    int i = 1;
    for(auto t: test){
        bool res = sol.checkInclusion(t.first.first, t.first.second);
        cout << "Test " << i++ << ": ";
        if(res == t.second) cout << "PASS (Expected: " << boolalpha << t.second << ", Got: " << res << ")\n";
        else cout << "FAIL (Expected: " << boolalpha << t.second << ", Got: " << res << ")\n";
    }
    return 0;
}
