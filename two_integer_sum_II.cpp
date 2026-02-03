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
                    res[0] = i;
                    res[1] = j;
                    return res;
                }
            }
        }

        return res;
    }
};

vector<pair<vector<int>, int>> test_case = {
    {{1,2,3,4}, 3},
    {{5,6,7,8}, 13}
};

int main(){
    Solution sol;
    for(auto& t: test_case){
        vector<int> res = sol.twoSum(t.first, t.second);
        cout << "( " << res[0] << " , " << res[1] << " )\n";
    }

    return 0;
}
