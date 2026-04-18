class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        vector<pair<int, int>> cars;
        vector<double> stack;
        for(int i = 0; i < position.size(); i++){
            cars.push_back({position[i], speed[i]});
        }

        // Sorting
        sort(cars.begin(), cars.end());
        for(auto c: cars){
            cout<<"Car at pos: "<<c.first<< "with speed: "<<c.second<<"\n";
        }
        cout<<"\n";

        auto lastcar = cars[cars.size()-1];
        stack.push_back((target - lastcar.first) / lastcar.second);

        for(int i = cars.size()-2; i >= 0; i--){
            double endtime = (double)(target - cars[i].first) / cars[i].second;
            cout<<"endtime: "<<endtime<<"\n";
            if(!stack.empty() && endtime <= stack.back()){

            }
            else {
                stack.push_back(endtime);
            }
        }

        return stack.size();
    }
};
