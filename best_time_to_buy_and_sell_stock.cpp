#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int l, r, res;
        l = r = res = 0;

        for(r = 0; r < prices.size(); r++){
            res = max(res, prices[r]-prices[l]);
            if(prices[r] < prices[l]) l = r;
        }
        return res;
    }
};


vector<pair<vector<int>, int>> test  = {
    {{10,1,5,6,7,1}, 6},
    {{10,8,7,5,2}, 0}
};


int main(){
    Solution sol;
    for(auto& t: test){
        int res = sol.maxProfit(t.first);
        if(res == t.second) cout<<"Matched!\n";
    }
}
