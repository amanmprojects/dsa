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


vector<vector<int>> test = {
    {-1,0,1,2,-1,-4},
    {0,1,1}
};


int main(){
    Solution sol;
    int testNum = 1;
    for(auto t: test){
        cout << "Test Case " << testNum++ << ": [";
        for(int i = 0; i < t.size(); i++){
            cout << t[i];
            if(i < t.size()-1) cout << ",";
        }
        cout << "]" << endl;
        
        vector<vector<int>> res;
        res = sol.threeSum(t);
        
        cout << "Result: [";
        for(int i = 0; i < res.size(); i++){
            cout << "[";
            for(int j = 0; j < res[i].size(); j++){
                cout << res[i][j];
                if(j < res[i].size()-1) cout << ",";
            }
            cout << "]";
            if(i < res.size()-1) cout << ",";
        }
        cout << "]" << endl << endl;
    }
    return 0;
}
