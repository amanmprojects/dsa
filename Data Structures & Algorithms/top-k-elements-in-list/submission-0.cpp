#include <vector>
#include <algorithm>
#include <unordered_map>
#include <iostream>

using namespace std;

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> m;

        for(const int num: nums){
            m[num]++;
        }

        vector<pair<int, int>> sorted;

        for(const auto& pair: m){
            sorted.push_back({pair.second, pair.first});
        }

        sort(sorted.rbegin(), sorted.rend());

        vector<int> res;

        for(int i = 0; i < k; i++){
            res.push_back(sorted[i].second);
        }

        return res;

    }
};