#include <string>
#include <unordered_map>


using namespace std;


class Solution {
public:
    string minWindow(string s, string t) {
        if (t.size() == 0) return "";

        unordered_map<char, int> countT, countS;

        for(char c: t){
            countT[c]++;
        }

        int need = countT.size();
        int have = 0;
        int l = 0, r = 0;
        pair<int, int> res = {-1,-1};
        int resLen = INT_MAX;

        
        for(r = 0; r < s.size(); r++){
            countS[s[r]]++;
            
            if(countS[s[r]] == countT[s[r]]) have++;
            cout<<"Have: "<<have<<" Need: "<<need<<"\n";
            while(have == need){
                cout<<"Yum l = "<<l<<" r = "<<r<<"\n";
                if((r-l+1) < resLen){
                    resLen = r-l+1;
                    res = {l, r};
                    cout<<"Updated Boss: res = {"<<res.first<<", "<<res.second<<"}\n";
                }
                countS[s[l]]--;
                if(countS[s[l]] < countT[s[l]]) have--;
                l++;
            }
        }

        string finalres = (resLen == INT_MAX) ? "" : s.substr(res.first, resLen);
        return finalres;
    }
};
