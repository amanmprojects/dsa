class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        vector<pair<int, int>> cars;
        vector<int> stack;
        for(int i = 0; i < position.size(); i++){
            cars.push_back({position[i], speed[i]});
        }

        // Sorting
        sort(cars.begin(), cars.end());

        for(int i = cars.size()-1; i >= 0; i--){
            int endtime = (target - cars[i].first) / cars[i].second;
            stack.push_back(endtime);
            while(!stack.empty() && stack.back() >= endtime) stack.pop_back();
        }

        return stack.size();
    }
};
