#include <vector>

using namespace std;

class Solution {
public:
    int findMin(vector<int> &nums) {
        int l = 0, r = nums.size()-1;
        int curr = nums[l];
        int mid;

        if(nums.size() == 1) return nums[0];
        else if (nums.size() == 2) return min(nums[0], nums[1]);
        
        if(nums[l] < nums[r]) return nums[l];
        while(l < r){
            mid = (l+r)/2;
            if(nums[mid] < nums[mid-1]) return nums[mid];
            if(nums[mid] > nums[l]) l = mid+1;
            else r = mid-1;
        }
        return 0;
    }
};
