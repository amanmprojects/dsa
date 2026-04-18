#include <vector>
#include <iostream>

using namespace std;
class Solution {

public:
    vector<int> productExceptSelf(vector<int>& nums) {
        // Zero Count and Prod calculation (without zeroes)
        int zeroes = 0;
        int prod = 1;

        for(int& n: nums){

            // If n is a zero, increment zeroes and skip multiplying to the product.
            if(n == 0){
                zeroes++;
                continue;
            }

            prod *= n;
        }

        vector<int> res(nums.size(), 0);
        
        // If the array is only zeroes or contains more than one zero
        if(zeroes > 1 || zeroes == nums.size()) return res;

        // If only one zero in array then handle edge case
        if(zeroes == 1){
            for(int i = 0; i < nums.size(); i++){
                if(nums[i] == 0) res[i] = prod;

            }
        }

        // No zeroes in array
        else {
            int i = 0;
            for(int& n: nums){
                res[i] = prod/n;
                i++;
            }
        }
        return res;
    }
};