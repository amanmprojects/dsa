class TimeMap {
public:
    unordered_map<string, pair<vector<int>, vector<string>>> store;
    TimeMap() {

    }
    
    void set(string key, string value, int timestamp) {
        if (store.count(key)){
            store.at(key).first.push_back(timestamp);
            store.at(key).second.push_back(value);
        }
        else {
            store.insert({key, {{timestamp}, {value}}});
        }
    }
    
    string get(string key, int timestamp) {
        if(store.count(key) == 0) return "";
        vector<int> ts = store.at(key).first;
        int mid;

        int l = 0, r = ts.size()-1;

        while(l <= r){
            mid = (l + r) / 2;
            if(ts[mid] == timestamp) {
                break;
            }
            else if(ts[mid] < timestamp) l = mid+1;
            else r = mid-1;
        }

        if (ts[mid] <= timestamp){
            return store.at(key).second[mid];
        } 
        mid--;
        if(mid >= 0 && ts[mid] <= timestamp) return store.at(key).second[mid];

        return "";
    }
};