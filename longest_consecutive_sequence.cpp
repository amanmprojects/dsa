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

vector<vector<int>> test_cases = {
    {2,20,4,10,3,4,5},
    {0,3,2,5,4,6,1,1}
};

int main(){
    Solution sol;
    for(auto& t: test_cases){
        int res = sol.longestConsecutive(t);
        cout << "The longest sequence is " << res << "\n";
    }

    return 0;
}
