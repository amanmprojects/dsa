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
        string res = "";

        // Key does not exist
        if(store.count(key) == 0) return res;

        //
        pair<vector<int>, vector<string>> values = store.at(key);
        int mid;

        int l = 0, r = values.first.size()-1;

        while(l <= r){
            mid = (l + r) / 2;
            if(values.first[mid] <= timestamp) {
                res = values.second[mid];
                l = mid + 1;
            }
            else r = mid-1;
        }
        return res;
    }
};