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
