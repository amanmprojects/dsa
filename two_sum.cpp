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


int main(){
    Solution sol;
    vector<int> nums = {1,2,3,4,5};
    vector<int> res;
    res = sol.twoSum(nums, 9);
    printf("[%d, %d]\n", res[0], res[1]);

    return 0;
}
