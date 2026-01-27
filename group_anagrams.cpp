#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {

        unordered_map<string, vector<string>> m;

        // Sort & insert into the map
        for(int i = 0; i < strs.size(); i++){
            string sortedS = strs[i];
            sort(sortedS.begin(), sortedS.end());
            m[sortedS].push_back(strs[i]);
        }

        vector<vector<string>> res;

        for(auto& v: m){
            res.push_back(v.second);
        }

        return res;
    }
};

int main(){
    Solution sol;
    vector<string> input {"aman", "nama", "das", "sad", "", "allah"};

    for(const auto& group : sol.groupAnagrams(input)) {
        printf("[");
        for(const auto& str : group) {
            printf("%s ", str.c_str());
        }
        printf("]\n");
    }
    return 0;
}
