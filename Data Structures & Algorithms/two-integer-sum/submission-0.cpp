#include <unordered_map>
#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> m;

        int i = 0;
        for(; i < nums.size(); i++){
            m[nums[i]] = i;
        }

        for(i = 0; i < nums.size(); i++){
            int difference = target - nums[i];
            if(m.count(difference) && m[difference] != i){
                return {i, m[difference]};
            }
        }
        return {};
    }
};