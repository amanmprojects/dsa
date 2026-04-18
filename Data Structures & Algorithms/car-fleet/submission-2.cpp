class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        vector<pair<double,double>>pairs;
        for(int i=0;i<position.size();i++){
            pairs.push_back({position[i], speed[i]});
        };
        sort(pairs.begin(), pairs.end(), [](pair<double,double>a,pair<double,double>b){
            return b.first < a.first;
        });
        int fleets=0;
        vector<double>timeToReach(pairs.size(),0);
        for(int i=0;i<pairs.size();i++){
            double timetoReach = (target - pairs[i].first)/pairs[i].second;
            if(i > 0 && timetoReach <= timeToReach[i-1]){
                timeToReach[i] = timeToReach[i-1];
            }else{
                fleets++;
                timeToReach[i] = timetoReach;
            }
        }

        return fleets;
    }
};
