#include <string>
#include <vector>
#include <iostream>
#include <math.h>

using namespace std;


class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        vector<string> stack;
        for(string t: tokens){
            if(!(t == "+" || t == "-" || t == "*" || t == "/")){
                stack.push_back(t);
            }
            else{
                int second = stoi(stack.back());
                stack.pop_back();
                int first = stoi(stack.back());
                stack.pop_back();
                int res=0;
                if(t == "+"){
                    res = first + second;
                }
                else if(t == "-"){
                    res = first - second;
                }
                else if(t == "*"){
                    res = first * second;
                }
                else {
                    res = first / second;
                }

                stack.push_back(to_string(res));
            }
        }
        return stoi(stack.back());
    }
};
