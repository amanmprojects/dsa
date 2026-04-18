#include <algorithm>
#include <vector>
#include <unordered_map>
#include <iostream>

using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> res;
        sort(nums.begin(), nums.end());
        int i, j, k;
        for(i = 0; i < nums.size()-2; i++){
            // Skip duplicate values for i
            if(i > 0 && nums[i] == nums[i-1]) continue;
            
            j = i+1;
            k = nums.size()-1;  // Fixed: should be index, not value
            while(j<k){
                int sum = nums[i] + nums[j]+nums[k];
                if(sum == 0) {
                    res.push_back({nums[i], nums[j], nums[k]});
                    // Skip duplicates for j and k
                    while(j < k && nums[j] == nums[j+1]) j++;
                    while(j < k && nums[k] == nums[k-1]) k--;
                    j++;
                    k--;
                }
                else if (sum < 0) {
                    j++;
                }
                else {
                    k--;
                }
            }
        }
        return res;
    }
};
