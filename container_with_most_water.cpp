#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    int maxArea(vector<int>& heights) {
        int l, r, curr, max;
        l = curr = max = 0;
        r = heights.size() - 1;

        while(l < r){
            curr = min(heights[l], heights[r]) * (r-l);
            if(curr > max) max = curr;

            if(heights[l] <= heights[r]) l++;
            else r--;
        }
        return max;
    }
};

vector<pair<vector<int>, int>> test = {
    {{1,7,2,5,4,7,3,6}, 36},
    {{2,2,2}, 4}
};


int main()
{
    Solution sol;
    for(auto t: test){
        int res = sol.maxArea(t.first);
        if (res == t.second) {
            cout<<"Matched!\n";
        }
    }
    return 0;
}
