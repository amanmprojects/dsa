#include <vector>

using namespace std;

class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int maxp = 0;
        for(int p: piles){
            maxp = max(maxp, p);
        }

        int l = 1, r = maxp;

        int mink = maxp;

        while(l <= r){
            int mid = (l+r) / 2;
            if(will_eat(mid, h, piles)) {
                mink = mid;
                r = mid - 1;
            }
            else {
                l = mid+1;
            }
        }
    }

    bool will_eat (int k, int h, vector<int>& piles) {
        for(int p: piles) {
            p = p - 
        }
    }
};
