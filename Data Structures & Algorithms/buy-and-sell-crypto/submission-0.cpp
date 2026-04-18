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