#include <vector>
#include <iostream> 

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int i = 0;
        int j = 1;

        vector<int> res = {0,0};

        for(; i < numbers.size()-1; i++){
            for(j = i+1; j < numbers.size(); j++){
                if((numbers[i] + numbers[j]) == target){
                    res[0] = i+1;
                    res[1] = j+1;
                    return res;
                }
            }
        }

        return res;
    }
};