#include <vector>
#include <iostream>

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
            cout<<"Mid : "<<mid;
            if(will_eat(mid, h, piles)) {
                cout<<" Will eat\n";
                mink = mid;
                r = mid - 1;
            }
            else {
                l = mid + 1;
            }
        }

        return mink;
    }

    bool will_eat (int k, int h, vector<int> piles) {
        long long hours_needed = 0;
        for(int p: piles) {
            hours_needed += (p + k - 1) / k;
        }
        return hours_needed <= h;
    }   
};
