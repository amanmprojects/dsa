#include <string>
#include <vector>
#include <iostream>
#include <math.h>

using namespace std;

class MinStack {
private:
        vector<int> stack;
        int m = INFINITY;
public:
    MinStack() {

    }
    
    void push(int val) {
        stack.push_back(val);
        m = min(m, val);
    }
    
    void pop() {
        int popped = stack.back();
        stack.pop_back();
        if(popped == m) {
            if(stack.empty()) m = INFINITY;
            else {
                m = stack[0];
                for(int t: stack){
                    m = min(m, t);
                }
            }
        }
    }
    
    int top() {
        return stack.back();
    }
    
    int getMin() {
        return m;
    }
};
