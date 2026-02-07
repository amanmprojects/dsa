#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    int trap(vector<int>& height) {
        vector<int> leftmax(height.size(), 0);
        vector<int> rightmax(height.size(), 0);

        int maxi = 0;
        for(int i = 1; i < height.size(); i++){
            maxi = max(height[i-1], maxi);
            leftmax[i] = maxi;
        }
        maxi = 0;
        for(int i = height.size()-2; i > -1; i--){
            maxi = max(height[i+1], maxi);
            rightmax[i] = maxi;
        }

        // Normal Pass
        int res = 0;
        int mini;
        for(int i = 0; i < height.size(); i++){
            mini = min(leftmax[i], rightmax[i]);
            if(height[i] >= mini) continue;

            res += (mini - height[i]);
        }

        return res;
    }
};

vector<pair<vector<int>, int>> test = {
    {{0,2,0,3,1,0,1,3,2,1}, 9}
};

int main(){
    Solution sol;
    for(auto t: test){
        int res = sol.trap(t.first);
        if(res == t.second) cout<<"Matched!\n";
    }

    return 0;
}
