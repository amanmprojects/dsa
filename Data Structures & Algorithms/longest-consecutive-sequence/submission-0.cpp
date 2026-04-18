#include <vector>
#include <unordered_set>
#include <iostream>

using namespace std;

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> s;

        for(int n: nums){
            s.insert(n);
        }

        int longest = 0;
        for(int n: nums){
            if(s.count(n-1)) continue;
            int length = 1;
            while(s.count(n+length)){
                length++;
            }
            longest = max(longest, length);
        }

        return longest;
    }
};
