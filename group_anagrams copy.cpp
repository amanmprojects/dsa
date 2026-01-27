#include <vector>
#include <string>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> res;

        for(const auto& s: strs){
            vector<int> count(26,0);
            
            for(char c: s){
                count[c - 'a']++;
            }

            string key = to_string(count[0]);

            for(int i = 1; i < 26; i++){
                key += to_string(count[i]);
            }
            res[key].push_back(s);
        }

        vector<vector<string>> result;

        for(const auto& pair: res){
            result.push_back(pair.second);
        }

        return result;
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
