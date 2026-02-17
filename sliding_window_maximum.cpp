#include <string>
#include <vector>
#include <iostream>
#include <math.h>

using namespace std;

class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        int l = 0; 
        int r = l+k-1;
        vector<int> res(nums.size()-k+1);

        for(r = 0; r < nums.size(); r++){
            int m, mi;
            
        }

        return res;
    }
};