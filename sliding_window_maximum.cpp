#include <string>
#include <vector>
#include <iostream>
#include <math.h>
#include <queue>
#include <deque>

using namespace std;

class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> result;
        deque<int> q;
        int l = 0, r = 0;
        while(r < nums.size()){
            while (!q.empty() && nums[q.back()] < nums[r]){
                q.pop_back();
            }
            q.push_back(r);

            if(l > q[0]){
                q.pop_front();
            }

            if(r+1 >= k){
                result.push_back(nums[q[0]]);
                l++;
            }

            r += 1;
        }
        return result;
    }
};