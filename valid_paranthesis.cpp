#include <string>
#include <vector>
#include <iostream>

using namespace std;


class Solution {
public:
    bool isValid(string s) {
        vector<char> stack;

        for(char c: s){
            switch(c){
                case '[':
                case '{':
                case '(':
                    stack.push_back(c);
                    break;
                case '}':
                    if(stack.empty() || stack.back() != '{') return false;
                    else stack.pop_back();
                    break;
                case ']':
                    if(stack.empty() || stack.back() != '[') return false;
                    else stack.pop_back();
                    break;
                case ')':
                    if(stack.empty() || stack.back() != '(') return false;
                    else stack.pop_back();
                    break;            
            }
        }
        if(stack.size() != 0) return false;
        return true;
    }
};
