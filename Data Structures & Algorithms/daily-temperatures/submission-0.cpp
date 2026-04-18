class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        vector<int> res(temperatures.size(), 0);
        vector<pair<int, int>> stack = {{temperatures[0],0}};

        for(int i = 1; i < temperatures.size(); i++){
            while(!stack.empty() && stack.back().first < temperatures[i]){
                pair<int, int> last = stack.back();
                stack.pop_back();
                res[last.second] = i - last.second;
            }
            stack.push_back({temperatures[i], i});
        }

        return res;
    }

};
