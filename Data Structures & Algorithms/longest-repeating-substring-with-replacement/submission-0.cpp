#include <string>
#include <vector>
#include <iostream>

using namespace std;


class Solution {
public:
    int characterReplacement(string s, int k) {
        vector<int> count(26, 0);
        int l = 0;
        int max_count = 0;
        int res = 0;

        for (int r = 0; r < s.size(); r++) {
            count[s[r] - 'A']++;
            max_count = max(max_count, count[s[r] - 'A']);

            while ((r - l + 1) - max_count > k) {
                count[s[l] - 'A']--;
                l++;
            }
            res = max(res, r - l + 1);
        }

        return res;
    }
};
