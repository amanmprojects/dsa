class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        vector<int> res(temperatures.size(), 0);
        vector<int> stack = {0};

        for(int i = 1; i < temperatures.size(); i++){
            while(!stack.empty() && temperatures[stack.back()] < temperatures[i]){
                int lasti = stack.back();
                stack.pop_back();
                res[lasti] = i - lasti;
            }
            stack.push_back(i);
        }

        return res;
    }
};
