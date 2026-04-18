#include <vector>
#include <string>
#include <iostream>

using namespace std;

class Solution {
public:

    string encode(vector<string>& strs) {
        string res = "";
        int i = 0;
        for(string s: strs){
            res = res + to_string(s.size()) + "#" + s;
        }
        return res;
    }

    vector<string> decode(string s) {
        int i = 0;
        vector<string> res;

        while(i < s.size()){
            string size = "";
            while(s[i] != '#'){
                size += s[i];
                i++;
            }
            i++;
            string temp = s.substr(i, stoi(size));
            res.push_back(temp);
            i = i+stoi(size);
        }

        return res;
    }
};

