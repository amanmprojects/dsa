class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        pair<int, int> dims;
        dims.first = matrix.size(); //Rows
        dims.second = matrix[0].size(); // Columns
        int total = dims.first * dims.second;

        int l, r, mid, i, j;
        l = 0;
        r = (dims.first * dims.second)-1;

        while(l <= r) {
            cout<<"l = "<<l<<" r = "<<r<<"\n";
            mid = ((l + r) / 2);
            i = mid / dims.second;
            j = mid % dims.second;
            cout<<"i = "<<i<<" j = "<<j<<'\n';
            cout<<"Curr: "<<matrix[i][j]<<" Mid(before): "<<mid<<"\n\n";
            if(matrix[i][j] == target) return true;
            else if(matrix[i][j] < target) l = mid+1;
            else r = mid - 1;
        }

        return false;
     }
};
